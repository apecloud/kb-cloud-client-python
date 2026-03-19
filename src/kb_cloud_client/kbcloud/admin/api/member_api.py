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


class MemberApi:
    """Member API client.

    Provides methods for the member endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._add_org_member_endpoint = _Endpoint(
            settings={
                "response_type": OrgMember,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members",
                "http_method": "POST",
                "operation_id": "add_org_member",
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
        self._delete_org_member_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members/{memberId}",
                "http_method": "DELETE",
                "operation_id": "delete_org_member",
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
        self._list_org_member_endpoint = _Endpoint(
            settings={
                "response_type": OrgMemberList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members",
                "http_method": "GET",
                "operation_id": "list_org_member",
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
        self._patch_org_member_endpoint = _Endpoint(
            settings={
                "response_type": OrgMember,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members/{memberId}",
                "http_method": "PATCH",
                "operation_id": "patch_org_member",
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
        self._read_org_member_endpoint = _Endpoint(
            settings={
                "response_type": OrgMember,
                "endpoint_path": "/admin/v1/organizations/{orgName}/members/{memberId}",
                "http_method": "GET",
                "operation_id": "read_org_member",
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


    def add_org_member(
        self,
        org_name: str,
        body: OrgMemberAdd,
    ) -> OrgMember:
        """Add member.

        Add organization with specific role
        :param org_name: Name of the Org
        :type org_name: str
        :type body: OrgMemberAdd
        :rtype: OrgMember
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._add_org_member_endpoint.call_with_http_info(**kwargs)

    def delete_org_member(
        self,
        org_name: str,
        member_id: str,
    ) -> APIErrorResponse:
        """Delete member.

        delete a Org Member
        :param org_name: Name of the Org
        :type org_name: str
        :param member_id: ID of the member
        :type member_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["member_id"] = member_id
        return self._delete_org_member_endpoint.call_with_http_info(**kwargs)

    def list_org_member(
        self,
        org_name: str,
    ) -> OrgMemberList:
        """List members.

        list members of the specified Org
        :param org_name: Name of the Org
        :type org_name: str
        :rtype: OrgMemberList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_org_member_endpoint.call_with_http_info(**kwargs)

    def patch_org_member(
        self,
        org_name: str,
        member_id: str,
        body: OrgMemberUpdate,
    ) -> OrgMember:
        """Update member role.

        Only authenticated organization admins can update the member's role
        :param org_name: name of the Org
        :type org_name: str
        :param member_id: ID of the member
        :type member_id: str
        :type body: OrgMemberUpdate
        :rtype: OrgMember
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["member_id"] = member_id
        kwargs["body"] = body
        return self._patch_org_member_endpoint.call_with_http_info(**kwargs)

    def read_org_member(
        self,
        org_name: str,
        member_id: str,
    ) -> OrgMember:
        """Get member.

        read the specified OrgMember
        :param org_name: name of the Org
        :type org_name: str
        :param member_id: ID of the member
        :type member_id: str
        :rtype: OrgMember
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["member_id"] = member_id
        return self._read_org_member_endpoint.call_with_http_info(**kwargs)
