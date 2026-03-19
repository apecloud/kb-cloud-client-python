# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .account_list_role_type import AccountListRoleType
from .redis_privilege_type import RedisPrivilegeType


@dataclass
class ACLUser:
    """ACLUser"""
    # Required fields
    role: AccountListRoleType
    name: str
    # Optional fields
    privileges: Optional[RedisPrivilegeType] = None
    enabled: Optional[bool] = None
    nopass: Optional[bool] = None
    passwords: Optional[List[str]] = None
    password_hashes: Optional[List[str]] = None
    passwords_to_remove: Optional[List[str]] = None
    password_hashes_to_remove: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ACLUser":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            role=AccountListRoleType.from_dict(data.get("role")) if isinstance(data.get("role"), dict) else data.get("role"),
            privileges=RedisPrivilegeType.from_dict(data.get("privileges")) if isinstance(data.get("privileges"), dict) else data.get("privileges"),
            name=data.get("name"),
            enabled=data.get("enabled"),
            nopass=data.get("nopass"),
            passwords=data.get("passwords"),
            password_hashes=data.get("password_hashes"),
            passwords_to_remove=data.get("passwords_to_remove"),
            password_hashes_to_remove=data.get("password_hashes_to_remove"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.role is not None:
            _v = self.role
            result["role"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.privileges is not None:
            _v = self.privileges
            result["privileges"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.nopass is not None:
            _v = self.nopass
            result["nopass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.passwords is not None:
            _v = self.passwords
            result["passwords"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.password_hashes is not None:
            _v = self.password_hashes
            result["password_hashes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.passwords_to_remove is not None:
            _v = self.passwords_to_remove
            result["passwords_to_remove"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.password_hashes_to_remove is not None:
            _v = self.password_hashes_to_remove
            result["password_hashes_to_remove"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
