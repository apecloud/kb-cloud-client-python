# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .storage_class_reclaim_policy import StorageClassReclaimPolicy
from .storage_class_volume_binding_mode import StorageClassVolumeBindingMode


@dataclass
class StorageClassCreate:
    """StorageClassCreate provides detailed creation information about a storage class."""
    # Required fields
    name: str
    reclaim_policy: StorageClassReclaimPolicy
    volume_binding_mode: StorageClassVolumeBindingMode
    description: str
    display_name: str
    enabled: bool
    # Optional fields
    provisioner: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    parameters: Optional[Dict[str, str]] = None
    allow_volume_expansion: Optional[bool] = None
    allow_clone: Optional[bool] = None
    allow_snapshot: Optional[bool] = None
    is_default_class: Optional[bool] = None
    type_: Optional[str] = None
    host_path: Optional[str] = None
    mount_options: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageClassCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            provisioner=data.get("provisioner"),
            labels=data.get("labels"),
            annotations=data.get("annotations"),
            parameters=data.get("parameters"),
            reclaim_policy=StorageClassReclaimPolicy.from_dict(data.get("reclaimPolicy")) if isinstance(data.get("reclaimPolicy"), dict) else data.get("reclaimPolicy"),
            allow_volume_expansion=data.get("allowVolumeExpansion"),
            volume_binding_mode=StorageClassVolumeBindingMode.from_dict(data.get("volumeBindingMode")) if isinstance(data.get("volumeBindingMode"), dict) else data.get("volumeBindingMode"),
            allow_clone=data.get("allowClone"),
            allow_snapshot=data.get("allowSnapshot"),
            is_default_class=data.get("isDefaultClass"),
            type_=data.get("type"),
            host_path=data.get("hostPath"),
            mount_options=data.get("mountOptions"),
            description=data.get("description"),
            display_name=data.get("displayName"),
            enabled=data.get("enabled"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.provisioner is not None:
            _v = self.provisioner
            result["provisioner"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.labels is not None:
            _v = self.labels
            result["labels"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.annotations is not None:
            _v = self.annotations
            result["annotations"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.parameters is not None:
            _v = self.parameters
            result["parameters"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.reclaim_policy is not None:
            _v = self.reclaim_policy
            result["reclaimPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.allow_volume_expansion is not None:
            _v = self.allow_volume_expansion
            result["allowVolumeExpansion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volume_binding_mode is not None:
            _v = self.volume_binding_mode
            result["volumeBindingMode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.allow_clone is not None:
            _v = self.allow_clone
            result["allowClone"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.allow_snapshot is not None:
            _v = self.allow_snapshot
            result["allowSnapshot"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_default_class is not None:
            _v = self.is_default_class
            result["isDefaultClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.host_path is not None:
            _v = self.host_path
            result["hostPath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mount_options is not None:
            _v = self.mount_options
            result["mountOptions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.enabled is not None:
            _v = self.enabled
            result["enabled"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
