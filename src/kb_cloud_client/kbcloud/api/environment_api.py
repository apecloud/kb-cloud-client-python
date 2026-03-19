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


class EnvironmentApi:
    """Environment API client.

    Provides methods for the environment endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_environment_endpoint = _Endpoint(
            settings={
                "response_type": Environment,
                "endpoint_path": "/api/v1/organizations/{orgName}/environments/{environmentName}",
                "http_method": "GET",
                "operation_id": "get_environment",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_environment_module_info_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentModuleInfo,
                "endpoint_path": "/api/v1/environments/{environmentName}/modules",
                "http_method": "GET",
                "operation_id": "get_environment_module_info",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_env_node_zone_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/api/v1/organizations/{orgName}/environments/{environmentName}/availableZones",
                "http_method": "GET",
                "operation_id": "list_env_node_zone",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_environment_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentList,
                "endpoint_path": "/api/v1/organizations/{orgName}/environments",
                "http_method": "GET",
                "operation_id": "list_environment",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "engine": {
                    "location": "query",
                    "attribute": "engine",
                },
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_node_group_endpoint = _Endpoint(
            settings={
                "response_type": List[NodeGroup],
                "endpoint_path": "/api/v1/environments/{environmentName}/nodeGroups",
                "http_method": "GET",
                "operation_id": "list_node_group",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "zones": {
                    "location": "query",
                    "attribute": "zones",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_environment(
        self,
        org_name: str,
        environment_name: str,
    ) -> Environment:
        """Get environment.
        :param org_name: name of the Org
        :type org_name: str
        :param environment_name: name of the Environment
        :type environment_name: str
        :rtype: Environment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["environment_name"] = environment_name
        return self._get_environment_endpoint.call_with_http_info(**kwargs)

    def get_environment_module_info(
        self,
        environment_name: str,
    ) -> EnvironmentModuleInfo:
        """Get environment module information in an environment.
        :param environment_name: Environment Name
        :type environment_name: str
        :rtype: EnvironmentModuleInfo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_module_info_endpoint.call_with_http_info(**kwargs)

    def list_env_node_zone(
        self,
        org_name: str,
        environment_name: str,
    ) -> List[str]:
        """List the availability zones where the environment's nodes are located.

        List available zones of an environment
        :param org_name: name of the Org
        :type org_name: str
        :param environment_name: name of the Environment
        :type environment_name: str
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["environment_name"] = environment_name
        return self._list_env_node_zone_endpoint.call_with_http_info(**kwargs)

    def list_environment(
        self,
        org_name: str,
        *,
        engine: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
    ) -> EnvironmentList:
        """List environments.

        List environments
        :param org_name: name of the Org
        :type org_name: str
        :param engine: engine name
        :type engine: str, optional
        :param version: version of the engine
        :type version: str, optional
        :rtype: EnvironmentList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if engine is not unset:
            kwargs["engine"] = engine
        if version is not unset:
            kwargs["version"] = version
        return self._list_environment_endpoint.call_with_http_info(**kwargs)

    def list_node_group(
        self,
        environment_name: str,
        *,
        zones: Union[List[str], UnsetType] = unset,
    ) -> List[NodeGroup]:
        """List environment node group.
        :param environment_name: name of the environment
        :type environment_name: str
        :param zones: available zone for filtering node groups
        :type zones: List[str], optional
        :rtype: List[NodeGroup]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if zones is not unset:
            kwargs["zones"] = zones
        return self._list_node_group_endpoint.call_with_http_info(**kwargs)
