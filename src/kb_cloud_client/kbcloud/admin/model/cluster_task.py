# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_task_details import ClusterTaskDetails
from .cluster_task_progresses import ClusterTaskProgresses


@dataclass
class ClusterTask:
    """task is the information of the operation"""
    # Required fields
    name: str
    namespace: str
    status: str
    task_type: str
    progress: str
    # Optional fields
    id_: Optional[str] = None
    org_name: Optional[str] = None
    cluster_name: Optional[str] = None
    task_progresses: Optional[ClusterTaskProgresses] = None
    task_details: Optional[ClusterTaskDetails] = None
    ops_log: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    completion_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterTask":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            namespace=data.get("namespace"),
            org_name=data.get("orgName"),
            cluster_name=data.get("clusterName"),
            status=data.get("status"),
            task_type=data.get("taskType"),
            progress=data.get("progress"),
            task_progresses=ClusterTaskProgresses.from_dict(data.get("taskProgresses")) if isinstance(data.get("taskProgresses"), dict) else data.get("taskProgresses"),
            task_details=ClusterTaskDetails.from_dict(data.get("taskDetails")) if isinstance(data.get("taskDetails"), dict) else data.get("taskDetails"),
            ops_log=data.get("opsLog"),
            description=data.get("description"),
            start_time=_parse_datetime(data.get("startTime")),
            completion_time=_parse_datetime(data.get("completionTime")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_type is not None:
            _v = self.task_type
            result["taskType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.progress is not None:
            _v = self.progress
            result["progress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_progresses is not None:
            _v = self.task_progresses
            result["taskProgresses"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_details is not None:
            _v = self.task_details
            result["taskDetails"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ops_log is not None:
            _v = self.ops_log
            result["opsLog"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_time is not None:
            _v = self.start_time
            result["startTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completion_time is not None:
            _v = self.completion_time
            result["completionTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
