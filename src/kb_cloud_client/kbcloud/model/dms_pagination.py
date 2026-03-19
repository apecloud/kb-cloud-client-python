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
class DmsPagination:
    """DmsPagination"""
    # Required fields
    # Optional fields
    rows_count: Optional[int] = None
    page: Optional[int] = None
    pages_count: Optional[int] = None
    per_page: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsPagination":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            rows_count=data.get("rows_count"),
            page=data.get("page"),
            pages_count=data.get("pages_count"),
            per_page=data.get("per_page"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.rows_count is not None:
            _v = self.rows_count
            result["rows_count"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.page is not None:
            _v = self.page
            result["page"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pages_count is not None:
            _v = self.pages_count
            result["pages_count"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.per_page is not None:
            _v = self.per_page
            result["per_page"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
