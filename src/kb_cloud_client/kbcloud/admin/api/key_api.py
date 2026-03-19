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


class KeyApi:
    """Key API client.

    Provides methods for the key endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_key_endpoint = _Endpoint(
            settings={
                "response_type": Key,
                "endpoint_path": "/admin/v1/keys",
                "http_method": "POST",
                "operation_id": "create_key",
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
        self._delete_key_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/keys/{keyName}",
                "http_method": "DELETE",
                "operation_id": "delete_key",
            },
            params_map={
                "key_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "keyName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._get_key_endpoint = _Endpoint(
            settings={
                "response_type": Key,
                "endpoint_path": "/admin/v1/keys/{keyName}",
                "http_method": "GET",
                "operation_id": "get_key",
            },
            params_map={
                "key_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "keyName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_keys_endpoint = _Endpoint(
            settings={
                "response_type": KeyList,
                "endpoint_path": "/admin/v1/keys",
                "http_method": "GET",
                "operation_id": "list_keys",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_key_endpoint = _Endpoint(
            settings={
                "response_type": Key,
                "endpoint_path": "/admin/v1/keys/{keyName}",
                "http_method": "PATCH",
                "operation_id": "update_key",
            },
            params_map={
                "key_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "keyName",
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


    def create_key(
        self,
        *,
        body: Union[Key, UnsetType] = unset,
    ) -> Key:
        """Create a new key.

        Store a new key in the system.
        :type body: Key, optional
        :rtype: Key
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._create_key_endpoint.call_with_http_info(**kwargs)

    def delete_key(
        self,
        key_name: str,
    ) -> APIErrorResponse:
        """Delete a specific key.
        :param key_name: the name of key
        :type key_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key_name"] = key_name
        return self._delete_key_endpoint.call_with_http_info(**kwargs)

    def get_key(
        self,
        key_name: str,
    ) -> Key:
        """get an existing key.
        :param key_name: the name of key
        :type key_name: str
        :rtype: Key
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key_name"] = key_name
        return self._get_key_endpoint.call_with_http_info(**kwargs)

    def list_keys(
        self,
    ) -> KeyList:
        """List Keys.
        :rtype: KeyList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_keys_endpoint.call_with_http_info(**kwargs)

    def update_key(
        self,
        key_name: str,
        body: Key,
    ) -> Key:
        """Update an existing key.
        :param key_name: the name of key
        :type key_name: str
        :type body: Key
        :rtype: Key
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key_name"] = key_name
        kwargs["body"] = body
        return self._update_key_endpoint.call_with_http_info(**kwargs)
