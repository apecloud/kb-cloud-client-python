# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_replication_create import DataReplicationCreate


@dataclass
class DataReplicationUpdate:
    """DataReplicationUpdate"""
    # Required fields
    # Optional fields
    cluster_updates: Optional[DataReplicationCreate] = None
    is_restart: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataReplicationUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cluster_updates=DataReplicationCreate.from_dict(data.get("clusterUpdates")) if isinstance(data.get("clusterUpdates"), dict) else data.get("clusterUpdates"),
            is_restart=data.get("isRestart"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cluster_updates is not None:
            _v = self.cluster_updates
            result["clusterUpdates"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_restart is not None:
            _v = self.is_restart
            result["isRestart"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
