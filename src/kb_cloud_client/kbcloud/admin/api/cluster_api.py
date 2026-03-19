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


class ClusterApi:
    """Cluster API client.

    Provides methods for the cluster endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._batch_update_clusters_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/batch",
                "http_method": "POST",
                "operation_id": "batch_update_clusters",
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
        self._create_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters",
                "http_method": "POST",
                "operation_id": "create_cluster",
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
        self._delete_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}",
                "http_method": "DELETE",
                "operation_id": "delete_cluster",
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
                "force": {
                    "location": "query",
                    "attribute": "force",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._describe_cluster_ha_history_endpoint = _Endpoint(
            settings={
                "response_type": HaHistoryList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/haHistory",
                "http_method": "GET",
                "operation_id": "describe_cluster_ha_history",
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
                "component_name": {
                    "location": "query",
                    "attribute": "componentName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}",
                "http_method": "GET",
                "operation_id": "get_cluster",
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
        self._get_cluster_by_id_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clustersWithDelete/{clusterID}",
                "http_method": "GET",
                "operation_id": "get_cluster_by_id",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "clusterID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_cluster_instance_log_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/workloads/{workloadName}/log",
                "http_method": "GET",
                "operation_id": "get_cluster_instance_log",
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
                "workload_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "workloadName",
                },
                "workload_type": {
                    "location": "query",
                    "attribute": "workloadType",
                },
                "previous": {
                    "location": "query",
                    "attribute": "previous",
                },
                "since_seconds": {
                    "location": "query",
                    "attribute": "sinceSeconds",
                },
                "tail_lines": {
                    "location": "query",
                    "attribute": "tailLines",
                },
            },
            headers_map={
                "accept": ["text/plain", "application/json"],
            },
            api_client=api_client,
        )
        self._get_instaces_metrics_endpoint = _Endpoint(
            settings={
                "response_type": InstanceMetricsList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/metrics",
                "http_method": "GET",
                "operation_id": "get_instaces_metrics",
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
        self._get_instance_container_log_endpoint = _Endpoint(
            settings={
                "response_type": InstanceLog,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/log",
                "http_method": "GET",
                "operation_id": "get_instance_container_log",
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
                "instance_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "instanceName",
                },
                "container": {
                    "location": "query",
                    "attribute": "container",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_cluster_endpoint = _Endpoint(
            settings={
                "response_type": ClusterList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters",
                "http_method": "GET",
                "operation_id": "list_cluster",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster_definition": {
                    "location": "query",
                    "attribute": "clusterDefinition",
                },
                "environment_name": {
                    "location": "query",
                    "attribute": "environmentName",
                },
                "environment_type": {
                    "location": "query",
                    "attribute": "environmentType",
                },
                "tag_key": {
                    "location": "query",
                    "attribute": "tagKey",
                },
                "tag_value": {
                    "location": "query",
                    "attribute": "tagValue",
                },
                "tag_keys": {
                    "location": "query",
                    "attribute": "tagKeys",
                    "collection_format": "multi",
                },
                "tag_values": {
                    "location": "query",
                    "attribute": "tagValues",
                    "collection_format": "multi",
                },
                "license_id": {
                    "location": "query",
                    "attribute": "licenseId",
                },
                "ref_cluster_name": {
                    "location": "query",
                    "attribute": "refClusterName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_clusters_endpoint = _Endpoint(
            settings={
                "response_type": ClusterList,
                "endpoint_path": "/admin/v1/clusters",
                "http_method": "GET",
                "operation_id": "list_clusters",
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
                "with_static": {
                    "location": "query",
                    "attribute": "withStatic",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_endpoints_endpoint = _Endpoint(
            settings={
                "response_type": EndpointList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/endpoints",
                "http_method": "GET",
                "operation_id": "list_endpoints",
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
                "node_port_host_count": {
                    "location": "query",
                    "attribute": "nodePortHostCount",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_instance_endpoint = _Endpoint(
            settings={
                "response_type": InstanceList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances",
                "http_method": "GET",
                "operation_id": "list_instance",
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
        self._list_instance_events_endpoint = _Endpoint(
            settings={
                "response_type": InstanceEventList,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/events",
                "http_method": "GET",
                "operation_id": "list_instance_events",
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
                "instance_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "instanceName",
                },
                "return_number": {
                    "location": "query",
                    "attribute": "returnNumber",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_cluster_endpoint = _Endpoint(
            settings={
                "response_type": Cluster,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}",
                "http_method": "PATCH",
                "operation_id": "patch_cluster",
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
        self._query_cluster_metrics_endpoint = _Endpoint(
            settings={
                "response_type": ClusterMetrics,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/metrics",
                "http_method": "GET",
                "operation_id": "query_cluster_metrics",
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
                "query": {
                    "required": True,
                    "location": "query",
                    "attribute": "query",
                },
                "query_type": {
                    "required": True,
                    "location": "query",
                    "attribute": "queryType",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._restart_instance_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/restart",
                "http_method": "POST",
                "operation_id": "restart_instance",
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
                "instance_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "instanceName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._validate_cluster_creation_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/organizations/{orgName}/clusters/validate",
                "http_method": "POST",
                "operation_id": "validate_cluster_creation",
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


    def batch_update_clusters(
        self,
        org_name: str,
        body: ClusterBatchUpdate,
    ) -> APIErrorResponse:
        """Batch update clusters.

        Update multiple clusters with the same update information (displayName and/or maintainceWindow) in a single request
        :param org_name: name of the Org
        :type org_name: str
        :type body: ClusterBatchUpdate
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._batch_update_clusters_endpoint.call_with_http_info(**kwargs)

    def create_cluster(
        self,
        org_name: str,
        body: ClusterCreate,
    ) -> Cluster:
        """Create new cluster.
        :param org_name: name of the Org
        :type org_name: str
        :type body: ClusterCreate
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_cluster_endpoint.call_with_http_info(**kwargs)

    def delete_cluster(
        self,
        org_name: str,
        cluster_name: str,
        *,
        force: Union[bool, UnsetType] = unset,
    ) -> Dict[str, Any]:
        """Delete cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param force: if it is true, the cluster will be deleted no matter what the termination policy is, and will not be moved to the...
        :type force: bool, optional
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if force is not unset:
            kwargs["force"] = force
        return self._delete_cluster_endpoint.call_with_http_info(**kwargs)

    def describe_cluster_ha_history(
        self,
        org_name: str,
        cluster_name: str,
        start: int,
        end: int,
        *,
        component_name: Union[str, UnsetType] = unset,
    ) -> HaHistoryList:
        """describe cluster HA history.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :param component_name: name of the component
        :type component_name: str, optional
        :rtype: HaHistoryList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["start"] = start
        kwargs["end"] = end
        if component_name is not unset:
            kwargs["component_name"] = component_name
        return self._describe_cluster_ha_history_endpoint.call_with_http_info(**kwargs)

    def get_cluster(
        self,
        org_name: str,
        cluster_name: str,
    ) -> Cluster:
        """Get cluster details.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_cluster_endpoint.call_with_http_info(**kwargs)

    def get_cluster_by_id(
        self,
        org_name: str,
        cluster_id: str,
    ) -> Cluster:
        """Get cluster details by ID.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_id: ID of the KubeBlocks cluster
        :type cluster_id: str
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_id"] = cluster_id
        return self._get_cluster_by_id_endpoint.call_with_http_info(**kwargs)

    def get_cluster_instance_log(
        self,
        org_name: str,
        cluster_name: str,
        workload_name: str,
        *,
        workload_type: Union[str, UnsetType] = unset,
        previous: Union[bool, UnsetType] = unset,
        since_seconds: Union[int, UnsetType] = unset,
        tail_lines: Union[int, UnsetType] = unset,
    ) -> str:
        """Tail cluster instance container log.

        read log of the specified cluster instance
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param workload_name: name of the workload
        :type workload_name: str
        :param workload_type: type of the workload, supported values ["Pod", "Job"], default value is Pod.
        :type workload_type: str, optional
        :param previous: Return previous terminated container logs. Defaults to false.
        :type previous: bool, optional
        :param since_seconds: A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod...
        :type since_seconds: int, optional
        :param tail_lines: If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of...
        :type tail_lines: int, optional
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["workload_name"] = workload_name
        if workload_type is not unset:
            kwargs["workload_type"] = workload_type
        if previous is not unset:
            kwargs["previous"] = previous
        if since_seconds is not unset:
            kwargs["since_seconds"] = since_seconds
        if tail_lines is not unset:
            kwargs["tail_lines"] = tail_lines
        return self._get_cluster_instance_log_endpoint.call_with_http_info(**kwargs)

    def get_instaces_metrics(
        self,
        org_name: str,
        cluster_name: str,
    ) -> InstanceMetricsList:
        """Get instaces metrics in cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: InstanceMetricsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._get_instaces_metrics_endpoint.call_with_http_info(**kwargs)

    def get_instance_container_log(
        self,
        org_name: str,
        cluster_name: str,
        instance_name: str,
        *,
        container: Union[str, UnsetType] = unset,
    ) -> InstanceLog:
        """Tail cluster instance container log.

        read log of the specified cluster instance
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param instance_name: name of the instance
        :type instance_name: str
        :param container: specify container name to get specific container log, if not specified, will return the log of the default container
        :type container: str, optional
        :rtype: InstanceLog
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["instance_name"] = instance_name
        if container is not unset:
            kwargs["container"] = container
        return self._get_instance_container_log_endpoint.call_with_http_info(**kwargs)

    def list_cluster(
        self,
        org_name: str,
        *,
        cluster_definition: Union[str, UnsetType] = unset,
        environment_name: Union[str, UnsetType] = unset,
        environment_type: Union[EnvironmentType, UnsetType] = unset,
        tag_key: Union[str, UnsetType] = unset,
        tag_value: Union[str, UnsetType] = unset,
        tag_keys: Union[List[str], UnsetType] = unset,
        tag_values: Union[List[str], UnsetType] = unset,
        license_id: Union[int, UnsetType] = unset,
        ref_cluster_name: Union[str, UnsetType] = unset,
    ) -> ClusterList:
        """List clusters in the Org.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_definition: The clusterDefinition in the List request
        :type cluster_definition: str, optional
        :param environment_name: Environment Type
        :type environment_name: str, optional
        :param environment_type: Environment Type
        :type environment_type: EnvironmentType, optional
        :param tag_key: Tag key; this parameter is deprecated, use tagKeys instead
        :type tag_key: str, optional
        :param tag_value: Tag value; this parameter is deprecated, use tagValues instead
        :type tag_value: str, optional
        :param tag_keys: A list of tags' keys
        :type tag_keys: List[str], optional
        :param tag_values: A list of tags' values corresponding to the tagKeys
        :type tag_values: List[str], optional
        :param license_id: license id
        :type license_id: int, optional
        :param ref_cluster_name: list clusters referenced by this cluster
        :type ref_cluster_name: str, optional
        :rtype: ClusterList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if cluster_definition is not unset:
            kwargs["cluster_definition"] = cluster_definition
        if environment_name is not unset:
            kwargs["environment_name"] = environment_name
        if environment_type is not unset:
            kwargs["environment_type"] = environment_type
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if tag_value is not unset:
            kwargs["tag_value"] = tag_value
        if tag_keys is not unset:
            kwargs["tag_keys"] = tag_keys
        if tag_values is not unset:
            kwargs["tag_values"] = tag_values
        if license_id is not unset:
            kwargs["license_id"] = license_id
        if ref_cluster_name is not unset:
            kwargs["ref_cluster_name"] = ref_cluster_name
        return self._list_cluster_endpoint.call_with_http_info(**kwargs)

    def list_clusters(
        self,
        *,
        org_name: Union[str, UnsetType] = unset,
        env_name: Union[str, UnsetType] = unset,
        with_static: Union[bool, UnsetType] = unset,
    ) -> ClusterList:
        """Get cluster list.

        Get cluster list
        :param org_name: Organization name, if envName is provided, orgName is required
        :type org_name: str, optional
        :param env_name: Environment name
        :type env_name: str, optional
        :param with_static: Whether to include static clusters
        :type with_static: bool, optional
        :rtype: ClusterList
        """
        kwargs: Dict[str, Any] = {}
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if env_name is not unset:
            kwargs["env_name"] = env_name
        if with_static is not unset:
            kwargs["with_static"] = with_static
        return self._list_clusters_endpoint.call_with_http_info(**kwargs)

    def list_endpoints(
        self,
        org_name: str,
        cluster_name: str,
        *,
        node_port_host_count: Union[int, UnsetType] = unset,
    ) -> EndpointList:
        """List cluster endpoints.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param node_port_host_count: count of the NodePort host
        :type node_port_host_count: int, optional
        :rtype: EndpointList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if node_port_host_count is not unset:
            kwargs["node_port_host_count"] = node_port_host_count
        return self._list_endpoints_endpoint.call_with_http_info(**kwargs)

    def list_instance(
        self,
        org_name: str,
        cluster_name: str,
    ) -> InstanceList:
        """List cluster instances.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: InstanceList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._list_instance_endpoint.call_with_http_info(**kwargs)

    def list_instance_events(
        self,
        org_name: str,
        cluster_name: str,
        instance_name: str,
        *,
        return_number: Union[int, UnsetType] = unset,
    ) -> InstanceEventList:
        """List instance events.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param instance_name: name of the instance
        :type instance_name: str
        :param return_number: return number of events
        :type return_number: int, optional
        :rtype: InstanceEventList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["instance_name"] = instance_name
        if return_number is not unset:
            kwargs["return_number"] = return_number
        return self._list_instance_events_endpoint.call_with_http_info(**kwargs)

    def patch_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: ClusterUpdate,
    ) -> Cluster:
        """Update cluster specified fields.

        Update the specified Cluster
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: ClusterUpdate
        :rtype: Cluster
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._patch_cluster_endpoint.call_with_http_info(**kwargs)

    def query_cluster_metrics(
        self,
        org_name: str,
        cluster_name: str,
        query: str,
        query_type: MetricsQueryType,
        start: int,
        end: int,
    ) -> ClusterMetrics:
        """Query cluster metrics.

        Query cluster metrics by specified metric name and instance name, support instant and range query
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param query: The promQL query string
        :type query: str
        :param query_type: The query type in the query, if use instant, the query will return the lastest instant value, if use range, the...
        :type query_type: MetricsQueryType
        :param start: The start of the time range for the query, unit is seconds.
        :type start: int
        :param end: The end of the time range for the query, unit is seconds.
        :type end: int
        :rtype: ClusterMetrics
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["query"] = query
        kwargs["query_type"] = query_type
        kwargs["start"] = start
        kwargs["end"] = end
        return self._query_cluster_metrics_endpoint.call_with_http_info(**kwargs)

    def restart_instance(
        self,
        org_name: str,
        cluster_name: str,
        instance_name: str,
    ) -> APIErrorResponse:
        """Restart instance of cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :param instance_name: name of the instance
        :type instance_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["instance_name"] = instance_name
        return self._restart_instance_endpoint.call_with_http_info(**kwargs)

    def validate_cluster_creation(
        self,
        org_name: str,
        body: ClusterCreate,
    ) -> APIErrorResponse:
        """Validate cluster creation.
        :param org_name: name of the Org
        :type org_name: str
        :type body: ClusterCreate
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._validate_cluster_creation_endpoint.call_with_http_info(**kwargs)
