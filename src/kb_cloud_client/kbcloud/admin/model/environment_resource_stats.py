# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .resource_stats import ResourceStats
from .storage_stats import StorageStats


@dataclass
class EnvironmentResourceStats:
    """EnvironmentResourceStats holds the cpuStats for a environment."""
    # Required fields
    cpu_stats: ResourceStats
    memory_stats: ResourceStats
    name: str
    storage_stats: StorageStats
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentResourceStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cpu_stats=ResourceStats.from_dict(data.get("cpuStats")) if isinstance(data.get("cpuStats"), dict) else data.get("cpuStats"),
            memory_stats=ResourceStats.from_dict(data.get("memoryStats")) if isinstance(data.get("memoryStats"), dict) else data.get("memoryStats"),
            name=data.get("name"),
            storage_stats=StorageStats.from_dict(data.get("storageStats")) if isinstance(data.get("storageStats"), dict) else data.get("storageStats"),
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
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_stats is not None:
            _v = self.storage_stats
            result["storageStats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
