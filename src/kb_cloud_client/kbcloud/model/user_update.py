# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .phone_number import PhoneNumber


@dataclass
class UserUpdate:
    """User update"""
    # Required fields
    # Optional fields
    display_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            display_name=data.get("displayName"),
            email=data.get("email"),
            phone_number=PhoneNumber.from_dict(data.get("phoneNumber")) if isinstance(data.get("phoneNumber"), dict) else data.get("phoneNumber"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.email is not None:
            _v = self.email
            result["email"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.phone_number is not None:
            _v = self.phone_number
            result["phoneNumber"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
