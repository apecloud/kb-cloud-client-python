# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .component import Component
from .environment_module import EnvironmentModule
from .node_pool import NodePool
from .register import Register
from .storage_config import StorageConfig


@dataclass
class ProvisionConfig:
    """Configuration to provision infrastructure for this environment"""
    # Required fields
    register: Register
    component: Component
    # Optional fields
    node_pool: Optional[List[NodePoolNode]] = None
    storage: Optional[StorageConfig] = None
    modules: Optional[List[EnvironmentModule]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProvisionConfig":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            register=Register.from_dict(data.get("register")) if isinstance(data.get("register"), dict) else data.get("register"),
            component=Component.from_dict(data.get("component")) if isinstance(data.get("component"), dict) else data.get("component"),
            node_pool=NodePool.from_dict(data.get("nodePool")) if isinstance(data.get("nodePool"), dict) else data.get("nodePool"),
            storage=StorageConfig.from_dict(data.get("storage")) if isinstance(data.get("storage"), dict) else data.get("storage"),
            modules=[EnvironmentModule.from_dict(i) if isinstance(i, dict) else i for i in data.get("modules")] if data.get("modules") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.register is not None:
            _v = self.register
            result["register"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_pool is not None:
            _v = self.node_pool
            result["nodePool"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage is not None:
            _v = self.storage
            result["storage"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.modules is not None:
            _v = self.modules
            result["modules"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
