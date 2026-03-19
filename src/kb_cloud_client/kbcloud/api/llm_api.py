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
        self._list_llm_for_org_endpoint = _Endpoint(
            settings={
                "response_type": LlmList,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm",
                "http_method": "GET",
                "operation_id": "list_llm_for_org",
                "deprecated": True,
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
        self._add_llm_for_org_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm",
                "http_method": "POST",
                "operation_id": "add_llm_for_org",
                "deprecated": True,
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
                "accept": ["*/*"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._check_api_key_for_org_endpoint = _Endpoint(
            settings={
                "response_type": bool,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm/check",
                "http_method": "POST",
                "operation_id": "check_api_key_for_org",
                "deprecated": True,
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
        self._delete_llm_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_llm",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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
        self._get_llm_by_id_in_org_endpoint = _Endpoint(
            settings={
                "response_type": Llm,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm/{id}",
                "http_method": "GET",
                "operation_id": "get_llm_by_id_in_org",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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
        self._list_available_model_in_org_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/api/v1/organizations/{orgName}/llm/models",
                "http_method": "GET",
                "operation_id": "list_available_model_in_org",
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
        self._update_llm_endpoint = _Endpoint(
            settings={
                "response_type": Llm,
                "endpoint_path": "/api/v1/organizations/{orgName}/llm/{id}",
                "http_method": "PATCH",
                "operation_id": "update_llm",
                "deprecated": True,
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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


    def list_llm_for_org(
        self,
        org_name: str,
    ) -> LlmList:
        """List available LLM for org.

        available
        :type org_name: str
        :rtype: LlmList
        """
        warnings.warn("list_llm_for_org is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_llm_for_org_endpoint.call_with_http_info(**kwargs)

    def add_llm_for_org(
        self,
        org_name: str,
        body: Llm,
    ) -> APIErrorResponse:
        """add LLM for org.

        add LLM for org
        :type org_name: str
        :type body: Llm
        :rtype: APIErrorResponse
        """
        warnings.warn("add_llm_for_org is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._add_llm_for_org_endpoint.call_with_http_info(**kwargs)

    def check_api_key_for_org(
        self,
        org_name: str,
        body: CheckAPIKey,
    ) -> bool:
        """check apikey available for org.

        check apikey available for org
        :type org_name: str
        :type body: CheckAPIKey
        :rtype: bool
        """
        warnings.warn("check_api_key_for_org is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._check_api_key_for_org_endpoint.call_with_http_info(**kwargs)

    def delete_llm(
        self,
        org_name: str,
        id_: str,
    ) -> APIErrorResponse:
        """Delete LLM.
        :type org_name: str
        :param id_: ID of the LLM
        :type id_: str
        :rtype: APIErrorResponse
        """
        warnings.warn("delete_llm is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["id_"] = id_
        return self._delete_llm_endpoint.call_with_http_info(**kwargs)

    def get_llm_by_id_in_org(
        self,
        org_name: str,
        id_: str,
    ) -> Llm:
        """Get LLM by ID in org.
        :type org_name: str
        :param id_: ID of the LLM
        :type id_: str
        :rtype: Llm
        """
        warnings.warn("get_llm_by_id_in_org is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["id_"] = id_
        return self._get_llm_by_id_in_org_endpoint.call_with_http_info(**kwargs)

    def list_available_model_in_org(
        self,
        org_name: str,
    ) -> List[str]:
        """List available model in org.
        :type org_name: str
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_available_model_in_org_endpoint.call_with_http_info(**kwargs)

    def update_llm(
        self,
        org_name: str,
        id_: str,
        body: Llm,
    ) -> Llm:
        """Update LLM.
        :type org_name: str
        :param id_: ID of the LLM
        :type id_: str
        :type body: Llm
        :rtype: Llm
        """
        warnings.warn("update_llm is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._update_llm_endpoint.call_with_http_info(**kwargs)
