# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .chat_response_type import ChatResponseType


@dataclass
class ChatResponse:
    """Chat message response"""
    # Required fields
    data: Dict[str, Any]
    type_: ChatResponseType
    message_id: str
    parent_id: str
    session_id: str
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChatResponse":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            data=data.get("data"),
            type_=ChatResponseType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            message_id=data.get("messageID"),
            parent_id=data.get("parentID"),
            session_id=data.get("sessionId"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.data is not None:
            _v = self.data
            result["data"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.message_id is not None:
            _v = self.message_id
            result["messageID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parent_id is not None:
            _v = self.parent_id
            result["parentID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.session_id is not None:
            _v = self.session_id
            result["sessionId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
