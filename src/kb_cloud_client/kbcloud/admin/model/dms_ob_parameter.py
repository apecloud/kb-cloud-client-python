# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class DmsObParameter:
    """DmsObParameter"""
    # Required fields
    name: str
    value: str
    description: str
    # Optional fields
    data_type: Optional[str] = None
    enum: Optional[List[Any]] = None
    maximum: Optional[str] = None
    minimum: Optional[str] = None
    immutable: Optional[bool] = None
    is_variable: Optional[bool] = None
    edit_level: Optional[str] = None
    read_only: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsObParameter":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            value=data.get("value"),
            data_type=data.get("dataType"),
            description=data.get("description"),
            enum=data.get("enum"),
            maximum=data.get("maximum"),
            minimum=data.get("minimum"),
            immutable=data.get("immutable"),
            is_variable=data.get("isVariable"),
            edit_level=data.get("editLevel"),
            read_only=data.get("readOnly"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.value is not None:
            _v = self.value
            result["value"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_type is not None:
            _v = self.data_type
            result["dataType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enum is not None:
            _v = self.enum
            result["enum"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.maximum is not None:
            _v = self.maximum
            result["maximum"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.minimum is not None:
            _v = self.minimum
            result["minimum"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.immutable is not None:
            _v = self.immutable
            result["immutable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_variable is not None:
            _v = self.is_variable
            result["isVariable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.edit_level is not None:
            _v = self.edit_level
            result["editLevel"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.read_only is not None:
            _v = self.read_only
            result["readOnly"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
