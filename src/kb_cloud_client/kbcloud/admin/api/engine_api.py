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


class EngineApi:
    """Engine API client.

    Provides methods for the engine endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_service_version_endpoint = _Endpoint(
            settings={
                "response_type": EngineServiceVersions,
                "endpoint_path": "/admin/v1/environments/{environmentName}/engines/{engineName}/serviceVersion",
                "http_method": "GET",
                "operation_id": "list_service_version",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
                "engine_mode": {
                    "required": True,
                    "location": "query",
                    "attribute": "engineMode",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_upgradeable_service_version_endpoint = _Endpoint(
            settings={
                "response_type": EngineServiceVersions,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/upgradeableServiceVersion",
                "http_method": "GET",
                "operation_id": "list_upgradeable_service_version",
            },
            params_map={
                "cluster_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterName",
                },
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "component": {
                    "required": True,
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._create_engine_resource_constraint_endpoint = _Endpoint(
            settings={
                "response_type": ResourceConstraint,
                "endpoint_path": "/admin/v1/engines/resourceConstraints",
                "http_method": "POST",
                "operation_id": "create_engine_resource_constraint",
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
        self._create_engine_version_endpoint = _Endpoint(
            settings={
                "response_type": EngineVersion,
                "endpoint_path": "/admin/v1/engineVersions",
                "http_method": "POST",
                "operation_id": "create_engine_version",
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
        self._delete_engine_resource_constraint_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/engines/resourceConstraints/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_engine_resource_constraint",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_engine_version_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/engineVersions",
                "http_method": "DELETE",
                "operation_id": "delete_engine_version",
            },
            params_map={
                "body": {
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._engine_action_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/environments/{environmentName}/engines/{engineName}",
                "http_method": "POST",
                "operation_id": "engine_action",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
                "action_info": {
                    "required": True,
                    "location": "query",
                    "attribute": "actionInfo",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_engine_by_name_in_env_endpoint = _Endpoint(
            settings={
                "response_type": Engine,
                "endpoint_path": "/admin/v1/environments/{environmentName}/engines/{engineName}",
                "http_method": "GET",
                "operation_id": "get_engine_by_name_in_env",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
                "version": {
                    "required": True,
                    "location": "query",
                    "attribute": "version",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_all_engines_endpoint = _Endpoint(
            settings={
                "response_type": List[Engine],
                "endpoint_path": "/admin/v1/engines",
                "http_method": "GET",
                "operation_id": "list_all_engines",
            },
            params_map={
                "name": {
                    "location": "query",
                    "attribute": "name",
                },
                "type_": {
                    "location": "query",
                    "attribute": "type",
                },
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
                "provider": {
                    "location": "query",
                    "attribute": "provider",
                },
                "all": {
                    "location": "query",
                    "attribute": "all",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_resource_constraints_endpoint = _Endpoint(
            settings={
                "response_type": ResourceConstraintList,
                "endpoint_path": "/admin/v1/engines/resourceConstraints",
                "http_method": "GET",
                "operation_id": "list_engine_resource_constraints",
            },
            params_map={
                "engine": {
                    "location": "query",
                    "attribute": "engine",
                },
                "mode": {
                    "location": "query",
                    "attribute": "mode",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_versions_endpoint = _Endpoint(
            settings={
                "response_type": EngineVersionList,
                "endpoint_path": "/admin/v1/engineVersions/{engineName}",
                "http_method": "GET",
                "operation_id": "list_engine_versions",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engines_in_env_endpoint = _Endpoint(
            settings={
                "response_type": List[Engine],
                "endpoint_path": "/admin/v1/environments/{environmentName}/engines",
                "http_method": "GET",
                "operation_id": "list_engines_in_env",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "name": {
                    "location": "query",
                    "attribute": "name",
                },
                "type_": {
                    "location": "query",
                    "attribute": "type",
                },
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
                "provider": {
                    "location": "query",
                    "attribute": "provider",
                },
                "all": {
                    "location": "query",
                    "attribute": "all",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_engine_version_endpoint = _Endpoint(
            settings={
                "response_type": EngineVersion,
                "endpoint_path": "/admin/v1/engineVersions",
                "http_method": "PATCH",
                "operation_id": "patch_engine_version",
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
        self._update_engine_resource_constraint_endpoint = _Endpoint(
            settings={
                "response_type": ResourceConstraint,
                "endpoint_path": "/admin/v1/engines/resourceConstraints/{id}",
                "http_method": "PATCH",
                "operation_id": "update_engine_resource_constraint",
            },
            params_map={
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
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


    def list_service_version(
        self,
        environment_name: str,
        engine_name: str,
        engine_mode: str,
        *,
        component: Union[str, UnsetType] = unset,
    ) -> EngineServiceVersions:
        """list the service version of the engine.

        list the service version of the engine
        :param environment_name: environment name
        :type environment_name: str
        :param engine_name: Name of the engine
        :type engine_name: str
        :param engine_mode: engine mode
        :type engine_mode: str
        :param component: component type, refer to componentDef and support NamePrefix
        :type component: str, optional
        :rtype: EngineServiceVersions
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["engine_name"] = engine_name
        kwargs["engine_mode"] = engine_mode
        if component is not unset:
            kwargs["component"] = component
        return self._list_service_version_endpoint.call_with_http_info(**kwargs)

    def list_upgradeable_service_version(
        self,
        cluster_name: str,
        org_name: str,
        component: str,
    ) -> EngineServiceVersions:
        """list upgraded service version of the component.

        list upgraded service version of the component
        :param cluster_name: Name of the cluster
        :type cluster_name: str
        :param org_name: organization name
        :type org_name: str
        :param component: component type
        :type component: str
        :rtype: EngineServiceVersions
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cluster_name"] = cluster_name
        kwargs["org_name"] = org_name
        kwargs["component"] = component
        return self._list_upgradeable_service_version_endpoint.call_with_http_info(**kwargs)

    def create_engine_resource_constraint(
        self,
        body: ResourceConstraintCreate,
    ) -> ResourceConstraint:
        """Create engine resource constraint.
        :param body: Request body for engine resource constraint
        :type body: ResourceConstraintCreate
        :rtype: ResourceConstraint
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_engine_resource_constraint_endpoint.call_with_http_info(**kwargs)

    def create_engine_version(
        self,
        body: EngineVersionCreate,
    ) -> EngineVersion:
        """Create engine version.

        Create engine version
        :type body: EngineVersionCreate
        :rtype: EngineVersion
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_engine_version_endpoint.call_with_http_info(**kwargs)

    def delete_engine_resource_constraint(
        self,
        id_: str,
    ) -> APIErrorResponse:
        """Delete engine resource constraint.
        :param id_: id of the engine resource constraint
        :type id_: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        return self._delete_engine_resource_constraint_endpoint.call_with_http_info(**kwargs)

    def delete_engine_version(
        self,
        *,
        body: Union[EngineVersionDelete, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Delete engine version.
        :type body: EngineVersionDelete, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._delete_engine_version_endpoint.call_with_http_info(**kwargs)

    def engine_action(
        self,
        environment_name: str,
        engine_name: str,
        action_info: Dict[str, Any],
    ) -> str:
        """Manage engine in environment.
        :param environment_name: name of the EnvironmentName
        :type environment_name: str
        :param engine_name: name of the engine
        :type engine_name: str
        :param action_info: Request body for engine operations
        :type action_info: Dict[str, Any]
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["engine_name"] = engine_name
        kwargs["action_info"] = action_info
        return self._engine_action_endpoint.call_with_http_info(**kwargs)

    def get_engine_by_name_in_env(
        self,
        environment_name: str,
        engine_name: str,
        version: str,
    ) -> Engine:
        """Get engine in environment.
        :param environment_name: name of the EnvironmentName
        :type environment_name: str
        :param engine_name: name of the engine
        :type engine_name: str
        :param version: engine version
        :type version: str
        :rtype: Engine
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["engine_name"] = engine_name
        kwargs["version"] = version
        return self._get_engine_by_name_in_env_endpoint.call_with_http_info(**kwargs)

    def list_all_engines(
        self,
        *,
        name: Union[str, UnsetType] = unset,
        type_: Union[EngineType, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        all: Union[bool, UnsetType] = unset,
    ) -> List[Engine]:
        """List all engines.
        :param name: engine name
        :type name: str, optional
        :param type_: engine Type
        :type type_: EngineType, optional
        :param version: engine version
        :type version: str, optional
        :param provider: engine provider
        :type provider: str, optional
        :param all: list all engines include uninstall engines
        :type all: bool, optional
        :rtype: List[Engine]
        """
        kwargs: Dict[str, Any] = {}
        if name is not unset:
            kwargs["name"] = name
        if type_ is not unset:
            kwargs["type_"] = type_
        if version is not unset:
            kwargs["version"] = version
        if provider is not unset:
            kwargs["provider"] = provider
        if all is not unset:
            kwargs["all"] = all
        return self._list_all_engines_endpoint.call_with_http_info(**kwargs)

    def list_engine_resource_constraints(
        self,
        *,
        engine: Union[str, UnsetType] = unset,
        mode: Union[str, UnsetType] = unset,
        component: Union[str, UnsetType] = unset,
    ) -> ResourceConstraintList:
        """List engine resource constraints.
        :param engine: engine name
        :type engine: str, optional
        :param mode: engine mode
        :type mode: str, optional
        :param component: engine component
        :type component: str, optional
        :rtype: ResourceConstraintList
        """
        kwargs: Dict[str, Any] = {}
        if engine is not unset:
            kwargs["engine"] = engine
        if mode is not unset:
            kwargs["mode"] = mode
        if component is not unset:
            kwargs["component"] = component
        return self._list_engine_resource_constraints_endpoint.call_with_http_info(**kwargs)

    def list_engine_versions(
        self,
        engine_name: str,
    ) -> EngineVersionList:
        """Get engine version list.

        Get engine version list
        :param engine_name: Name of Engine.
        :type engine_name: str
        :rtype: EngineVersionList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        return self._list_engine_versions_endpoint.call_with_http_info(**kwargs)

    def list_engines_in_env(
        self,
        environment_name: str,
        *,
        name: Union[str, UnsetType] = unset,
        type_: Union[EngineType, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        all: Union[bool, UnsetType] = unset,
    ) -> List[Engine]:
        """List engines in environment.
        :param environment_name: name of the EnvironmentName
        :type environment_name: str
        :param name: engine name
        :type name: str, optional
        :param type_: engine Type
        :type type_: EngineType, optional
        :param version: engine version
        :type version: str, optional
        :param provider: engine provider
        :type provider: str, optional
        :param all: list all engines include uninstall engines
        :type all: bool, optional
        :rtype: List[Engine]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if name is not unset:
            kwargs["name"] = name
        if type_ is not unset:
            kwargs["type_"] = type_
        if version is not unset:
            kwargs["version"] = version
        if provider is not unset:
            kwargs["provider"] = provider
        if all is not unset:
            kwargs["all"] = all
        return self._list_engines_in_env_endpoint.call_with_http_info(**kwargs)

    def patch_engine_version(
        self,
        body: EngineVersionUpdate,
    ) -> EngineVersion:
        """Update the specified engine version.

        Update the specified engine version
        :type body: EngineVersionUpdate
        :rtype: EngineVersion
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._patch_engine_version_endpoint.call_with_http_info(**kwargs)

    def update_engine_resource_constraint(
        self,
        id_: str,
        body: ResourceConstraintUpdate,
    ) -> ResourceConstraint:
        """Update engine resource constraint.
        :param id_: id of the engine resource constraint
        :type id_: str
        :param body: Request body for engine resource constraint update
        :type body: ResourceConstraintUpdate
        :rtype: ResourceConstraint
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._update_engine_resource_constraint_endpoint.call_with_http_info(**kwargs)
