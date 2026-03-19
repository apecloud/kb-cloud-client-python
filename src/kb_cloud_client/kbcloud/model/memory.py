# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class Memory:
    """Memory"""
    # Required fields
    # Optional fields
    mem_capacity: Optional[str] = None
    memory_limit: Optional[str] = None
    mem_assigned: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Memory":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            mem_capacity=data.get("mem_capacity"),
            memory_limit=data.get("memory_limit"),
            mem_assigned=data.get("mem_assigned"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.mem_capacity is not None:
            _v = self.mem_capacity
            result["mem_capacity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_limit is not None:
            _v = self.memory_limit
            result["memory_limit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mem_assigned is not None:
            _v = self.mem_assigned
            result["mem_assigned"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
