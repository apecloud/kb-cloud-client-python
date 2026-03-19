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


class ImageregistryApi:
    """ImageRegistry API client.

    Provides methods for the imageRegistry endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_image_registry_endpoint = _Endpoint(
            settings={
                "response_type": ImageRegistry,
                "endpoint_path": "/admin/v1/imageRegistries",
                "http_method": "POST",
                "operation_id": "create_image_registry",
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
        self._delete_image_registry_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/imageRegistries/{imageRegistryName}",
                "http_method": "DELETE",
                "operation_id": "delete_image_registry",
            },
            params_map={
                "image_registry_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "imageRegistryName",
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
        self._get_image_registry_endpoint = _Endpoint(
            settings={
                "response_type": ImageRegistry,
                "endpoint_path": "/admin/v1/imageRegistries/{imageRegistryName}",
                "http_method": "GET",
                "operation_id": "get_image_registry",
            },
            params_map={
                "image_registry_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "imageRegistryName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_image_registries_endpoint = _Endpoint(
            settings={
                "response_type": ImageRegistryList,
                "endpoint_path": "/admin/v1/imageRegistries",
                "http_method": "GET",
                "operation_id": "list_image_registries",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_image_registry_endpoint = _Endpoint(
            settings={
                "response_type": ImageRegistry,
                "endpoint_path": "/admin/v1/imageRegistries/{imageRegistryName}",
                "http_method": "PATCH",
                "operation_id": "patch_image_registry",
            },
            params_map={
                "image_registry_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "imageRegistryName",
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


    def create_image_registry(
        self,
        body: ImageRegistry,
    ) -> ImageRegistry:
        """Create image registry.
        :type body: ImageRegistry
        :rtype: ImageRegistry
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_image_registry_endpoint.call_with_http_info(**kwargs)

    def delete_image_registry(
        self,
        image_registry_name: str,
        *,
        body: Union[ImageRegistry, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Delete image registry.
        :param image_registry_name: name of the image registry
        :type image_registry_name: str
        :type body: ImageRegistry, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["image_registry_name"] = image_registry_name
        if body is not unset:
            kwargs["body"] = body
        return self._delete_image_registry_endpoint.call_with_http_info(**kwargs)

    def get_image_registry(
        self,
        image_registry_name: str,
    ) -> ImageRegistry:
        """Get image registry.
        :param image_registry_name: name of the image registry
        :type image_registry_name: str
        :rtype: ImageRegistry
        """
        kwargs: Dict[str, Any] = {}
        kwargs["image_registry_name"] = image_registry_name
        return self._get_image_registry_endpoint.call_with_http_info(**kwargs)

    def list_image_registries(
        self,
    ) -> ImageRegistryList:
        """List image registries.

        List image registries
        :rtype: ImageRegistryList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_image_registries_endpoint.call_with_http_info(**kwargs)

    def patch_image_registry(
        self,
        image_registry_name: str,
        body: ImageRegistry,
    ) -> ImageRegistry:
        """Update image registry.

        partially update the specified image registry
        :param image_registry_name: name of the image registry
        :type image_registry_name: str
        :type body: ImageRegistry
        :rtype: ImageRegistry
        """
        kwargs: Dict[str, Any] = {}
        kwargs["image_registry_name"] = image_registry_name
        kwargs["body"] = body
        return self._patch_image_registry_endpoint.call_with_http_info(**kwargs)
