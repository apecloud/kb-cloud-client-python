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
class StorageDisplayName:
    """the storage displayName"""
    # Required fields
    # Optional fields
    zh: Optional[str] = None
    en: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageDisplayName":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            zh=data.get("zh"),
            en=data.get("en"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.zh is not None:
            _v = self.zh
            result["zh"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.en is not None:
            _v = self.en
            result["en"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
