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
class ApikeyWithSK:
    """APIKeyWithSK is the response for creating an APIKey"""
    # Required fields
    access_key: str
    secret_key: str
    description: str
    create_at: datetime
    # Optional fields
    expired_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ApikeyWithSK":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            access_key=data.get("accessKey"),
            secret_key=data.get("secretKey"),
            description=data.get("description"),
            expired_at=_parse_datetime(data.get("expiredAt")),
            create_at=_parse_datetime(data.get("createAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.access_key is not None:
            _v = self.access_key
            result["accessKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.secret_key is not None:
            _v = self.secret_key
            result["secretKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.expired_at is not None:
            _v = self.expired_at
            result["expiredAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.create_at is not None:
            _v = self.create_at
            result["createAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
