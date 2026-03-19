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
class DisasterRecoveryStatusResponse:
    """Status of the Disaster Recovery instance"""
    # Required fields
    cluster_id: str
    parent_id: str
    # Optional fields
    cluster_name: Optional[str] = None
    display_name: Optional[str] = None
    status: Optional[str] = None
    parent_name: Optional[str] = None
    parent_display_name: Optional[str] = None
    parent_status: Optional[str] = None
    delay: Optional[float] = None
    current_replication_point: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DisasterRecoveryStatusResponse":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cluster_id=data.get("clusterId"),
            cluster_name=data.get("clusterName"),
            display_name=data.get("displayName"),
            status=data.get("status"),
            parent_id=data.get("parentId"),
            parent_name=data.get("parentName"),
            parent_display_name=data.get("parentDisplayName"),
            parent_status=data.get("parentStatus"),
            delay=data.get("delay"),
            current_replication_point=data.get("currentReplicationPoint"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_id is not None:
            _v = self.parent_id
            result["parentId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_name is not None:
            _v = self.parent_name
            result["parentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_display_name is not None:
            _v = self.parent_display_name
            result["parentDisplayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_status is not None:
            _v = self.parent_status
            result["parentStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.delay is not None:
            _v = self.delay
            result["delay"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.current_replication_point is not None:
            _v = self.current_replication_point
            result["currentReplicationPoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
