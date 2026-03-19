# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .mode_service_ref import ModeServiceRef


@dataclass
class ModeObjectStorage:
    """object storage related configs
"""
    # Required fields
    # Optional fields
    enabled: Optional[bool] = None
    service_ref: Optional[ModeServiceRef] = None
    additional_helm_value_path: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeObjectStorage":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enabled=data.get("enabled"),
            service_ref=ModeServiceRef.from_dict(data.get("serviceRef")) if isinstance(data.get("serviceRef"), dict) else data.get("serviceRef"),
            additional_helm_value_path=data.get("additionalHelmValuePath"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_ref is not None:
            _v = self.service_ref
            result["serviceRef"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.additional_helm_value_path is not None:
            _v = self.additional_helm_value_path
            result["additionalHelmValuePath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
