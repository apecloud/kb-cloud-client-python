# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .environment_storage_type import EnvironmentStorageType
from .static_cluster import StaticCluster
from .storage_create import StorageCreate


@dataclass
class EnvironmentStorage:
    """Storage config"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    type_: Optional[EnvironmentStorageType] = None
    reused_cluster_name: Optional[str] = None
    reused_cluster_namespace: Optional[str] = None
    config: Optional[StorageCreate] = None
    cluster: Optional[StaticCluster] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentStorage":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            type_=EnvironmentStorageType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            reused_cluster_name=data.get("reusedClusterName"),
            reused_cluster_namespace=data.get("reusedClusterNamespace"),
            config=StorageCreate.from_dict(data.get("config")) if isinstance(data.get("config"), dict) else data.get("config"),
            cluster=StaticCluster.from_dict(data.get("cluster")) if isinstance(data.get("cluster"), dict) else data.get("cluster"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reused_cluster_name is not None:
            _v = self.reused_cluster_name
            result["reusedClusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reused_cluster_namespace is not None:
            _v = self.reused_cluster_namespace
            result["reusedClusterNamespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.config is not None:
            _v = self.config
            result["config"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
