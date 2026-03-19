# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ops_expose_type import OpsExposeType
from .ops_expose_vpc_service_type import OpsExposeVPCServiceType


@dataclass
class OpsExpose:
    """OpsExpose is the payload to expose a KubeBlocks cluster"""
    # Required fields
    component: str
    enable: bool
    type_: OpsExposeType
    # Optional fields
    readonly: Optional[bool] = None
    vpc_service_type: Optional[OpsExposeVPCServiceType] = None
    ports_mapping: Optional[List[Dict[str, Any]]] = None
    load_balancer_ip: Optional[str] = None
    load_balancer_ip_pool_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsExpose":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            enable=data.get("enable"),
            readonly=data.get("readonly"),
            type_=OpsExposeType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            vpc_service_type=OpsExposeVPCServiceType.from_dict(data.get("vpcServiceType")) if isinstance(data.get("vpcServiceType"), dict) else data.get("vpcServiceType"),
            ports_mapping=data.get("portsMapping"),
            load_balancer_ip=data.get("loadBalancerIP"),
            load_balancer_ip_pool_id=data.get("loadBalancerIPPoolID"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enable is not None:
            _v = self.enable
            result["enable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.readonly is not None:
            _v = self.readonly
            result["readonly"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.vpc_service_type is not None:
            _v = self.vpc_service_type
            result["vpcServiceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ports_mapping is not None:
            _v = self.ports_mapping
            result["portsMapping"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.load_balancer_ip is not None:
            _v = self.load_balancer_ip
            result["loadBalancerIP"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.load_balancer_ip_pool_id is not None:
            _v = self.load_balancer_ip_pool_id
            result["loadBalancerIPPoolID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
