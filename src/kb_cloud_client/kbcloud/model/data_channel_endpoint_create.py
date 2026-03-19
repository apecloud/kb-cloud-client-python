# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .custom_endpoint_create import CustomEndpointCreate
from .data_replication_endpoint_type import DataReplication_endpointType
from .kubeblocks_endpoint import KubeblocksEndpoint


@dataclass
class DataChannelEndpointCreate:
    """DataChannelEndpointCreate"""
    # Required fields
    # Optional fields
    engine_name: Optional[str] = None
    definition_name: Optional[str] = None
    endpoint_type: Optional[DataReplication_endpointType] = None
    custom: Optional[CustomEndpointCreate] = None
    kubeblocks: Optional[KubeblocksEndpoint] = None
    extra_cfgs: Optional[Dict[str, str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataChannelEndpointCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            engine_name=data.get("engineName"),
            definition_name=data.get("definitionName"),
            endpoint_type=DataReplication_endpointType.from_dict(data.get("endpointType")) if isinstance(data.get("endpointType"), dict) else data.get("endpointType"),
            custom=CustomEndpointCreate.from_dict(data.get("custom")) if isinstance(data.get("custom"), dict) else data.get("custom"),
            kubeblocks=KubeblocksEndpoint.from_dict(data.get("kubeblocks")) if isinstance(data.get("kubeblocks"), dict) else data.get("kubeblocks"),
            extra_cfgs=data.get("extraCfgs"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.definition_name is not None:
            _v = self.definition_name
            result["definitionName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.endpoint_type is not None:
            _v = self.endpoint_type
            result["endpointType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.custom is not None:
            _v = self.custom
            result["custom"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.kubeblocks is not None:
            _v = self.kubeblocks
            result["kubeblocks"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_cfgs is not None:
            _v = self.extra_cfgs
            result["extraCfgs"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
