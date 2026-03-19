# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .task_failure_policy import TaskFailurePolicy
from .task_status import TaskStatus
from .task_step import TaskStep


@dataclass
class Task:
    """Task"""
    # Required fields
    task_id: str
    task_name: str
    task_type: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    # Optional fields
    deleted_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completion_time: Optional[datetime] = None
    message: Optional[str] = None
    progress: Optional[int] = None
    steps: Optional[List[TaskStep]] = None
    parallelism: Optional[int] = None
    failure_policy: Optional[TaskFailurePolicy] = None
    retry_limit: Optional[int] = None
    timeout_second: Optional[int] = None
    operator: Optional[str] = None
    cluster_task_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            task_id=data.get("taskId"),
            task_name=data.get("taskName"),
            task_type=data.get("taskType"),
            status=TaskStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            deleted_at=_parse_datetime(data.get("deletedAt")),
            started_at=_parse_datetime(data.get("startedAt")),
            completion_time=_parse_datetime(data.get("completionTime")),
            message=data.get("message"),
            progress=data.get("progress"),
            steps=[TaskStep.from_dict(i) if isinstance(i, dict) else i for i in data.get("steps")] if data.get("steps") is not None else None,
            parallelism=data.get("parallelism"),
            failure_policy=TaskFailurePolicy.from_dict(data.get("failurePolicy")) if isinstance(data.get("failurePolicy"), dict) else data.get("failurePolicy"),
            retry_limit=data.get("retryLimit"),
            timeout_second=data.get("timeoutSecond"),
            operator=data.get("operator"),
            cluster_task_id=data.get("clusterTaskId"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.task_id is not None:
            _v = self.task_id
            result["taskId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_name is not None:
            _v = self.task_name
            result["taskName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_type is not None:
            _v = self.task_type
            result["taskType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.deleted_at is not None:
            _v = self.deleted_at
            result["deletedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.started_at is not None:
            _v = self.started_at
            result["startedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completion_time is not None:
            _v = self.completion_time
            result["completionTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.progress is not None:
            _v = self.progress
            result["progress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.steps is not None:
            _v = self.steps
            result["steps"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parallelism is not None:
            _v = self.parallelism
            result["parallelism"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.failure_policy is not None:
            _v = self.failure_policy
            result["failurePolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retry_limit is not None:
            _v = self.retry_limit
            result["retryLimit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timeout_second is not None:
            _v = self.timeout_second
            result["timeoutSecond"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator is not None:
            _v = self.operator
            result["operator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_task_id is not None:
            _v = self.cluster_task_id
            result["clusterTaskId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
