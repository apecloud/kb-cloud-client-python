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
class DmsForeignKeyReference:
    """The reference details of the foreign key"""
    # Required fields
    # Optional fields
    database: Optional[str] = None
    schema: Optional[str] = None
    table: Optional[str] = None
    columns: Optional[List[str]] = None
    match_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsForeignKeyReference":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            database=data.get("database"),
            schema=data.get("schema"),
            table=data.get("table"),
            columns=data.get("columns"),
            match_type=data.get("matchType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.schema is not None:
            _v = self.schema
            result["schema"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.table is not None:
            _v = self.table
            result["table"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.columns is not None:
            _v = self.columns
            result["columns"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.match_type is not None:
            _v = self.match_type
            result["matchType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
