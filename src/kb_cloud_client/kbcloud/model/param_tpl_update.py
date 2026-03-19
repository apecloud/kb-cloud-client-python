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
class ParamTplUpdate:
    """paramTplUpdate is the payload to update a parameter template"""
    # Required fields
    # Optional fields
    spec_name: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    new_param_tpl_name: Optional[str] = None
    raw_content: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParamTplUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            spec_name=data.get("specName"),
            parameters=data.get("parameters"),
            new_param_tpl_name=data.get("newParamTplName"),
            raw_content=data.get("rawContent"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.spec_name is not None:
            _v = self.spec_name
            result["specName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parameters is not None:
            _v = self.parameters
            result["parameters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.new_param_tpl_name is not None:
            _v = self.new_param_tpl_name
            result["newParamTplName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.raw_content is not None:
            _v = self.raw_content
            result["rawContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
