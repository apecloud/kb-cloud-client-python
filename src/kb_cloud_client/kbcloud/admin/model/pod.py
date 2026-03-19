# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .container_info import ContainerInfo
from .pod_condition import PodCondition
from .pod_owner_reference import PodOwnerReference
from .pod_resources import PodResources


@dataclass
class Pod:
    """Single pod information for environment module"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    namespace: Optional[str] = None
    node_name: Optional[str] = None
    status: Optional[str] = None
    phase: Optional[str] = None
    ip: Optional[str] = None
    creation_timestamp: Optional[datetime] = None
    resources: Optional[PodResources] = None
    owner_references: Optional[List[PodOwnerReference]] = None
    containers: Optional[List[ContainerInfo]] = None
    conditions: Optional[List[PodCondition]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pod":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            namespace=data.get("namespace"),
            node_name=data.get("nodeName"),
            status=data.get("status"),
            phase=data.get("phase"),
            ip=data.get("ip"),
            creation_timestamp=_parse_datetime(data.get("creationTimestamp")),
            resources=PodResources.from_dict(data.get("resources")) if isinstance(data.get("resources"), dict) else data.get("resources"),
            owner_references=[PodOwnerReference.from_dict(i) if isinstance(i, dict) else i for i in data.get("ownerReferences")] if data.get("ownerReferences") is not None else None,
            containers=[ContainerInfo.from_dict(i) if isinstance(i, dict) else i for i in data.get("containers")] if data.get("containers") is not None else None,
            conditions=[PodCondition.from_dict(i) if isinstance(i, dict) else i for i in data.get("conditions")] if data.get("conditions") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_name is not None:
            _v = self.node_name
            result["nodeName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.phase is not None:
            _v = self.phase
            result["phase"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ip is not None:
            _v = self.ip
            result["ip"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.creation_timestamp is not None:
            _v = self.creation_timestamp
            result["creationTimestamp"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.resources is not None:
            _v = self.resources
            result["resources"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.owner_references is not None:
            _v = self.owner_references
            result["ownerReferences"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.containers is not None:
            _v = self.containers
            result["containers"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.conditions is not None:
            _v = self.conditions
            result["conditions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
