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


class InspectionApi:
    """Inspection API client.

    Provides methods for the inspection endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_auto_inspection_endpoint = _Endpoint(
            settings={
                "response_type": AutoInspection,
                "endpoint_path": "/admin/v1/autoInspections",
                "http_method": "POST",
                "operation_id": "create_auto_inspection",
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
        self._create_inspection_script_endpoint = _Endpoint(
            settings={
                "response_type": InspectionScript,
                "endpoint_path": "/admin/v1/inspectionScripts",
                "http_method": "POST",
                "operation_id": "create_inspection_script",
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
        self._create_inspection_task_by_env_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/inspectionTasksByEnv",
                "http_method": "POST",
                "operation_id": "create_inspection_task_by_env",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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
        self._create_inspection_task_by_org_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/inspectionTasksByOrg",
                "http_method": "POST",
                "operation_id": "create_inspection_task_by_org",
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
        self._delete_auto_inspection_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/autoInspections/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_auto_inspection",
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
        self._delete_inspection_script_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/inspectionScripts/{scriptId}",
                "http_method": "DELETE",
                "operation_id": "delete_inspection_script",
            },
            params_map={
                "script_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "scriptId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_aggregate_task_result_endpoint = _Endpoint(
            settings={
                "response_type": AggregateTaskResultList,
                "endpoint_path": "/admin/v1/inspectionTasks/aggregate",
                "http_method": "GET",
                "operation_id": "get_aggregate_task_result",
            },
            params_map={
                "aggregate_type": {
                    "required": True,
                    "location": "query",
                    "attribute": "aggregateType",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
                "engine": {
                    "location": "query",
                    "attribute": "engine",
                },
                "resource_name": {
                    "location": "query",
                    "attribute": "resourceName",
                },
                "result_type": {
                    "location": "query",
                    "attribute": "resultType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_auto_inspection_endpoint = _Endpoint(
            settings={
                "response_type": AutoInspection,
                "endpoint_path": "/admin/v1/autoInspections",
                "http_method": "GET",
                "operation_id": "get_auto_inspection",
            },
            params_map={
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "env_name": {
                    "location": "query",
                    "attribute": "envName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_inspection_task_by_env_endpoint = _Endpoint(
            settings={
                "response_type": List[InspectionTaskItem],
                "endpoint_path": "/admin/v1/environments/{environmentName}/inspectionTasksByEnv/{taskId}",
                "http_method": "GET",
                "operation_id": "get_inspection_task_by_env",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "task_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "taskId",
                },
                "format_": {
                    "location": "query",
                    "attribute": "format",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_inspection_task_by_org_endpoint = _Endpoint(
            settings={
                "response_type": InspectionTask,
                "endpoint_path": "/admin/v1/organizations/{orgName}/inspectionTasksByOrg/{taskId}",
                "http_method": "GET",
                "operation_id": "get_inspection_task_by_org",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "task_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "taskId",
                },
                "format_": {
                    "location": "query",
                    "attribute": "format",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_inspection_scripts_endpoint = _Endpoint(
            settings={
                "response_type": List[InspectionScript],
                "endpoint_path": "/admin/v1/inspectionScripts",
                "http_method": "GET",
                "operation_id": "list_inspection_scripts",
            },
            params_map={
                "org_names": {
                    "location": "query",
                    "attribute": "orgNames",
                },
                "engines": {
                    "location": "query",
                    "attribute": "engines",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_inspection_tasks_by_env_endpoint = _Endpoint(
            settings={
                "response_type": List[InspectionTask],
                "endpoint_path": "/admin/v1/environments/{environmentName}/inspectionTasksByEnv",
                "http_method": "GET",
                "operation_id": "list_inspection_tasks_by_env",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
                "node_name": {
                    "location": "query",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_inspection_tasks_by_org_endpoint = _Endpoint(
            settings={
                "response_type": List[InspectionTask],
                "endpoint_path": "/admin/v1/organizations/{orgName}/inspectionTasksByOrg",
                "http_method": "GET",
                "operation_id": "list_inspection_tasks_by_org",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "start": {
                    "required": True,
                    "location": "query",
                    "attribute": "start",
                },
                "end": {
                    "required": True,
                    "location": "query",
                    "attribute": "end",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_auto_inspection_endpoint = _Endpoint(
            settings={
                "response_type": AutoInspection,
                "endpoint_path": "/admin/v1/autoInspections/{id}",
                "http_method": "PATCH",
                "operation_id": "update_auto_inspection",
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
        self._update_inspection_script_endpoint = _Endpoint(
            settings={
                "response_type": InspectionScript,
                "endpoint_path": "/admin/v1/inspectionScripts/{scriptId}",
                "http_method": "PATCH",
                "operation_id": "update_inspection_script",
            },
            params_map={
                "script_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "scriptId",
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


    def create_auto_inspection(
        self,
        body: AutoInspection,
    ) -> AutoInspection:
        """Create inspection cron job.
        :type body: AutoInspection
        :rtype: AutoInspection
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_auto_inspection_endpoint.call_with_http_info(**kwargs)

    def create_inspection_script(
        self,
        body: InspectionScript,
    ) -> InspectionScript:
        """Create inspection script.
        :type body: InspectionScript
        :rtype: InspectionScript
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_inspection_script_endpoint.call_with_http_info(**kwargs)

    def create_inspection_task_by_env(
        self,
        environment_name: str,
        body: InspectionTask,
    ) -> APIErrorResponse:
        """create inspection task by env.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: InspectionTask
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_inspection_task_by_env_endpoint.call_with_http_info(**kwargs)

    def create_inspection_task_by_org(
        self,
        org_name: str,
        body: InspectionTask,
    ) -> APIErrorResponse:
        """create inspection task by org.
        :param org_name: name of the Org
        :type org_name: str
        :type body: InspectionTask
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_inspection_task_by_org_endpoint.call_with_http_info(**kwargs)

    def delete_auto_inspection(
        self,
        id_: int,
    ) -> APIErrorResponse:
        """delete auto inspection.
        :param id_: id of the auto inspection
        :type id_: int
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        return self._delete_auto_inspection_endpoint.call_with_http_info(**kwargs)

    def delete_inspection_script(
        self,
        script_id: int,
    ) -> APIErrorResponse:
        """Delete inspection script.
        :param script_id: id of the inspection script
        :type script_id: int
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["script_id"] = script_id
        return self._delete_inspection_script_endpoint.call_with_http_info(**kwargs)

    def get_aggregate_task_result(
        self,
        aggregate_type: AggregateTaskType,
        start: int,
        end: int,
        *,
        engine: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        result_type: Union[AggregateTaskResultType, UnsetType] = unset,
    ) -> AggregateTaskResultList:
        """get aggregate task result.
        :param aggregate_type: the type of the aggregate task
        :type aggregate_type: AggregateTaskType
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param engine: the engine of the task
        :type engine: str, optional
        :param resource_name: only show the result of the specific organization or environment
        :type resource_name: str, optional
        :param result_type: result of the task
        :type result_type: AggregateTaskResultType, optional
        :rtype: AggregateTaskResultList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aggregate_type"] = aggregate_type
        kwargs["start"] = start
        kwargs["end"] = end
        if engine is not unset:
            kwargs["engine"] = engine
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if result_type is not unset:
            kwargs["result_type"] = result_type
        return self._get_aggregate_task_result_endpoint.call_with_http_info(**kwargs)

    def get_auto_inspection(
        self,
        *,
        org_name: Union[str, UnsetType] = unset,
        env_name: Union[str, UnsetType] = unset,
    ) -> AutoInspection:
        """get auto inspection.
        :param org_name: name of the Org
        :type org_name: str, optional
        :param env_name: name of the environment
        :type env_name: str, optional
        :rtype: AutoInspection
        """
        kwargs: Dict[str, Any] = {}
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if env_name is not unset:
            kwargs["env_name"] = env_name
        return self._get_auto_inspection_endpoint.call_with_http_info(**kwargs)

    def get_inspection_task_by_env(
        self,
        environment_name: str,
        task_id: str,
        *,
        format_: Union[InspectionTaskFormat, UnsetType] = unset,
    ) -> List[InspectionTaskItem]:
        """get inspection task by env.
        :param environment_name: name of the environment
        :type environment_name: str
        :param task_id: list task details if specified
        :type task_id: str
        :param format_: the format of the task
        :type format_: InspectionTaskFormat, optional
        :rtype: List[InspectionTaskItem]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["task_id"] = task_id
        if format_ is not unset:
            kwargs["format_"] = format_
        return self._get_inspection_task_by_env_endpoint.call_with_http_info(**kwargs)

    def get_inspection_task_by_org(
        self,
        org_name: str,
        task_id: str,
        *,
        format_: Union[InspectionTaskFormat, UnsetType] = unset,
    ) -> InspectionTask:
        """get inspection task by org.
        :param org_name: name of the Org
        :type org_name: str
        :param task_id: list task details if specified
        :type task_id: str
        :param format_: the format of the task
        :type format_: InspectionTaskFormat, optional
        :rtype: InspectionTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["task_id"] = task_id
        if format_ is not unset:
            kwargs["format_"] = format_
        return self._get_inspection_task_by_org_endpoint.call_with_http_info(**kwargs)

    def list_inspection_scripts(
        self,
        *,
        org_names: Union[str, UnsetType] = unset,
        engines: Union[str, UnsetType] = unset,
    ) -> List[InspectionScript]:
        """list inspection scripts.
        :param org_names: name of the Org, multiple orgs separated by ',', if not provided, return all scripts
        :type org_names: str, optional
        :param engines: query by, such as "node"/"mysql", multiple engines separated by ','
        :type engines: str, optional
        :rtype: List[InspectionScript]
        """
        kwargs: Dict[str, Any] = {}
        if org_names is not unset:
            kwargs["org_names"] = org_names
        if engines is not unset:
            kwargs["engines"] = engines
        return self._list_inspection_scripts_endpoint.call_with_http_info(**kwargs)

    def list_inspection_tasks_by_env(
        self,
        environment_name: str,
        start: int,
        end: int,
        *,
        node_name: Union[str, UnsetType] = unset,
    ) -> List[InspectionTask]:
        """list inspection tasks by env.
        :param environment_name: name of the environment
        :type environment_name: str
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param node_name: list tasks for the specified node
        :type node_name: str, optional
        :rtype: List[InspectionTask]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["start"] = start
        kwargs["end"] = end
        if node_name is not unset:
            kwargs["node_name"] = node_name
        return self._list_inspection_tasks_by_env_endpoint.call_with_http_info(**kwargs)

    def list_inspection_tasks_by_org(
        self,
        org_name: str,
        start: int,
        end: int,
        *,
        cluster_id: Union[str, UnsetType] = unset,
    ) -> List[InspectionTask]:
        """list inspection tasks by org.
        :param org_name: name of the Org
        :type org_name: str
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param cluster_id: list tasks for the specified cluster
        :type cluster_id: str, optional
        :rtype: List[InspectionTask]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["start"] = start
        kwargs["end"] = end
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        return self._list_inspection_tasks_by_org_endpoint.call_with_http_info(**kwargs)

    def update_auto_inspection(
        self,
        id_: int,
        body: AutoInspection,
    ) -> AutoInspection:
        """update auto inspection.
        :param id_: id of the auto inspection
        :type id_: int
        :type body: AutoInspection
        :rtype: AutoInspection
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._update_auto_inspection_endpoint.call_with_http_info(**kwargs)

    def update_inspection_script(
        self,
        script_id: int,
        body: InspectionScript,
    ) -> InspectionScript:
        """Update inspection script.
        :param script_id: id of the inspection script
        :type script_id: int
        :type body: InspectionScript
        :rtype: InspectionScript
        """
        kwargs: Dict[str, Any] = {}
        kwargs["script_id"] = script_id
        kwargs["body"] = body
        return self._update_inspection_script_endpoint.call_with_http_info(**kwargs)
