# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .dms_pagination import DmsPagination
from .dms_result_stats import DmsResultStats
from .dms_row import DmsRow


@dataclass
class DmsResult:
    """DmsResult"""
    # Required fields
    # Optional fields
    pagination: Optional[DmsPagination] = None
    columns: Optional[List[str]] = None
    rows: Optional[List[List[Dict[str, Any]]]] = None
    stats: Optional[DmsResultStats] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsResult":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            pagination=DmsPagination.from_dict(data.get("pagination")) if isinstance(data.get("pagination"), dict) else data.get("pagination"),
            columns=data.get("columns"),
            rows=[DmsRow.from_dict(i) if isinstance(i, dict) else i for i in data.get("rows")] if data.get("rows") is not None else None,
            stats=DmsResultStats.from_dict(data.get("stats")) if isinstance(data.get("stats"), dict) else data.get("stats"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.pagination is not None:
            _v = self.pagination
            result["pagination"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.columns is not None:
            _v = self.columns
            result["columns"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rows is not None:
            _v = self.rows
            result["rows"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.stats is not None:
            _v = self.stats
            result["stats"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
