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
class DataChannelObject:
    """DataChannelObject"""
    # Required fields
    # Optional fields
    include_objects: Optional[List[str]] = None
    exclude_objects: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelObject":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            include_objects=data.get("includeObjects"),
            exclude_objects=data.get("excludeObjects"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.include_objects is not None:
            _v = self.include_objects
            result["includeObjects"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.exclude_objects is not None:
            _v = self.exclude_objects
            result["excludeObjects"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
