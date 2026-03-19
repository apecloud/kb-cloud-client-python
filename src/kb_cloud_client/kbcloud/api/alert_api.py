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


class AlertApi:
    """Alert API client.

    Provides methods for the alert endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._alert_statistic_endpoint = _Endpoint(
            settings={
                "response_type": AlertStatistic,
                "endpoint_path": "/api/v1/alerts/statistic",
                "http_method": "GET",
                "operation_id": "alert_statistic",
            },
            params_map={
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._batch_check_url_connectivity_endpoint = _Endpoint(
            settings={
                "response_type": URLCheck,
                "endpoint_path": "/api/v1/alerts/checkURL",
                "http_method": "POST",
                "operation_id": "batch_check_url_connectivity",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def alert_statistic(
        self,
        *,
        org_name: Union[str, UnsetType] = unset,
    ) -> AlertStatistic:
        """alert statistic.

        alert statistic
        :param org_name: name of the Org
        :type org_name: str, optional
        :rtype: AlertStatistic
        """
        kwargs: Dict[str, Any] = {}
        if org_name is not unset:
            kwargs["org_name"] = org_name
        return self._alert_statistic_endpoint.call_with_http_info(**kwargs)

    def batch_check_url_connectivity(
        self,
        body: URLCheck,
    ) -> URLCheck:
        """Batch check URLs connectivity.

        Tests multiple URLs for connectivity in parallel
        :type body: URLCheck
        :rtype: URLCheck
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._batch_check_url_connectivity_endpoint.call_with_http_info(**kwargs)
