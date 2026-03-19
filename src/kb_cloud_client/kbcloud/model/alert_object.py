# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .alert_severity import AlertSeverity
from .alert_status import AlertStatus


@dataclass
class AlertObject:
    """Alert object information"""
    # Required fields
    # Optional fields
    id_: Optional[int] = None
    alert_name: Optional[str] = None
    group_name: Optional[str] = None
    expr: Optional[str] = None
    cluster_name: Optional[str] = None
    object_name: Optional[str] = None
    engine: Optional[str] = None
    namespace: Optional[str] = None
    pod: Optional[str] = None
    severity: Optional[AlertSeverity] = None
    description: Optional[str] = None
    fingerprint: Optional[str] = None
    starts_at: Optional[datetime] = None
    ends_at: Optional[datetime] = None
    status: Optional[AlertStatus] = None
    count: Optional[int] = None
    org_name: Optional[str] = None
    page: Optional[int] = None
    page_size: Optional[int] = None
    env: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertObject":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            alert_name=data.get("alertName"),
            group_name=data.get("groupName"),
            expr=data.get("expr"),
            cluster_name=data.get("clusterName"),
            object_name=data.get("objectName"),
            engine=data.get("engine"),
            namespace=data.get("namespace"),
            pod=data.get("pod"),
            severity=AlertSeverity.from_dict(data.get("severity")) if isinstance(data.get("severity"), dict) else data.get("severity"),
            description=data.get("description"),
            fingerprint=data.get("fingerprint"),
            starts_at=_parse_datetime(data.get("startsAt")),
            ends_at=_parse_datetime(data.get("endsAt")),
            status=AlertStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            count=data.get("count"),
            org_name=data.get("orgName"),
            page=data.get("page"),
            page_size=data.get("pageSize"),
            env=data.get("env"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.alert_name is not None:
            _v = self.alert_name
            result["alertName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.group_name is not None:
            _v = self.group_name
            result["groupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.expr is not None:
            _v = self.expr
            result["expr"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.object_name is not None:
            _v = self.object_name
            result["objectName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod is not None:
            _v = self.pod
            result["pod"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.severity is not None:
            _v = self.severity
            result["severity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.fingerprint is not None:
            _v = self.fingerprint
            result["fingerprint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.starts_at is not None:
            _v = self.starts_at
            result["startsAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ends_at is not None:
            _v = self.ends_at
            result["endsAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.count is not None:
            _v = self.count
            result["count"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.page is not None:
            _v = self.page
            result["page"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.page_size is not None:
            _v = self.page_size
            result["pageSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env is not None:
            _v = self.env
            result["env"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
