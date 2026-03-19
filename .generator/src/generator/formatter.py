"""Python data formatter for the KubeBlocks Cloud API client generator."""
import keyword
import re
from typing import Any

from .utils import safe_snake_case, snake_case, camel_case, upperfirst

PRIMITIVE_TYPES = ["string", "number", "boolean", "integer"]

PYTHON_KEYWORDS = set(keyword.kwlist) | {
    "property",
    "cls",
    "self",
    "type",
    "id",
    "input",
    "format",
    "filter",
    "object",
    "list",
    "dict",
    "set",
    "bytes",
    "str",
    "int",
    "float",
    "bool",
    "None",
    "True",
    "False",
}


def escape_reserved_keyword(word: str) -> str:
    """Escape Python reserved keywords by appending an underscore."""
    if word in PYTHON_KEYWORDS:
        return f"{word}_"
    return word


def attribute_name(attribute: str) -> str:
    """Convert an OpenAPI attribute name to a Python attribute name."""
    return escape_reserved_keyword(snake_case(attribute))


def class_name(name: str) -> str:
    """Convert a name to a Python class name (PascalCase)."""
    # Remove spaces, capitalize first letter of each word
    name = re.sub(r"[^a-zA-Z0-9_]", " ", name)
    return "".join(word.capitalize() for word in name.split())


_RESERVED_FILENAMES = set(keyword.kwlist) | {
    "type", "id", "input", "format", "filter", "object", "list",
    "dict", "set", "bytes", "str", "int", "float", "bool",
}


def model_filename(name: str) -> str:
    """Convert a model name to a Python filename (snake_case), avoiding reserved keywords."""
    filename = safe_snake_case(name)
    if filename in _RESERVED_FILENAMES:
        filename = filename + "_model"
    return filename


def type_to_python(schema: Any, alternative_name: str = None, optional: bool = False) -> str:
    """Return the Python type annotation for a schema."""
    if schema is None:
        return "Any"

    # Handle True (additionalProperties: true)
    if schema is True:
        return "Dict[str, Any]"

    name = _get_schema_name(schema)

    if "enum" in schema:
        return name or "str"

    type_ = schema.get("type")

    if name and (type_ == "object" or (type_ is None and "properties" in schema)):
        return name

    if type_ == "string":
        fmt = schema.get("format")
        if fmt in ("date", "date-time"):
            return "datetime"
        if fmt == "binary":
            return "bytes"
        if fmt == "uuid":
            return "str"
        return "str"
    elif type_ == "integer":
        return "int"
    elif type_ == "number":
        return "float"
    elif type_ == "boolean":
        return "bool"
    elif type_ == "array":
        items = schema.get("items", {})
        item_type = type_to_python(items, alternative_name=alternative_name)
        return f"List[{item_type}]"
    elif type_ == "object":
        if "additionalProperties" in schema:
            v = schema["additionalProperties"]
            if v is True:
                return "Dict[str, Any]"
            val_type = type_to_python(v, alternative_name=alternative_name)
            return f"Dict[str, {val_type}]"
        return name or alternative_name or "Dict[str, Any]"
    elif type_ is None:
        if "oneOf" in schema:
            types = [type_to_python(s) for s in schema["oneOf"] if s]
            if name:
                return name
            return f"Union[{', '.join(types)}]" if len(types) > 1 else (types[0] if types else "Any")
        if "anyOf" in schema:
            types = [type_to_python(s) for s in schema["anyOf"] if s]
            if name:
                return name
            return f"Union[{', '.join(types)}]" if len(types) > 1 else (types[0] if types else "Any")
        if "allOf" in schema:
            if name:
                return name
            return alternative_name or "Any"
        if name:
            return name
        return "Any"

    return "Any"


def _get_schema_name(schema: Any) -> str:
    """Get the name of a schema from its $ref, normalized to PascalCase."""
    if hasattr(schema, "__reference__"):
        name = schema.__reference__["$ref"].split("/")[-1]
        return upperfirst(name)
    return None


def get_typing_imports(schema: Any) -> set:
    """Return the set of typing imports needed for a schema type."""
    t = type_to_python(schema)
    imports = set()
    if "List[" in t:
        imports.add("List")
    if "Dict[" in t:
        imports.add("Dict")
    if "Optional[" in t:
        imports.add("Optional")
    if "Union[" in t:
        imports.add("Union")
    if "Any" in t:
        imports.add("Any")
    if "datetime" in t:
        imports.add("datetime")
    return imports


def is_nullable(schema: Any) -> bool:
    """Check if a schema is nullable."""
    if schema is None:
        return False
    return schema.get("nullable", False)


def format_value(value: Any) -> str:
    """Format a Python literal value."""
    if isinstance(value, str):
        return repr(value)
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return "None"
    return str(value)


def deserialize_field(prop_schema: Any, var_name: str) -> str:
    """Return a Python expression that deserializes ``var_name`` according to ``prop_schema``.

    Generated inline — no runtime helper import required.
    Rules:
      - $ref → TypeName.from_dict(v) if isinstance(v, dict) else v
      - array of $ref → [TypeName.from_dict(i) … for i in (v or [])]
      - datetime string → datetime.fromisoformat(v) …
      - everything else → v  (pass-through)
    """
    if prop_schema is None:
        return var_name

    # $ref to another model
    name = _get_schema_name(prop_schema)
    if name:
        return f"{name}.from_dict({var_name}) if isinstance({var_name}, dict) else {var_name}"

    type_ = prop_schema.get("type")

    if type_ == "array":
        items = prop_schema.get("items", {})
        item_name = _get_schema_name(items)
        if item_name:
            item_expr = f"{item_name}.from_dict(i) if isinstance(i, dict) else i"
            return (
                f"[{item_expr} for i in {var_name}] "
                f"if {var_name} is not None else None"
            )
        # array of primitives or dates
        item_type = type_to_python(items)
        if item_type == "datetime":
            return (
                f"[_parse_datetime(i) for i in {var_name}] "
                f"if {var_name} is not None else None"
            )
        return var_name

    if type_ == "string" and prop_schema.get("format") in ("date", "date-time"):
        # Use _parse_datetime for Python 3.10 compat (handles 'Z' UTC suffix)
        return f"_parse_datetime({var_name})"

    return var_name


def get_model_references(model: Any, model_name: str) -> list:
    """Return list of direct model names referenced by a model's properties.

    Only looks one level deep (direct property references) to avoid recursion
    with circular schemas. The returned names are needed as runtime imports so
    that generated ``from_dict`` methods can call ``TypeName.from_dict(...)``.
    """
    refs: dict = {}

    def _collect_direct(schema: Any) -> None:
        """Collect $ref names one level deep from a schema."""
        if schema is None:
            return
        name = _get_schema_name(schema)
        if name and name != model_name:
            refs[name] = None
            return  # don't recurse into this ref's properties

        type_ = schema.get("type")
        if type_ == "array":
            items = schema.get("items", {})
            item_name = _get_schema_name(items)
            if item_name and item_name != model_name:
                refs[item_name] = None
        elif type_ == "object" or "properties" in schema:
            for prop in schema.get("properties", {}).values():
                prop_name = _get_schema_name(prop)
                if prop_name and prop_name != model_name:
                    refs[prop_name] = None
                elif prop.get("type") == "array":
                    item_name = _get_schema_name(prop.get("items", {}))
                    if item_name and item_name != model_name:
                        refs[item_name] = None
        for key in ("allOf",):
            for sub in schema.get(key, []):
                sub_name = _get_schema_name(sub)
                if sub_name and sub_name != model_name:
                    refs[sub_name] = None
                elif sub.get("properties"):
                    for prop in sub.get("properties", {}).values():
                        prop_name = _get_schema_name(prop)
                        if prop_name and prop_name != model_name:
                            refs[prop_name] = None
                        elif prop.get("type") == "array":
                            item_name = _get_schema_name(prop.get("items", {}))
                            if item_name and item_name != model_name:
                                refs[item_name] = None

    _collect_direct(model)
    return list(refs)
