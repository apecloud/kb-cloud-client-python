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
class StorageStats:
    """StorageStats holds the resource stats of the volume, including bound PVC capacity, pod-used PVC capacity, and actual storage usage."""
    # Required fields
    requests: float
    pod_used_capacity: float
    pod_used_usage: float
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            requests=data.get("requests"),
            pod_used_capacity=data.get("podUsedCapacity"),
            pod_used_usage=data.get("podUsedUsage"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.requests is not None:
            _v = self.requests
            result["requests"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_used_capacity is not None:
            _v = self.pod_used_capacity
            result["podUsedCapacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_used_usage is not None:
            _v = self.pod_used_usage
            result["podUsedUsage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
