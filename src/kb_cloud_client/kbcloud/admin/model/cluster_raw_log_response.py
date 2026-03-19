# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_log_pagination import ClusterLogPagination
from .cluster_raw_log_item import ClusterRawLogItem


@dataclass
class ClusterRawLogResponse:
    """Cluster raw log is the raw log of the cluster"""
    # Required fields
    # Optional fields
    filenames: Optional[List[str]] = None
    items: Optional[List[ClusterRawLogItem]] = None
    pagination: Optional[ClusterLogPagination] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterRawLogResponse":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            filenames=data.get("filenames"),
            items=[ClusterRawLogItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("items")] if data.get("items") is not None else None,
            pagination=ClusterLogPagination.from_dict(data.get("pagination")) if isinstance(data.get("pagination"), dict) else data.get("pagination"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.filenames is not None:
            _v = self.filenames
            result["filenames"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.items is not None:
            _v = self.items
            result["items"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pagination is not None:
            _v = self.pagination
            result["pagination"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
