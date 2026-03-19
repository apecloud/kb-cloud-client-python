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
        self._create_user_apikey_endpoint = _Endpoint(
            settings={
                "response_type": ApikeyWithSK,
                "endpoint_path": "/api/v1/user/apikeys",
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
                "endpoint_path": "/api/v1/user/apikey/{keyName}",
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
        self._get_authenticated_user_endpoint = _Endpoint(
            settings={
                "response_type": User,
                "endpoint_path": "/api/v1/user",
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
        self._patch_ap_ikey_endpoint = _Endpoint(
            settings={
                "response_type": Apikey,
                "endpoint_path": "/api/v1/user/apikey/{keyName}",
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
                "endpoint_path": "/api/v1/user",
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
        self._phone_verification_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/user/phone-verification-code",
                "http_method": "POST",
                "operation_id": "phone_verification",
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
        self._read_user_apikeys_endpoint = _Endpoint(
            settings={
                "response_type": ApikeyList,
                "endpoint_path": "/api/v1/user/apikeys",
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
                "endpoint_path": "/api/v1/user/password",
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

    def get_authenticated_user(
        self,
    ) -> User:
        """Get authenticated user.

        Get authenticated login user info
        :rtype: User
        """
        kwargs: Dict[str, Any] = {}
        return self._get_authenticated_user_endpoint.call_with_http_info(**kwargs)

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

    def phone_verification(
        self,
        body: Dict[str, Any],
    ) -> APIErrorResponse:
        """Send verification code to user's phone.

        to update user phone number, send verification code first
        :type body: Dict[str, Any]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._phone_verification_endpoint.call_with_http_info(**kwargs)

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
