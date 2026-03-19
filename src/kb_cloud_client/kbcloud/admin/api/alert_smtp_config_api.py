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


class AlertsmtpconfigApi:
    """AlertSMTPConfig API client.

    Provides methods for the alertSMTPConfig endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_alert_smtp_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertSMTPConfig,
                "endpoint_path": "/admin/v1/alertSMTPConfig",
                "http_method": "GET",
                "operation_id": "get_alert_smtp_config",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_alert_smtp_config_endpoint = _Endpoint(
            settings={
                "response_type": AlertSMTPConfig,
                "endpoint_path": "/admin/v1/alertSMTPConfig",
                "http_method": "POST",
                "operation_id": "update_alert_smtp_config",
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


    def get_alert_smtp_config(
        self,
    ) -> AlertSMTPConfig:
        """Get alert SMTP config.
        :rtype: AlertSMTPConfig
        """
        kwargs: Dict[str, Any] = {}
        return self._get_alert_smtp_config_endpoint.call_with_http_info(**kwargs)

    def update_alert_smtp_config(
        self,
        body: AlertSMTPConfig,
    ) -> AlertSMTPConfig:
        """Update alert SMTP config.
        :type body: AlertSMTPConfig
        :rtype: AlertSMTPConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._update_alert_smtp_config_endpoint.call_with_http_info(**kwargs)
