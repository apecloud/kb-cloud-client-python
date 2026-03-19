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
class AutohealingConfig:
    """cluster instance autohealing process config"""
    # Required fields
    enable_auto_healing: bool
    rebuild_start_delay_seconds_when_node_fail: int
    rebuild_start_delay_seconds_when_in_maintenance: int
    min_cluster_rebuild_interval_seconds: int
    rebuild_concurrency_per_node: int
    rebuild_concurrency_globally: int
    # Optional fields

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AutohealingConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            enable_auto_healing=data.get("enableAutoHealing"),
            rebuild_start_delay_seconds_when_node_fail=data.get("rebuildStartDelaySecondsWhenNodeFail"),
            rebuild_start_delay_seconds_when_in_maintenance=data.get("rebuildStartDelaySecondsWhenInMaintenance"),
            min_cluster_rebuild_interval_seconds=data.get("minClusterRebuildIntervalSeconds"),
            rebuild_concurrency_per_node=data.get("rebuildConcurrencyPerNode"),
            rebuild_concurrency_globally=data.get("rebuildConcurrencyGlobally"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.enable_auto_healing is not None:
            _v = self.enable_auto_healing
            result["enableAutoHealing"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_start_delay_seconds_when_node_fail is not None:
            _v = self.rebuild_start_delay_seconds_when_node_fail
            result["rebuildStartDelaySecondsWhenNodeFail"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_start_delay_seconds_when_in_maintenance is not None:
            _v = self.rebuild_start_delay_seconds_when_in_maintenance
            result["rebuildStartDelaySecondsWhenInMaintenance"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.min_cluster_rebuild_interval_seconds is not None:
            _v = self.min_cluster_rebuild_interval_seconds
            result["minClusterRebuildIntervalSeconds"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_concurrency_per_node is not None:
            _v = self.rebuild_concurrency_per_node
            result["rebuildConcurrencyPerNode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.rebuild_concurrency_globally is not None:
            _v = self.rebuild_concurrency_globally
            result["rebuildConcurrencyGlobally"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
