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
class OpsPromote:
    """OpsPromote is the payload to promote a KubeBlocks cluster"""
    # Required fields
    component_name: str
    instance_name: str
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsPromote":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component_name=data.get("componentName"),
            instance_name=data.get("instanceName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component_name is not None:
            _v = self.component_name
            result["componentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.instance_name is not None:
            _v = self.instance_name
            result["instanceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
