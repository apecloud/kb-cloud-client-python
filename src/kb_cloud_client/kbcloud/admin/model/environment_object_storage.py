# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .raw_cluster import RawCluster


@dataclass
class EnvironmentObjectStorage:
    """EnvironmentObjectStorage"""
    # Required fields
    # Optional fields
    clusters: Optional[List[RawCluster]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentObjectStorage":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            clusters=[RawCluster.from_dict(i) if isinstance(i, dict) else i for i in data.get("clusters")] if data.get("clusters") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.clusters is not None:
            _v = self.clusters
            result["clusters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
