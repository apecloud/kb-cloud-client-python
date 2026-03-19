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


class OrganizationApi:
    """Organization API client.

    Provides methods for the organization endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_org_endpoint = _Endpoint(
            settings={
                "response_type": Org,
                "endpoint_path": "/admin/v1/organizations",
                "http_method": "POST",
                "operation_id": "create_org",
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
        self._delete_org_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}",
                "http_method": "DELETE",
                "operation_id": "delete_org",
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
        self._disable_org_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/disable",
                "http_method": "POST",
                "operation_id": "disable_org",
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
        self._enable_org_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/enable",
                "http_method": "POST",
                "operation_id": "enable_org",
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
        self._freeze_member_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members/{memberId}/freeze",
                "http_method": "POST",
                "operation_id": "freeze_member",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "member_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "memberId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_organizations_endpoint = _Endpoint(
            settings={
                "response_type": OrganizationList,
                "endpoint_path": "/admin/v1/organizations",
                "http_method": "GET",
                "operation_id": "list_organizations",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_org_endpoint = _Endpoint(
            settings={
                "response_type": Org,
                "endpoint_path": "/admin/v1/organizations/{orgName}",
                "http_method": "PATCH",
                "operation_id": "patch_org",
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
        self._read_org_endpoint = _Endpoint(
            settings={
                "response_type": Org,
                "endpoint_path": "/admin/v1/organizations/{orgName}",
                "http_method": "GET",
                "operation_id": "read_org",
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
        self._unfreeze_member_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members/{memberId}/unfreeze",
                "http_method": "POST",
                "operation_id": "unfreeze_member",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "member_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "memberId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def create_org(
        self,
        body: OrgCreate,
    ) -> Org:
        """Create organization.

        Create a new organization
        :type body: OrgCreate
        :rtype: Org
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_org_endpoint.call_with_http_info(**kwargs)

    def delete_org(
        self,
        org_name: str,
    ) -> APIErrorResponse:
        """Delete organization.

        partially delete the specified org
        :param org_name: name of the Org
        :type org_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._delete_org_endpoint.call_with_http_info(**kwargs)

    def disable_org(
        self,
        org_name: str,
    ) -> APIErrorResponse:
        """disable the organization.

        disable the organization
        :param org_name: name of the Org
        :type org_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._disable_org_endpoint.call_with_http_info(**kwargs)

    def enable_org(
        self,
        org_name: str,
    ) -> APIErrorResponse:
        """enable the organization.

        enable the organization
        :param org_name: name of the Org
        :type org_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._enable_org_endpoint.call_with_http_info(**kwargs)

    def freeze_member(
        self,
        org_name: str,
        member_id: str,
    ) -> APIErrorResponse:
        """freeze the member in org.

        freeze the member in org
        :param org_name: name of the Org
        :type org_name: str
        :param member_id: ID of the member
        :type member_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["member_id"] = member_id
        return self._freeze_member_endpoint.call_with_http_info(**kwargs)

    def list_organizations(
        self,
    ) -> OrganizationList:
        """Get organization list.

        Get organization list
        :rtype: OrganizationList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_organizations_endpoint.call_with_http_info(**kwargs)

    def patch_org(
        self,
        org_name: str,
        body: OrgUpdate,
    ) -> Org:
        """Update organization.

        partially update the specified Org
        :param org_name: name of the Org
        :type org_name: str
        :type body: OrgUpdate
        :rtype: Org
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._patch_org_endpoint.call_with_http_info(**kwargs)

    def read_org(
        self,
        org_name: str,
    ) -> Org:
        """Get organization.

        read the specified Org
        :param org_name: name of the Org
        :type org_name: str
        :rtype: Org
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._read_org_endpoint.call_with_http_info(**kwargs)

    def unfreeze_member(
        self,
        org_name: str,
        member_id: str,
    ) -> APIErrorResponse:
        """unfreeze the member in org.

        unfreeze the member in org
        :param org_name: name of the Org
        :type org_name: str
        :param member_id: ID of the member
        :type member_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["member_id"] = member_id
        return self._unfreeze_member_endpoint.call_with_http_info(**kwargs)
