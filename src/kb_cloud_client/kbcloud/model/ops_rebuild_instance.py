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
class OpsRebuildInstance:
    """rebuild the instances of the cluster."""
    # Required fields
    # Optional fields
    ignore_role_check: Optional[bool] = None
    requests: Optional[List[Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OpsRebuildInstance":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            ignore_role_check=data.get("ignoreRoleCheck"),
            requests=data.get("requests"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.ignore_role_check is not None:
            _v = self.ignore_role_check
            result["ignoreRoleCheck"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.requests is not None:
            _v = self.requests
            result["requests"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
