# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .service_descriptor_address_style import ServiceDescriptorAddressStyle
from .service_selector import ServiceSelector


@dataclass
class ModeServiceRef:
    """Defines a ServiceRef for a cluster, enabling access to both external services and
Services provided by other Clusters. The defined serviceRef must be provided when creating cluster.
"""
    # Required fields
    name: str
    engine_name: str
    address_style: ServiceDescriptorAddressStyle
    helm_value_path: Dict[str, Any]
    # Optional fields
    service_selectors: Optional[List[ServiceSelector]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeServiceRef":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            engine_name=data.get("engineName"),
            address_style=ServiceDescriptorAddressStyle.from_dict(data.get("addressStyle")) if isinstance(data.get("addressStyle"), dict) else data.get("addressStyle"),
            helm_value_path=data.get("helmValuePath"),
            service_selectors=[ServiceSelector.from_dict(i) if isinstance(i, dict) else i for i in data.get("serviceSelectors")] if data.get("serviceSelectors") is not None else None,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine_name is not None:
            _v = self.engine_name
            result["engineName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.address_style is not None:
            _v = self.address_style
            result["addressStyle"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.helm_value_path is not None:
            _v = self.helm_value_path
            result["helmValuePath"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_selectors is not None:
            _v = self.service_selectors
            result["serviceSelectors"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
