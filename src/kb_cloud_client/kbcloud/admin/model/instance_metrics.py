# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .instance_disk_usage_item import InstanceDiskUsageItem


@dataclass
class InstanceMetrics:
    """instance metrics"""
    # Required fields
    instance_name: str
    # Optional fields
    cpu_usage: Optional[str] = None
    memory_usage: Optional[str] = None
    disk_usage_items: Optional[List[InstanceDiskUsageItem]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InstanceMetrics":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            instance_name=data.get("instanceName"),
            cpu_usage=data.get("cpuUsage"),
            memory_usage=data.get("memoryUsage"),
            disk_usage_items=[InstanceDiskUsageItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("diskUsageItems")] if data.get("diskUsageItems") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.instance_name is not None:
            _v = self.instance_name
            result["instanceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_usage is not None:
            _v = self.cpu_usage
            result["cpuUsage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_usage is not None:
            _v = self.memory_usage
            result["memoryUsage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disk_usage_items is not None:
            _v = self.disk_usage_items
            result["diskUsageItems"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
