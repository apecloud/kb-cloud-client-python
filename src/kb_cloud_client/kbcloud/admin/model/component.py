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
class Component:
    """Component info in environment"""
    # Required fields
    default_storage_class: str
    # Optional fields
    kubernetes_version: Optional[str] = None
    kb_version: Optional[str] = None
    gemini_version: Optional[str] = None
    oteld_version: Optional[str] = None
    image_registry: Optional[str] = None
    cpu_overcommit_ratio: Optional[float] = None
    memory_overcommit_ratio: Optional[float] = None
    replicas: Optional[int] = None
    namespaces: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Component":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            kubernetes_version=data.get("kubernetesVersion"),
            kb_version=data.get("kbVersion"),
            gemini_version=data.get("geminiVersion"),
            oteld_version=data.get("oteldVersion"),
            image_registry=data.get("imageRegistry"),
            default_storage_class=data.get("defaultStorageClass"),
            cpu_overcommit_ratio=data.get("cpuOvercommitRatio"),
            memory_overcommit_ratio=data.get("memoryOvercommitRatio"),
            replicas=data.get("replicas"),
            namespaces=data.get("namespaces"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.kubernetes_version is not None:
            _v = self.kubernetes_version
            result["kubernetesVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.kb_version is not None:
            _v = self.kb_version
            result["kbVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.gemini_version is not None:
            _v = self.gemini_version
            result["geminiVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.oteld_version is not None:
            _v = self.oteld_version
            result["oteldVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.image_registry is not None:
            _v = self.image_registry
            result["imageRegistry"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.default_storage_class is not None:
            _v = self.default_storage_class
            result["defaultStorageClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu_overcommit_ratio is not None:
            _v = self.cpu_overcommit_ratio
            result["cpuOvercommitRatio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory_overcommit_ratio is not None:
            _v = self.memory_overcommit_ratio
            result["memoryOvercommitRatio"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.namespaces is not None:
            _v = self.namespaces
            result["namespaces"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
