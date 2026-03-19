# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .event_resource_type import EventResourceType
from .event_result_status import EventResultStatus
from .event_source import EventSource


@dataclass
class Event:
    """event is the information of operation event"""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    resource_id: Optional[str] = None
    resource_type: Optional[EventResourceType] = None
    resource_name: Optional[str] = None
    operator: Optional[str] = None
    operator_id: Optional[str] = None
    details: Optional[str] = None
    has_task: Optional[bool] = None
    result: Optional[str] = None
    event_name: Optional[str] = None
    display_name: Optional[str] = None
    org_name: Optional[str] = None
    result_status: Optional[EventResultStatus] = None
    source: Optional[EventSource] = None
    end: Optional[datetime] = None
    start: Optional[datetime] = None
    created_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Event":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            resource_id=data.get("resourceId"),
            resource_type=EventResourceType.from_dict(data.get("resourceType")) if isinstance(data.get("resourceType"), dict) else data.get("resourceType"),
            resource_name=data.get("resourceName"),
            operator=data.get("operator"),
            operator_id=data.get("operatorId"),
            details=data.get("details"),
            has_task=data.get("hasTask"),
            result=data.get("result"),
            event_name=data.get("eventName"),
            display_name=data.get("displayName"),
            org_name=data.get("orgName"),
            result_status=EventResultStatus.from_dict(data.get("resultStatus")) if isinstance(data.get("resultStatus"), dict) else data.get("resultStatus"),
            source=EventSource.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            end=_parse_datetime(data.get("end")),
            start=_parse_datetime(data.get("start")),
            created_at=_parse_datetime(data.get("createdAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_id is not None:
            _v = self.resource_id
            result["resourceId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_type is not None:
            _v = self.resource_type
            result["resourceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_name is not None:
            _v = self.resource_name
            result["resourceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.details is not None:
            _v = self.details
            result["details"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.has_task is not None:
            _v = self.has_task
            result["hasTask"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.result is not None:
            _v = self.result
            result["result"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_name is not None:
            _v = self.event_name
            result["eventName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.result_status is not None:
            _v = self.result_status
            result["resultStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source is not None:
            _v = self.source
            result["source"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.end is not None:
            _v = self.end
            result["end"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start is not None:
            _v = self.start
            result["start"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
