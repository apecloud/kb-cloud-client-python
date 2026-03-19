# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .localized_description import LocalizedDescription


@dataclass
class ImportBaseField:
    """ImportBaseField"""
    # Required fields
    name: str
    label: LocalizedDescription
    # Optional fields
    required: Optional[bool] = None
    sensitive: Optional[bool] = None
    description: Optional[LocalizedDescription] = None
    placeholder: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImportBaseField":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            label=LocalizedDescription.from_dict(data.get("label")) if isinstance(data.get("label"), dict) else data.get("label"),
            required=data.get("required"),
            sensitive=data.get("sensitive"),
            description=LocalizedDescription.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            placeholder=data.get("placeholder"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.label is not None:
            _v = self.label
            result["label"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.required is not None:
            _v = self.required
            result["required"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sensitive is not None:
            _v = self.sensitive
            result["sensitive"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.placeholder is not None:
            _v = self.placeholder
            result["placeholder"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
