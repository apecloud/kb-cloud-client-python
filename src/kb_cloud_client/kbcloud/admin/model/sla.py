# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .cluster_list_item import ClusterListItem
from .outage_record_list import OutageRecordList


@dataclass
class SLA:
    """The SLA (Service Level Agreement) for a cluster."""
    # Required fields
    # Optional fields
    cluster: Optional[ClusterListItem] = None
    detail: Optional[List[OutageRecord]] = None
    sla: Optional[float] = None
    total_duration: Optional[int] = None
    total_downtime: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SLA":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            cluster=ClusterListItem.from_dict(data.get("cluster")) if isinstance(data.get("cluster"), dict) else data.get("cluster"),
            detail=OutageRecordList.from_dict(data.get("detail")) if isinstance(data.get("detail"), dict) else data.get("detail"),
            sla=data.get("sla"),
            total_duration=data.get("totalDuration"),
            total_downtime=data.get("totalDowntime"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.detail is not None:
            _v = self.detail
            result["detail"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.sla is not None:
            _v = self.sla
            result["sla"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_duration is not None:
            _v = self.total_duration
            result["totalDuration"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.total_downtime is not None:
            _v = self.total_downtime
            result["totalDowntime"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
