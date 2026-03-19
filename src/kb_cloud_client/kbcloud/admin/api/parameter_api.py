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


class ParameterApi:
    """Parameter API client.

    Provides methods for the parameter endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_parameter_props_endpoint = _Endpoint(
            settings={
                "response_type": ParameterList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameters",
                "http_method": "GET",
                "operation_id": "list_parameter_props",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
                "raw_content": {
                    "location": "query",
                    "attribute": "rawContent",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_parameters_history_endpoint = _Endpoint(
            settings={
                "response_type": ParameterHistoryList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterHistories",
                "http_method": "GET",
                "operation_id": "list_parameters_history",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "component": {
                    "required": True,
                    "location": "query",
                    "attribute": "component",
                },
                "parameter_name": {
                    "location": "query",
                    "attribute": "parameterName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def list_parameter_props(
        self,
        org_name: str,
        cluster_name: str,
        *,
        component: Union[str, UnsetType] = unset,
        raw_content: Union[bool, UnsetType] = unset,
    ) -> ParameterList:
        """List parameter properties of the cluster.
        :param org_name: name of the organization
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param component: component type
        :type component: str, optional
        :param raw_content: whether to return the raw template content
        :type raw_content: bool, optional
        :rtype: ParameterList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if component is not unset:
            kwargs["component"] = component
        if raw_content is not unset:
            kwargs["raw_content"] = raw_content
        return self._list_parameter_props_endpoint.call_with_http_info(**kwargs)

    def list_parameters_history(
        self,
        org_name: str,
        cluster_name: str,
        component: str,
        *,
        parameter_name: Union[str, UnsetType] = unset,
    ) -> ParameterHistoryList:
        """List parameters history of the cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param component: component type
        :type component: str
        :param parameter_name: name of the parameter
        :type parameter_name: str, optional
        :rtype: ParameterHistoryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["component"] = component
        if parameter_name is not unset:
            kwargs["parameter_name"] = parameter_name
        return self._list_parameters_history_endpoint.call_with_http_info(**kwargs)
