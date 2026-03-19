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
class OrgMemberAdd:
    """MemberAdd is the payload for adding organization member"""
    # Required fields
    role: str
    user_name: str
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OrgMemberAdd":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            role=data.get("role"),
            user_name=data.get("userName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.role is not None:
            _v = self.role
            result["role"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.user_name is not None:
            _v = self.user_name
            result["userName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
