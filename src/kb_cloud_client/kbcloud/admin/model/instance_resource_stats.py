# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .instance_resource_stats_type import InstanceResourceStatsType
from .resource_stats import ResourceStats


@dataclass
class InstanceResourceStats:
    """InstanceResourceStats holds the requests, limits, and available stats for an instance."""
    # Required fields
    cpu_stats: ResourceStats
    memory_stats: ResourceStats
    name: str
    # Optional fields
    ephemeral_storage_stats: Optional[ResourceStats] = None
    type_: Optional[InstanceResourceStatsType] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InstanceResourceStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cpu_stats=ResourceStats.from_dict(data.get("cpuStats")) if isinstance(data.get("cpuStats"), dict) else data.get("cpuStats"),
            memory_stats=ResourceStats.from_dict(data.get("memoryStats")) if isinstance(data.get("memoryStats"), dict) else data.get("memoryStats"),
            ephemeral_storage_stats=ResourceStats.from_dict(data.get("ephemeralStorageStats")) if isinstance(data.get("ephemeralStorageStats"), dict) else data.get("ephemeralStorageStats"),
            name=data.get("name"),
            type_=InstanceResourceStatsType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cpu_stats is not None:
            _v = self.cpu_stats
            result["cpuStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_stats is not None:
            _v = self.memory_stats
            result["memoryStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ephemeral_storage_stats is not None:
            _v = self.ephemeral_storage_stats
            result["ephemeralStorageStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
