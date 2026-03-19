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
class DmsViewMetadata:
    """DmsViewMetadata"""
    # Required fields
    # Optional fields
    view_name: Optional[str] = None
    database: Optional[str] = None
    replace: Optional[bool] = None
    definer: Optional[str] = None
    sql_security: Optional[str] = None
    check_option: Optional[str] = None
    algorithm: Optional[str] = None
    definition: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsViewMetadata":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            view_name=data.get("viewName"),
            database=data.get("database"),
            replace=data.get("replace"),
            definer=data.get("definer"),
            sql_security=data.get("sqlSecurity"),
            check_option=data.get("checkOption"),
            algorithm=data.get("algorithm"),
            definition=data.get("definition"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.view_name is not None:
            _v = self.view_name
            result["viewName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replace is not None:
            _v = self.replace
            result["replace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.definer is not None:
            _v = self.definer
            result["definer"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sql_security is not None:
            _v = self.sql_security
            result["sqlSecurity"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.check_option is not None:
            _v = self.check_option
            result["checkOption"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.algorithm is not None:
            _v = self.algorithm
            result["algorithm"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.definition is not None:
            _v = self.definition
            result["definition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
