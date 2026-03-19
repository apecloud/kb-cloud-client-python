# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cdc_network_type import CdcNetworkType


@dataclass
class CdcClusterEndpoint:
    """CdcClusterEndpoint"""
    # Required fields
    # Optional fields
    role: Optional[str] = None
    component: Optional[str] = None
    port_name: Optional[str] = None
    port: Optional[int] = None
    auth_database: Optional[str] = None
    network_type: Optional[CdcNetworkType] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcClusterEndpoint":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            role=data.get("role"),
            component=data.get("component"),
            port_name=data.get("portName"),
            port=data.get("port"),
            auth_database=data.get("authDatabase"),
            network_type=CdcNetworkType.from_dict(data.get("networkType")) if isinstance(data.get("networkType"), dict) else data.get("networkType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.role is not None:
            _v = self.role
            result["role"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.auth_database is not None:
            _v = self.auth_database
            result["authDatabase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_type is not None:
            _v = self.network_type
            result["networkType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
