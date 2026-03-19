# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class ModeOptionValuesMappingsMappingsItem:
    """ModeOptionValuesMappingsMappingsItem"""
    # Required fields
    source_key: str
    target_key: str
    # Optional fields
    component: Optional[str] = None
    source_value: Optional[Any] = None
    target_value: Optional[Any] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeOptionValuesMappingsMappingsItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            source_key=data.get("sourceKey"),
            source_value=data.get("sourceValue"),
            target_key=data.get("targetKey"),
            target_value=data.get("targetValue"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source_key is not None:
            _v = self.source_key
            result["sourceKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source_value is not None:
            _v = self.source_value
            result["sourceValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_key is not None:
            _v = self.target_key
            result["targetKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_value is not None:
            _v = self.target_value
            result["targetValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
