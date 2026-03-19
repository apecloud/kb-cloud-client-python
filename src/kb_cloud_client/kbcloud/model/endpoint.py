# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .endpoint_network_type import EndpointNetworkType
from .endpoint_type import EndpointType


@dataclass
class Endpoint:
    """Endpoint is the information of cluster endpoints"""
    # Required fields
    title: str
    component: str
    hosts: List[str]
    port: int
    type_: EndpointType
    network_type: EndpointNetworkType
    service_name: str
    port_name: str
    mutable: bool
    # Optional fields
    pod_service: Optional[bool] = None
    instances: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Endpoint":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            title=data.get("title"),
            component=data.get("component"),
            hosts=data.get("hosts"),
            port=data.get("port"),
            type_=EndpointType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            network_type=EndpointNetworkType.from_dict(data.get("networkType")) if isinstance(data.get("networkType"), dict) else data.get("networkType"),
            service_name=data.get("serviceName"),
            pod_service=data.get("podService"),
            port_name=data.get("portName"),
            instances=data.get("instances"),
            mutable=data.get("mutable"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hosts is not None:
            _v = self.hosts
            result["hosts"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.port is not None:
            _v = self.port
            result["port"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_type is not None:
            _v = self.network_type
            result["networkType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_name is not None:
            _v = self.service_name
            result["serviceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_service is not None:
            _v = self.pod_service
            result["podService"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.port_name is not None:
            _v = self.port_name
            result["portName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.instances is not None:
            _v = self.instances
            result["instances"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mutable is not None:
            _v = self.mutable
            result["mutable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
