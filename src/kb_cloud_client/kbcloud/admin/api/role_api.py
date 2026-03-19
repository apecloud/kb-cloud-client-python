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


class RoleApi:
    """Role API client.

    Provides methods for the role endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._batch_add_role_permissions_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}/permissions/batch",
                "http_method": "POST",
                "operation_id": "batch_add_role_permissions",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._batch_remove_role_permissions_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}/permissions/batch",
                "http_method": "DELETE",
                "operation_id": "batch_remove_role_permissions",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
                },
                "body": {
                    "required": True,
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._create_role_endpoint = _Endpoint(
            settings={
                "response_type": Role,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles",
                "http_method": "POST",
                "operation_id": "create_role",
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
        self._delete_role_by_name_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}",
                "http_method": "DELETE",
                "operation_id": "delete_role_by_name",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_role_by_name_endpoint = _Endpoint(
            settings={
                "response_type": Role,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}",
                "http_method": "GET",
                "operation_id": "get_role_by_name",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_permissions_endpoint = _Endpoint(
            settings={
                "response_type": PermissionList,
                "endpoint_path": "/admin/v1/permissions",
                "http_method": "GET",
                "operation_id": "list_permissions",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_role_permissions_endpoint = _Endpoint(
            settings={
                "response_type": PermissionList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}/permissions",
                "http_method": "GET",
                "operation_id": "list_role_permissions",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_roles_endpoint = _Endpoint(
            settings={
                "response_type": RoleList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles",
                "http_method": "GET",
                "operation_id": "list_roles",
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
        self._update_role_by_name_endpoint = _Endpoint(
            settings={
                "response_type": Role,
                "endpoint_path": "/admin/v1/organizations/{orgName}/roles/{roleName}",
                "http_method": "PATCH",
                "operation_id": "update_role_by_name",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "role_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "roleName",
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


    def batch_add_role_permissions(
        self,
        org_name: str,
        role_name: str,
        body: List[str],
    ) -> APIErrorResponse:
        """Batch add permissions to a role.

        Batch add permissions to a role
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :type body: List[str]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        kwargs["body"] = body
        return self._batch_add_role_permissions_endpoint.call_with_http_info(**kwargs)

    def batch_remove_role_permissions(
        self,
        org_name: str,
        role_name: str,
        body: List[str],
    ) -> APIErrorResponse:
        """Batch remove permissions from a role.

        Batch remove permissions from a role
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :type body: List[str]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        kwargs["body"] = body
        return self._batch_remove_role_permissions_endpoint.call_with_http_info(**kwargs)

    def create_role(
        self,
        org_name: str,
        body: RoleCreate,
    ) -> Role:
        """Create role.

        Create role
        :param org_name: name of the Org
        :type org_name: str
        :type body: RoleCreate
        :rtype: Role
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_role_endpoint.call_with_http_info(**kwargs)

    def delete_role_by_name(
        self,
        org_name: str,
        role_name: str,
    ) -> APIErrorResponse:
        """Delete role by name.

        Delete role by name
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        return self._delete_role_by_name_endpoint.call_with_http_info(**kwargs)

    def get_role_by_name(
        self,
        org_name: str,
        role_name: str,
    ) -> Role:
        """Get role by name.

        Get role by name
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :rtype: Role
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        return self._get_role_by_name_endpoint.call_with_http_info(**kwargs)

    def list_permissions(
        self,
    ) -> PermissionList:
        """List all permissions.

        List all permissions
        :rtype: PermissionList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_permissions_endpoint.call_with_http_info(**kwargs)

    def list_role_permissions(
        self,
        org_name: str,
        role_name: str,
    ) -> PermissionList:
        """List permissions of a role.

        List permissions of a role
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :rtype: PermissionList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        return self._list_role_permissions_endpoint.call_with_http_info(**kwargs)

    def list_roles(
        self,
        org_name: str,
    ) -> RoleList:
        """List roles of a organization.

        List roles of a organization
        :param org_name: name of the Org
        :type org_name: str
        :rtype: RoleList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_roles_endpoint.call_with_http_info(**kwargs)

    def update_role_by_name(
        self,
        org_name: str,
        role_name: str,
        body: RoleUpdate,
    ) -> Role:
        """Update role by name.

        Update role by name
        :param org_name: name of the Org
        :type org_name: str
        :type role_name: str
        :type body: RoleUpdate
        :rtype: Role
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["role_name"] = role_name
        kwargs["body"] = body
        return self._update_role_by_name_endpoint.call_with_http_info(**kwargs)
