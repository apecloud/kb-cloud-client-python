# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_options_disaster_recovery_source import EngineOptionsDisasterRecoverySource


@dataclass
class EngineOptionsDisasterRecoveryStatus:
    """EngineOptionsDisasterRecoveryStatus"""
    # Required fields
    # Optional fields
    delay: Optional[EngineOptionsDisasterRecoverySource] = None
    replication_point: Optional[EngineOptionsDisasterRecoverySource] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EngineOptionsDisasterRecoveryStatus":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            delay=EngineOptionsDisasterRecoverySource.from_dict(data.get("delay")) if isinstance(data.get("delay"), dict) else data.get("delay"),
            replication_point=EngineOptionsDisasterRecoverySource.from_dict(data.get("replicationPoint")) if isinstance(data.get("replicationPoint"), dict) else data.get("replicationPoint"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.delay is not None:
            _v = self.delay
            result["delay"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replication_point is not None:
            _v = self.replication_point
            result["replicationPoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
