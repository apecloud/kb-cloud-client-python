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


class UserApi:
    """User API client.

    Provides methods for the user endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_user_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/users",
                "http_method": "POST",
                "operation_id": "create_user",
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
        self._create_user_apikey_endpoint = _Endpoint(
            settings={
                "response_type": ApikeyWithSK,
                "endpoint_path": "/admin/v1/user/apikeys",
                "http_method": "POST",
                "operation_id": "create_user_apikey",
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
        self._delete_apikey_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/user/apikey/{keyName}",
                "http_method": "DELETE",
                "operation_id": "delete_apikey",
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
        self._delete_user_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/users/{userID}",
                "http_method": "DELETE",
                "operation_id": "delete_user",
            },
            params_map={
                "user_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "userID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_authenticated_user_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/user",
                "http_method": "GET",
                "operation_id": "get_authenticated_user",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_users_endpoint = _Endpoint(
            settings={
                "response_type": UserList,
                "endpoint_path": "/admin/v1/users",
                "http_method": "GET",
                "operation_id": "list_users",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_ap_ikey_endpoint = _Endpoint(
            settings={
                "response_type": Apikey,
                "endpoint_path": "/admin/v1/user/apikey/{keyName}",
                "http_method": "PATCH",
                "operation_id": "patch_ap_ikey",
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
        self._patch_authenticated_user_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/user",
                "http_method": "PATCH",
                "operation_id": "patch_authenticated_user",
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
        self._patch_user_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/admin/v1/users/{userID}",
                "http_method": "PATCH",
                "operation_id": "patch_user",
            },
            params_map={
                "user_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "userID",
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
        self._read_user_apikeys_endpoint = _Endpoint(
            settings={
                "response_type": ApikeyList,
                "endpoint_path": "/admin/v1/user/apikeys",
                "http_method": "GET",
                "operation_id": "read_user_apikeys",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_authenticated_user_password_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/user/password",
                "http_method": "PATCH",
                "operation_id": "update_authenticated_user_password",
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
        self._update_user_password_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/users/{userID}/password",
                "http_method": "PATCH",
                "operation_id": "update_user_password",
            },
            params_map={
                "user_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "userID",
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


    def create_user(
        self,
        body: UserCreate,
    ) -> User:
        """Create a new user.

        Create a new user
        :type body: UserCreate
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_user_endpoint.call_with_http_info(**kwargs)

    def create_user_apikey(
        self,
        body: ApikeyCreate,
    ) -> ApikeyWithSK:
        """Create apikey of the authenticated user.

        Create apikey of the authenticated user
        :type body: ApikeyCreate
        :rtype: ApikeyWithSK
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_user_apikey_endpoint.call_with_http_info(**kwargs)

    def delete_apikey(
        self,
        key_name: str,
    ) -> APIErrorResponse:
        """Delete apikey.

        delete apikey
        :param key_name: Name of the Apikey
        :type key_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key_name"] = key_name
        return self._delete_apikey_endpoint.call_with_http_info(**kwargs)

    def delete_user(
        self,
        user_id: str,
    ) -> APIErrorResponse:
        """delete user.

        delete user
        :param user_id: ID of the user
        :type user_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_id"] = user_id
        return self._delete_user_endpoint.call_with_http_info(**kwargs)

    def get_authenticated_user(
        self,
    ) -> User:
        """Get authenticated user.

        Get authenticated login user info
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        return self._get_authenticated_user_endpoint.call_with_http_info(**kwargs)

    def list_users(
        self,
    ) -> UserList:
        """List users.

        List users
        :rtype: UserList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_users_endpoint.call_with_http_info(**kwargs)

    def patch_ap_ikey(
        self,
        key_name: str,
        body: ApikeyCreate,
    ) -> Apikey:
        """Update apikey information.

        partially update the specified apikey
        :param key_name: Name of the apikey
        :type key_name: str
        :type body: ApikeyCreate
        :rtype: Apikey
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key_name"] = key_name
        kwargs["body"] = body
        return self._patch_ap_ikey_endpoint.call_with_http_info(**kwargs)

    def patch_authenticated_user(
        self,
        body: UserUpdate,
    ) -> User:
        """Update user information.

        partially update the specified User. If you want to update phone number, you must request /api/v1/user/phone-verification-code first.
        :type body: UserUpdate
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._patch_authenticated_user_endpoint.call_with_http_info(**kwargs)

    def patch_user(
        self,
        user_id: str,
        body: UserUpdate,
    ) -> User:
        """Update the information of the specified user.

        Update the information of the specified user
        :param user_id: ID of the user
        :type user_id: str
        :type body: UserUpdate
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_id"] = user_id
        kwargs["body"] = body
        return self._patch_user_endpoint.call_with_http_info(**kwargs)

    def read_user_apikeys(
        self,
    ) -> ApikeyList:
        """Get apikeys of the authenticated user.

        Get apikeys of the authenticated user
        :rtype: ApikeyList
        """
        kwargs: Dict[str, Any] = {}
        return self._read_user_apikeys_endpoint.call_with_http_info(**kwargs)

    def update_authenticated_user_password(
        self,
        body: Dict[str, Any],
    ) -> APIErrorResponse:
        """Update current authenticated user password.

        Update current authenticated user password.
        :type body: Dict[str, Any]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._update_authenticated_user_password_endpoint.call_with_http_info(**kwargs)

    def update_user_password(
        self,
        user_id: str,
        body: Password,
    ) -> APIErrorResponse:
        """Update user password.

        Update user password
        :param user_id: ID of the user
        :type user_id: str
        :type body: Password
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_id"] = user_id
        kwargs["body"] = body
        return self._update_user_password_endpoint.call_with_http_info(**kwargs)
