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
class IoQuantity:
    """IO Quantity describes IOPS and BPS of a volume"""
    # Required fields
    # Optional fields
    read_iops: Optional[int] = None
    write_iops: Optional[int] = None
    read_bps: Optional[int] = None
    write_bps: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IoQuantity":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            read_iops=data.get("readIOPS"),
            write_iops=data.get("writeIOPS"),
            read_bps=data.get("readBPS"),
            write_bps=data.get("writeBPS"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.read_iops is not None:
            _v = self.read_iops
            result["readIOPS"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.write_iops is not None:
            _v = self.write_iops
            result["writeIOPS"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.read_bps is not None:
            _v = self.read_bps
            result["readBPS"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.write_bps is not None:
            _v = self.write_bps
            result["writeBPS"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
