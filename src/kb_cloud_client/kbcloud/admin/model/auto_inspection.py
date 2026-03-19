# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .auto_inspection_resource_type import AutoInspectionResourceType
from .auto_inspection_run_unit import AutoInspectionRunUnit


@dataclass
class AutoInspection:
    """AutoInspection"""
    # Required fields
    resource_type: AutoInspectionResourceType
    resource_name: str
    creator: str
    enabled: bool
    # Optional fields
    id_: Optional[str] = None
    resource_id: Optional[str] = None
    schedule: Optional[str] = None
    run_every: Optional[AutoInspectionRunUnit] = None
    days_of_week: Optional[List[int]] = None
    days_of_month: Optional[List[int]] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    saved_days: Optional[int] = None
    next_run_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AutoInspection":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            resource_type=AutoInspectionResourceType.from_dict(data.get("resourceType")) if isinstance(data.get("resourceType"), dict) else data.get("resourceType"),
            resource_id=data.get("resourceID"),
            resource_name=data.get("resourceName"),
            creator=data.get("creator"),
            schedule=data.get("schedule"),
            run_every=AutoInspectionRunUnit.from_dict(data.get("runEvery")) if isinstance(data.get("runEvery"), dict) else data.get("runEvery"),
            days_of_week=data.get("daysOfWeek"),
            days_of_month=data.get("daysOfMonth"),
            hour=data.get("hour"),
            minute=data.get("minute"),
            saved_days=data.get("savedDays"),
            next_run_time=_parse_datetime(data.get("nextRunTime")),
            enabled=data.get("enabled"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_type is not None:
            _v = self.resource_type
            result["resourceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_id is not None:
            _v = self.resource_id
            result["resourceID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resource_name is not None:
            _v = self.resource_name
            result["resourceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.creator is not None:
            _v = self.creator
            result["creator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.schedule is not None:
            _v = self.schedule
            result["schedule"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.run_every is not None:
            _v = self.run_every
            result["runEvery"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.days_of_week is not None:
            _v = self.days_of_week
            result["daysOfWeek"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.days_of_month is not None:
            _v = self.days_of_month
            result["daysOfMonth"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hour is not None:
            _v = self.hour
            result["hour"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.minute is not None:
            _v = self.minute
            result["minute"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.saved_days is not None:
            _v = self.saved_days
            result["savedDays"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.next_run_time is not None:
            _v = self.next_run_time
            result["nextRunTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
