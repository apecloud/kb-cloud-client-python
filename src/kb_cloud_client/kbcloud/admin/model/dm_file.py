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
class DmFile:
    """DmFile"""
    # Required fields
    name: str
    # Optional fields
    id_: Optional[str] = None
    auto_extend: Optional[bool] = None
    allocated_size_mb: Optional[str] = None
    used_size_mb: Optional[str] = None
    used_ratio: Optional[str] = None
    extend_step_mb: Optional[str] = None
    max_size_gb: Optional[str] = None
    used_ratio_in_max: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmFile":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            auto_extend=data.get("autoExtend"),
            allocated_size_mb=data.get("allocatedSizeMB"),
            used_size_mb=data.get("usedSizeMB"),
            used_ratio=data.get("usedRatio"),
            extend_step_mb=data.get("extendStepMB"),
            max_size_gb=data.get("maxSizeGB"),
            used_ratio_in_max=data.get("usedRatioInMax"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auto_extend is not None:
            _v = self.auto_extend
            result["autoExtend"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.allocated_size_mb is not None:
            _v = self.allocated_size_mb
            result["allocatedSizeMB"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.used_size_mb is not None:
            _v = self.used_size_mb
            result["usedSizeMB"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.used_ratio is not None:
            _v = self.used_ratio
            result["usedRatio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extend_step_mb is not None:
            _v = self.extend_step_mb
            result["extendStepMB"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.max_size_gb is not None:
            _v = self.max_size_gb
            result["maxSizeGB"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.used_ratio_in_max is not None:
            _v = self.used_ratio_in_max
            result["usedRatioInMax"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
