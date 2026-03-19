# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_batch_update_data import ClusterBatchUpdateData


@dataclass
class ClusterBatchUpdate:
    """ClusterBatchUpdate is the payload for batch updating multiple clusters with the same update information"""
    # Required fields
    names: List[str]
    update: ClusterBatchUpdateData
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterBatchUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            names=data.get("names"),
            update=ClusterBatchUpdateData.from_dict(data.get("update")) if isinstance(data.get("update"), dict) else data.get("update"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.names is not None:
            _v = self.names
            result["names"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.update is not None:
            _v = self.update
            result["update"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
