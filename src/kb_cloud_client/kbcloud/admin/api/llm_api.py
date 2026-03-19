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


class LlmApi:
    """Llm API client.

    Provides methods for the llm endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._add_llm_endpoint = _Endpoint(
            settings={
                "response_type": Llm,
                "endpoint_path": "/admin/v1/llm",
                "http_method": "POST",
                "operation_id": "add_llm",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._check_api_key_endpoint = _Endpoint(
            settings={
                "response_type": CheckAPIKey,
                "endpoint_path": "/admin/v1/llm/check",
                "http_method": "POST",
                "operation_id": "check_api_key",
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
        self._delete_llm_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/llm/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_llm",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_llm_by_id_endpoint = _Endpoint(
            settings={
                "response_type": Llm,
                "endpoint_path": "/admin/v1/llm/{id}",
                "http_method": "GET",
                "operation_id": "get_llm_by_id",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_available_model_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/admin/v1/llm/models",
                "http_method": "GET",
                "operation_id": "list_available_model",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_llm_endpoint = _Endpoint(
            settings={
                "response_type": LlmList,
                "endpoint_path": "/admin/v1/llm",
                "http_method": "GET",
                "operation_id": "list_llm",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_llm_endpoint = _Endpoint(
            settings={
                "response_type": Llm,
                "endpoint_path": "/admin/v1/llm/{id}",
                "http_method": "PATCH",
                "operation_id": "update_llm",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
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


    def add_llm(
        self,
        body: Llm,
        *,
        org_name: Union[str, UnsetType] = unset,
    ) -> Llm:
        """add LLM.
        :type body: Llm
        :param org_name: orgName the LLM belongs to
        :type org_name: str, optional
        :rtype: Llm
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        if org_name is not unset:
            kwargs["org_name"] = org_name
        return self._add_llm_endpoint.call_with_http_info(**kwargs)

    def check_api_key(
        self,
        body: Llm,
    ) -> CheckAPIKey:
        """check apikey available.

        check apikey available
        :type body: Llm
        :rtype: CheckAPIKey
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._check_api_key_endpoint.call_with_http_info(**kwargs)

    def delete_llm(
        self,
        id_: str,
    ) -> APIErrorResponse:
        """Delete LLM.
        :param id_: ID of the LLM
        :type id_: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        return self._delete_llm_endpoint.call_with_http_info(**kwargs)

    def get_llm_by_id(
        self,
        id_: str,
    ) -> Llm:
        """Get LLM by ID.
        :param id_: ID of the LLM
        :type id_: str
        :rtype: Llm
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        return self._get_llm_by_id_endpoint.call_with_http_info(**kwargs)

    def list_available_model(
        self,
    ) -> List[str]:
        """List available model.
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        return self._list_available_model_endpoint.call_with_http_info(**kwargs)

    def list_llm(
        self,
    ) -> LlmList:
        """List LLM.
        :rtype: LlmList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_llm_endpoint.call_with_http_info(**kwargs)

    def update_llm(
        self,
        id_: str,
        body: Llm,
    ) -> Llm:
        """Update LLM.
        :param id_: ID of the LLM
        :type id_: str
        :type body: Llm
        :rtype: Llm
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._update_llm_endpoint.call_with_http_info(**kwargs)
