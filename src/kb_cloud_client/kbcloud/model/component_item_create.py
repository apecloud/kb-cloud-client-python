# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .component_volume_item import ComponentVolumeItem


@dataclass
class ComponentItemCreate:
    """ComponentItem is the information of a component"""
    # Required fields
    component: str
    # Optional fields
    comp_num: Optional[int] = None
    replicas: Optional[int] = None
    class_code: Optional[str] = None
    cpu: Optional[float] = None
    memory: Optional[float] = None
    storage_class: Optional[str] = None
    volumes: Optional[List[ComponentVolumeItem]] = None
    system_account_secret_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComponentItemCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            component=data.get("component"),
            comp_num=data.get("compNum"),
            replicas=data.get("replicas"),
            class_code=data.get("classCode"),
            cpu=data.get("cpu"),
            memory=data.get("memory"),
            storage_class=data.get("storageClass"),
            volumes=[ComponentVolumeItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("volumes")] if data.get("volumes") is not None else None,
            system_account_secret_name=data.get("systemAccountSecretName"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.comp_num is not None:
            _v = self.comp_num
            result["compNum"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replicas is not None:
            _v = self.replicas
            result["replicas"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.class_code is not None:
            _v = self.class_code
            result["classCode"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cpu is not None:
            _v = self.cpu
            result["cpu"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.memory is not None:
            _v = self.memory
            result["memory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_class is not None:
            _v = self.storage_class
            result["storageClass"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.volumes is not None:
            _v = self.volumes
            result["volumes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.system_account_secret_name is not None:
            _v = self.system_account_secret_name
            result["systemAccountSecretName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
