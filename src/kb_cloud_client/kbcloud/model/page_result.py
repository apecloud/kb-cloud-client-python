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
class PageResult:
    """PageResult info"""
    # Required fields
    # Optional fields
    first: Optional[str] = None
    last: Optional[str] = None
    next: Optional[str] = None
    prev: Optional[str] = None
    total_size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PageResult":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            first=data.get("first"),
            last=data.get("last"),
            next=data.get("next"),
            prev=data.get("prev"),
            total_size=data.get("totalSize"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.first is not None:
            _v = self.first
            result["first"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.last is not None:
            _v = self.last
            result["last"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.next is not None:
            _v = self.next
            result["next"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.prev is not None:
            _v = self.prev
            result["prev"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_size is not None:
            _v = self.total_size
            result["totalSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
