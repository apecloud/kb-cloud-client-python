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
class ConsumerGroupDescribe:
    """ConsumerGroupDescribe"""
    # Required fields
    # Optional fields
    group_id: Optional[str] = None
    topic: Optional[str] = None
    partition: Optional[int] = None
    current_offset: Optional[int] = None
    log_beginning_offset: Optional[int] = None
    log_end_offset: Optional[int] = None
    lag: Optional[int] = None
    consumer_id: Optional[str] = None
    host: Optional[str] = None
    client_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConsumerGroupDescribe":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            group_id=data.get("groupId"),
            topic=data.get("topic"),
            partition=data.get("partition"),
            current_offset=data.get("currentOffset"),
            log_beginning_offset=data.get("logBeginningOffset"),
            log_end_offset=data.get("logEndOffset"),
            lag=data.get("lag"),
            consumer_id=data.get("consumerId"),
            host=data.get("host"),
            client_id=data.get("clientId"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.group_id is not None:
            _v = self.group_id
            result["groupId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
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
        if self.current_offset is not None:
            _v = self.current_offset
            result["currentOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_beginning_offset is not None:
            _v = self.log_beginning_offset
            result["logBeginningOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.log_end_offset is not None:
            _v = self.log_end_offset
            result["logEndOffset"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.lag is not None:
            _v = self.lag
            result["lag"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.consumer_id is not None:
            _v = self.consumer_id
            result["consumerId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.host is not None:
            _v = self.host
            result["host"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.client_id is not None:
            _v = self.client_id
            result["clientId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
