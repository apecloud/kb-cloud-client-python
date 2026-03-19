# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .auth_type import AuthType
from .basic_auth_model import BasicAuthModel


@dataclass
class CustomEndpointCreate:
    """CustomEndpointCreate"""
    # Required fields
    # Optional fields
    connection: Optional[str] = None
    auth_type: Optional[AuthType] = None
    basic_auth: Optional[BasicAuthModel] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomEndpointCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            connection=data.get("connection"),
            auth_type=AuthType.from_dict(data.get("authType")) if isinstance(data.get("authType"), dict) else data.get("authType"),
            basic_auth=BasicAuthModel.from_dict(data.get("basicAuth")) if isinstance(data.get("basicAuth"), dict) else data.get("basicAuth"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.connection is not None:
            _v = self.connection
            result["connection"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auth_type is not None:
            _v = self.auth_type
            result["authType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.basic_auth is not None:
            _v = self.basic_auth
            result["basicAuth"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
