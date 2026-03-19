# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class AlertStatistic:
    """AlertStatistic"""
    # Required fields
    # Optional fields
    total: Optional[int] = None
    critical: Optional[int] = None
    warning: Optional[int] = None
    info: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertStatistic":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            total=data.get("total"),
            critical=data.get("critical"),
            warning=data.get("warning"),
            info=data.get("info"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.total is not None:
            _v = self.total
            result["total"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.critical is not None:
            _v = self.critical
            result["critical"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.warning is not None:
            _v = self.warning
            result["warning"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.info is not None:
            _v = self.info
            result["info"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
