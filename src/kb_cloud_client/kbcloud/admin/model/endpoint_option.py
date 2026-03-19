# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_options_service_pattern import EngineOptionsServicePattern
from .localized_description import LocalizedDescription


@dataclass
class EndpointOption:
    """EndpointOption"""
    # Required fields
    title: LocalizedDescription
    component: str
    port_name: str
    port: int
    protocol: str
    target_port: str
    type_: List[str]
    # Optional fields
    supports_system_use: Optional[bool] = None
    supports_readonly: Optional[bool] = None
    service_pattern: Optional[EngineOptionsServicePattern] = None
    service_name_regex: Optional[str] = None
    service_name: Optional[str] = None
    selector: Optional[Dict[str, str]] = None
    follow_network_mode: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EndpointOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            title=LocalizedDescription.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            component=data.get("component"),
            port_name=data.get("portName"),
            port=data.get("port"),
            protocol=data.get("protocol"),
            target_port=data.get("targetPort"),
            type_=data.get("type"),
            supports_system_use=data.get("supportsSystemUse"),
            supports_readonly=data.get("supportsReadonly"),
            service_pattern=EngineOptionsServicePattern.from_dict(data.get("servicePattern")) if isinstance(data.get("servicePattern"), dict) else data.get("servicePattern"),
            service_name_regex=data.get("serviceNameRegex"),
            service_name=data.get("serviceName"),
            selector=data.get("selector"),
            follow_network_mode=data.get("followNetworkMode"),
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
        if self.port_name is not None:
            _v = self.port_name
            result["portName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.port is not None:
            _v = self.port
            result["port"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.protocol is not None:
            _v = self.protocol
            result["protocol"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_port is not None:
            _v = self.target_port
            result["targetPort"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.supports_system_use is not None:
            _v = self.supports_system_use
            result["supportsSystemUse"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.supports_readonly is not None:
            _v = self.supports_readonly
            result["supportsReadonly"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_pattern is not None:
            _v = self.service_pattern
            result["servicePattern"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_name_regex is not None:
            _v = self.service_name_regex
            result["serviceNameRegex"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_name is not None:
            _v = self.service_name
            result["serviceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.selector is not None:
            _v = self.selector
            result["selector"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.follow_network_mode is not None:
            _v = self.follow_network_mode
            result["followNetworkMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
