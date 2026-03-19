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
class TopicMessage:
    """TopicMessage"""
    # Required fields
    # Optional fields
    topic: Optional[str] = None
    partition: Optional[int] = None
    offset: Optional[int] = None
    timestamp: Optional[int] = None
    key: Optional[str] = None
    value: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TopicMessage":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            topic=data.get("topic"),
            partition=data.get("partition"),
            offset=data.get("offset"),
            timestamp=data.get("timestamp"),
            key=data.get("key"),
            value=data.get("value"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.topic is not None:
            _v = self.topic
            result["topic"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.partition is not None:
            _v = self.partition
            result["partition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.offset is not None:
            _v = self.offset
            result["offset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.timestamp is not None:
            _v = self.timestamp
            result["timestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.key is not None:
            _v = self.key
            result["key"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.value is not None:
            _v = self.value
            result["value"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
