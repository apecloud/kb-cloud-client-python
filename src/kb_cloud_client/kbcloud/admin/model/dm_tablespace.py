# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .dm_file import DmFile
from .table_space_status import TableSpaceStatus


@dataclass
class DmTablespace:
    """DmTablespace"""
    # Required fields
    name: str
    files: List[DmFile]
    # Optional fields
    users: Optional[str] = None
    allocated_size_mb: Optional[str] = None
    used_size_mb: Optional[str] = None
    used_ratio: Optional[str] = None
    auto_extend: Optional[bool] = None
    max_size_gb: Optional[str] = None
    used_ratio_in_max: Optional[str] = None
    status: Optional[TableSpaceStatus] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmTablespace":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            users=data.get("users"),
            files=[DmFile.from_dict(i) if isinstance(i, dict) else i for i in data.get("files")] if data.get("files") is not None else None,
            allocated_size_mb=data.get("allocatedSizeMB"),
            used_size_mb=data.get("usedSizeMB"),
            used_ratio=data.get("usedRatio"),
            auto_extend=data.get("autoExtend"),
            max_size_gb=data.get("maxSizeGB"),
            used_ratio_in_max=data.get("usedRatioInMax"),
            status=TableSpaceStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.users is not None:
            _v = self.users
            result["users"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.files is not None:
            _v = self.files
            result["files"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.auto_extend is not None:
            _v = self.auto_extend
            result["autoExtend"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
