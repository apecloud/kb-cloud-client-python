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
class RestoreStatus:
    """restore status"""
    # Required fields
    # Optional fields
    actions: Optional[List[Dict[str, Any]]] = None
    completion_timestamp: Optional[datetime] = None
    conditions: Optional[List[Dict[str, Any]]] = None
    phase: Optional[str] = None
    start_timestamp: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RestoreStatus":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            actions=data.get("actions"),
            completion_timestamp=_parse_datetime(data.get("completionTimestamp")),
            conditions=data.get("conditions"),
            phase=data.get("phase"),
            start_timestamp=_parse_datetime(data.get("startTimestamp")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.actions is not None:
            _v = self.actions
            result["actions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.completion_timestamp is not None:
            _v = self.completion_timestamp
            result["completionTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.conditions is not None:
            _v = self.conditions
            result["conditions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.phase is not None:
            _v = self.phase
            result["phase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.start_timestamp is not None:
            _v = self.start_timestamp
            result["startTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
