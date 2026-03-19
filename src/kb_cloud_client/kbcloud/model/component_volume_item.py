# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .io_quantity import IoQuantity


@dataclass
class ComponentVolumeItem:
    """ComponentVolumeItem is the information of a component volume"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    storage: Optional[float] = None
    io_limits: Optional[IoQuantity] = None
    io_reserves: Optional[IoQuantity] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentVolumeItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            storage=data.get("storage"),
            io_limits=IoQuantity.from_dict(data.get("ioLimits")) if isinstance(data.get("ioLimits"), dict) else data.get("ioLimits"),
            io_reserves=IoQuantity.from_dict(data.get("ioReserves")) if isinstance(data.get("ioReserves"), dict) else data.get("ioReserves"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage is not None:
            _v = self.storage
            result["storage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.io_limits is not None:
            _v = self.io_limits
            result["ioLimits"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.io_reserves is not None:
            _v = self.io_reserves
            result["ioReserves"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
