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
class BackupStatsType:
    """Totalsize and number of backups for the backup type"""
    # Required fields
    # Optional fields
    type_: Optional[str] = None
    size: Optional[str] = None
    num: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BackupStatsType":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            type_=data.get("type"),
            size=data.get("size"),
            num=data.get("num"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.size is not None:
            _v = self.size
            result["size"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.num is not None:
            _v = self.num
            result["num"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
