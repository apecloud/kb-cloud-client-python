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
class ScaleInHealthCheck:
    """ScaleInHealthCheck"""
    # Required fields
    # Optional fields
    enabled: Optional[bool] = None
    healthy_threshold: Optional[int] = None
    unhealthy_threshold: Optional[int] = None
    interval: Optional[str] = None
    timeout: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ScaleInHealthCheck":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enabled=data.get("enabled"),
            healthy_threshold=data.get("healthyThreshold"),
            unhealthy_threshold=data.get("unhealthyThreshold"),
            interval=data.get("interval"),
            timeout=data.get("timeout"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.healthy_threshold is not None:
            _v = self.healthy_threshold
            result["healthyThreshold"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.unhealthy_threshold is not None:
            _v = self.unhealthy_threshold
            result["unhealthyThreshold"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.interval is not None:
            _v = self.interval
            result["interval"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timeout is not None:
            _v = self.timeout
            result["timeout"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
