# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .environment_condition_status import EnvironmentConditionStatus


@dataclass
class EnvironmentCondition:
    """EnvironmentCondition contains details for the current condition of this environment."""
    # Required fields
    status: EnvironmentConditionStatus
    type_: str
    # Optional fields
    message: Optional[str] = None
    reason: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentCondition":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            message=data.get("message"),
            reason=data.get("reason"),
            status=EnvironmentConditionStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            type_=data.get("type"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reason is not None:
            _v = self.reason
            result["reason"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
