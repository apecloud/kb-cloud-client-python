# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .international_desc import InternationalDesc
from .module_definition_values import ModuleDefinitionValues


@dataclass
class ModuleDefinition:
    """ModuleDefinition"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    title: Optional[InternationalDesc] = None
    values: Optional[List[ModuleDefinitionValues]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModuleDefinition":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            title=InternationalDesc.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            values=[ModuleDefinitionValues.from_dict(i) if isinstance(i, dict) else i for i in data.get("values")] if data.get("values") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.values is not None:
            _v = self.values
            result["values"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
