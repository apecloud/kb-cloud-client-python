# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .pre_check_result import PreCheckResult
from .pre_check_status import PreCheckStatus
from .pre_check_task_item import PreCheckTaskItem


@dataclass
class PreCheckTaskDetail:
    """PreCheckTaskDetail"""
    # Required fields
    # Optional fields
    task_id: Optional[str] = None
    task_status: Optional[PreCheckStatus] = None
    progress: Optional[int] = None
    checkers: Optional[List[PreCheckTaskItem]] = None
    errors: Optional[List[PreCheckResult]] = None
    warnings: Optional[List[PreCheckResult]] = None
    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreCheckTaskDetail":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            task_id=data.get("taskID"),
            task_status=PreCheckStatus.from_dict(data.get("taskStatus")) if isinstance(data.get("taskStatus"), dict) else data.get("taskStatus"),
            progress=data.get("progress"),
            checkers=[PreCheckTaskItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("checkers")] if data.get("checkers") is not None else None,
            errors=[PreCheckResult.from_dict(i) if isinstance(i, dict) else i for i in data.get("errors")] if data.get("errors") is not None else None,
            warnings=[PreCheckResult.from_dict(i) if isinstance(i, dict) else i for i in data.get("warnings")] if data.get("warnings") is not None else None,
            created_at=_parse_datetime(data.get("createdAt")),
            completed_at=_parse_datetime(data.get("completedAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.task_id is not None:
            _v = self.task_id
            result["taskID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.task_status is not None:
            _v = self.task_status
            result["taskStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.progress is not None:
            _v = self.progress
            result["progress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.checkers is not None:
            _v = self.checkers
            result["checkers"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.errors is not None:
            _v = self.errors
            result["errors"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.warnings is not None:
            _v = self.warnings
            result["warnings"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completed_at is not None:
            _v = self.completed_at
            result["completedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
