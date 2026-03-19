# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class AlertMetric:
    """Alert metric information"""
    # Required fields
    key: str
    # Optional fields
    threshold: Optional[int] = None
    notation: Optional[str] = None
    category: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertMetric":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            key=data.get("key"),
            threshold=data.get("threshold"),
            notation=data.get("notation"),
            category=data.get("category"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.key is not None:
            _v = self.key
            result["key"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.threshold is not None:
            _v = self.threshold
            result["threshold"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.notation is not None:
            _v = self.notation
            result["notation"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.category is not None:
            _v = self.category
            result["category"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
