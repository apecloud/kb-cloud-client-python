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
from .environment_architecture import EnvironmentArchitecture
from .environment_delete_policy import EnvironmentDeletePolicy
from .environment_state import EnvironmentState
from .environment_type import EnvironmentType
from .network_config import NetworkConfig
from .provision_config import ProvisionConfig
from .scheduling_config import SchedulingConfig


@dataclass
class Environment:
    """Environment info"""
    # Required fields
    provider: str
    region: str
    availability_zones: List[str]
    display_name: str
    id_: str
    name: str
    organizations: List[str]
    state: EnvironmentState
    type_: EnvironmentType
    provision_config: ProvisionConfig
    created_at: datetime
    updated_at: datetime
    # Optional fields
    scheduling_config: Optional[SchedulingConfig] = None
    network_config: Optional[NetworkConfig] = None
    description: Optional[str] = None
    metrics_monitor_enabled: Optional[bool] = None
    autohealing_config: Optional[AutohealingConfig] = None
    extra_info: Optional[str] = None
    delete_policy: Optional[EnvironmentDeletePolicy] = None
    cluster_validation_policy: Optional[ClusterValidationPolicy] = None
    architecture: Optional[EnvironmentArchitecture] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Environment":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            provider=data.get("provider"),
            region=data.get("region"),
            availability_zones=data.get("availabilityZones"),
            scheduling_config=SchedulingConfig.from_dict(data.get("schedulingConfig")) if isinstance(data.get("schedulingConfig"), dict) else data.get("schedulingConfig"),
            network_config=NetworkConfig.from_dict(data.get("networkConfig")) if isinstance(data.get("networkConfig"), dict) else data.get("networkConfig"),
            description=data.get("description"),
            display_name=data.get("displayName"),
            id_=data.get("id"),
            name=data.get("name"),
            organizations=data.get("organizations"),
            metrics_monitor_enabled=data.get("metricsMonitorEnabled"),
            state=EnvironmentState.from_dict(data.get("state")) if isinstance(data.get("state"), dict) else data.get("state"),
            type_=EnvironmentType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            provision_config=ProvisionConfig.from_dict(data.get("provisionConfig")) if isinstance(data.get("provisionConfig"), dict) else data.get("provisionConfig"),
            autohealing_config=AutohealingConfig.from_dict(data.get("autohealingConfig")) if isinstance(data.get("autohealingConfig"), dict) else data.get("autohealingConfig"),
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
            extra_info=data.get("extraInfo"),
            delete_policy=EnvironmentDeletePolicy.from_dict(data.get("deletePolicy")) if isinstance(data.get("deletePolicy"), dict) else data.get("deletePolicy"),
            cluster_validation_policy=ClusterValidationPolicy.from_dict(data.get("clusterValidationPolicy")) if isinstance(data.get("clusterValidationPolicy"), dict) else data.get("clusterValidationPolicy"),
            architecture=EnvironmentArchitecture.from_dict(data.get("architecture")) if isinstance(data.get("architecture"), dict) else data.get("architecture"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.provider is not None:
            _v = self.provider
            result["provider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.region is not None:
            _v = self.region
            result["region"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.availability_zones is not None:
            _v = self.availability_zones
            result["availabilityZones"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scheduling_config is not None:
            _v = self.scheduling_config
            result["schedulingConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_config is not None:
            _v = self.network_config
            result["networkConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
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
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.organizations is not None:
            _v = self.organizations
            result["organizations"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.metrics_monitor_enabled is not None:
            _v = self.metrics_monitor_enabled
            result["metricsMonitorEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.state is not None:
            _v = self.state
            result["state"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.provision_config is not None:
            _v = self.provision_config
            result["provisionConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.autohealing_config is not None:
            _v = self.autohealing_config
            result["autohealingConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_info is not None:
            _v = self.extra_info
            result["extraInfo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.architecture is not None:
            _v = self.architecture
            result["architecture"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
