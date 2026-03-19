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
class ClassBatch:
    """ClassBatch"""
    # Required fields
    # Optional fields
    engine: Optional[str] = None
    mode: Optional[str] = None
    component: Optional[str] = None
    class_type: Optional[str] = None
    cpu_over_commit: Optional[float] = None
    memory_over_commit: Optional[float] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClassBatch":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine=data.get("engine"),
            mode=data.get("mode"),
            component=data.get("component"),
            class_type=data.get("classType"),
            cpu_over_commit=data.get("cpuOverCommit"),
            memory_over_commit=data.get("memoryOverCommit"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.class_type is not None:
            _v = self.class_type
            result["classType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_over_commit is not None:
            _v = self.cpu_over_commit
            result["cpuOverCommit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_over_commit is not None:
            _v = self.memory_over_commit
            result["memoryOverCommit"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
