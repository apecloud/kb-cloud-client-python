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
class SshConfigCheckResult:
    """SshConfigCheckResult"""
    # Required fields
    ip: str
    reachable: bool
    # Optional fields
    message: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SshConfigCheckResult":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            ip=data.get("ip"),
            reachable=data.get("reachable"),
            message=data.get("message"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.ip is not None:
            _v = self.ip
            result["ip"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reachable is not None:
            _v = self.reachable
            result["reachable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
