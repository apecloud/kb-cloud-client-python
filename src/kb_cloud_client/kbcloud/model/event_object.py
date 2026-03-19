# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .event_type import EventType


@dataclass
class EventObject:
    """EventObject"""
    # Required fields
    # Optional fields
    event_type: Optional[EventType] = None
    event_value: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EventObject":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            event_type=EventType.from_dict(data.get("eventType")) if isinstance(data.get("eventType"), dict) else data.get("eventType"),
            event_value=data.get("eventValue"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.event_type is not None:
            _v = self.event_type
            result["eventType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.event_value is not None:
            _v = self.event_value
            result["eventValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
