# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .config_type import ConfigType
from .connection_cfg_type import ConnectionCfgType
from .international_desc import InternationalDesc


@dataclass
class ExtraConfig:
    """ExtraConfig"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    title: Optional[InternationalDesc] = None
    type_: Optional[ConfigType] = None
    is_required: Optional[bool] = None
    connection_cfg_type: Optional[ConnectionCfgType] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExtraConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            title=InternationalDesc.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            type_=ConfigType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            is_required=data.get("isRequired"),
            connection_cfg_type=ConnectionCfgType.from_dict(data.get("connectionCfgType")) if isinstance(data.get("connectionCfgType"), dict) else data.get("connectionCfgType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_required is not None:
            _v = self.is_required
            result["isRequired"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.connection_cfg_type is not None:
            _v = self.connection_cfg_type
            result["connectionCfgType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
