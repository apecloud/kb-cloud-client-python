# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .load_balancer_available_type import LoadBalancerAvailableType
from .load_balancer_ipam_status import LoadBalancerIpamStatus
from .load_balancer_status import LoadBalancerStatus


@dataclass
class LoadBalancer:
    """The load balancer info"""
    # Required fields
    status: LoadBalancerStatus
    # Optional fields
    version: Optional[str] = None
    type_: Optional[str] = None
    available: Optional[LoadBalancerAvailableType] = None
    class_: Optional[str] = None
    charge_type: Optional[str] = None
    ipam: Optional[LoadBalancerIpamStatus] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LoadBalancer":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            version=data.get("version"),
            type_=data.get("type"),
            status=LoadBalancerStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            available=LoadBalancerAvailableType.from_dict(data.get("available")) if isinstance(data.get("available"), dict) else data.get("available"),
            class_=data.get("class"),
            charge_type=data.get("chargeType"),
            ipam=LoadBalancerIpamStatus.from_dict(data.get("ipam")) if isinstance(data.get("ipam"), dict) else data.get("ipam"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.available is not None:
            _v = self.available
            result["available"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.class_ is not None:
            _v = self.class_
            result["class"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.charge_type is not None:
            _v = self.charge_type
            result["chargeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ipam is not None:
            _v = self.ipam
            result["ipam"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
