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


class AlertconfigApi:
    """AlertConfig API client.

    Provides methods for the alertConfig endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_alert_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertConfig,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/config",
                "http_method": "GET",
                "operation_id": "get_alert_config",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._set_alert_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertConfig,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/config",
                "http_method": "PATCH",
                "operation_id": "set_alert_config",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "body": {
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def get_alert_config(
        self,
        org_name: str,
    ) -> AlertConfig:
        """Get alert config.
        :param org_name: name of the Org
        :type org_name: str
        :rtype: AlertConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._get_alert_config_endpoint.call_with_http_info(**kwargs)

    def set_alert_config(
        self,
        org_name: str,
        *,
        body: Union[AlertConfig, UnsetType] = unset,
    ) -> AlertConfig:
        """Set alert config.
        :param org_name: name of the Org
        :type org_name: str
        :type body: AlertConfig, optional
        :rtype: AlertConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if body is not unset:
            kwargs["body"] = body
        return self._set_alert_config_endpoint.call_with_http_info(**kwargs)
