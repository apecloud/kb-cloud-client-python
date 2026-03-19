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
class EngineDefinitionVersionQuery:
    """EngineDefinitionVersionQuery"""
    # Required fields
    # Optional fields
    sql: Optional[str] = None
    column: Optional[str] = None
    regex: Optional[str] = None
    min: Optional[float] = None
    max: Optional[float] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineDefinitionVersionQuery":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            sql=data.get("sql"),
            column=data.get("column"),
            regex=data.get("regex"),
            min=data.get("min"),
            max=data.get("max"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.sql is not None:
            _v = self.sql
            result["sql"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.column is not None:
            _v = self.column
            result["column"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.regex is not None:
            _v = self.regex
            result["regex"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.min is not None:
            _v = self.min
            result["min"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.max is not None:
            _v = self.max
            result["max"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
