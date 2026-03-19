# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ....api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .import_capability_type import ImportCapabilityType
from .import_connection_field import ImportConnectionField
from .import_replication_metadata import ImportReplicationMetadata
from .import_source_category import ImportSourceCategory
from .import_source_type import ImportSourceType
from .localized_description import LocalizedDescription


@dataclass
class ImportSupportedSource:
    """Supported data source definition for an import capability."""
    # Required fields
    type_: ImportSourceType
    category: ImportSourceCategory
    name: str
    supported: bool
    connection_fields: List[ImportConnectionField]
    # Optional fields
    description: Optional[LocalizedDescription] = None
    guide: Optional[LocalizedDescription] = None
    capabilities: Optional[List[ImportCapabilityType]] = None
    requirements: Optional[List[LocalizedDescription]] = None
    supported_versions: Optional[List[str]] = None
    replication_metadata: Optional[ImportReplicationMetadata] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImportSupportedSource":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            type_=ImportSourceType.from_dict(data.get("type")) if isinstance(data.get("type"), dict) else data.get("type"),
            category=ImportSourceCategory.from_dict(data.get("category")) if isinstance(data.get("category"), dict) else data.get("category"),
            name=data.get("name"),
            supported=data.get("supported"),
            description=LocalizedDescription.from_dict(data.get("description")) if isinstance(data.get("description"), dict) else data.get("description"),
            guide=LocalizedDescription.from_dict(data.get("guide")) if isinstance(data.get("guide"), dict) else data.get("guide"),
            capabilities=[ImportCapabilityType.from_dict(i) if isinstance(i, dict) else i for i in data.get("capabilities")] if data.get("capabilities") is not None else None,
            requirements=[LocalizedDescription.from_dict(i) if isinstance(i, dict) else i for i in data.get("requirements")] if data.get("requirements") is not None else None,
            connection_fields=[ImportConnectionField.from_dict(i) if isinstance(i, dict) else i for i in data.get("connectionFields")] if data.get("connectionFields") is not None else None,
            supported_versions=data.get("supportedVersions"),
            replication_metadata=ImportReplicationMetadata.from_dict(data.get("replicationMetadata")) if isinstance(data.get("replicationMetadata"), dict) else data.get("replicationMetadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            _v = self.type_
            result["type"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.category is not None:
            _v = self.category
            result["category"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.supported is not None:
            _v = self.supported
            result["supported"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.description is not None:
            _v = self.description
            result["description"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.guide is not None:
            _v = self.guide
            result["guide"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.capabilities is not None:
            _v = self.capabilities
            result["capabilities"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.requirements is not None:
            _v = self.requirements
            result["requirements"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.connection_fields is not None:
            _v = self.connection_fields
            result["connectionFields"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.supported_versions is not None:
            _v = self.supported_versions
            result["supportedVersions"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.replication_metadata is not None:
            _v = self.replication_metadata
            result["replicationMetadata"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
