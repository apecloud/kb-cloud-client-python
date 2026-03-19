# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .key import Key
from .page_result import PageResult


@dataclass
class KeyList:
    """key list"""
    # Required fields
    items: List[Key]
    # Optional fields
    page_result: Optional[PageResult] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KeyList":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            items=[Key.from_dict(i) if isinstance(i, dict) else i for i in data.get("items")] if data.get("items") is not None else None,
            page_result=PageResult.from_dict(data.get("pageResult")) if isinstance(data.get("pageResult"), dict) else data.get("pageResult"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.items is not None:
            _v = self.items
            result["items"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.page_result is not None:
            _v = self.page_result
            result["pageResult"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
