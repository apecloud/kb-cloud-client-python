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
class HttpBody:
    """Represents an HTTP request or response body."""
    # Required fields
    # Optional fields
    content_type: Optional[str] = None
    data: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "HttpBody":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            content_type=data.get("contentType"),
            data=data.get("data"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.content_type is not None:
            _v = self.content_type
            result["contentType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.data is not None:
            _v = self.data
            result["data"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
