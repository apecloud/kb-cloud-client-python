# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .broker_node import BrokerNode


@dataclass
class Partition:
    """Partition"""
    # Required fields
    id_: int
    leader: BrokerNode
    # Optional fields
    replicas: Optional[List[BrokerNode]] = None
    isr: Optional[List[BrokerNode]] = None
    beginning_offset: Optional[int] = None
    end_offset: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Partition":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            leader=BrokerNode.from_dict(data.get("leader")) if isinstance(data.get("leader"), dict) else data.get("leader"),
            replicas=[BrokerNode.from_dict(i) if isinstance(i, dict) else i for i in data.get("replicas")] if data.get("replicas") is not None else None,
            isr=[BrokerNode.from_dict(i) if isinstance(i, dict) else i for i in data.get("isr")] if data.get("isr") is not None else None,
            beginning_offset=data.get("beginningOffset"),
            end_offset=data.get("endOffset"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.leader is not None:
            _v = self.leader
            result["leader"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.isr is not None:
            _v = self.isr
            result["isr"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        return result
