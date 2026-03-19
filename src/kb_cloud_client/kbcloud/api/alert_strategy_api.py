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


class AlertstrategyApi:
    """AlertStrategy API client.

    Provides methods for the alertStrategy endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_alert_strategy_endpoint = _Endpoint(
            settings={
                "response_type": AlertStrategy,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/strategies",
                "http_method": "POST",
                "operation_id": "create_alert_strategy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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
        self._delete_alert_strategy_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/strategies/{strategyId}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_strategy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "strategy_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "strategyId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_strategies_endpoint = _Endpoint(
            settings={
                "response_type": AlertStrategyList,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/strategies",
                "http_method": "GET",
                "operation_id": "list_alert_strategies",
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
        self._patch_alert_strategy_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/strategies",
                "http_method": "PATCH",
                "operation_id": "patch_alert_strategy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
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
        self._update_alert_strategy_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/strategies/{strategyId}",
                "http_method": "PATCH",
                "operation_id": "update_alert_strategy",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "strategy_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "strategyId",
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


    def create_alert_strategy(
        self,
        org_name: str,
        body: AlertStrategy,
    ) -> AlertStrategy:
        """Create alert strategy in org.
        :param org_name: name of the Org
        :type org_name: str
        :type body: AlertStrategy
        :rtype: AlertStrategy
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_alert_strategy_endpoint.call_with_http_info(**kwargs)

    def delete_alert_strategy(
        self,
        org_name: str,
        strategy_id: str,
    ) -> Dict[str, Any]:
        """Delete alert strategy.
        :param org_name: name of the Org
        :type org_name: str
        :param strategy_id: id of the alert strategies
        :type strategy_id: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["strategy_id"] = strategy_id
        return self._delete_alert_strategy_endpoint.call_with_http_info(**kwargs)

    def list_alert_strategies(
        self,
        org_name: str,
    ) -> AlertStrategyList:
        """List alert strategies.
        :param org_name: name of the Org
        :type org_name: str
        :rtype: AlertStrategyList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_alert_strategies_endpoint.call_with_http_info(**kwargs)

    def patch_alert_strategy(
        self,
        org_name: str,
        body: AlertStrategy,
    ) -> Dict[str, Any]:
        """Update alert strategy.
        :param org_name: name of the Org
        :type org_name: str
        :type body: AlertStrategy
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._patch_alert_strategy_endpoint.call_with_http_info(**kwargs)

    def update_alert_strategy(
        self,
        org_name: str,
        strategy_id: str,
        body: AlertStrategy,
    ) -> Dict[str, Any]:
        """Update alert strategy.
        :param org_name: name of the Org
        :type org_name: str
        :param strategy_id: id of the alert strategies
        :type strategy_id: str
        :type body: AlertStrategy
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["strategy_id"] = strategy_id
        kwargs["body"] = body
        return self._update_alert_strategy_endpoint.call_with_http_info(**kwargs)
