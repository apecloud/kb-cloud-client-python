# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union


from enum import Enum


class SysbenchTestType(str, Enum):
    """Test type for sysbench"""
    OLTP_DELETE = "oltp_delete"
    OLTP_INSERT = "oltp_insert"
    OLTP_POINT_SELECT = "oltp_point_select"
    OLTP_READ_ONLY = "oltp_read_only"
    OLTP_READ_WRITE = "oltp_read_write"
    OLTP_UPDATE_INDEX = "oltp_update_index"
    OLTP_UPDATE_NON_INDEX = "oltp_update_non_index"
    OLTP_WRITE_ONLY = "oltp_write_only"
    SELECT_RANDOM_POINTS = "select_random_points"
    SELECT_RANDOM_RANGES = "select_random_ranges"
    BULK_INSERT = "bulk_insert"
    OLTP_READ_WRITE_PCT = "oltp_read_write_pct"
