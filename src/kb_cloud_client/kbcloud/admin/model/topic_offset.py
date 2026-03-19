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
class TopicOffset:
    """TopicOffset"""
    # Required fields
    # Optional fields
    topic: Optional[str] = None
    partition: Optional[int] = None
    consumer_offset: Optional[int] = None
    beginning_offset: Optional[int] = None
    end_offset: Optional[int] = None
    group_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TopicOffset":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            topic=data.get("topic"),
            partition=data.get("partition"),
            consumer_offset=data.get("consumerOffset"),
            beginning_offset=data.get("beginningOffset"),
            end_offset=data.get("endOffset"),
            group_id=data.get("groupId"),
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
        if self.consumer_offset is not None:
            _v = self.consumer_offset
            result["consumerOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.beginning_offset is not None:
            _v = self.beginning_offset
            result["beginningOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.end_offset is not None:
            _v = self.end_offset
            result["endOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.group_id is not None:
            _v = self.group_id
            result["groupId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
