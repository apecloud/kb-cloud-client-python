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
        self._get_alert_sms_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertSMSConfig,
                "endpoint_path": "/admin/v1/alertSMSConfig",
                "http_method": "GET",
                "operation_id": "get_alert_sms_config",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_alert_tz_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertConfig,
                "endpoint_path": "/admin/v1/alerts/config",
                "http_method": "GET",
                "operation_id": "get_alert_tz_config",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._set_alert_tz_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertConfig,
                "endpoint_path": "/admin/v1/alerts/config",
                "http_method": "PATCH",
                "operation_id": "set_alert_tz_config",
            },
            params_map={
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
        self._update_alert_sms_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertSMSConfig,
                "endpoint_path": "/admin/v1/alertSMSConfig",
                "http_method": "POST",
                "operation_id": "update_alert_sms_config",
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


    def get_alert_sms_config(
        self,
    ) -> AlertSMSConfig:
        """Get alert SMS config.
        :rtype: AlertSMSConfig
        """
        kwargs: Dict[str, Any] = {}
        return self._get_alert_sms_config_endpoint.call_with_http_info(**kwargs)

    def get_alert_tz_config(
        self,
    ) -> AlertConfig:
        """Get alert time zone config.
        :rtype: AlertConfig
        """
        kwargs: Dict[str, Any] = {}
        return self._get_alert_tz_config_endpoint.call_with_http_info(**kwargs)

    def set_alert_tz_config(
        self,
        *,
        body: Union[AlertConfig, UnsetType] = unset,
    ) -> AlertConfig:
        """Set alert timezone config.
        :type body: AlertConfig, optional
        :rtype: AlertConfig
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._set_alert_tz_config_endpoint.call_with_http_info(**kwargs)

    def update_alert_sms_config(
        self,
        body: AlertSMSConfig,
    ) -> AlertSMSConfig:
        """Update alert SMS config.
        :type body: AlertSMSConfig
        :rtype: AlertSMSConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._update_alert_sms_config_endpoint.call_with_http_info(**kwargs)
