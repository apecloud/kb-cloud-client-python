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
class ModeServiceRefHelmValuePath:
    """The path to be used in values. Separated with commas. ClusterCreate API will use these path to override values in the cluster chart."""
    # Required fields
    namespace: str
    cluster: str
    service_descriptor: str
    # Optional fields
    component: Optional[str] = None
    service: Optional[str] = None
    port: Optional[str] = None
    credential_component: Optional[str] = None
    credential_name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ModeServiceRefHelmValuePath":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            namespace=data.get("namespace"),
            cluster=data.get("cluster"),
            component=data.get("component"),
            service=data.get("service"),
            port=data.get("port"),
            credential_component=data.get("credentialComponent"),
            credential_name=data.get("credentialName"),
            service_descriptor=data.get("serviceDescriptor"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.namespace is not None:
            _v = self.namespace
            result["namespace"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.cluster is not None:
            _v = self.cluster
            result["cluster"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.component is not None:
            _v = self.component
            result["component"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service is not None:
            _v = self.service
            result["service"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.port is not None:
            _v = self.port
            result["port"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.credential_component is not None:
            _v = self.credential_component
            result["credentialComponent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.credential_name is not None:
            _v = self.credential_name
            result["credentialName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_descriptor is not None:
            _v = self.service_descriptor
            result["serviceDescriptor"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
