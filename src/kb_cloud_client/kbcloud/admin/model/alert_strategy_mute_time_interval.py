# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class AlertStrategyMuteTimeInterval:
    """AlertStrategyMuteTimeInterval"""
    # Required fields
    # Optional fields
    weekdays: Optional[List[int]] = None
    times: Optional[Dict[str, Any]] = None
    once_minutes: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertStrategyMuteTimeInterval":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            weekdays=data.get("weekdays"),
            times=data.get("times"),
            once_minutes=data.get("onceMinutes"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.weekdays is not None:
            _v = self.weekdays
            result["weekdays"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.times is not None:
            _v = self.times
            result["times"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.once_minutes is not None:
            _v = self.once_minutes
            result["onceMinutes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
