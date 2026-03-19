# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .parameter_template import ParameterTemplate


@dataclass
class ParameterOption:
    """ParameterOption"""
    # Required fields
    component: str
    export_tpl: bool
    enable_template: bool
    config_specs: List[str]
    # Optional fields
    enable_raw_content: Optional[bool] = None
    disable_ha: Optional[bool] = None
    templates: Optional[List[ParameterTemplate]] = None
    init_options: Optional[Dict[str, Dict[str, Any]]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParameterOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            export_tpl=data.get("exportTpl"),
            enable_template=data.get("enableTemplate"),
            enable_raw_content=data.get("enableRawContent"),
            config_specs=data.get("configSpecs"),
            disable_ha=data.get("disableHA"),
            templates=[ParameterTemplate.from_dict(i) if isinstance(i, dict) else i for i in data.get("templates")] if data.get("templates") is not None else None,
            init_options=data.get("initOptions"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.export_tpl is not None:
            _v = self.export_tpl
            result["exportTpl"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enable_template is not None:
            _v = self.enable_template
            result["enableTemplate"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.enable_raw_content is not None:
            _v = self.enable_raw_content
            result["enableRawContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_specs is not None:
            _v = self.config_specs
            result["configSpecs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.disable_ha is not None:
            _v = self.disable_ha
            result["disableHA"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.templates is not None:
            _v = self.templates
            result["templates"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.init_options is not None:
            _v = self.init_options
            result["initOptions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
