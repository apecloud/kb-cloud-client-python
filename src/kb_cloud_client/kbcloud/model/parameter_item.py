# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .parameter_prop import ParameterProp


@dataclass
class ParameterItem:
    """With the list of parameter properties and the configuration file name"""
    # Required fields
    # Optional fields
    props: Optional[List[ParameterProp]] = None
    additional_props: Optional[List[ParameterProp]] = None
    file_name: Optional[str] = None
    spec_name: Optional[str] = None
    raw_content: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParameterItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            props=[ParameterProp.from_dict(i) if isinstance(i, dict) else i for i in data.get("props")] if data.get("props") is not None else None,
            additional_props=[ParameterProp.from_dict(i) if isinstance(i, dict) else i for i in data.get("additionalProps")] if data.get("additionalProps") is not None else None,
            file_name=data.get("fileName"),
            spec_name=data.get("specName"),
            raw_content=data.get("rawContent"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.props is not None:
            _v = self.props
            result["props"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.additional_props is not None:
            _v = self.additional_props
            result["additionalProps"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.file_name is not None:
            _v = self.file_name
            result["fileName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.spec_name is not None:
            _v = self.spec_name
            result["specName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.raw_content is not None:
            _v = self.raw_content
            result["rawContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
