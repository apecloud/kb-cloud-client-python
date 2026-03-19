# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .localized_description import LocalizedDescription
from .mode_compatible_kubeblocks_version import ModeCompatibleKubeblocksVersion
from .mode_component import ModeComponent
from .mode_object_storage import ModeObjectStorage
from .mode_service_ref import ModeServiceRef


@dataclass
class ModeOption:
    """ModeOption"""
    # Required fields
    name: str
    title: LocalizedDescription
    description: LocalizedDescription
    components: List[ModeComponent]
    # Optional fields
    scheduling_policy: Optional[Dict[str, Any]] = None
    compatible_kubeblocks_version: Optional[ModeCompatibleKubeblocksVersion] = None
    proxy: Optional[Dict[str, Any]] = None
    versions: Optional[List[str]] = None
    extra: Optional[Dict[str, Any]] = None
    service_refs: Optional[List[ModeServiceRef]] = None
    object_storage: Optional[ModeObjectStorage] = None
    values_mappings: Optional[Dict[str, Any]] = None
    hide_on_create: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            title=LocalizedDescription.from_dict(data.get("title")) if isinstance(data.get("title"), dict) else data.get("title"),
            description=LocalizedDescription.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            scheduling_policy=data.get("schedulingPolicy"),
            compatible_kubeblocks_version=ModeCompatibleKubeblocksVersion.from_dict(data.get("compatibleKubeblocksVersion")) if isinstance(data.get("compatibleKubeblocksVersion"), dict) else data.get("compatibleKubeblocksVersion"),
            components=[ModeComponent.from_dict(i) if isinstance(i, dict) else i for i in data.get("components")] if data.get("components") is not None else None,
            proxy=data.get("proxy"),
            versions=data.get("versions"),
            extra=data.get("extra"),
            service_refs=[ModeServiceRef.from_dict(i) if isinstance(i, dict) else i for i in data.get("serviceRefs")] if data.get("serviceRefs") is not None else None,
            object_storage=ModeObjectStorage.from_dict(data.get("objectStorage")) if isinstance(data.get("objectStorage"), dict) else data.get("objectStorage"),
            values_mappings=data.get("valuesMappings"),
            hide_on_create=data.get("hideOnCreate"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.title is not None:
            _v = self.title
            result["title"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scheduling_policy is not None:
            _v = self.scheduling_policy
            result["schedulingPolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.compatible_kubeblocks_version is not None:
            _v = self.compatible_kubeblocks_version
            result["compatibleKubeblocksVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.components is not None:
            _v = self.components
            result["components"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.proxy is not None:
            _v = self.proxy
            result["proxy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.versions is not None:
            _v = self.versions
            result["versions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra is not None:
            _v = self.extra
            result["extra"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_refs is not None:
            _v = self.service_refs
            result["serviceRefs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.object_storage is not None:
            _v = self.object_storage
            result["objectStorage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.values_mappings is not None:
            _v = self.values_mappings
            result["valuesMappings"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.hide_on_create is not None:
            _v = self.hide_on_create
            result["hideOnCreate"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
