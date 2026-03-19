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


class ClusterlogApi:
    """ClusterLog API client.

    Provides methods for the clusterLog endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._query_audit_logs_endpoint = _Endpoint(
            settings={
                "response_type": ClusterExecutionLog,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/audit",
                "http_method": "GET",
                "operation_id": "query_audit_logs",
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
                "start_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "endTime",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "instance_name": {
                    "location": "query",
                    "attribute": "instanceName",
                },
                "sort_type": {
                    "location": "query",
                    "attribute": "sortType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_error_logs_endpoint = _Endpoint(
            settings={
                "response_type": ClusterRawLogResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/error",
                "http_method": "GET",
                "operation_id": "query_error_logs",
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
                "start_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "endTime",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "instance_name": {
                    "location": "query",
                    "attribute": "instanceName",
                },
                "filename": {
                    "location": "query",
                    "attribute": "filename",
                },
                "query": {
                    "location": "query",
                    "attribute": "query",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
                "sort_type": {
                    "location": "query",
                    "attribute": "sortType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_pod_logs_endpoint = _Endpoint(
            settings={
                "response_type": ClusterRawLogResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/pod",
                "http_method": "GET",
                "operation_id": "query_pod_logs",
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
                "start_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "endTime",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "instance_name": {
                    "location": "query",
                    "attribute": "instanceName",
                },
                "filename": {
                    "location": "query",
                    "attribute": "filename",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
                "sort_type": {
                    "location": "query",
                    "attribute": "sortType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_running_logs_endpoint = _Endpoint(
            settings={
                "response_type": ClusterRawLogResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/running",
                "http_method": "GET",
                "operation_id": "query_running_logs",
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
                "start_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "endTime",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "instance_name": {
                    "location": "query",
                    "attribute": "instanceName",
                },
                "filename": {
                    "location": "query",
                    "attribute": "filename",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
                "query": {
                    "location": "query",
                    "attribute": "query",
                },
                "sort_type": {
                    "location": "query",
                    "attribute": "sortType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._query_slow_logs_endpoint = _Endpoint(
            settings={
                "response_type": ClusterExecutionLog,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow",
                "http_method": "GET",
                "operation_id": "query_slow_logs",
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
                "start_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "required": True,
                    "location": "query",
                    "attribute": "endTime",
                },
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
                "instance_name": {
                    "location": "query",
                    "attribute": "instanceName",
                },
                "query": {
                    "location": "query",
                    "attribute": "query",
                },
                "limit": {
                    "location": "query",
                    "attribute": "limit",
                },
                "sort_type": {
                    "location": "query",
                    "attribute": "sortType",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def query_audit_logs(
        self,
        org_name: str,
        cluster_name: str,
        start_time: str,
        end_time: str,
        *,
        limit: Union[str, UnsetType] = unset,
        component_name: Union[str, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        sort_type: Union[SortType, UnsetType] = unset,
    ) -> ClusterExecutionLog:
        """Query cluster audit logs.

        Query audit logs of a cluster
        :type org_name: str
        :type cluster_name: str
        :type start_time: str
        :type end_time: str
        :type limit: str, optional
        :type component_name: str, optional
        :type instance_name: str, optional
        :type sort_type: SortType, optional
        :rtype: ClusterExecutionLog
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start_time"] = start_time
        kwargs["end_time"] = end_time
        if limit is not unset:
            kwargs["limit"] = limit
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if sort_type is not unset:
            kwargs["sort_type"] = sort_type
        return self._query_audit_logs_endpoint.call_with_http_info(**kwargs)

    def query_error_logs(
        self,
        org_name: str,
        cluster_name: str,
        start_time: str,
        end_time: str,
        *,
        component_name: Union[str, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        limit: Union[str, UnsetType] = unset,
        sort_type: Union[SortType, UnsetType] = unset,
    ) -> ClusterRawLogResponse:
        """Query cluster error logs.

        Query error logs of a cluster
        :type org_name: str
        :type cluster_name: str
        :type start_time: str
        :type end_time: str
        :type component_name: str, optional
        :type instance_name: str, optional
        :type filename: str, optional
        :type query: str, optional
        :type limit: str, optional
        :type sort_type: SortType, optional
        :rtype: ClusterRawLogResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start_time"] = start_time
        kwargs["end_time"] = end_time
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if filename is not unset:
            kwargs["filename"] = filename
        if query is not unset:
            kwargs["query"] = query
        if limit is not unset:
            kwargs["limit"] = limit
        if sort_type is not unset:
            kwargs["sort_type"] = sort_type
        return self._query_error_logs_endpoint.call_with_http_info(**kwargs)

    def query_pod_logs(
        self,
        org_name: str,
        cluster_name: str,
        start_time: str,
        end_time: str,
        *,
        component_name: Union[str, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        limit: Union[str, UnsetType] = unset,
        sort_type: Union[SortType, UnsetType] = unset,
    ) -> ClusterRawLogResponse:
        """Query cluster pod logs.

        Query pod logs of a cluster
        :type org_name: str
        :type cluster_name: str
        :type start_time: str
        :type end_time: str
        :type component_name: str, optional
        :type instance_name: str, optional
        :type filename: str, optional
        :type limit: str, optional
        :type sort_type: SortType, optional
        :rtype: ClusterRawLogResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start_time"] = start_time
        kwargs["end_time"] = end_time
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if filename is not unset:
            kwargs["filename"] = filename
        if limit is not unset:
            kwargs["limit"] = limit
        if sort_type is not unset:
            kwargs["sort_type"] = sort_type
        return self._query_pod_logs_endpoint.call_with_http_info(**kwargs)

    def query_running_logs(
        self,
        org_name: str,
        cluster_name: str,
        start_time: str,
        end_time: str,
        *,
        component_name: Union[str, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        limit: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sort_type: Union[SortType, UnsetType] = unset,
    ) -> ClusterRawLogResponse:
        """Query cluster running logs.

        Query running logs of a cluster
        :type org_name: str
        :type cluster_name: str
        :type start_time: str
        :type end_time: str
        :type component_name: str, optional
        :type instance_name: str, optional
        :type filename: str, optional
        :type limit: str, optional
        :type query: str, optional
        :type sort_type: SortType, optional
        :rtype: ClusterRawLogResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start_time"] = start_time
        kwargs["end_time"] = end_time
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if filename is not unset:
            kwargs["filename"] = filename
        if limit is not unset:
            kwargs["limit"] = limit
        if query is not unset:
            kwargs["query"] = query
        if sort_type is not unset:
            kwargs["sort_type"] = sort_type
        return self._query_running_logs_endpoint.call_with_http_info(**kwargs)

    def query_slow_logs(
        self,
        org_name: str,
        cluster_name: str,
        start_time: str,
        end_time: str,
        *,
        component_name: Union[str, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        limit: Union[str, UnsetType] = unset,
        sort_type: Union[SortType, UnsetType] = unset,
    ) -> ClusterExecutionLog:
        """Query cluster slow logs.

        Query slow logs of a cluster
        :type org_name: str
        :type cluster_name: str
        :type start_time: str
        :type end_time: str
        :type component_name: str, optional
        :type instance_name: str, optional
        :type query: str, optional
        :type limit: str, optional
        :type sort_type: SortType, optional
        :rtype: ClusterExecutionLog
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start_time"] = start_time
        kwargs["end_time"] = end_time
        if component_name is not unset:
            kwargs["component_name"] = component_name
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if query is not unset:
            kwargs["query"] = query
        if limit is not unset:
            kwargs["limit"] = limit
        if sort_type is not unset:
            kwargs["sort_type"] = sort_type
        return self._query_slow_logs_endpoint.call_with_http_info(**kwargs)
