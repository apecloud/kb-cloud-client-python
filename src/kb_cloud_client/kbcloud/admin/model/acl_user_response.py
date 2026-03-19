# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .acl_user import ACLUser


@dataclass
class ACLUserResponse:
    """ACLUserResponse"""
    # Required fields
    # Optional fields
    mode: Optional[str] = None
    master: Optional[List[ACLUser]] = None
    sentinel: Optional[List[ACLUser]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ACLUserResponse":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            mode=data.get("mode"),
            master=[ACLUser.from_dict(i) if isinstance(i, dict) else i for i in data.get("master")] if data.get("master") is not None else None,
            sentinel=[ACLUser.from_dict(i) if isinstance(i, dict) else i for i in data.get("sentinel")] if data.get("sentinel") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.master is not None:
            _v = self.master
            result["master"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sentinel is not None:
            _v = self.sentinel
            result["sentinel"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
