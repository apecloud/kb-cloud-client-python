# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .localized_description import LocalizedDescription


@dataclass
class ComponentOption:
    """ComponentOption"""
    # Required fields
    name: str
    title: LocalizedDescription
    order: int
    # Optional fields
    cloud_shell_type: Optional[str] = None
    match_regex: Optional[str] = None
    role_order: Optional[List[str]] = None
    version: Optional[Dict[str, Any]] = None
    main: Optional[bool] = None
    custom_secret: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cloud_shell_type=data.get("cloudShellType"),
            name=data.get("name"),
            match_regex=data.get("matchRegex"),
            title=LocalizedDescription.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            order=data.get("order"),
            role_order=data.get("roleOrder"),
            version=data.get("version"),
            main=data.get("main"),
            custom_secret=data.get("customSecret"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cloud_shell_type is not None:
            _v = self.cloud_shell_type
            result["cloudShellType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.match_regex is not None:
            _v = self.match_regex
            result["matchRegex"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.order is not None:
            _v = self.order
            result["order"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.role_order is not None:
            _v = self.role_order
            result["roleOrder"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.main is not None:
            _v = self.main
            result["main"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.custom_secret is not None:
            _v = self.custom_secret
            result["customSecret"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
