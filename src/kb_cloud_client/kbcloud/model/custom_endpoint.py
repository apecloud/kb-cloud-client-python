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
class CustomEndpoint:
    """CustomEndpoint"""
    # Required fields
    # Optional fields
    connection_string: Optional[str] = None
    user_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomEndpoint":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            connection_string=data.get("connectionString"),
            user_name=data.get("userName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.connection_string is not None:
            _v = self.connection_string
            result["connectionString"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.user_name is not None:
            _v = self.user_name
            result["userName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
