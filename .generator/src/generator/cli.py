"""CLI entry point for the KubeBlocks Cloud Python client generator."""
import json as _json
import pathlib

import click
from jinja2 import Environment, FileSystemLoader

from . import openapi
from . import formatter
from . import utils

PACKAGE_NAME = "kb_cloud_client"

# Maps spec stem → (module_dir_parts, display_name, description)
# module_dir_parts are relative to the output root.
SPEC_CONFIG = {
    # User-facing API: output/kbcloud/
    "openapi": {
        "parts": ["kbcloud"],
        "display": "kbcloud",
        "description": "KubeBlocks Cloud API – user portal",
    },
    # Admin API: output/kbcloud/admin/ (nested, mirrors Go api/kbcloud/admin)
    "adminapi": {
        "parts": ["kbcloud", "admin"],
        "display": "kbcloud.admin",
        "description": "KubeBlocks Cloud API – admin portal",
    },
    # Data API (reserved): output/kbcloud/data/
    "dataapi": {
        "parts": ["kbcloud", "data"],
        "display": "kbcloud.data",
        "description": "KubeBlocks Cloud API – data plane",
    },
}


@click.command()
@click.argument(
    "specs",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=pathlib.Path),
)
@click.option("-o", "--output", type=click.Path(path_type=pathlib.Path))
def cli(specs, output):
    """Generate Python client code from OpenAPI specifications.

    Mirrors the Go client structure:
      kbcloud/        ← user portal  (openapi.yaml)
      kbcloud/admin/  ← admin portal (adminapi.yaml)
    """
    env = Environment(
        loader=FileSystemLoader(str(pathlib.Path(__file__).parent / "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["tojson"] = lambda v: _json.dumps(v)
    env.filters["attribute_name"] = formatter.attribute_name
    env.filters["class_name"] = formatter.class_name
    env.filters["model_filename"] = formatter.model_filename
    env.filters["snake_case"] = utils.snake_case
    env.filters["safe_snake_case"] = utils.safe_snake_case
    env.filters["camel_case"] = utils.camel_case
    env.filters["upperfirst"] = utils.upperfirst
    env.filters["type_to_python"] = formatter.type_to_python
    env.filters["format_value"] = formatter.format_value
    env.filters["is_nullable"] = formatter.is_nullable
    env.filters["deserialize_field"] = formatter.deserialize_field
    env.filters["parameters"] = openapi.parameters
    env.filters["return_type"] = _return_type
    env.filters["accept_headers"] = openapi.accept_headers
    env.filters["collection_format"] = openapi.collection_format

    env.globals["get_name"] = openapi.get_name
    env.globals["type_to_python"] = formatter.type_to_python
    env.globals["get_model_references"] = formatter.get_model_references
    env.globals["get_type_for_parameter"] = _get_type_for_parameter
    env.globals["package"] = PACKAGE_NAME
    env.globals["enumerate"] = enumerate
    env.globals["is_required_prop"] = _is_required_prop

    api_j2 = env.get_template("api.j2")
    model_j2 = env.get_template("model.j2")
    api_init_j2 = env.get_template("api_init.j2")
    model_init_j2 = env.get_template("model_init.j2")
    module_init_j2 = env.get_template("module_init.j2")

    output.mkdir(parents=True, exist_ok=True)

    # Track which sub-packages were generated so we can stitch __init__.py files
    generated_submodules: dict[str, list[str]] = {}  # parent_dir → [child_names]

    for spec_path in specs:
        spec_name = spec_path.stem
        cfg = SPEC_CONFIG.get(spec_name, {"parts": [spec_name], "display": spec_name, "description": ""})

        parts = cfg["parts"]
        display = cfg["display"]
        print(f"Processing spec: {spec_name}  →  {display}/")

        spec = openapi.load(spec_path)
        env.globals["openapi"] = spec
        env.globals["module_name"] = display
        # Relative prefix to reach the top-level package from a model file.
        # model file depth = len(parts) [package dirs] + 1 [model subdir] + 1 [up to pkg root]
        env.globals["pkg_import_prefix"] = "." * (len(parts) + 2)

        apis = openapi.apis(spec)
        models = openapi.models(spec)

        # Build the output directory (e.g. output/kbcloud/admin)
        module_dir = output.joinpath(*parts)
        module_dir.mkdir(parents=True, exist_ok=True)

        api_dir = module_dir / "api"
        api_dir.mkdir(exist_ok=True)
        model_dir = module_dir / "model"
        model_dir.mkdir(exist_ok=True)

        # Normalize model names to PascalCase, deduplicate lower/upper variants
        normalized: dict = {}
        for mname, mschema in models.items():
            canonical = utils.upperfirst(mname)
            if canonical not in normalized or canonical == mname:
                normalized[canonical] = mschema
        models = normalized

        # ── Models ────────────────────────────────────────────────────────────
        generated_models: list[str] = []
        for name, model in sorted(models.items()):
            filename = formatter.model_filename(name) + ".py"
            model_path = model_dir / filename
            try:
                content = model_j2.render(name=name, model=model, models=models)
                with model_path.open("w") as fp:
                    fp.write(content)
                generated_models.append(name)
                print(f"  model: {name}")
            except Exception as exc:
                print(f"  WARNING: model {name} failed: {exc}")

        with (model_dir / "__init__.py").open("w") as fp:
            fp.write(model_init_j2.render(models=sorted(generated_models)))

        # ── APIs ──────────────────────────────────────────────────────────────
        generated_apis: list[str] = []
        for name, operations in sorted(apis.items()):
            if name is None:
                print(f"  WARNING: Missing tag for {operations}")
                continue
            operations = utils.removeWebSocketOP(operations)
            if not operations:
                continue
            filename = utils.safe_snake_case(name) + "_api.py"
            api_path = api_dir / filename
            try:
                content = api_j2.render(name=name, operations=operations)
                with api_path.open("w") as fp:
                    fp.write(content)
                generated_apis.append(name)
                print(f"  api:   {name}")
            except Exception as exc:
                print(f"  WARNING: api {name} failed: {exc}")

        with (api_dir / "__init__.py").open("w") as fp:
            fp.write(api_init_j2.render(apis=sorted(generated_apis)))

        # ── Module __init__.py ────────────────────────────────────────────────
        with (module_dir / "__init__.py").open("w") as fp:
            fp.write(module_init_j2.render(
                module_name=display,
                description=cfg["description"],
                apis=sorted(generated_apis),
                models=sorted(generated_models),
                # Whether this is a nested sub-package (admin, data, …)
                is_subpackage=len(parts) > 1,
            ))

        # Record sub-package relationships for parent __init__.py stitching
        if len(parts) > 1:
            parent_key = str(output.joinpath(*parts[:-1]))
            generated_submodules.setdefault(parent_key, []).append(parts[-1])

    # ── Stitch parent __init__.py files to expose sub-packages ───────────────
    for parent_dir_str, children in generated_submodules.items():
        parent_init = pathlib.Path(parent_dir_str) / "__init__.py"
        if parent_init.exists():
            existing = parent_init.read_text()
            lines_to_add = []
            for child in sorted(children):
                line = f"from . import {child}  # noqa: F401\n"
                if line not in existing:
                    lines_to_add.append(line)
            if lines_to_add:
                with parent_init.open("a") as fp:
                    fp.write("\n# Sub-packages\n")
                    fp.writelines(lines_to_add)

    # ── Top-level package __init__.py ─────────────────────────────────────────
    _write_top_init(output)


def _write_top_init(output: pathlib.Path) -> None:
    """Write the top-level kb_cloud_client __init__.py."""
    content = (
        "# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.\n"
        "# This product includes software developed at ApeCloud (https://www.apecloud.com/).\n"
        "# Copyright 2022-Present ApeCloud Co., Ltd\n"
        '"""KubeBlocks Cloud Python client.\n\n'
        "Packages:\n"
        "  kbcloud        – user-portal API\n"
        "  kbcloud.admin  – admin-portal API\n"
        '"""\n\n'
        "from .api_client import ApiClient\n"
        "from .configuration import Configuration\n"
        "from .exceptions import ApiException, NotFoundException, UnauthorizedException\n"
        "from . import kbcloud\n"
    )
    (output / "__init__.py").write_text(content)


def _return_type(operation: dict) -> str:
    for response in operation.get("responses", {}).values():
        for content in response.get("content", {}).values():
            if "schema" in content:
                return formatter.type_to_python(content["schema"])
    return None


def _get_type_for_parameter(parameter: dict, optional: bool = False) -> str:
    if "content" in parameter:
        for content in parameter["content"].values():
            if "schema" in content:
                return formatter.type_to_python(content["schema"])
    schema = parameter.get("schema", {})
    return formatter.type_to_python(schema)


def _is_required_prop(prop_name: str, model: dict) -> bool:
    return prop_name in model.get("required", [])
