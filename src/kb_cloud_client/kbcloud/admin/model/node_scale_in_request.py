# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .scale_in_strategy import ScaleInStrategy


@dataclass
class NodeScaleInRequest:
    """NodeScaleInRequest"""
    # Required fields
    nodes: List[str]
    # Optional fields
    drain: Optional[bool] = None
    strategy: Optional[ScaleInStrategy] = None
    force: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NodeScaleInRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            nodes=data.get("nodes"),
            drain=data.get("drain"),
            strategy=ScaleInStrategy.from_dict(data.get("strategy")) if isinstance(data.get("strategy"), dict) else data.get("strategy"),
            force=data.get("force"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.nodes is not None:
            _v = self.nodes
            result["nodes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.drain is not None:
            _v = self.drain
            result["drain"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.strategy is not None:
            _v = self.strategy
            result["strategy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.force is not None:
            _v = self.force
            result["force"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
