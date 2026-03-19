# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from ...api_client import _parse_datetime  # noqa: F401 – used in generated from_dict

from .dms_check_constraint import DmsCheckConstraint
from .dms_exclude_constraint import DmsExcludeConstraint
from .dms_foreign_key import DmsForeignKey
from .dms_primary_key import DmsPrimaryKey
from .dms_table_column import DmsTableColumn
from .dms_table_index import DmsTableIndex
from .dms_table_options import DmsTableOptions
from .dms_table_partitioning import DmsTablePartitioning
from .dms_unique_key import DmsUniqueKey


@dataclass
class DmsTableMetadata:
    """DmsTableMetadata"""
    # Required fields
    # Optional fields
    name: Optional[str] = None
    schema: Optional[str] = None
    database: Optional[str] = None
    comment: Optional[str] = None
    columns: Optional[List[DmsTableColumn]] = None
    indexes: Optional[List[DmsTableIndex]] = None
    primary_key: Optional[DmsPrimaryKey] = None
    foreign_keys: Optional[List[DmsForeignKey]] = None
    unique_keys: Optional[List[DmsUniqueKey]] = None
    check_constraints: Optional[List[DmsCheckConstraint]] = None
    exclude_constraints: Optional[List[DmsExcludeConstraint]] = None
    partitioning: Optional[DmsTablePartitioning] = None
    options: Optional[DmsTableOptions] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsTableMetadata":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            name=data.get("name"),
            schema=data.get("schema"),
            database=data.get("database"),
            comment=data.get("comment"),
            columns=[DmsTableColumn.from_dict(i) if isinstance(i, dict) else i for i in data.get("columns")] if data.get("columns") is not None else None,
            indexes=[DmsTableIndex.from_dict(i) if isinstance(i, dict) else i for i in data.get("indexes")] if data.get("indexes") is not None else None,
            primary_key=DmsPrimaryKey.from_dict(data.get("primaryKey")) if isinstance(data.get("primaryKey"), dict) else data.get("primaryKey"),
            foreign_keys=[DmsForeignKey.from_dict(i) if isinstance(i, dict) else i for i in data.get("foreignKeys")] if data.get("foreignKeys") is not None else None,
            unique_keys=[DmsUniqueKey.from_dict(i) if isinstance(i, dict) else i for i in data.get("uniqueKeys")] if data.get("uniqueKeys") is not None else None,
            check_constraints=[DmsCheckConstraint.from_dict(i) if isinstance(i, dict) else i for i in data.get("checkConstraints")] if data.get("checkConstraints") is not None else None,
            exclude_constraints=[DmsExcludeConstraint.from_dict(i) if isinstance(i, dict) else i for i in data.get("excludeConstraints")] if data.get("excludeConstraints") is not None else None,
            partitioning=DmsTablePartitioning.from_dict(data.get("partitioning")) if isinstance(data.get("partitioning"), dict) else data.get("partitioning"),
            options=DmsTableOptions.from_dict(data.get("options")) if isinstance(data.get("options"), dict) else data.get("options"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.name is not None:
            _v = self.name
            result["name"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.schema is not None:
            _v = self.schema
            result["schema"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.comment is not None:
            _v = self.comment
            result["comment"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.columns is not None:
            _v = self.columns
            result["columns"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.indexes is not None:
            _v = self.indexes
            result["indexes"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.primary_key is not None:
            _v = self.primary_key
            result["primaryKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.foreign_keys is not None:
            _v = self.foreign_keys
            result["foreignKeys"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.unique_keys is not None:
            _v = self.unique_keys
            result["uniqueKeys"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.check_constraints is not None:
            _v = self.check_constraints
            result["checkConstraints"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.exclude_constraints is not None:
            _v = self.exclude_constraints
            result["excludeConstraints"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.partitioning is not None:
            _v = self.partitioning
            result["partitioning"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.options is not None:
            _v = self.options
            result["options"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
