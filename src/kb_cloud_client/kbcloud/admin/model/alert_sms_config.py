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
class AlertSMSConfig:
    """Alert sms config"""
    # Required fields
    access_key_id: str
    access_key_secret: str
    template_code: str
    # Optional fields
    name: Optional[str] = None
    endpoint: Optional[str] = None
    sign_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlertSMSConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            access_key_id=data.get("accessKeyID"),
            access_key_secret=data.get("accessKeySecret"),
            endpoint=data.get("endpoint"),
            template_code=data.get("templateCode"),
            sign_name=data.get("signName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.access_key_id is not None:
            _v = self.access_key_id
            result["accessKeyID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.access_key_secret is not None:
            _v = self.access_key_secret
            result["accessKeySecret"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint is not None:
            _v = self.endpoint
            result["endpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.template_code is not None:
            _v = self.template_code
            result["templateCode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sign_name is not None:
            _v = self.sign_name
            result["signName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
