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


class ClustertaskApi:
    """ClusterTask API client.

    Provides methods for the clusterTask endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_cluster_task_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTask,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/clustertasks/{taskId}",
                "http_method": "GET",
                "operation_id": "get_cluster_task",
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
                "task_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "taskId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_cluster_tasks_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTaskList,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/clustertasks",
                "http_method": "GET",
                "operation_id": "list_cluster_tasks",
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
                "status": {
                    "location": "query",
                    "attribute": "status",
                },
                "cluster_task_type": {
                    "location": "query",
                    "attribute": "clusterTaskType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def get_cluster_task(
        self,
        org_name: str,
        cluster_name: str,
        task_id: str,
    ) -> ClusterTask:
        """Get cluster task.

        Get cluster task
        :param org_name: Organization Name
        :type org_name: str
        :param cluster_name: Cluster Name
        :type cluster_name: str
        :param task_id: Task ID
        :type task_id: str
        :rtype: ClusterTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["task_id"] = task_id
        return self._get_cluster_task_endpoint.call_with_http_info(**kwargs)

    def list_cluster_tasks(
        self,
        org_name: str,
        cluster_name: str,
        *,
        status: Union[OpsStatus, UnsetType] = unset,
        cluster_task_type: Union[OpsType, UnsetType] = unset,
    ) -> ClusterTaskList:
        """List cluster tasks in console.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param status: You want to check the status of the task. If not passed, all selected by default
        :type status: OpsStatus, optional
        :param cluster_task_type: You want to check the type of the task. If not passed, all selected by default
        :type cluster_task_type: OpsType, optional
        :rtype: ClusterTaskList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if status is not unset:
            kwargs["status"] = status
        if cluster_task_type is not unset:
            kwargs["cluster_task_type"] = cluster_task_type
        return self._list_cluster_tasks_endpoint.call_with_http_info(**kwargs)
