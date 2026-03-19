# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .storage_display_name import StorageDisplayName


@dataclass
class StorageProvider:
    """Storage Provider comprises specifications that provide guidance accessing remote storage."""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    name: Optional[str] = None
    credential: Optional[List[str]] = None
    schema: Optional[Dict[str, StorageProviderSchemaProps]] = None
    required: Optional[List[str]] = None
    display_name: Optional[StorageDisplayName] = None
    is_local: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageProvider":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            credential=data.get("credential"),
            schema=data.get("schema"),
            required=data.get("required"),
            display_name=StorageDisplayName.from_dict(data.get("displayName")) if isinstance(data.get("displayName"), dict) else data.get("displayName"),
            is_local=data.get("isLocal"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.credential is not None:
            _v = self.credential
            result["credential"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.schema is not None:
            _v = self.schema
            result["schema"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.required is not None:
            _v = self.required
            result["required"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_local is not None:
            _v = self.is_local
            result["isLocal"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
