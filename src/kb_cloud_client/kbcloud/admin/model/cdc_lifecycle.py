# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cdc_lifecycle_action import CdcLifecycleAction


@dataclass
class CdcLifecycle:
    """CdcLifecycle"""
    # Required fields
    # Optional fields
    pre_start: Optional[CdcLifecycleAction] = None
    post_start: Optional[CdcLifecycleAction] = None
    pre_stop: Optional[CdcLifecycleAction] = None
    post_stop: Optional[CdcLifecycleAction] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcLifecycle":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            pre_start=CdcLifecycleAction.from_dict(data.get("preStart")) if isinstance(data.get("preStart"), dict) else data.get("preStart"),
            post_start=CdcLifecycleAction.from_dict(data.get("postStart")) if isinstance(data.get("postStart"), dict) else data.get("postStart"),
            pre_stop=CdcLifecycleAction.from_dict(data.get("preStop")) if isinstance(data.get("preStop"), dict) else data.get("preStop"),
            post_stop=CdcLifecycleAction.from_dict(data.get("postStop")) if isinstance(data.get("postStop"), dict) else data.get("postStop"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.pre_start is not None:
            _v = self.pre_start
            result["preStart"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.post_start is not None:
            _v = self.post_start
            result["postStart"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pre_stop is not None:
            _v = self.pre_stop
            result["preStop"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.post_stop is not None:
            _v = self.post_stop
            result["postStop"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
