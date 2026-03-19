# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_maintaince_window import ClusterMaintainceWindow


@dataclass
class ClusterBatchUpdateData:
    """ClusterBatchUpdateData contains the update information to be applied to all clusters in the batch"""
    # Required fields
    # Optional fields
    display_name: Optional[str] = None
    maintaince_window: Optional[ClusterMaintainceWindow] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterBatchUpdateData":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            display_name=data.get("displayName"),
            maintaince_window=ClusterMaintainceWindow.from_dict(data.get("maintainceWindow")) if isinstance(data.get("maintainceWindow"), dict) else data.get("maintainceWindow"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.maintaince_window is not None:
            _v = self.maintaince_window
            result["maintainceWindow"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
