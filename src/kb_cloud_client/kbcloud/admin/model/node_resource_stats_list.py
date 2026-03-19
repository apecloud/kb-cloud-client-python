# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .node_resource_stats import NodeResourceStats


@dataclass
class NodeResourceStatsList:
    """NodeResourceStatsList is a list of NodeResourceStats"""
    # Required fields
    items: List[NodeResourceStats]
    updated_at: datetime
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NodeResourceStatsList":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            items=[NodeResourceStats.from_dict(i) if isinstance(i, dict) else i for i in data.get("items")] if data.get("items") is not None else None,
            updated_at=_parse_datetime(data.get("updatedAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.items is not None:
            _v = self.items
            result["items"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
