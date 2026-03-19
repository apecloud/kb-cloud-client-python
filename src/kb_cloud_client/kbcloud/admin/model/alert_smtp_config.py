# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class AlertSMTPConfig:
    """Alert smtp config"""
    # Required fields
    smtp_auth_password: str
    smtp_auth_username: str
    smtp_from: str
    smtp_smarthost: str
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertSMTPConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            smtp_auth_password=data.get("smtp_auth_password"),
            smtp_auth_username=data.get("smtp_auth_username"),
            smtp_from=data.get("smtp_from"),
            smtp_smarthost=data.get("smtp_smarthost"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.smtp_auth_password is not None:
            _v = self.smtp_auth_password
            result["smtp_auth_password"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.smtp_auth_username is not None:
            _v = self.smtp_auth_username
            result["smtp_auth_username"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.smtp_from is not None:
            _v = self.smtp_from
            result["smtp_from"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.smtp_smarthost is not None:
            _v = self.smtp_smarthost
            result["smtp_smarthost"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
