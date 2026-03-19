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
class ParameterConfig:
    """ParameterConfig"""
    # Required fields
    config_spec_name: str
    template_ref: str
    config_file_name: str
    format_: str
    # Optional fields
    section: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParameterConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            config_spec_name=data.get("configSpecName"),
            template_ref=data.get("templateRef"),
            config_file_name=data.get("configFileName"),
            format_=data.get("format"),
            section=data.get("section"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.config_spec_name is not None:
            _v = self.config_spec_name
            result["configSpecName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.template_ref is not None:
            _v = self.template_ref
            result["templateRef"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config_file_name is not None:
            _v = self.config_file_name
            result["configFileName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.format_ is not None:
            _v = self.format_
            result["format"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.section is not None:
            _v = self.section
            result["section"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
