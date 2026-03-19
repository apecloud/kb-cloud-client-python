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


class AlertmetricsApi:
    """AlertMetrics API client.

    Provides methods for the alertMetrics endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_alert_metrics_endpoint = _Endpoint(
            settings={
                "response_type": AlertMetricList,
                "endpoint_path": "/admin/v1/alerts/metrics",
                "http_method": "GET",
                "operation_id": "list_alert_metrics",
            },
            params_map={
                "category": {
                    "location": "query",
                    "attribute": "category",
                },
            },
            headers_map={
                "accept": ["*/*", "application/json"],
            },
            api_client=api_client,
        )


    def list_alert_metrics(
        self,
        *,
        category: Union[str, UnsetType] = unset,
    ) -> AlertMetricList:
        """List alert metric types.
        :type category: str, optional
        :rtype: AlertMetricList
        """
        kwargs: Dict[str, Any] = {}
        if category is not unset:
            kwargs["category"] = category
        return self._list_alert_metrics_endpoint.call_with_http_info(**kwargs)
