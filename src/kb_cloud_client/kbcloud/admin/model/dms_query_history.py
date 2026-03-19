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
class DmsQueryHistory:
    """DmsQueryHistory"""
    # Required fields
    # Optional fields
    sql: Optional[str] = None
    err_massage: Optional[str] = None
    created_at: Optional[datetime] = None
    duration: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsQueryHistory":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            sql=data.get("sql"),
            err_massage=data.get("errMassage"),
            created_at=_parse_datetime(data.get("createdAt")),
            duration=data.get("duration"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.sql is not None:
            _v = self.sql
            result["sql"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.err_massage is not None:
            _v = self.err_massage
            result["errMassage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.duration is not None:
            _v = self.duration
            result["duration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
