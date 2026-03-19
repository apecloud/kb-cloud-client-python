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
class DmsTableColumn:
    """DmsTableColumn"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    type_: Optional[str] = None
    length: Optional[int] = None
    scale: Optional[int] = None
    not_null: Optional[bool] = None
    default: Optional[str] = None
    comment: Optional[str] = None
    auto_increment: Optional[bool] = None
    seed: Optional[int] = None
    increment: Optional[int] = None
    unsigned: Optional[bool] = None
    on_update_current_timestamp: Optional[bool] = None
    hidden: Optional[bool] = None
    generated: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsTableColumn":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            type_=data.get("type"),
            length=data.get("length"),
            scale=data.get("scale"),
            not_null=data.get("notNull"),
            default=data.get("default"),
            comment=data.get("comment"),
            auto_increment=data.get("autoIncrement"),
            seed=data.get("seed"),
            increment=data.get("increment"),
            unsigned=data.get("unsigned"),
            on_update_current_timestamp=data.get("onUpdateCurrentTimestamp"),
            hidden=data.get("hidden"),
            generated=data.get("generated"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.length is not None:
            _v = self.length
            result["length"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scale is not None:
            _v = self.scale
            result["scale"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.not_null is not None:
            _v = self.not_null
            result["notNull"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default is not None:
            _v = self.default
            result["default"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.comment is not None:
            _v = self.comment
            result["comment"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.auto_increment is not None:
            _v = self.auto_increment
            result["autoIncrement"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.seed is not None:
            _v = self.seed
            result["seed"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.increment is not None:
            _v = self.increment
            result["increment"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.unsigned is not None:
            _v = self.unsigned
            result["unsigned"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.on_update_current_timestamp is not None:
            _v = self.on_update_current_timestamp
            result["onUpdateCurrentTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hidden is not None:
            _v = self.hidden
            result["hidden"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.generated is not None:
            _v = self.generated
            result["generated"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
