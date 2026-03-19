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
class LogDisk:
    """LogDisk"""
    # Required fields
    # Optional fields
    log_disk_capacity: Optional[str] = None
    log_disk_assigned: Optional[str] = None
    log_disk_in_use: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LogDisk":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            log_disk_capacity=data.get("log_disk_capacity"),
            log_disk_assigned=data.get("log_disk_assigned"),
            log_disk_in_use=data.get("log_disk_in_use"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.log_disk_capacity is not None:
            _v = self.log_disk_capacity
            result["log_disk_capacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_disk_assigned is not None:
            _v = self.log_disk_assigned
            result["log_disk_assigned"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_disk_in_use is not None:
            _v = self.log_disk_in_use
            result["log_disk_in_use"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
