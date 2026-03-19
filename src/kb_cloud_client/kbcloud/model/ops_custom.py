# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .ops_parameter import OpsParameter


@dataclass
class OpsCustom:
    """OpsCustom is the payload to create a custom KubeBlocks OpsRequest"""
    # Required fields
    comp_name: str
    ops_type: str
    # Optional fields
    dependent_on_ops: Optional[List[str]] = None
    params: Optional[List[OpsParameter]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsCustom":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            comp_name=data.get("compName"),
            ops_type=data.get("opsType"),
            dependent_on_ops=data.get("dependentOnOps"),
            params=[OpsParameter.from_dict(i) if isinstance(i, dict) else i for i in data.get("params")] if data.get("params") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.comp_name is not None:
            _v = self.comp_name
            result["compName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ops_type is not None:
            _v = self.ops_type
            result["opsType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dependent_on_ops is not None:
            _v = self.dependent_on_ops
            result["dependentOnOps"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.params is not None:
            _v = self.params
            result["params"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
