# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .autohealing_config import AutohealingConfig
from .cluster_validation_policy import ClusterValidationPolicy
from .environment_delete_policy import EnvironmentDeletePolicy
from .network_mode import NetworkMode


@dataclass
class EnvironmentUpdate:
    """Environment info"""
    # Required fields
    # Optional fields
    description: Optional[str] = None
    display_name: Optional[str] = None
    organizations: Optional[List[str]] = None
    namespaces: Optional[List[str]] = None
    cpu_over_commit_ratio: Optional[float] = None
    memory_over_commit_ratio: Optional[float] = None
    autohealing_config: Optional[AutohealingConfig] = None
    default_storage_class: Optional[str] = None
    pod_anti_affinity_enabled: Optional[bool] = None
    image_registry: Optional[str] = None
    node_port_enabled: Optional[bool] = None
    lb_enabled: Optional[bool] = None
    internet_lb_enabled: Optional[bool] = None
    network_modes: Optional[List[NetworkMode]] = None
    delete_policy: Optional[EnvironmentDeletePolicy] = None
    cluster_validation_policy: Optional[ClusterValidationPolicy] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentUpdate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            description=data.get("description"),
            display_name=data.get("displayName"),
            organizations=data.get("organizations"),
            namespaces=data.get("namespaces"),
            cpu_over_commit_ratio=data.get("cpuOverCommitRatio"),
            memory_over_commit_ratio=data.get("memoryOverCommitRatio"),
            autohealing_config=AutohealingConfig.from_dict(data.get("autohealingConfig")) if isinstance(data.get("autohealingConfig"), dict) else data.get("autohealingConfig"),
            default_storage_class=data.get("defaultStorageClass"),
            pod_anti_affinity_enabled=data.get("podAntiAffinityEnabled"),
            image_registry=data.get("imageRegistry"),
            node_port_enabled=data.get("nodePortEnabled"),
            lb_enabled=data.get("lbEnabled"),
            internet_lb_enabled=data.get("internetLBEnabled"),
            network_modes=[NetworkMode.from_dict(i) if isinstance(i, dict) else i for i in data.get("networkModes")] if data.get("networkModes") is not None else None,
            delete_policy=EnvironmentDeletePolicy.from_dict(data.get("deletePolicy")) if isinstance(data.get("deletePolicy"), dict) else data.get("deletePolicy"),
            cluster_validation_policy=ClusterValidationPolicy.from_dict(data.get("clusterValidationPolicy")) if isinstance(data.get("clusterValidationPolicy"), dict) else data.get("clusterValidationPolicy"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.organizations is not None:
            _v = self.organizations
            result["organizations"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespaces is not None:
            _v = self.namespaces
            result["namespaces"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_over_commit_ratio is not None:
            _v = self.cpu_over_commit_ratio
            result["cpuOverCommitRatio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_over_commit_ratio is not None:
            _v = self.memory_over_commit_ratio
            result["memoryOverCommitRatio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.autohealing_config is not None:
            _v = self.autohealing_config
            result["autohealingConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_storage_class is not None:
            _v = self.default_storage_class
            result["defaultStorageClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_anti_affinity_enabled is not None:
            _v = self.pod_anti_affinity_enabled
            result["podAntiAffinityEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.image_registry is not None:
            _v = self.image_registry
            result["imageRegistry"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_port_enabled is not None:
            _v = self.node_port_enabled
            result["nodePortEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.lb_enabled is not None:
            _v = self.lb_enabled
            result["lbEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.internet_lb_enabled is not None:
            _v = self.internet_lb_enabled
            result["internetLBEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_modes is not None:
            _v = self.network_modes
            result["networkModes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.delete_policy is not None:
            _v = self.delete_policy
            result["deletePolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_validation_policy is not None:
            _v = self.cluster_validation_policy
            result["clusterValidationPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
