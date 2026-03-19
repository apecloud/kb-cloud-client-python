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


class ClassApi:
    """Class API client.

    Provides methods for the class endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._batch_class_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/classes/batch",
                "http_method": "POST",
                "operation_id": "batch_class",
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
        self._create_class_endpoint = _Endpoint(
            settings={
                "response_type": Class,
                "endpoint_path": "/admin/v1/classes",
                "http_method": "POST",
                "operation_id": "create_class",
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
        self._delete_class_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/classes",
                "http_method": "DELETE",
                "operation_id": "delete_class",
            },
            params_map={
                "code": {
                    "required": True,
                    "location": "query",
                    "attribute": "code",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_classes_endpoint = _Endpoint(
            settings={
                "response_type": List[Class],
                "endpoint_path": "/admin/v1/classes",
                "http_method": "GET",
                "operation_id": "list_classes",
            },
            params_map={
                "engine_name": {
                    "location": "query",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_class_endpoint = _Endpoint(
            settings={
                "response_type": Class,
                "endpoint_path": "/admin/v1/classes",
                "http_method": "PATCH",
                "operation_id": "patch_class",
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


    def batch_class(
        self,
        *,
        body: Union[ClassBatch, UnsetType] = unset,
    ) -> APIErrorResponse:
        """batch update class over-commit.
        :type body: ClassBatch, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._batch_class_endpoint.call_with_http_info(**kwargs)

    def create_class(
        self,
        *,
        body: Union[Class, UnsetType] = unset,
    ) -> Class:
        """Create class.
        :type body: Class, optional
        :rtype: Class
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._create_class_endpoint.call_with_http_info(**kwargs)

    def delete_class(
        self,
        code: str,
    ) -> Dict[str, Any]:
        """Delete class.
        :param code: code
        :type code: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["code"] = code
        return self._delete_class_endpoint.call_with_http_info(**kwargs)

    def list_classes(
        self,
        *,
        engine_name: Union[str, UnsetType] = unset,
    ) -> List[Class]:
        """List classes.
        :param engine_name: filter by engine name
        :type engine_name: str, optional
        :rtype: List[Class]
        """
        kwargs: Dict[str, Any] = {}
        if engine_name is not unset:
            kwargs["engine_name"] = engine_name
        return self._list_classes_endpoint.call_with_http_info(**kwargs)

    def patch_class(
        self,
        *,
        body: Union[Class, UnsetType] = unset,
    ) -> Class:
        """Patch class.
        :type body: Class, optional
        :rtype: Class
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._patch_class_endpoint.call_with_http_info(**kwargs)
