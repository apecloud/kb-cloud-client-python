# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_parameter_option import DataChannelParameterOption
from .international_desc import InternationalDesc
from .standard_resource import StandardResource


@dataclass
class StandardDefinition:
    """StandardDefinition"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    title: Optional[InternationalDesc] = None
    description: Optional[InternationalDesc] = None
    is_default: Optional[bool] = None
    cpu: Optional[StandardResource] = None
    memory: Optional[StandardResource] = None
    parameter_template: Optional[DataChannelParameterOption] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StandardDefinition":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            title=InternationalDesc.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            description=InternationalDesc.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            is_default=data.get("isDefault"),
            cpu=StandardResource.from_dict(data.get("cpu")) if isinstance(data.get("cpu"), dict) else data.get("cpu"),
            memory=StandardResource.from_dict(data.get("memory")) if isinstance(data.get("memory"), dict) else data.get("memory"),
            parameter_template=DataChannelParameterOption.from_dict(data.get("parameterTemplate")) if isinstance(data.get("parameterTemplate"), dict) else data.get("parameterTemplate"),
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
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_default is not None:
            _v = self.is_default
            result["isDefault"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu is not None:
            _v = self.cpu
            result["cpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory is not None:
            _v = self.memory
            result["memory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parameter_template is not None:
            _v = self.parameter_template
            result["parameterTemplate"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
