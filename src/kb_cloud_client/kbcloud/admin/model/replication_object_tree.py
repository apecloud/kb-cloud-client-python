# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .replication_object_node import ReplicationObjectNode


@dataclass
class ReplicationObjectTree:
    """ReplicationObjectTree"""
    # Required fields
    # Optional fields
    node_type: Optional[str] = None
    node_values: Optional[List[ReplicationObjectNode]] = None
    children_node_types: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ReplicationObjectTree":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            node_type=data.get("nodeType"),
            node_values=[ReplicationObjectNode.from_dict(i) if isinstance(i, dict) else i for i in data.get("nodeValues")] if data.get("nodeValues") is not None else None,
            children_node_types=data.get("childrenNodeTypes"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.node_type is not None:
            _v = self.node_type
            result["nodeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_values is not None:
            _v = self.node_values
            result["nodeValues"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.children_node_types is not None:
            _v = self.children_node_types
            result["childrenNodeTypes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
