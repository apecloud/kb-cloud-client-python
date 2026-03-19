# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .dms_console_net_mode import DMSConsoleNetMode
from .dms_console_svc_type import DMSConsoleSvcType


@dataclass
class DMSConsoleEnableOpt:
    """DMSConsoleEnableOpt"""
    # Required fields
    network_mode: DMSConsoleNetMode
    service_type: DMSConsoleSvcType
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DMSConsoleEnableOpt":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            network_mode=DMSConsoleNetMode.from_dict(data.get("networkMode")) if isinstance(data.get("networkMode"), dict) else data.get("networkMode"),
            service_type=DMSConsoleSvcType.from_dict(data.get("serviceType")) if isinstance(data.get("serviceType"), dict) else data.get("serviceType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.network_mode is not None:
            _v = self.network_mode
            result["networkMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_type is not None:
            _v = self.service_type
            result["serviceType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
