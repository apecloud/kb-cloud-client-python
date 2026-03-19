# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .tolerate_default_taints import TolerateDefaultTaints


@dataclass
class SchedulingConfig:
    """Configuration of resource scheduling for this environment"""
    # Required fields
    # Optional fields
    pod_anti_affinity_enabled: Optional[bool] = None
    tolerate_default_taints: Optional[TolerateDefaultTaints] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SchedulingConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            pod_anti_affinity_enabled=data.get("podAntiAffinityEnabled"),
            tolerate_default_taints=TolerateDefaultTaints.from_dict(data.get("tolerateDefaultTaints")) if isinstance(data.get("tolerateDefaultTaints"), dict) else data.get("tolerateDefaultTaints"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.pod_anti_affinity_enabled is not None:
            _v = self.pod_anti_affinity_enabled
            result["podAntiAffinityEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.tolerate_default_taints is not None:
            _v = self.tolerate_default_taints
            result["tolerateDefaultTaints"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
