# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .environment_delete_policy import EnvironmentDeletePolicy
from .environment_type import EnvironmentType
from .provision_config import ProvisionConfig
from .scheduling_config import SchedulingConfig


@dataclass
class EnvironmentCreate:
    """Environment creation info"""
    # Required fields
    name: str
    type_: EnvironmentType
    provision_config: ProvisionConfig
    organizations: List[str]
    provider: str
    region: str
    display_name: str
    # Optional fields
    scheduling_config: Optional[SchedulingConfig] = None
    availability_zones: Optional[List[str]] = None
    description: Optional[str] = None
    id_: Optional[str] = None
    extra_info: Optional[str] = None
    delete_policy: Optional[EnvironmentDeletePolicy] = None
    overwrite: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnvironmentCreate":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            type_=EnvironmentType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            scheduling_config=SchedulingConfig.from_dict(data.get("schedulingConfig")) if isinstance(data.get("schedulingConfig"), dict) else data.get("schedulingConfig"),
            provision_config=ProvisionConfig.from_dict(data.get("provisionConfig")) if isinstance(data.get("provisionConfig"), dict) else data.get("provisionConfig"),
            organizations=data.get("organizations"),
            provider=data.get("provider"),
            region=data.get("region"),
            availability_zones=data.get("availabilityZones"),
            description=data.get("description"),
            display_name=data.get("displayName"),
            id_=data.get("id"),
            extra_info=data.get("extraInfo"),
            delete_policy=EnvironmentDeletePolicy.from_dict(data.get("deletePolicy")) if isinstance(data.get("deletePolicy"), dict) else data.get("deletePolicy"),
            overwrite=data.get("overwrite"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.scheduling_config is not None:
            _v = self.scheduling_config
            result["schedulingConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.provision_config is not None:
            _v = self.provision_config
            result["provisionConfig"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.organizations is not None:
            _v = self.organizations
            result["organizations"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.provider is not None:
            _v = self.provider
            result["provider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.region is not None:
            _v = self.region
            result["region"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.availability_zones is not None:
            _v = self.availability_zones
            result["availabilityZones"] = _v.to_dict() if hasattr(_v, "to_dict") else (
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
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.extra_info is not None:
            _v = self.extra_info
            result["extraInfo"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.delete_policy is not None:
            _v = self.delete_policy
            result["deletePolicy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.overwrite is not None:
            _v = self.overwrite
            result["overwrite"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
