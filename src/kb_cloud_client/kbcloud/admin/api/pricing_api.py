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


class PricingApi:
    """Pricing API client.

    Provides methods for the pricing endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._delete_environment_pricing_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/pricing",
                "http_method": "DELETE",
                "operation_id": "delete_environment_pricing",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "query",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_environment_pricing_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentPricingList,
                "endpoint_path": "/admin/v1/pricing",
                "http_method": "GET",
                "operation_id": "get_environment_pricing",
            },
            params_map={
                "environment_name": {
                    "location": "query",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_global_pricing_endpoint = _Endpoint(
            settings={
                "response_type": GlobalPricing,
                "endpoint_path": "/admin/v1/pricing/global",
                "http_method": "GET",
                "operation_id": "get_global_pricing",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._save_environment_pricing_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/pricing",
                "http_method": "POST",
                "operation_id": "save_environment_pricing",
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
        self._save_global_pricing_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/pricing/global",
                "http_method": "POST",
                "operation_id": "save_global_pricing",
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


    def delete_environment_pricing(
        self,
        environment_name: str,
    ) -> Dict[str, Any]:
        """Delete the environment pricing.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._delete_environment_pricing_endpoint.call_with_http_info(**kwargs)

    def get_environment_pricing(
        self,
        *,
        environment_name: Union[str, UnsetType] = unset,
    ) -> EnvironmentPricingList:
        """Get the environment pricing.
        :param environment_name: name of the environment (if provided, returns a list with one item; if omitted, returns all environment prices)
        :type environment_name: str, optional
        :rtype: EnvironmentPricingList
        """
        kwargs: Dict[str, Any] = {}
        if environment_name is not unset:
            kwargs["environment_name"] = environment_name
        return self._get_environment_pricing_endpoint.call_with_http_info(**kwargs)

    def get_global_pricing(
        self,
    ) -> GlobalPricing:
        """Get the global information of pricing.
        :rtype: GlobalPricing
        """
        kwargs: Dict[str, Any] = {}
        return self._get_global_pricing_endpoint.call_with_http_info(**kwargs)

    def save_environment_pricing(
        self,
        *,
        body: Union[EnvironmentPricing, UnsetType] = unset,
    ) -> Dict[str, Any]:
        """Save the environment pricing.
        :type body: EnvironmentPricing, optional
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._save_environment_pricing_endpoint.call_with_http_info(**kwargs)

    def save_global_pricing(
        self,
        *,
        body: Union[GlobalPricing, UnsetType] = unset,
    ) -> Dict[str, Any]:
        """Save the global information of pricing.
        :type body: GlobalPricing, optional
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._save_global_pricing_endpoint.call_with_http_info(**kwargs)
