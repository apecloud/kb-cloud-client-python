# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_quota import EngineQuota


@dataclass
class License:
    """License info"""
    # Required fields
    cluster_id: str
    email: str
    user_name: str
    unit: str
    quantity: str
    engines: List[EngineQuota]
    not_after: datetime
    not_before: datetime
    used: float
    license: str
    # Optional fields
    mode: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "License":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cluster_id=data.get("clusterID"),
            email=data.get("email"),
            user_name=data.get("userName"),
            unit=data.get("unit"),
            quantity=data.get("quantity"),
            engines=[EngineQuota.from_dict(i) if isinstance(i, dict) else i for i in data.get("engines")] if data.get("engines") is not None else None,
            not_after=_parse_datetime(data.get("notAfter")),
            not_before=_parse_datetime(data.get("notBefore")),
            used=data.get("used"),
            license=data.get("license"),
            mode=data.get("mode"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.email is not None:
            _v = self.email
            result["email"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.user_name is not None:
            _v = self.user_name
            result["userName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.unit is not None:
            _v = self.unit
            result["unit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.quantity is not None:
            _v = self.quantity
            result["quantity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engines is not None:
            _v = self.engines
            result["engines"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_after is not None:
            _v = self.not_after
            result["notAfter"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_before is not None:
            _v = self.not_before
            result["notBefore"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.used is not None:
            _v = self.used
            result["used"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.license is not None:
            _v = self.license
            result["license"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
