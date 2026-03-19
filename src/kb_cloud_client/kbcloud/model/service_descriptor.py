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
class ServiceDescriptor:
    """serviceDescriptor that will be used in serviceRef. The field definition is in line with kubeblocks."""
    # Required fields
    # Optional fields
    host: Optional[str] = None
    port: Optional[str] = None
    endpoint: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ServiceDescriptor":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            host=data.get("host"),
            port=data.get("port"),
            endpoint=data.get("endpoint"),
            username=data.get("username"),
            password=data.get("password"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.host is not None:
            _v = self.host
            result["host"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.port is not None:
            _v = self.port
            result["port"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint is not None:
            _v = self.endpoint
            result["endpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.username is not None:
            _v = self.username
            result["username"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.password is not None:
            _v = self.password
            result["password"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
