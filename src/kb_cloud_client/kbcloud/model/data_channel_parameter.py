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
from .parameter_value_type import ParameterValueType


@dataclass
class DataChannelParameter:
    """DataChannelParameter"""
    # Required fields
    key: str
    # Optional fields
    display_name: Optional[str] = None
    desc: Optional[InternationalDesc] = None
    default_value: Optional[str] = None
    value_type: Optional[ParameterValueType] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelParameter":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            display_name=data.get("displayName"),
            desc=InternationalDesc.from_dict(data.get("desc")) if isinstance(data.get("desc"), dict) else data.get("desc"),
            key=data.get("key"),
            default_value=data.get("defaultValue"),
            value_type=ParameterValueType.from_dict(data.get("valueType")) if isinstance(data.get("valueType"), dict) else data.get("valueType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.desc is not None:
            _v = self.desc
            result["desc"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.key is not None:
            _v = self.key
            result["key"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_value is not None:
            _v = self.default_value
            result["defaultValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.value_type is not None:
            _v = self.value_type
            result["valueType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
