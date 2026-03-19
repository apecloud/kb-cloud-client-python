# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .preflight import Preflight


@dataclass
class PreflightList:
    """The preflight results"""
    # Required fields
    # Optional fields
    pass_: Optional[List[Preflight]] = None
    warn: Optional[List[Preflight]] = None
    fail: Optional[List[Preflight]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PreflightList":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            pass_=[Preflight.from_dict(i) if isinstance(i, dict) else i for i in data.get("pass")] if data.get("pass") is not None else None,
            warn=[Preflight.from_dict(i) if isinstance(i, dict) else i for i in data.get("warn")] if data.get("warn") is not None else None,
            fail=[Preflight.from_dict(i) if isinstance(i, dict) else i for i in data.get("fail")] if data.get("fail") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.pass_ is not None:
            _v = self.pass_
            result["pass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.warn is not None:
            _v = self.warn
            result["warn"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.fail is not None:
            _v = self.fail
            result["fail"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
