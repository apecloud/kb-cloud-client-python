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
class ComponentOptionVersionMinorVersion:
    """ComponentOptionVersionMinorVersion"""
    # Required fields
    # Optional fields
    default: Optional[str] = None
    rollback: Optional[bool] = None
    disable_rollback_pre_release: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentOptionVersionMinorVersion":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            default=data.get("default"),
            rollback=data.get("rollback"),
            disable_rollback_pre_release=data.get("disableRollbackPreRelease"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.default is not None:
            _v = self.default
            result["default"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rollback is not None:
            _v = self.rollback
            result["rollback"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disable_rollback_pre_release is not None:
            _v = self.disable_rollback_pre_release
            result["disableRollbackPreRelease"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
