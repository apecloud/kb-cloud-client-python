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
class StorageProvisioner:
    """StorageProvisioner provides detailed information about the provisioner used by storage classes."""
    # Required fields
    # Optional fields
    provisioner: Optional[str] = None
    type_: Optional[str] = None
    cloud_provider: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StorageProvisioner":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            provisioner=data.get("provisioner"),
            type_=data.get("type"),
            cloud_provider=data.get("cloudProvider"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.provisioner is not None:
            _v = self.provisioner
            result["provisioner"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cloud_provider is not None:
            _v = self.cloud_provider
            result["cloudProvider"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
