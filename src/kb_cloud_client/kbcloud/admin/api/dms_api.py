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


class DmsApi:
    """Dms API client.

    Provides methods for the dms endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._data_export_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/export",
                "http_method": "POST",
                "operation_id": "data_export",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
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
        self._data_import_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/import",
                "http_method": "POST",
                "operation_id": "data_import",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
                "file": {
                    "required": True,
                    "location": "form",
                    "attribute": "file",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json", "multipart/form-data"],
            },
            api_client=api_client,
        )
        self._get_object_info_endpoint = _Endpoint(
            settings={
                "response_type": DmsObjectResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}/{objectName}",
                "http_method": "GET",
                "operation_id": "get_object_info",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "schema": {
                    "required": True,
                    "location": "path",
                    "attribute": "schema",
                },
                "type_": {
                    "required": True,
                    "location": "path",
                    "attribute": "type",
                },
                "object_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "objectName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_task_list_endpoint = _Endpoint(
            settings={
                "response_type": DmsTaskList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/tasks",
                "http_method": "GET",
                "operation_id": "get_task_list",
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
        self._get_task_progress_endpoint = _Endpoint(
            settings={
                "response_type": DmsTaskInfo,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/task",
                "http_method": "GET",
                "operation_id": "get_task_progress",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "task_id": {
                    "required": True,
                    "location": "query",
                    "attribute": "taskId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_object_names_by_type_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}",
                "http_method": "GET",
                "operation_id": "list_object_names_by_type",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "schema": {
                    "required": True,
                    "location": "path",
                    "attribute": "schema",
                },
                "type_": {
                    "required": True,
                    "location": "path",
                    "attribute": "type",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_object_types_in_schema_endpoint = _Endpoint(
            settings={
                "response_type": List[DmsObject],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}",
                "http_method": "GET",
                "operation_id": "list_object_types_in_schema",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "schema": {
                    "required": True,
                    "location": "path",
                    "attribute": "schema",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._alter_parameter_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameter",
                "http_method": "POST",
                "operation_id": "alter_parameter",
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
                "tenant_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tenantId",
                },
                "body": {
                    "required": True,
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["text/plain", "application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._close_sessions_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/session/{session}",
                "http_method": "DELETE",
                "operation_id": "close_sessions",
                "deprecated": True,
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
                "session": {
                    "required": True,
                    "location": "path",
                    "attribute": "session",
                },
                "keep": {
                    "location": "query",
                    "attribute": "keep",
                },
            },
            headers_map={
                "accept": ["text/plain", "application/json"],
            },
            api_client=api_client,
        )
        self._create_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": Datasource,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/createDS",
                "http_method": "POST",
                "operation_id": "create_data_source_v2",
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
        self._delete_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}",
                "http_method": "DELETE",
                "operation_id": "delete_data_source_v2",
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
        self._disable_console_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console",
                "http_method": "DELETE",
                "operation_id": "disable_console",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )
        self._enable_console_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console",
                "http_method": "POST",
                "operation_id": "enable_console",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
        self._generate_ddl_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/generateDDL",
                "http_method": "POST",
                "operation_id": "generate_ddl",
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
                "id_": {
                    "required": True,
                    "location": "path",
                    "attribute": "id",
                },
                "body": {
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": Datasource,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}",
                "http_method": "GET",
                "operation_id": "get_data_source_v2",
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
        self._get_engine_available_console_endpoint = _Endpoint(
            settings={
                "response_type": Console,
                "endpoint_path": "/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console",
                "http_method": "GET",
                "operation_id": "get_engine_available_console",
            },
            params_map={
                "engine_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "engineName",
                },
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_schema_list_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/schemas",
                "http_method": "GET",
                "operation_id": "get_schema_list",
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
        self._list_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": List[Datasource],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource",
                "http_method": "GET",
                "operation_id": "list_data_source_v2",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_parameters_endpoint = _Endpoint(
            settings={
                "response_type": List[DmsObParameter],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameters",
                "http_method": "GET",
                "operation_id": "list_parameters",
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
                "tenant_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tenantId",
                },
                "mode": {
                    "required": True,
                    "location": "query",
                    "attribute": "mode",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_query_history_endpoint = _Endpoint(
            settings={
                "response_type": List[DmsQueryHistory],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/history",
                "http_method": "GET",
                "operation_id": "list_query_history",
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
        self._list_sessions_old_endpoint = _Endpoint(
            settings={
                "response_type": List[DmsSession],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/sessions",
                "http_method": "GET",
                "operation_id": "list_sessions_old",
                "deprecated": True,
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
        self._query_endpoint = _Endpoint(
            settings={
                "response_type": DmsQueryResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/query",
                "http_method": "POST",
                "operation_id": "query",
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
        self._show_data_endpoint = _Endpoint(
            settings={
                "response_type": DmsResult,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/showData",
                "http_method": "POST",
                "operation_id": "show_data",
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
        self._sql_explain_endpoint = _Endpoint(
            settings={
                "response_type": DmsQueryResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/sqlExplain",
                "http_method": "POST",
                "operation_id": "sql_explain",
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
        self._tenant_parameter_history_endpoint = _Endpoint(
            settings={
                "response_type": ParameterHistoryList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameterHistory",
                "http_method": "GET",
                "operation_id": "tenant_parameter_history",
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
                "tenant_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "tenantId",
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
        self._test_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": bool,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/testDS",
                "http_method": "POST",
                "operation_id": "test_data_source_v2",
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
        self._update_data_source_v2_endpoint = _Endpoint(
            settings={
                "response_type": Datasource,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/updateDS",
                "http_method": "POST",
                "operation_id": "update_data_source_v2",
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


    def data_export(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        *,
        body: Union[DmsExportRequest, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Data Export.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: DmsExportRequest, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        if body is not unset:
            kwargs["body"] = body
        return self._data_export_endpoint.call_with_http_info(**kwargs)

    def data_import(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        body: DmsImportRequest,
        file: bytes,
    ) -> Dict[str, Any]:
        """Data Import.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: DmsImportRequest
        :param file: the data file, csv or other format
        :type file: bytes
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["body"] = body
        kwargs["file"] = file
        return self._data_import_endpoint.call_with_http_info(**kwargs)

    def get_object_info(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        schema: str,
        type_: str,
        object_name: str,
    ) -> DmsObjectResponse:
        """get the detail object info.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :param schema: schema or database name
        :type schema: str
        :param type_: object type
        :type type_: str
        :param object_name: object name
        :type object_name: str
        :rtype: DmsObjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["schema"] = schema
        kwargs["type_"] = type_
        kwargs["object_name"] = object_name
        return self._get_object_info_endpoint.call_with_http_info(**kwargs)

    def get_task_list(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> DmsTaskList:
        """Get the task list.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :rtype: DmsTaskList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._get_task_list_endpoint.call_with_http_info(**kwargs)

    def get_task_progress(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        task_id: str,
    ) -> DmsTaskInfo:
        """Get the task progress.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :param task_id: the task id
        :type task_id: str
        :rtype: DmsTaskInfo
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["task_id"] = task_id
        return self._get_task_progress_endpoint.call_with_http_info(**kwargs)

    def list_object_names_by_type(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        schema: str,
        type_: str,
    ) -> List[str]:
        """list the all name for the specified object type.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :param schema: schema or database name
        :type schema: str
        :param type_: object type
        :type type_: str
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["schema"] = schema
        kwargs["type_"] = type_
        return self._list_object_names_by_type_endpoint.call_with_http_info(**kwargs)

    def list_object_types_in_schema(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        schema: str,
    ) -> List[DmsObject]:
        """list the type and number of database objects in the specified database or schema.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :param schema: schema or database name
        :type schema: str
        :rtype: List[DmsObject]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["schema"] = schema
        return self._list_object_types_in_schema_endpoint.call_with_http_info(**kwargs)

    def alter_parameter(
        self,
        org_name: str,
        cluster_name: str,
        tenant_id: str,
        body: DmsObAlterParameter,
    ) -> str:
        """alter cluster parameter.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type tenant_id: str
        :type body: DmsObAlterParameter
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tenant_id"] = tenant_id
        kwargs["body"] = body
        return self._alter_parameter_endpoint.call_with_http_info(**kwargs)

    def close_sessions(
        self,
        org_name: str,
        cluster_name: str,
        session: str,
        *,
        keep: Union[str, UnsetType] = unset,
    ) -> str:
        """close the session for the cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param session: name of the storage volume
        :type session: str
        :param keep: whether only close the query and keep the session
        :type keep: str, optional
        :rtype: str
        """
        warnings.warn("close_sessions is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["session"] = session
        if keep is not unset:
            kwargs["keep"] = keep
        return self._close_sessions_endpoint.call_with_http_info(**kwargs)

    def create_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
        body: Datasource,
    ) -> Datasource:
        """create the datasource.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: Datasource
        :rtype: Datasource
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._create_data_source_v2_endpoint.call_with_http_info(**kwargs)

    def delete_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> APIErrorResponse:
        """delete the datasource.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._delete_data_source_v2_endpoint.call_with_http_info(**kwargs)

    def disable_console(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
    ) -> APIErrorResponse:
        """disable console.

        disable console
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._disable_console_endpoint.call_with_http_info(**kwargs)

    def enable_console(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
        *,
        body: Union[DMSConsoleEnableOpt, UnsetType] = unset,
    ) -> APIErrorResponse:
        """enable console.

        enable console
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: DMSConsoleEnableOpt, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if body is not unset:
            kwargs["body"] = body
        return self._enable_console_endpoint.call_with_http_info(**kwargs)

    def generate_ddl(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        *,
        body: Union[DmsGenerateDDLRequest, UnsetType] = unset,
    ) -> str:
        """support ddl and dml operations.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: DmsGenerateDDLRequest, optional
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        if body is not unset:
            kwargs["body"] = body
        return self._generate_ddl_endpoint.call_with_http_info(**kwargs)

    def get_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> Datasource:
        """get the datasource.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :rtype: Datasource
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._get_data_source_v2_endpoint.call_with_http_info(**kwargs)

    def get_engine_available_console(
        self,
        engine_name: str,
        org_name: str,
        cluster_name: str,
    ) -> Console:
        """get engine available console.

        get engine available console
        :param engine_name: name of the engine
        :type engine_name: str
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: Console
        """
        kwargs: Dict[str, Any] = {}
        kwargs["engine_name"] = engine_name
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_engine_available_console_endpoint.call_with_http_info(**kwargs)

    def get_schema_list(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> List[str]:
        """list all databases or schema of the cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._get_schema_list_endpoint.call_with_http_info(**kwargs)

    def list_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
    ) -> List[Datasource]:
        """list the datasource of a cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :rtype: List[Datasource]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_data_source_v2_endpoint.call_with_http_info(**kwargs)

    def list_parameters(
        self,
        org_name: str,
        cluster_name: str,
        tenant_id: str,
        mode: str,
    ) -> List[DmsObParameter]:
        """list cluster parameters.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type tenant_id: str
        :type mode: str
        :rtype: List[DmsObParameter]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tenant_id"] = tenant_id
        kwargs["mode"] = mode
        return self._list_parameters_endpoint.call_with_http_info(**kwargs)

    def list_query_history(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
    ) -> List[DmsQueryHistory]:
        """list the query History.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :rtype: List[DmsQueryHistory]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        return self._list_query_history_endpoint.call_with_http_info(**kwargs)

    def list_sessions_old(
        self,
        org_name: str,
        cluster_name: str,
        *,
        all: Union[str, UnsetType] = unset,
    ) -> List[DmsSession]:
        """list all session for the cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param all: whether list all session includes sleep
        :type all: str, optional
        :rtype: List[DmsSession]
        """
        warnings.warn("list_sessions_old is deprecated", DeprecationWarning, stacklevel=2)
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if all is not unset:
            kwargs["all"] = all
        return self._list_sessions_old_endpoint.call_with_http_info(**kwargs)

    def query(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        body: DmsQueryRequest,
    ) -> DmsQueryResponse:
        """create a SQL query.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: DmsQueryRequest
        :rtype: DmsQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._query_endpoint.call_with_http_info(**kwargs)

    def show_data(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        body: ShowDataRequest,
    ) -> DmsResult:
        """read data of table or view.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: ShowDataRequest
        :rtype: DmsResult
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._show_data_endpoint.call_with_http_info(**kwargs)

    def sql_explain(
        self,
        org_name: str,
        cluster_name: str,
        id_: str,
        body: DmsExplainRequest,
    ) -> DmsQueryResponse:
        """explain a SQL.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param id_: id of the datasource
        :type id_: str
        :type body: DmsExplainRequest
        :rtype: DmsQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["id_"] = id_
        kwargs["body"] = body
        return self._sql_explain_endpoint.call_with_http_info(**kwargs)

    def tenant_parameter_history(
        self,
        org_name: str,
        cluster_name: str,
        tenant_id: str,
        *,
        parameter_name: Union[str, UnsetType] = unset,
    ) -> ParameterHistoryList:
        """List parameters history of the Oceanbase tenant.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param tenant_id: id of the tenant
        :type tenant_id: str
        :param parameter_name: name of the parameter
        :type parameter_name: str, optional
        :rtype: ParameterHistoryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["tenant_id"] = tenant_id
        if parameter_name is not unset:
            kwargs["parameter_name"] = parameter_name
        return self._tenant_parameter_history_endpoint.call_with_http_info(**kwargs)

    def test_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
        body: Datasource,
    ) -> bool:
        """test the datasource.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: Datasource
        :rtype: bool
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._test_data_source_v2_endpoint.call_with_http_info(**kwargs)

    def update_data_source_v2(
        self,
        org_name: str,
        cluster_name: str,
        body: Datasource,
    ) -> Datasource:
        """update the datasource.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: Datasource
        :rtype: Datasource
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._update_data_source_v2_endpoint.call_with_http_info(**kwargs)
