# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .task_status import TaskStatus


@dataclass
class TaskStep:
    """TaskStep"""
    # Required fields
    step_id: str
    step_name: str
    method_name: str
    inputs: Dict[str, str]
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    # Optional fields
    outputs: Optional[Dict[str, str]] = None
    retry_limit: Optional[int] = None
    curr_retry_count: Optional[int] = None
    timeout_second: Optional[int] = None
    message: Optional[str] = None
    started_at: Optional[datetime] = None
    completion_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TaskStep":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            step_id=data.get("stepId"),
            step_name=data.get("stepName"),
            method_name=data.get("methodName"),
            inputs=data.get("inputs"),
            outputs=data.get("outputs"),
            retry_limit=data.get("retryLimit"),
            curr_retry_count=data.get("currRetryCount"),
            timeout_second=data.get("timeoutSecond"),
            status=TaskStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            message=data.get("message"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            started_at=_parse_datetime(data.get("startedAt")),
            completion_time=_parse_datetime(data.get("completionTime")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.step_id is not None:
            _v = self.step_id
            result["stepId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.step_name is not None:
            _v = self.step_name
            result["stepName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.method_name is not None:
            _v = self.method_name
            result["methodName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.inputs is not None:
            _v = self.inputs
            result["inputs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.outputs is not None:
            _v = self.outputs
            result["outputs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.retry_limit is not None:
            _v = self.retry_limit
            result["retryLimit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.curr_retry_count is not None:
            _v = self.curr_retry_count
            result["currRetryCount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timeout_second is not None:
            _v = self.timeout_second
            result["timeoutSecond"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        return result
