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
class DmsObAlterParameter:
    """DmsObAlterParameter"""
    # Required fields
    parameter: str
    new_value: str
    mode: str
    tenant_name: str
    is_variable: bool
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsObAlterParameter":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            parameter=data.get("parameter"),
            new_value=data.get("newValue"),
            mode=data.get("mode"),
            tenant_name=data.get("tenantName"),
            is_variable=data.get("isVariable"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.parameter is not None:
            _v = self.parameter
            result["parameter"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.new_value is not None:
            _v = self.new_value
            result["newValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.tenant_name is not None:
            _v = self.tenant_name
            result["tenantName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_variable is not None:
            _v = self.is_variable
            result["isVariable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
