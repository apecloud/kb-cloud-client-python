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
class EventItem:
    """EventItem"""
    # Required fields
    # Optional fields
    event_id: Optional[str] = None
    event_name: Optional[str] = None
    event_time: Optional[datetime] = None
    event_message: Optional[str] = None
    operator: Optional[str] = None
    operator_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EventItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            event_id=data.get("eventID"),
            event_name=data.get("eventName"),
            event_time=_parse_datetime(data.get("eventTime")),
            event_message=data.get("eventMessage"),
            operator=data.get("operator"),
            operator_id=data.get("operatorID"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.event_id is not None:
            _v = self.event_id
            result["eventID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_name is not None:
            _v = self.event_name
            result["eventName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_time is not None:
            _v = self.event_time
            result["eventTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_message is not None:
            _v = self.event_message
            result["eventMessage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator is not None:
            _v = self.operator
            result["operator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator_id is not None:
            _v = self.operator_id
            result["operatorID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
