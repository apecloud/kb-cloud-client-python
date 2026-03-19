# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_options_metrics_query_type import EngineOptionsMetricsQueryType


@dataclass
class MetricsOptionQuery:
    """MetricsOptionQuery"""
    # Required fields
    # Optional fields
    query_pattern: Optional[str] = None
    query_type: Optional[EngineOptionsMetricsQueryType] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MetricsOptionQuery":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            query_pattern=data.get("queryPattern"),
            query_type=EngineOptionsMetricsQueryType.from_dict(data.get("queryType")) if isinstance(data.get("queryType"), dict) else data.get("queryType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.query_pattern is not None:
            _v = self.query_pattern
            result["queryPattern"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query_type is not None:
            _v = self.query_type
            result["queryType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
