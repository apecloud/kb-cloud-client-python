# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_validation_policy import ClusterValidationPolicy
from .environment_architecture import EnvironmentArchitecture
from .environment_state import EnvironmentState
from .environment_type import EnvironmentType
from .network_config import NetworkConfig


@dataclass
class Environment:
    """Environment info"""
    # Required fields
    provider: str
    region: str
    availability_zones: List[str]
    created_at: datetime
    id_: str
    name: str
    org_name: str
    state: EnvironmentState
    type_: EnvironmentType
    updated_at: datetime
    default_storage_class: str
    # Optional fields
    network_config: Optional[NetworkConfig] = None
    description: Optional[str] = None
    display_name: Optional[str] = None
    image_registry: Optional[str] = None
    extra_info: Optional[str] = None
    kb_version: Optional[str] = None
    namespaces: Optional[List[str]] = None
    pod_anti_affinity_enabled: Optional[bool] = None
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
            network_config=NetworkConfig.from_dict(data.get("networkConfig")) if isinstance(data.get("networkConfig"), dict) else data.get("networkConfig"),
            created_at=_parse_datetime(data.get("createdAt")),
            description=data.get("description"),
            display_name=data.get("displayName"),
            id_=data.get("id"),
            name=data.get("name"),
            org_name=data.get("orgName"),
            state=EnvironmentState.from_dict(data.get("state")) if isinstance(data.get("state"), dict) else data.get("state"),
            type_=EnvironmentType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            updated_at=_parse_datetime(data.get("updatedAt")),
            image_registry=data.get("imageRegistry"),
            extra_info=data.get("extraInfo"),
            kb_version=data.get("kbVersion"),
            namespaces=data.get("namespaces"),
            pod_anti_affinity_enabled=data.get("podAntiAffinityEnabled"),
            default_storage_class=data.get("defaultStorageClass"),
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
        if self.network_config is not None:
            _v = self.network_config
            result["networkConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.image_registry is not None:
            _v = self.image_registry
            result["imageRegistry"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_info is not None:
            _v = self.extra_info
            result["extraInfo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.kb_version is not None:
            _v = self.kb_version
            result["kbVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespaces is not None:
            _v = self.namespaces
            result["namespaces"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.pod_anti_affinity_enabled is not None:
            _v = self.pod_anti_affinity_enabled
            result["podAntiAffinityEnabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_storage_class is not None:
            _v = self.default_storage_class
            result["defaultStorageClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
