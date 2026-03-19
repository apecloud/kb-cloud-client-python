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


class ClustertagApi:
    """ClusterTag API client.

    Provides methods for the clusterTag endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_tag_endpoint = _Endpoint(
            settings={
                "response_type": TagCreate,
                "endpoint_path": "/admin/v1/organizations/{orgName}/tags",
                "http_method": "POST",
                "operation_id": "create_tag",
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
        self._delete_tag_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/tags/{tagId}",
                "http_method": "DELETE",
                "operation_id": "delete_tag",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "tag_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tagId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_tags_endpoint = _Endpoint(
            settings={
                "response_type": List[ClusterTags],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusterTags",
                "http_method": "GET",
                "operation_id": "get_tags",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_ids": {
                    "required": True,
                    "location": "query",
                    "attribute": "clusterIds",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_org_tags_endpoint = _Endpoint(
            settings={
                "response_type": OrgTagsList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/tags",
                "http_method": "GET",
                "operation_id": "list_org_tags",
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
        self._update_tag_endpoint = _Endpoint(
            settings={
                "response_type": Tag,
                "endpoint_path": "/admin/v1/organizations/{orgName}/tags/{tagId}",
                "http_method": "PATCH",
                "operation_id": "update_tag",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "tag_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tagId",
                },
                "tag_update": {
                    "required": True,
                    "location": "query",
                    "attribute": "tagUpdate",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def create_tag(
        self,
        org_name: str,
        body: TagCreate,
    ) -> TagCreate:
        """Create cluster tags.

        create tag
        :type org_name: str
        :type body: TagCreate
        :rtype: TagCreate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_tag_endpoint.call_with_http_info(**kwargs)

    def delete_tag(
        self,
        org_name: str,
        tag_id: str,
    ) -> APIErrorResponse:
        """Delete tag.

        delete cluster tag
        :type org_name: str
        :type tag_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["tag_id"] = tag_id
        return self._delete_tag_endpoint.call_with_http_info(**kwargs)

    def get_tags(
        self,
        org_name: str,
        cluster_ids: str,
    ) -> List[ClusterTags]:
        """Get cluster tags.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_ids: Comma-separated list of cluster IDs
        :type cluster_ids: str
        :rtype: List[ClusterTags]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_ids"] = cluster_ids
        return self._get_tags_endpoint.call_with_http_info(**kwargs)

    def list_org_tags(
        self,
        org_name: str,
    ) -> OrgTagsList:
        """List tags by organization name.

        List tags by organization name.
        :param org_name: name of the Org
        :type org_name: str
        :rtype: OrgTagsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._list_org_tags_endpoint.call_with_http_info(**kwargs)

    def update_tag(
        self,
        org_name: str,
        tag_id: str,
        tag_update: TagUpdate,
    ) -> Tag:
        """updateTag.

        Update cluster tags
        :type org_name: str
        :type tag_id: str
        :type tag_update: TagUpdate
        :rtype: Tag
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["tag_id"] = tag_id
        kwargs["tag_update"] = tag_update
        return self._update_tag_endpoint.call_with_http_info(**kwargs)
