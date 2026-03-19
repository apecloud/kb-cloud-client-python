# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .tls_option import TlsOption


@dataclass
class TlsRequest:
    """TlsRequest"""
    # Required fields
    enable: bool
    # Optional fields
    options: Optional[TlsOption] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TlsRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enable=data.get("enable"),
            options=TlsOption.from_dict(data.get("options")) if isinstance(data.get("options"), dict) else data.get("options"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enable is not None:
            _v = self.enable
            result["enable"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.options is not None:
            _v = self.options
            result["options"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
