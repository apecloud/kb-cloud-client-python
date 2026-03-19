# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict



@dataclass
class ParamTplListItem:
    """parameter template information"""
    # Required fields
    description: str
    major_version: str
    engine: str
    component: str
    name: str
    partition: str
    param_tpl_id: str
    # Optional fields
    org_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParamTplListItem":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            org_name=data.get("orgName"),
            created_at=_parse_datetime(data.get("createdAt")),
            description=data.get("description"),
            major_version=data.get("majorVersion"),
            engine=data.get("engine"),
            component=data.get("component"),
            name=data.get("name"),
            partition=data.get("partition"),
            param_tpl_id=data.get("paramTplID"),
            updated_at=_parse_datetime(data.get("updatedAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.major_version is not None:
            _v = self.major_version
            result["majorVersion"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.partition is not None:
            _v = self.partition
            result["partition"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.param_tpl_id is not None:
            _v = self.param_tpl_id
            result["paramTplID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
