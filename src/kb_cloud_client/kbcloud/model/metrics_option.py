# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .metrics_option_query import MetricsOptionQuery


@dataclass
class MetricsOption:
    """MetricsOption"""
    # Required fields
    # Optional fields
    replication_lag: Optional[MetricsOptionQuery] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MetricsOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            replication_lag=MetricsOptionQuery.from_dict(data.get("replicationLag")) if isinstance(data.get("replicationLag"), dict) else data.get("replicationLag"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.replication_lag is not None:
            _v = self.replication_lag
            result["replicationLag"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
