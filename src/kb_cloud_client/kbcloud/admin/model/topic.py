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
class Topic:
    """Topic"""
    # Required fields
    name: str
    # Optional fields
    partitions_count: Optional[int] = None
    consumer_groups_count: Optional[int] = None
    replica_count: Optional[int] = None
    total_log_size: Optional[int] = None
    internal: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Topic":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            partitions_count=data.get("partitionsCount"),
            consumer_groups_count=data.get("consumerGroupsCount"),
            replica_count=data.get("replicaCount"),
            total_log_size=data.get("TotalLogSize"),
            internal=data.get("internal"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.partitions_count is not None:
            _v = self.partitions_count
            result["partitionsCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.consumer_groups_count is not None:
            _v = self.consumer_groups_count
            result["consumerGroupsCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replica_count is not None:
            _v = self.replica_count
            result["replicaCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_log_size is not None:
            _v = self.total_log_size
            result["TotalLogSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.internal is not None:
            _v = self.internal
            result["internal"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
