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
class DmsResultStats:
    """DmsResultStats"""
    # Required fields
    # Optional fields
    columns_count: Optional[int] = None
    rows_count: Optional[int] = None
    rows_affected: Optional[int] = None
    query_start_time: Optional[datetime] = None
    query_finish_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsResultStats":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            columns_count=data.get("columns_count"),
            rows_count=data.get("rows_count"),
            rows_affected=data.get("rows_affected"),
            query_start_time=_parse_datetime(data.get("query_start_time")),
            query_finish_time=_parse_datetime(data.get("query_finish_time")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.columns_count is not None:
            _v = self.columns_count
            result["columns_count"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rows_count is not None:
            _v = self.rows_count
            result["rows_count"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rows_affected is not None:
            _v = self.rows_affected
            result["rows_affected"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query_start_time is not None:
            _v = self.query_start_time
            result["query_start_time"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query_finish_time is not None:
            _v = self.query_finish_time
            result["query_finish_time"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
