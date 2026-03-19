# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .disaster_recovery_event_type import DisasterRecoveryEventType
from .disaster_recovery_status import DisasterRecoveryStatus


@dataclass
class DisasterRecoveryHistoryItem:
    """DisasterRecovery history detail for Cluster"""
    # Required fields
    # Optional fields
    task_id: Optional[str] = None
    parent_cluster_id: Optional[str] = None
    parent_cluster_name: Optional[str] = None
    parent_env_name: Optional[str] = None
    cluster_id: Optional[str] = None
    cluster_name: Optional[str] = None
    env_name: Optional[str] = None
    event_type: Optional[DisasterRecoveryEventType] = None
    reason: Optional[str] = None
    operator: Optional[str] = None
    operator_id: Optional[str] = None
    created_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    status: Optional[DisasterRecoveryStatus] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DisasterRecoveryHistoryItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            task_id=data.get("taskID"),
            parent_cluster_id=data.get("parentClusterID"),
            parent_cluster_name=data.get("parentClusterName"),
            parent_env_name=data.get("parentEnvName"),
            cluster_id=data.get("clusterID"),
            cluster_name=data.get("clusterName"),
            env_name=data.get("envName"),
            event_type=DisasterRecoveryEventType.from_dict(data.get("eventType")) if isinstance(data.get("eventType"), dict) else data.get("eventType"),
            reason=data.get("reason"),
            operator=data.get("operator"),
            operator_id=data.get("operatorId"),
            created_at=_parse_datetime(data.get("createdAt")),
            update_at=_parse_datetime(data.get("updateAt")),
            status=DisasterRecoveryStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.task_id is not None:
            _v = self.task_id
            result["taskID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_cluster_id is not None:
            _v = self.parent_cluster_id
            result["parentClusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_cluster_name is not None:
            _v = self.parent_cluster_name
            result["parentClusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_env_name is not None:
            _v = self.parent_env_name
            result["parentEnvName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env_name is not None:
            _v = self.env_name
            result["envName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_type is not None:
            _v = self.event_type
            result["eventType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reason is not None:
            _v = self.reason
            result["reason"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator is not None:
            _v = self.operator
            result["operator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator_id is not None:
            _v = self.operator_id
            result["operatorId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.update_at is not None:
            _v = self.update_at
            result["updateAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
