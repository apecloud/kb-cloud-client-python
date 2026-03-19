# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .event_source import EventSource


@dataclass
class ParameterHistory:
    """The history of a parameter"""
    # Required fields
    parameter_name: str
    old_value: str
    new_value: str
    updated_at: datetime
    # Optional fields
    source: Optional[EventSource] = None
    operator: Optional[str] = None
    operator_id: Optional[str] = None
    file_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParameterHistory":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            parameter_name=data.get("parameterName"),
            old_value=data.get("oldValue"),
            new_value=data.get("newValue"),
            updated_at=_parse_datetime(data.get("updatedAt")),
            source=EventSource.from_dict(data.get("source")) if isinstance(data.get("source"), dict) else data.get("source"),
            operator=data.get("operator"),
            operator_id=data.get("operatorId"),
            file_name=data.get("fileName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.parameter_name is not None:
            _v = self.parameter_name
            result["parameterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.old_value is not None:
            _v = self.old_value
            result["oldValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.new_value is not None:
            _v = self.new_value
            result["newValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.source is not None:
            _v = self.source
            result["source"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator is not None:
            _v = self.operator
            result["operator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.operator_id is not None:
            _v = self.operator_id
            result["operatorId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.file_name is not None:
            _v = self.file_name
            result["fileName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
