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
class OpsRequestName:
    """OpsRequestName is the name of a KubeBlocks OpsRequest"""
    # Required fields
    ops_request_name: str
    # Optional fields
    dependent_ops_name: Optional[str] = None
    cluster_task_id: Optional[str] = None
    dependent_cluster_task_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsRequestName":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            ops_request_name=data.get("opsRequestName"),
            dependent_ops_name=data.get("dependentOpsName"),
            cluster_task_id=data.get("clusterTaskId"),
            dependent_cluster_task_id=data.get("dependentClusterTaskId"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.ops_request_name is not None:
            _v = self.ops_request_name
            result["opsRequestName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dependent_ops_name is not None:
            _v = self.dependent_ops_name
            result["dependentOpsName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster_task_id is not None:
            _v = self.cluster_task_id
            result["clusterTaskId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.dependent_cluster_task_id is not None:
            _v = self.dependent_cluster_task_id
            result["dependentClusterTaskId"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
