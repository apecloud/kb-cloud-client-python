# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_status import EngineStatus
from .engine_type import EngineType


@dataclass
class Engine:
    """Engine"""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    kb_version_constraint: Optional[str] = None
    type_: Optional[EngineType] = None
    installed: Optional[bool] = None
    provider: Optional[str] = None
    status: Optional[EngineStatus] = None
    available_version: Optional[List[str]] = None
    upgrade_history: Optional[str] = None
    err_msg: Optional[str] = None
    cluster_versions: Optional[List[str]] = None
    maturity_level: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Engine":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            description=data.get("description"),
            name=data.get("name"),
            version=data.get("version"),
            kb_version_constraint=data.get("kbVersionConstraint"),
            type_=EngineType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            installed=data.get("installed"),
            provider=data.get("provider"),
            status=EngineStatus.from_dict(data.get("status")) if isinstance(data.get("status"), dict) else data.get("status"),
            available_version=data.get("availableVersion"),
            upgrade_history=data.get("upgradeHistory"),
            err_msg=data.get("errMsg"),
            cluster_versions=data.get("clusterVersions"),
            maturity_level=data.get("maturityLevel"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
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
        if self.kb_version_constraint is not None:
            _v = self.kb_version_constraint
            result["kbVersionConstraint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.installed is not None:
            _v = self.installed
            result["installed"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.provider is not None:
            _v = self.provider
            result["provider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.available_version is not None:
            _v = self.available_version
            result["availableVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.upgrade_history is not None:
            _v = self.upgrade_history
            result["upgradeHistory"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.err_msg is not None:
            _v = self.err_msg
            result["errMsg"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_versions is not None:
            _v = self.cluster_versions
            result["clusterVersions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.maturity_level is not None:
            _v = self.maturity_level
            result["maturityLevel"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
