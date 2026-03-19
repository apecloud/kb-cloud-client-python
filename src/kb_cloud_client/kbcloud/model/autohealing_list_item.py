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
class AutohealingListItem:
    """AutohealingListItem"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    component_name: Optional[str] = None
    pod_name: Optional[str] = None
    start_time: Optional[datetime] = None
    phase: Optional[str] = None
    started: Optional[bool] = None
    start_message: Optional[str] = None
    finished: Optional[bool] = None
    finish_message: Optional[str] = None
    backup_name: Optional[str] = None
    rebuild_instance_ops_request_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AutohealingListItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            component_name=data.get("componentName"),
            pod_name=data.get("podName"),
            start_time=_parse_datetime(data.get("startTime")),
            phase=data.get("phase"),
            started=data.get("started"),
            start_message=data.get("startMessage"),
            finished=data.get("finished"),
            finish_message=data.get("finishMessage"),
            backup_name=data.get("backupName"),
            rebuild_instance_ops_request_name=data.get("rebuildInstanceOpsRequestName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component_name is not None:
            _v = self.component_name
            result["componentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_name is not None:
            _v = self.pod_name
            result["podName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_time is not None:
            _v = self.start_time
            result["startTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.phase is not None:
            _v = self.phase
            result["phase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.started is not None:
            _v = self.started
            result["started"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_message is not None:
            _v = self.start_message
            result["startMessage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.finished is not None:
            _v = self.finished
            result["finished"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.finish_message is not None:
            _v = self.finish_message
            result["finishMessage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup_name is not None:
            _v = self.backup_name
            result["backupName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_instance_ops_request_name is not None:
            _v = self.rebuild_instance_ops_request_name
            result["rebuildInstanceOpsRequestName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
