# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .pre_check_status import PreCheckStatus


@dataclass
class PreCheckTaskItem:
    """PreCheckTaskItem"""
    # Required fields
    # Optional fields
    checker_name: Optional[str] = None
    checker_desc: Optional[str] = None
    message: Optional[str] = None
    status: Optional[PreCheckStatus] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreCheckTaskItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            checker_name=data.get("checkerName"),
            checker_desc=data.get("checkerDesc"),
            message=data.get("message"),
            status=PreCheckStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.checker_name is not None:
            _v = self.checker_name
            result["checkerName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.checker_desc is not None:
            _v = self.checker_desc
            result["checkerDesc"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message is not None:
            _v = self.message
            result["message"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
