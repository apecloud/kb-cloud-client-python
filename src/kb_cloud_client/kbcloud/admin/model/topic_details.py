# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .partition_info import PartitionInfo


@dataclass
class TopicDetails:
    """TopicDetails"""
    # Required fields
    name: str
    # Optional fields
    internal: Optional[bool] = None
    replica_count: Optional[int] = None
    partitions: Optional[List[PartitionInfo]] = None
    total_log_size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TopicDetails":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            internal=data.get("internal"),
            replica_count=data.get("replicaCount"),
            partitions=[PartitionInfo.from_dict(i) if isinstance(i, dict) else i for i in data.get("partitions")] if data.get("partitions") is not None else None,
            total_log_size=data.get("totalLogSize"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.internal is not None:
            _v = self.internal
            result["internal"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replica_count is not None:
            _v = self.replica_count
            result["replicaCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.partitions is not None:
            _v = self.partitions
            result["partitions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_log_size is not None:
            _v = self.total_log_size
            result["totalLogSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
