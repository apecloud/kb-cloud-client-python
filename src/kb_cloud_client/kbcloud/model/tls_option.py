# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .certificate_issuer import CertificateIssuer


@dataclass
class TlsOption:
    """TLS options"""
    # Required fields
    issuer: CertificateIssuer
    # Optional fields
    service_name: Optional[List[str]] = None
    ca_content: Optional[str] = None
    certificate_content: Optional[str] = None
    private_key_content: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TlsOption":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            issuer=CertificateIssuer.from_dict(data.get("issuer")) if isinstance(data.get("issuer"), dict) else data.get("issuer"),
            service_name=data.get("serviceName"),
            ca_content=data.get("caContent"),
            certificate_content=data.get("certificateContent"),
            private_key_content=data.get("privateKeyContent"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.issuer is not None:
            _v = self.issuer
            result["issuer"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.service_name is not None:
            _v = self.service_name
            result["serviceName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ca_content is not None:
            _v = self.ca_content
            result["caContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.certificate_content is not None:
            _v = self.certificate_content
            result["certificateContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.private_key_content is not None:
            _v = self.private_key_content
            result["privateKeyContent"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
