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
class CdcSqlExecutor:
    """CdcSqlExecutor"""
    # Required fields
    # Optional fields
    sql: Optional[List[str]] = None
    result: Optional[List[str]] = None
    auth_database: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CdcSqlExecutor":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            sql=data.get("sql"),
            result=data.get("result"),
            auth_database=data.get("authDatabase"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.sql is not None:
            _v = self.sql
            result["sql"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.result is not None:
            _v = self.result
            result["result"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auth_database is not None:
            _v = self.auth_database
            result["authDatabase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
