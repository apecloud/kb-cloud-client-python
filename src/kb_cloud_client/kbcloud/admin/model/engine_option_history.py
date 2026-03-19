# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_option import EngineOption


@dataclass
class EngineOptionHistory:
    """EngineOptionHistory"""
    # Required fields
    modifier_id: str
    modifier_email: str
    option: EngineOption
    created_at: datetime
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineOptionHistory":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            modifier_id=data.get("modifierId"),
            modifier_email=data.get("modifierEmail"),
            option=EngineOption.from_dict(data.get("option")) if isinstance(data.get("option"), dict) else data.get("option"),
            created_at=_parse_datetime(data.get("createdAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.modifier_id is not None:
            _v = self.modifier_id
            result["modifierId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modifier_email is not None:
            _v = self.modifier_email
            result["modifierEmail"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.option is not None:
            _v = self.option
            result["option"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
