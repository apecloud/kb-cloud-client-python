# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .engine_definition import EngineDefinition
from .engine_mapping import EngineMapping
from .module_definition import ModuleDefinition
from .standard_definition import StandardDefinition


@dataclass
class DataReplicationOption:
    """DataReplicationOption"""
    # Required fields
    # Optional fields
    module_definitions: Optional[List[ModuleDefinition]] = None
    engine_definitions: Optional[List[EngineDefinition]] = None
    mappings: Optional[List[EngineMapping]] = None
    standards: Optional[List[StandardDefinition]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataReplicationOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            module_definitions=[ModuleDefinition.from_dict(i) if isinstance(i, dict) else i for i in data.get("moduleDefinitions")] if data.get("moduleDefinitions") is not None else None,
            engine_definitions=[EngineDefinition.from_dict(i) if isinstance(i, dict) else i for i in data.get("engineDefinitions")] if data.get("engineDefinitions") is not None else None,
            mappings=[EngineMapping.from_dict(i) if isinstance(i, dict) else i for i in data.get("mappings")] if data.get("mappings") is not None else None,
            standards=[StandardDefinition.from_dict(i) if isinstance(i, dict) else i for i in data.get("standards")] if data.get("standards") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.module_definitions is not None:
            _v = self.module_definitions
            result["moduleDefinitions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine_definitions is not None:
            _v = self.engine_definitions
            result["engineDefinitions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.mappings is not None:
            _v = self.mappings
            result["mappings"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.standards is not None:
            _v = self.standards
            result["standards"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
