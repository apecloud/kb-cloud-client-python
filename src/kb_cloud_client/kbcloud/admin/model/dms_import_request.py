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
class DmsImportRequest:
    """the data of the import task"""
    # Required fields
    file_type: str
    table_name: str
    database: str
    # Optional fields
    first_line_column: Optional[bool] = None
    fields_terminal_by: Optional[str] = None
    field_names: Optional[List[str]] = None
    ignore_foreign_key: Optional[bool] = None
    file: Optional[bytes] = None
    skip_null: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DmsImportRequest":
        """Deserialize from a dict, recursively converting nested models."""
        if data is None:
            return None
        return cls(
            first_line_column=data.get("firstLineColumn"),
            fields_terminal_by=data.get("fieldsTerminalBy"),
            field_names=data.get("fieldNames"),
            ignore_foreign_key=data.get("ignoreForeignKey"),
            file_type=data.get("fileType"),
            file=data.get("file"),
            table_name=data.get("tableName"),
            database=data.get("database"),
            skip_null=data.get("skipNull"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a dict, omitting None values."""
        result: Dict[str, Any] = {}
        if self.first_line_column is not None:
            _v = self.first_line_column
            result["firstLineColumn"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.fields_terminal_by is not None:
            _v = self.fields_terminal_by
            result["fieldsTerminalBy"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.field_names is not None:
            _v = self.field_names
            result["fieldNames"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.ignore_foreign_key is not None:
            _v = self.ignore_foreign_key
            result["ignoreForeignKey"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.file_type is not None:
            _v = self.file_type
            result["fileType"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.file is not None:
            _v = self.file
            result["file"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.table_name is not None:
            _v = self.table_name
            result["tableName"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.database is not None:
            _v = self.database
            result["database"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        if self.skip_null is not None:
            _v = self.skip_null
            result["skipNull"] = _v.to_dict() if hasattr(_v, "to_dict") else (
                [i.to_dict() if hasattr(i, "to_dict") else i for i in _v] if isinstance(_v, list) else _v
            )
        return result
