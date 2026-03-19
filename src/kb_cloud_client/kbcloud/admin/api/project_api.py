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


class ProjectApi:
    """Project API client.

    Provides methods for the project endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_project_endpoint = _Endpoint(
            settings={
                "response_type": Project,
                "endpoint_path": "/admin/v1/environments/{environmentName}/projects",
                "http_method": "POST",
                "operation_id": "create_project",
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
        self._delete_project_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/projects/{projectName}",
                "http_method": "DELETE",
                "operation_id": "delete_project",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "project_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "projectName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_projects_endpoint = _Endpoint(
            settings={
                "response_type": ProjectList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/projects",
                "http_method": "GET",
                "operation_id": "list_projects",
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


    def create_project(
        self,
        environment_name: str,
        body: ProjectCreate,
    ) -> Project:
        """Create a project in an environment.
        :param environment_name: environment name
        :type environment_name: str
        :type body: ProjectCreate
        :rtype: Project
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_project_endpoint.call_with_http_info(**kwargs)

    def delete_project(
        self,
        environment_name: str,
        project_name: str,
    ) -> APIErrorResponse:
        """Delete a project in an environment.
        :param environment_name: environment name
        :type environment_name: str
        :param project_name: project name
        :type project_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["project_name"] = project_name
        return self._delete_project_endpoint.call_with_http_info(**kwargs)

    def list_projects(
        self,
        environment_name: str,
    ) -> ProjectList:
        """List projects in an environment.
        :param environment_name: environment name
        :type environment_name: str
        :rtype: ProjectList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_projects_endpoint.call_with_http_info(**kwargs)
