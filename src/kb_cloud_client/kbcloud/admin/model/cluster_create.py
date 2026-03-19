# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_backup import ClusterBackup
from .cluster_license import ClusterLicense
from .cluster_maintaince_window import ClusterMaintainceWindow
from .cluster_object_storage_config import ClusterObjectStorageConfig
from .cluster_termination_policy import ClusterTerminationPolicy
from .cluster_type import ClusterType
from .components_create import ComponentsCreate
from .init_options import InitOptions
from .network_mode import NetworkMode
from .param_tpls import ParamTpls
from .service_ref import ServiceRef


@dataclass
class ClusterCreate:
    """KubeBlocks cluster information"""
    # Required fields
    environment_name: str
    name: str
    engine: str
    # Optional fields
    parent_id: Optional[str] = None
    cluster_type: Optional[ClusterType] = None
    org_name: Optional[str] = None
    project: Optional[str] = None
    license: Optional[ClusterLicense] = None
    param_tpls: Optional[List[ParamTplsItem]] = None
    version: Optional[str] = None
    termination_policy: Optional[ClusterTerminationPolicy] = None
    mode: Optional[str] = None
    components: Optional[List[ComponentItemCreate]] = None
    extra: Optional[Dict[str, Dict[str, Any]]] = None
    init_options: Optional[List[InitOptionItem]] = None
    single_zone: Optional[bool] = None
    availability_zones: Optional[List[str]] = None
    backup: Optional[ClusterBackup] = None
    node_group: Optional[str] = None
    display_name: Optional[str] = None
    static: Optional[bool] = None
    network_mode: Optional[NetworkMode] = None
    service_refs: Optional[List[ServiceRef]] = None
    object_storage_config: Optional[ClusterObjectStorageConfig] = None
    maintaince_window: Optional[ClusterMaintainceWindow] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClusterCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            parent_id=data.get("parentId"),
            cluster_type=ClusterType.from_dict(data.get("clusterType")) if isinstance(data.get("clusterType"), dict) else data.get("clusterType"),
            org_name=data.get("orgName"),
            environment_name=data.get("environmentName"),
            project=data.get("project"),
            name=data.get("name"),
            engine=data.get("engine"),
            license=ClusterLicense.from_dict(data.get("license")) if isinstance(data.get("license"), dict) else data.get("license"),
            param_tpls=ParamTpls.from_dict(data.get("paramTpls")) if isinstance(data.get("paramTpls"), dict) else data.get("paramTpls"),
            version=data.get("version"),
            termination_policy=ClusterTerminationPolicy.from_dict(data.get("terminationPolicy")) if isinstance(data.get("terminationPolicy"), dict) else data.get("terminationPolicy"),
            mode=data.get("mode"),
            components=ComponentsCreate.from_dict(data.get("components")) if isinstance(data.get("components"), dict) else data.get("components"),
            extra=data.get("extra"),
            init_options=InitOptions.from_dict(data.get("initOptions")) if isinstance(data.get("initOptions"), dict) else data.get("initOptions"),
            single_zone=data.get("singleZone"),
            availability_zones=data.get("availabilityZones"),
            backup=ClusterBackup.from_dict(data.get("backup")) if isinstance(data.get("backup"), dict) else data.get("backup"),
            node_group=data.get("nodeGroup"),
            display_name=data.get("displayName"),
            static=data.get("static"),
            network_mode=NetworkMode.from_dict(data.get("networkMode")) if isinstance(data.get("networkMode"), dict) else data.get("networkMode"),
            service_refs=[ServiceRef.from_dict(i) if isinstance(i, dict) else i for i in data.get("serviceRefs")] if data.get("serviceRefs") is not None else None,
            object_storage_config=ClusterObjectStorageConfig.from_dict(data.get("objectStorageConfig")) if isinstance(data.get("objectStorageConfig"), dict) else data.get("objectStorageConfig"),
            maintaince_window=ClusterMaintainceWindow.from_dict(data.get("maintainceWindow")) if isinstance(data.get("maintainceWindow"), dict) else data.get("maintainceWindow"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.parent_id is not None:
            _v = self.parent_id
            result["parentId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_type is not None:
            _v = self.cluster_type
            result["clusterType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.environment_name is not None:
            _v = self.environment_name
            result["environmentName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.project is not None:
            _v = self.project
            result["project"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.license is not None:
            _v = self.license
            result["license"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.param_tpls is not None:
            _v = self.param_tpls
            result["paramTpls"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.termination_policy is not None:
            _v = self.termination_policy
            result["terminationPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mode is not None:
            _v = self.mode
            result["mode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.components is not None:
            _v = self.components
            result["components"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra is not None:
            _v = self.extra
            result["extra"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.init_options is not None:
            _v = self.init_options
            result["initOptions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.single_zone is not None:
            _v = self.single_zone
            result["singleZone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.availability_zones is not None:
            _v = self.availability_zones
            result["availabilityZones"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.backup is not None:
            _v = self.backup
            result["backup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_group is not None:
            _v = self.node_group
            result["nodeGroup"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.display_name is not None:
            _v = self.display_name
            result["displayName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.static is not None:
            _v = self.static
            result["static"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.network_mode is not None:
            _v = self.network_mode
            result["networkMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_refs is not None:
            _v = self.service_refs
            result["serviceRefs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.object_storage_config is not None:
            _v = self.object_storage_config
            result["objectStorageConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.maintaince_window is not None:
            _v = self.maintaince_window
            result["maintainceWindow"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
