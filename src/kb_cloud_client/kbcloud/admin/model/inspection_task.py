# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .inspection_supported_engines import InspectionSupportedEngines
from .inspection_task_item import InspectionTaskItem


@dataclass
class InspectionTask:
    """InspectionTask"""
    # Required fields
    # Optional fields
    id_: Optional[str] = None
    creator: Optional[str] = None
    status: Optional[str] = None
    engine: Optional[InspectionSupportedEngines] = None
    org_name: Optional[str] = None
    cluster_id: Optional[str] = None
    cluster_name: Optional[str] = None
    env_name: Optional[str] = None
    env_id: Optional[str] = None
    node_name: Optional[str] = None
    is_auto: Optional[bool] = None
    score: Optional[int] = None
    result: Optional[str] = None
    items: Optional[List[InspectionTaskItem]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InspectionTask":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            id_=data.get("id"),
            creator=data.get("creator"),
            status=data.get("status"),
            engine=InspectionSupportedEngines.from_dict(data.get("engine")) if isinstance(data.get("engine"), dict) else data.get("engine"),
            org_name=data.get("orgName"),
            cluster_id=data.get("clusterID"),
            cluster_name=data.get("clusterName"),
            env_name=data.get("envName"),
            env_id=data.get("envID"),
            node_name=data.get("nodeName"),
            is_auto=data.get("isAuto"),
            score=data.get("score"),
            result=data.get("result"),
            items=[InspectionTaskItem.from_dict(i) if isinstance(i, dict) else i for i in data.get("items")] if data.get("items") is not None else None,
            created_at=_parse_datetime(data.get("createdAt")),
            updated_at=_parse_datetime(data.get("updatedAt")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.id_ is not None:
            _v = self.id_
            result["id"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.creator is not None:
            _v = self.creator
            result["creator"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.status is not None:
            _v = self.status
            result["status"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.engine is not None:
            _v = self.engine
            result["engine"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.org_name is not None:
            _v = self.org_name
            result["orgName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_id is not None:
            _v = self.cluster_id
            result["clusterID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_name is not None:
            _v = self.cluster_name
            result["clusterName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env_name is not None:
            _v = self.env_name
            result["envName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.env_id is not None:
            _v = self.env_id
            result["envID"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.node_name is not None:
            _v = self.node_name
            result["nodeName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.is_auto is not None:
            _v = self.is_auto
            result["isAuto"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.score is not None:
            _v = self.score
            result["score"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.result is not None:
            _v = self.result
            result["result"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.items is not None:
            _v = self.items
            result["items"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.created_at is not None:
            _v = self.created_at
            result["createdAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.updated_at is not None:
            _v = self.updated_at
            result["updatedAt"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
