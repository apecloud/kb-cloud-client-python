# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .scale_in_health_check import ScaleInHealthCheck
from .scale_in_type import ScaleInType


@dataclass
class ScaleInStrategy:
    """ScaleInStrategy"""
    # Required fields
    # Optional fields
    type_: Optional[ScaleInType] = None
    max_unavailable: Optional[str] = None
    max_surge: Optional[str] = None
    drain_timeout: Optional[str] = None
    pod_eviction_wait_time: Optional[str] = None
    min_ready_seconds: Optional[int] = None
    health_check: Optional[ScaleInHealthCheck] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ScaleInStrategy":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            type_=ScaleInType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            max_unavailable=data.get("maxUnavailable"),
            max_surge=data.get("maxSurge"),
            drain_timeout=data.get("drainTimeout"),
            pod_eviction_wait_time=data.get("podEvictionWaitTime"),
            min_ready_seconds=data.get("minReadySeconds"),
            health_check=ScaleInHealthCheck.from_dict(data.get("healthCheck")) if isinstance(data.get("healthCheck"), dict) else data.get("healthCheck"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.max_unavailable is not None:
            _v = self.max_unavailable
            result["maxUnavailable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.max_surge is not None:
            _v = self.max_surge
            result["maxSurge"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.drain_timeout is not None:
            _v = self.drain_timeout
            result["drainTimeout"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_eviction_wait_time is not None:
            _v = self.pod_eviction_wait_time
            result["podEvictionWaitTime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.min_ready_seconds is not None:
            _v = self.min_ready_seconds
            result["minReadySeconds"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.health_check is not None:
            _v = self.health_check
            result["healthCheck"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
