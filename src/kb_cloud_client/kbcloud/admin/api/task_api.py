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


class TaskApi:
    """Task API client.

    Provides methods for the task endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_task_endpoint = _Endpoint(
            settings={
                "response_type": Task,
                "endpoint_path": "/admin/v1/tasks/{taskId}",
                "http_method": "GET",
                "operation_id": "get_task",
            },
            params_map={
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
        self._get_task_log_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/tasks/{taskId}/log",
                "http_method": "GET",
                "operation_id": "get_task_log",
            },
            params_map={
                "task_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "taskId",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._list_task_endpoint = _Endpoint(
            settings={
                "response_type": TaskList,
                "endpoint_path": "/admin/v1/tasks",
                "http_method": "GET",
                "operation_id": "list_task",
            },
            params_map={
                "task_type": {
                    "location": "query",
                    "attribute": "taskType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._retry_task_endpoint = _Endpoint(
            settings={
                "response_type": Task,
                "endpoint_path": "/admin/v1/tasks/{taskId}/retry",
                "http_method": "PATCH",
                "operation_id": "retry_task",
            },
            params_map={
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
        self._stop_task_endpoint = _Endpoint(
            settings={
                "response_type": Task,
                "endpoint_path": "/admin/v1/tasks/{taskId}/stop",
                "http_method": "PATCH",
                "operation_id": "stop_task",
            },
            params_map={
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


    def get_task(
        self,
        task_id: str,
    ) -> Task:
        """Get task detail.

        Get task
        :param task_id: ID of the task
        :type task_id: str
        :rtype: Task
        """
        kwargs: Dict[str, Any] = {}
        kwargs["task_id"] = task_id
        return self._get_task_endpoint.call_with_http_info(**kwargs)

    def get_task_log(
        self,
        task_id: str,
    ) -> APIErrorResponse:
        """Get task log.
        :param task_id: ID of the task
        :type task_id: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["task_id"] = task_id
        return self._get_task_log_endpoint.call_with_http_info(**kwargs)

    def list_task(
        self,
        *,
        task_type: Union[str, UnsetType] = unset,
    ) -> TaskList:
        """List task.

        List tasks
        :param task_type: Filter by task type
        :type task_type: str, optional
        :rtype: TaskList
        """
        kwargs: Dict[str, Any] = {}
        if task_type is not unset:
            kwargs["task_type"] = task_type
        return self._list_task_endpoint.call_with_http_info(**kwargs)

    def retry_task(
        self,
        task_id: str,
    ) -> Task:
        """Retry a task.

        retry task
        :param task_id: ID of the task
        :type task_id: str
        :rtype: Task
        """
        kwargs: Dict[str, Any] = {}
        kwargs["task_id"] = task_id
        return self._retry_task_endpoint.call_with_http_info(**kwargs)

    def stop_task(
        self,
        task_id: str,
    ) -> Task:
        """Stop a task.

        stop task
        :param task_id: ID of the task
        :type task_id: str
        :rtype: Task
        """
        kwargs: Dict[str, Any] = {}
        kwargs["task_id"] = task_id
        return self._stop_task_endpoint.call_with_http_info(**kwargs)
