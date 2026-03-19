# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .parameter_template_partition import ParameterTemplatePartition


@dataclass
class ParamTplsItem:
    """the item of the parameter template"""
    # Required fields
    # Optional fields
    component: Optional[str] = None
    param_tpl_name: Optional[str] = None
    param_tpl_id: Optional[str] = None
    param_tpl_partition: Optional[ParameterTemplatePartition] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParamTplsItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            param_tpl_name=data.get("paramTplName"),
            param_tpl_id=data.get("paramTplID"),
            param_tpl_partition=ParameterTemplatePartition.from_dict(data.get("paramTplPartition")) if isinstance(data.get("paramTplPartition"), dict) else data.get("paramTplPartition"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.param_tpl_name is not None:
            _v = self.param_tpl_name
            result["paramTplName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.param_tpl_id is not None:
            _v = self.param_tpl_id
            result["paramTplID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.param_tpl_partition is not None:
            _v = self.param_tpl_partition
            result["paramTplPartition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
