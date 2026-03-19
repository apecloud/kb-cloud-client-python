# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd
# This file is auto-generated. Do not edit manually.
from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional, Union

from kb_cloud_client.api_client import ApiClient, Endpoint as _Endpoint, UnsetType, unset
from kb_cloud_client.configuration import Configuration
from ..model import *  # noqa: F401, F403


class MetricsApi:
    """Metrics API client.

    Provides methods for the metrics endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_aggregate_meta_data_endpoint = _Endpoint(
            settings={
                "response_type": AggregateMetaData,
                "endpoint_path": "/admin/v1/metrics/metaData/aggregate",
                "http_method": "GET",
                "operation_id": "get_aggregate_meta_data",
            },
            params_map={
                "meta_data": {
                    "required": True,
                    "location": "query",
                    "attribute": "metaData",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_aggregate_meta_data(
        self,
        meta_data: AggregateMetaDataType,
        start: int,
        end: int,
    ) -> AggregateMetaData:
        """Get aggregate meta data.

        Get aggregate meta data including total count and time series
        :type meta_data: AggregateMetaDataType
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :rtype: AggregateMetaData
        """
        kwargs: Dict[str, Any] = {}
        kwargs["meta_data"] = meta_data
        kwargs["start"] = start
        kwargs["end"] = end
        return self._get_aggregate_meta_data_endpoint.call_with_http_info(**kwargs)
