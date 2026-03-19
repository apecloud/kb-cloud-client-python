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


class ProviderApi:
    """Provider API client.

    Provides methods for the provider endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_cloud_provider_endpoint = _Endpoint(
            settings={
                "response_type": Provider,
                "endpoint_path": "/admin/v1/providers",
                "http_method": "POST",
                "operation_id": "create_cloud_provider",
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
        self._delete_cloud_provider_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/providers/{providerName}",
                "http_method": "DELETE",
                "operation_id": "delete_cloud_provider",
            },
            params_map={
                "provider_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "providerName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._get_cloud_provider_endpoint = _Endpoint(
            settings={
                "response_type": Provider,
                "endpoint_path": "/admin/v1/providers/{providerName}",
                "http_method": "GET",
                "operation_id": "get_cloud_provider",
            },
            params_map={
                "provider_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "providerName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_cloud_providers_endpoint = _Endpoint(
            settings={
                "response_type": ProviderList,
                "endpoint_path": "/admin/v1/providers",
                "http_method": "GET",
                "operation_id": "list_cloud_providers",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_cloud_provider_endpoint = _Endpoint(
            settings={
                "response_type": Provider,
                "endpoint_path": "/admin/v1/providers/{providerName}",
                "http_method": "PATCH",
                "operation_id": "update_cloud_provider",
            },
            params_map={
                "provider_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "providerName",
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


    def create_cloud_provider(
        self,
        body: ProviderCreate,
    ) -> Provider:
        """Create a cloud provider.

        Create a cloud provider
        :type body: ProviderCreate
        :rtype: Provider
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_cloud_provider_endpoint.call_with_http_info(**kwargs)

    def delete_cloud_provider(
        self,
        provider_name: str,
    ) -> APIErrorResponse:
        """Delete a cloud provider.

        Delete a cloud provider
        :param provider_name: Name of the cloud provider
        :type provider_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_name"] = provider_name
        return self._delete_cloud_provider_endpoint.call_with_http_info(**kwargs)

    def get_cloud_provider(
        self,
        provider_name: str,
    ) -> Provider:
        """Get cloud provider.

        Get cloud provider
        :param provider_name: Name of the cloud provider
        :type provider_name: str
        :rtype: Provider
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_name"] = provider_name
        return self._get_cloud_provider_endpoint.call_with_http_info(**kwargs)

    def list_cloud_providers(
        self,
    ) -> ProviderList:
        """List cloud providers.

        List cloud providers
        :rtype: ProviderList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cloud_providers_endpoint.call_with_http_info(**kwargs)

    def update_cloud_provider(
        self,
        provider_name: str,
        body: ProviderUpdate,
    ) -> Provider:
        """Update a cloud provider.

        Update a cloud provider
        :param provider_name: Name of the cloud provider
        :type provider_name: str
        :type body: ProviderUpdate
        :rtype: Provider
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_name"] = provider_name
        kwargs["body"] = body
        return self._update_cloud_provider_endpoint.call_with_http_info(**kwargs)
