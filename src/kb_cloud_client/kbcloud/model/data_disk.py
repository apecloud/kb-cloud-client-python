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
class DataDisk:
    """DataDisk"""
    # Required fields
    # Optional fields
    data_disk_capacity: Optional[str] = None
    data_disk_allocated: Optional[str] = None
    data_disk_in_use: Optional[str] = None
    data_disk_health_status: Optional[str] = None
    data_disk_abnormal_time: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataDisk":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            data_disk_capacity=data.get("data_disk_capacity"),
            data_disk_allocated=data.get("data_disk_allocated"),
            data_disk_in_use=data.get("data_disk_in_use"),
            data_disk_health_status=data.get("data_disk_health_status"),
            data_disk_abnormal_time=data.get("data_disk_abnormal_time"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.data_disk_capacity is not None:
            _v = self.data_disk_capacity
            result["data_disk_capacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_disk_allocated is not None:
            _v = self.data_disk_allocated
            result["data_disk_allocated"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_disk_in_use is not None:
            _v = self.data_disk_in_use
            result["data_disk_in_use"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_disk_health_status is not None:
            _v = self.data_disk_health_status
            result["data_disk_health_status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data_disk_abnormal_time is not None:
            _v = self.data_disk_abnormal_time
            result["data_disk_abnormal_time"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
