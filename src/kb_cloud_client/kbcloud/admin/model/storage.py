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
class Storage:
    """Storage is a specification that provides guidance accessing remote storage."""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    name: Optional[str] = None
    storage_provider: Optional[str] = None
    params: Optional[Dict[str, str]] = None
    env_name: Optional[str] = None
    created_by: Optional[datetime] = None
    cluster_id: Optional[str] = None
    cluster_metadata_address: Optional[str] = None
    updated_by: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    engines: Optional[List[str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Storage":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            storage_provider=data.get("storageProvider"),
            params=data.get("params"),
            env_name=data.get("envName"),
            created_by=_parse_datetime(data.get("createdBy")),
            cluster_id=data.get("clusterID"),
            cluster_metadata_address=data.get("clusterMetadataAddress"),
            updated_by=_parse_datetime(data.get("updatedBy")),
            tags=data.get("tags"),
            engines=data.get("engines"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.storage_provider is not None:
            _v = self.storage_provider
            result["storageProvider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.params is not None:
            _v = self.params
            result["params"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env_name is not None:
            _v = self.env_name
            result["envName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_by is not None:
            _v = self.created_by
            result["createdBy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_metadata_address is not None:
            _v = self.cluster_metadata_address
            result["clusterMetadataAddress"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_by is not None:
            _v = self.updated_by
            result["updatedBy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.tags is not None:
            _v = self.tags
            result["tags"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engines is not None:
            _v = self.engines
            result["engines"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
