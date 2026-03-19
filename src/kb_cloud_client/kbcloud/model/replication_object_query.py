# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .data_channel_endpoint_create import DataChannelEndpointCreate


@dataclass
class ReplicationObjectQuery:
    """ReplicationObjectQuery"""
    # Required fields
    # Optional fields
    source_engine_definition: Optional[str] = None
    target_engine_definition: Optional[str] = None
    endpoint: Optional[DataChannelEndpointCreate] = None
    node_type: Optional[str] = None
    node_value: Optional[str] = None
    query_node_type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ReplicationObjectQuery":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            source_engine_definition=data.get("sourceEngineDefinition"),
            target_engine_definition=data.get("targetEngineDefinition"),
            endpoint=DataChannelEndpointCreate.from_dict(data.get("endpoint")) if isinstance(data.get("endpoint"), dict) else data.get("endpoint"),
            node_type=data.get("nodeType"),
            node_value=data.get("nodeValue"),
            query_node_type=data.get("queryNodeType"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.source_engine_definition is not None:
            _v = self.source_engine_definition
            result["sourceEngineDefinition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.target_engine_definition is not None:
            _v = self.target_engine_definition
            result["targetEngineDefinition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint is not None:
            _v = self.endpoint
            result["endpoint"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_type is not None:
            _v = self.node_type
            result["nodeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_value is not None:
            _v = self.node_value
            result["nodeValue"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.query_node_type is not None:
            _v = self.query_node_type
            result["queryNodeType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
