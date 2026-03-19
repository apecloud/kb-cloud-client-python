# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .persistent_volume_claim import PersistentVolumeClaim


@dataclass
class PersistentVolumeClaimList:
    """the List stands for stats for persistentvolumeclaims."""
    # Required fields
    # Optional fields
    items: Optional[List[PersistentVolumeClaim]] = None
    current_page: Optional[int] = None
    total_page: Optional[int] = None
    page_size: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PersistentVolumeClaimList":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            items=[PersistentVolumeClaim.from_dict(i) if isinstance(i, dict) else i for i in data.get("items")] if data.get("items") is not None else None,
            current_page=data.get("currentPage"),
            total_page=data.get("totalPage"),
            page_size=data.get("pageSize"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.items is not None:
            _v = self.items
            result["items"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.current_page is not None:
            _v = self.current_page
            result["currentPage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_page is not None:
            _v = self.total_page
            result["totalPage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.page_size is not None:
            _v = self.page_size
            result["pageSize"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
