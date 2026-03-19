# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_info import ClusterInfo
from .environment_module_status import EnvironmentModuleStatus
from .hosting_status import HostingStatus
from .localized_description import LocalizedDescription


@dataclass
class EnvironmentModule:
    """Single environment module information"""
    # Required fields
    name: str
    status: EnvironmentModuleStatus
    # Optional fields
    version: Optional[str] = None
    hosting_status: Optional[HostingStatus] = None
    replicas: Optional[int] = None
    location: Optional[str] = None
    cluster_info: Optional[ClusterInfo] = None
    description: Optional[LocalizedDescription] = None
    optional: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentModule":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            version=data.get("version"),
            status=EnvironmentModuleStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            hosting_status=HostingStatus.from_dict(data.get("hostingStatus")) if isinstance(data.get("hostingStatus"), dict) else data.get("hostingStatus"),
            replicas=data.get("replicas"),
            location=data.get("location"),
            cluster_info=ClusterInfo.from_dict(data.get("clusterInfo")) if isinstance(data.get("clusterInfo"), dict) else data.get("clusterInfo"),
            description=LocalizedDescription.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            optional=data.get("optional"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.version is not None:
            _v = self.version
            result["version"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hosting_status is not None:
            _v = self.hosting_status
            result["hostingStatus"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.location is not None:
            _v = self.location
            result["location"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_info is not None:
            _v = self.cluster_info
            result["clusterInfo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.optional is not None:
            _v = self.optional
            result["optional"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
