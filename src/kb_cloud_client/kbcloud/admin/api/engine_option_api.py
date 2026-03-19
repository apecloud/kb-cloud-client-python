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


class EngineoptionApi:
    """EngineOption API client.

    Provides methods for the engineOption endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": EngineOption,
                "endpoint_path": "/admin/v1/engineOptions",
                "http_method": "POST",
                "operation_id": "create_engine_option",
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
        self._delete_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/engineOptions/{engineName}",
                "http_method": "DELETE",
                "operation_id": "delete_engine_option",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._get_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": EngineOption,
                "endpoint_path": "/admin/v1/engineOptions/{engineName}",
                "http_method": "GET",
                "operation_id": "get_engine_option",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_option_history_endpoint = _Endpoint(
            settings={
                "response_type": EngineOptionHistoryList,
                "endpoint_path": "/admin/v1/engineOptionHistories",
                "http_method": "GET",
                "operation_id": "list_engine_option_history",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "query",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_options_endpoint = _Endpoint(
            settings={
                "response_type": EngineOptionList,
                "endpoint_path": "/admin/v1/engineOptions",
                "http_method": "GET",
                "operation_id": "list_engine_options",
            },
            params_map={
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._release_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": EngineOption,
                "endpoint_path": "/admin/v1/engineOptions/{engineName}/release",
                "http_method": "POST",
                "operation_id": "release_engine_option",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_engine_option_endpoint = _Endpoint(
            settings={
                "response_type": EngineOption,
                "endpoint_path": "/admin/v1/engineOptions/{engineName}",
                "http_method": "PUT",
                "operation_id": "update_engine_option",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
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


    def create_engine_option(
        self,
        body: EngineOption,
    ) -> EngineOption:
        """Create engineOption.

        Create a new engineOption
        :type body: EngineOption
        :rtype: EngineOption
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_engine_option_endpoint.call_with_http_info(**kwargs)

    def delete_engine_option(
        self,
        engine_name: str,
    ) -> APIErrorResponse:
        """Delete engineOption.

        Delete a engineOption
        :param engine_name: Name of the engine
        :type engine_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        return self._delete_engine_option_endpoint.call_with_http_info(**kwargs)

    def get_engine_option(
        self,
        engine_name: str,
        *,
        version: Union[EngineOptionVersion, UnsetType] = unset,
    ) -> EngineOption:
        """Get engineOption.

        Get a engineOption detail
        :param engine_name: Name of the engine
        :type engine_name: str
        :param version: The version of the engineOption to query, `current` from potentially modified data, `original` from the json files...
        :type version: EngineOptionVersion, optional
        :rtype: EngineOption
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        if version is not unset:
            kwargs["version"] = version
        return self._get_engine_option_endpoint.call_with_http_info(**kwargs)

    def list_engine_option_history(
        self,
        engine_name: str,
    ) -> EngineOptionHistoryList:
        """List engineOption history.

        List a engineOption histories of a engine
        :param engine_name: Name of the engine
        :type engine_name: str
        :rtype: EngineOptionHistoryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        return self._list_engine_option_history_endpoint.call_with_http_info(**kwargs)

    def list_engine_options(
        self,
        *,
        version: Union[EngineOptionVersion, UnsetType] = unset,
    ) -> EngineOptionList:
        """List all engineOptions.

        list all engineOptions
        :param version: The version of the engineOption to query, `current` from potentially modified data, `original` from the json files...
        :type version: EngineOptionVersion, optional
        :rtype: EngineOptionList
        """
        kwargs: Dict[str, Any] = {}
        if version is not unset:
            kwargs["version"] = version
        return self._list_engine_options_endpoint.call_with_http_info(**kwargs)

    def release_engine_option(
        self,
        engine_name: str,
    ) -> EngineOption:
        """Release engineOption.

        Release a engineOption
        :param engine_name: Name of the engineOption
        :type engine_name: str
        :rtype: EngineOption
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        return self._release_engine_option_endpoint.call_with_http_info(**kwargs)

    def update_engine_option(
        self,
        engine_name: str,
        body: EngineOption,
    ) -> EngineOption:
        """Update engineOption.

        Update a engineOption
        :param engine_name: Name of the engine
        :type engine_name: str
        :type body: EngineOption
        :rtype: EngineOption
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["body"] = body
        return self._update_engine_option_endpoint.call_with_http_info(**kwargs)
