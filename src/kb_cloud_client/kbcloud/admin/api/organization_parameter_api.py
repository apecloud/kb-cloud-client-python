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


class OrganizationparameterApi:
    """OrganizationParameter API client.

    Provides methods for the organizationParameter endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._batch_update_org_parameters_endpoint = _Endpoint(
            settings={
                "response_type": List[OrgParameter],
                "endpoint_path": "/admin/v1/organizations/{orgName}/parameters",
                "http_method": "POST",
                "operation_id": "batch_update_org_parameters",
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
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_org_parameter_endpoint = _Endpoint(
            settings={
                "response_type": OrgParameter,
                "endpoint_path": "/admin/v1/organizations/{orgName}/parameters/{parameterName}",
                "http_method": "GET",
                "operation_id": "get_org_parameter",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "parameter_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "parameterName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_org_parameters_endpoint = _Endpoint(
            settings={
                "response_type": List[OrgParameter],
                "endpoint_path": "/admin/v1/organizations/{orgName}/parameters",
                "http_method": "GET",
                "operation_id": "list_org_parameters",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "category": {
                    "location": "query",
                    "attribute": "category",
                },
                "name": {
                    "location": "query",
                    "attribute": "name",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_org_parameter_endpoint = _Endpoint(
            settings={
                "response_type": OrgParameter,
                "endpoint_path": "/admin/v1/organizations/{orgName}/parameters/{parameterName}",
                "http_method": "PATCH",
                "operation_id": "patch_org_parameter",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "parameter_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "parameterName",
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


    def batch_update_org_parameters(
        self,
        org_name: str,
        body: List[OrgParameter],
    ) -> List[OrgParameter]:
        """Batch update parameters of an organization.

        Batch update parameters of an organization
        :param org_name: The name of the organization
        :type org_name: str
        :type body: List[OrgParameter]
        :rtype: List[OrgParameter]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._batch_update_org_parameters_endpoint.call_with_http_info(**kwargs)

    def get_org_parameter(
        self,
        org_name: str,
        parameter_name: str,
    ) -> OrgParameter:
        """Get a parameter of an organization.
        :param org_name: The name of the organization
        :type org_name: str
        :param parameter_name: The name of the parameter
        :type parameter_name: str
        :rtype: OrgParameter
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["parameter_name"] = parameter_name
        return self._get_org_parameter_endpoint.call_with_http_info(**kwargs)

    def list_org_parameters(
        self,
        org_name: str,
        *,
        category: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
    ) -> List[OrgParameter]:
        """List parameters of an organization.
        :param org_name: The name of the organization
        :type org_name: str
        :param category: the category of the parameters
        :type category: str, optional
        :param name: the name of the parameter
        :type name: str, optional
        :rtype: List[OrgParameter]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if category is not unset:
            kwargs["category"] = category
        if name is not unset:
            kwargs["name"] = name
        return self._list_org_parameters_endpoint.call_with_http_info(**kwargs)

    def patch_org_parameter(
        self,
        org_name: str,
        parameter_name: str,
        body: OrgParameter,
    ) -> OrgParameter:
        """Update a parameter of an organization.

        Update a parameter of an organization
        :param org_name: The name of the organization
        :type org_name: str
        :param parameter_name: The name of the parameter
        :type parameter_name: str
        :type body: OrgParameter
        :rtype: OrgParameter
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["parameter_name"] = parameter_name
        kwargs["body"] = body
        return self._patch_org_parameter_endpoint.call_with_http_info(**kwargs)
