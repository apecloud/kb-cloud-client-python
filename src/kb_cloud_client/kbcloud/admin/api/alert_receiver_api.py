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


class AlertreceiverApi:
    """AlertReceiver API client.

    Provides methods for the alertReceiver endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_alert_receiver_endpoint = _Endpoint(
            settings={
                "response_type": AlertReceiver,
                "endpoint_path": "/admin/v1/alerts/receivers",
                "http_method": "POST",
                "operation_id": "create_alert_receiver",
            },
            params_map={
                "category": {
                    "required": True,
                    "location": "query",
                    "attribute": "category",
                },
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
        self._delete_alert_receiver_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/alerts/receivers/{receiverId}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_receiver",
            },
            params_map={
                "receiver_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "receiverId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_receivers_endpoint = _Endpoint(
            settings={
                "response_type": AlertReceiverList,
                "endpoint_path": "/admin/v1/alerts/receivers",
                "http_method": "GET",
                "operation_id": "list_alert_receivers",
            },
            params_map={
                "category": {
                    "location": "query",
                    "attribute": "category",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_alert_receiver_endpoint = _Endpoint(
            settings={
                "response_type": AlertReceiver,
                "endpoint_path": "/admin/v1/alerts/receivers/{receiverId}",
                "http_method": "PATCH",
                "operation_id": "update_alert_receiver",
            },
            params_map={
                "receiver_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "receiverId",
                },
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


    def create_alert_receiver(
        self,
        category: AlertReceiverCategory,
        body: AlertReceiver,
    ) -> AlertReceiver:
        """Create alert receiver.
        :param category: alert receiver category
        :type category: AlertReceiverCategory
        :type body: AlertReceiver
        :rtype: AlertReceiver
        """
        kwargs: Dict[str, Any] = {}
        kwargs["category"] = category
        kwargs["body"] = body
        return self._create_alert_receiver_endpoint.call_with_http_info(**kwargs)

    def delete_alert_receiver(
        self,
        receiver_id: str,
    ) -> APIErrorResponse:
        """Delete alert receiver.
        :param receiver_id: receiver id
        :type receiver_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["receiver_id"] = receiver_id
        return self._delete_alert_receiver_endpoint.call_with_http_info(**kwargs)

    def list_alert_receivers(
        self,
        *,
        category: Union[AlertReceiverCategory, UnsetType] = unset,
    ) -> AlertReceiverList:
        """List alert receivers.
        :param category: alert receiver category
        :type category: AlertReceiverCategory, optional
        :rtype: AlertReceiverList
        """
        kwargs: Dict[str, Any] = {}
        if category is not unset:
            kwargs["category"] = category
        return self._list_alert_receivers_endpoint.call_with_http_info(**kwargs)

    def update_alert_receiver(
        self,
        receiver_id: str,
        body: AlertReceiver,
    ) -> AlertReceiver:
        """Update alert receiver.
        :param receiver_id: receiver id
        :type receiver_id: str
        :type body: AlertReceiver
        :rtype: AlertReceiver
        """
        kwargs: Dict[str, Any] = {}
        kwargs["receiver_id"] = receiver_id
        kwargs["body"] = body
        return self._update_alert_receiver_endpoint.call_with_http_info(**kwargs)
