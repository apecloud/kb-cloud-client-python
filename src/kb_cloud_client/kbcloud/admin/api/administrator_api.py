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


class AdministratorApi:
    """Administrator API client.

    Provides methods for the administrator endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_administrator_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/administrators",
                "http_method": "POST",
                "operation_id": "create_administrator",
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
        self._delete_administrator_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/administrators/{administratorID}",
                "http_method": "DELETE",
                "operation_id": "delete_administrator",
            },
            params_map={
                "administrator_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "administratorID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_administrators_endpoint = _Endpoint(
            settings={
                "response_type": UserList,
                "endpoint_path": "/admin/v1/administrators",
                "http_method": "GET",
                "operation_id": "list_administrators",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_administrator_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/administrators/{administratorID}",
                "http_method": "PATCH",
                "operation_id": "patch_administrator",
            },
            params_map={
                "administrator_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "administratorID",
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
        self._update_administrator_password_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/administrators/{administratorID}/password",
                "http_method": "PATCH",
                "operation_id": "update_administrator_password",
            },
            params_map={
                "administrator_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "administratorID",
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


    def create_administrator(
        self,
        body: UserCreate,
    ) -> User:
        """Create a new administrator.

        Create a new administrator
        :type body: UserCreate
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_administrator_endpoint.call_with_http_info(**kwargs)

    def delete_administrator(
        self,
        administrator_id: str,
    ) -> APIErrorResponse:
        """delete administrator.

        delete administrator
        :param administrator_id: ID of the administrator
        :type administrator_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["administrator_id"] = administrator_id
        return self._delete_administrator_endpoint.call_with_http_info(**kwargs)

    def list_administrators(
        self,
    ) -> UserList:
        """List administrators.

        List administrators
        :rtype: UserList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_administrators_endpoint.call_with_http_info(**kwargs)

    def patch_administrator(
        self,
        administrator_id: str,
        body: UserUpdate,
    ) -> User:
        """Update the information of the specified administrator.

        Update the information of the specified administrator
        :param administrator_id: ID of the administrator
        :type administrator_id: str
        :type body: UserUpdate
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        kwargs["administrator_id"] = administrator_id
        kwargs["body"] = body
        return self._patch_administrator_endpoint.call_with_http_info(**kwargs)

    def update_administrator_password(
        self,
        administrator_id: str,
        body: Password,
    ) -> APIErrorResponse:
        """Update administrator password.

        Update administrator password
        :param administrator_id: ID of the administrator
        :type administrator_id: str
        :type body: Password
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["administrator_id"] = administrator_id
        kwargs["body"] = body
        return self._update_administrator_password_endpoint.call_with_http_info(**kwargs)
