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
class AccountOption:
    """AccountOption"""
    # Required fields
    enabled: bool
    account_name_pattern: str
    create: bool
    reset_password: bool
    delete: bool
    # Optional fields
    max_super_user_account: Optional[int] = None
    privileges: Optional[List[str]] = None
    display_root_account: Optional[bool] = None
    reset_root_password: Optional[bool] = None
    support_multiple_component: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AccountOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            max_super_user_account=data.get("maxSuperUserAccount"),
            enabled=data.get("enabled"),
            privileges=data.get("privileges"),
            account_name_pattern=data.get("accountNamePattern"),
            create=data.get("create"),
            reset_password=data.get("resetPassword"),
            delete=data.get("delete"),
            display_root_account=data.get("displayRootAccount"),
            reset_root_password=data.get("resetRootPassword"),
            support_multiple_component=data.get("supportMultipleComponent"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.max_super_user_account is not None:
            _v = self.max_super_user_account
            result["maxSuperUserAccount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.privileges is not None:
            _v = self.privileges
            result["privileges"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.account_name_pattern is not None:
            _v = self.account_name_pattern
            result["accountNamePattern"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.create is not None:
            _v = self.create
            result["create"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reset_password is not None:
            _v = self.reset_password
            result["resetPassword"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.delete is not None:
            _v = self.delete
            result["delete"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_root_account is not None:
            _v = self.display_root_account
            result["displayRootAccount"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reset_root_password is not None:
            _v = self.reset_root_password
            result["resetRootPassword"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.support_multiple_component is not None:
            _v = self.support_multiple_component
            result["supportMultipleComponent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
