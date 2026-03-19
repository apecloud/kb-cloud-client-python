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


class OrganizationresourcequotaApi:
    """OrganizationResourceQuota API client.

    Provides methods for the organizationResourceQuota endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._resource_quota_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/resourceQuota",
                "http_method": "POST",
                "operation_id": "resource_quota",
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
        self._resource_quota_and_usage_endpoint = _Endpoint(
            settings={
                "response_type": OrgResourceQuotaAndUsage,
                "endpoint_path": "/admin/v1/organizations/{orgName}/resourceQuota",
                "http_method": "GET",
                "operation_id": "resource_quota_and_usage",
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


    def resource_quota(
        self,
        org_name: str,
        body: OrgResourceQuota,
    ) -> APIErrorResponse:
        """Update the resource quota of an organization.

        Update the resource quota of an organization
        :param org_name: The name of the organization
        :type org_name: str
        :type body: OrgResourceQuota
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._resource_quota_endpoint.call_with_http_info(**kwargs)

    def resource_quota_and_usage(
        self,
        org_name: str,
    ) -> OrgResourceQuotaAndUsage:
        """Get the resource quota and usage of an organization.
        :param org_name: The name of the organization
        :type org_name: str
        :rtype: OrgResourceQuotaAndUsage
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._resource_quota_and_usage_endpoint.call_with_http_info(**kwargs)
