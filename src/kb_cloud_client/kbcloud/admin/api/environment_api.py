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
        self._add_nodes_endpoint = _Endpoint(
            settings={
                "response_type": List[NodePoolNode],
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes",
                "http_method": "POST",
                "operation_id": "add_nodes",
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
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._check_kubeconfig_endpoint = _Endpoint(
            settings={
                "response_type": HttpBody,
                "endpoint_path": "/admin/v1/checkKubeconfig",
                "http_method": "POST",
                "operation_id": "check_kubeconfig",
            },
            params_map={
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
        self._check_node_ssh_config_endpoint = _Endpoint(
            settings={
                "response_type": SshConfigCheckResponse,
                "endpoint_path": "/admin/v1/environments/checkNodeSSHConfig",
                "http_method": "POST",
                "operation_id": "check_node_ssh_config",
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
        self._cordon_environment_node_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/cordon",
                "http_method": "PATCH",
                "operation_id": "cordon_environment_node",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._create_environment_endpoint = _Endpoint(
            settings={
                "response_type": Environment,
                "endpoint_path": "/admin/v1/environments",
                "http_method": "POST",
                "operation_id": "create_environment",
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
        self._create_node_group_endpoint = _Endpoint(
            settings={
                "response_type": NodeGroup,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodeGroups",
                "http_method": "POST",
                "operation_id": "create_node_group",
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
        self._create_workflow_endpoint = _Endpoint(
            settings={
                "response_type": Workflow,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow",
                "http_method": "POST",
                "operation_id": "create_workflow",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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
        self._delete_environment_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}",
                "http_method": "DELETE",
                "operation_id": "delete_environment",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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
        self._delete_node_group_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodeGroups/{nodeGroupName}",
                "http_method": "DELETE",
                "operation_id": "delete_node_group",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_group_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeGroupName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_environment_endpoint = _Endpoint(
            settings={
                "response_type": Environment,
                "endpoint_path": "/admin/v1/environments/{environmentName}",
                "http_method": "GET",
                "operation_id": "get_environment",
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
        self._get_environment_backup_repo_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentBackupRepo,
                "endpoint_path": "/admin/v1/environmentBackupRepo",
                "http_method": "POST",
                "operation_id": "get_environment_backup_repo",
            },
            params_map={
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
        self._get_environment_bootstrap_manifests_endpoint = _Endpoint(
            settings={
                "response_type": HttpBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/bootstrapManifests",
                "http_method": "GET",
                "operation_id": "get_environment_bootstrap_manifests",
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
        self._get_environment_kubeconfig_endpoint = _Endpoint(
            settings={
                "response_type": HttpBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/kubeconfig",
                "http_method": "GET",
                "operation_id": "get_environment_kubeconfig",
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
        self._get_environment_metrics_monitor_stats_endpoint = _Endpoint(
            settings={
                "response_type": JsonBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/monitorStatus",
                "http_method": "GET",
                "operation_id": "get_environment_metrics_monitor_stats",
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
        self._get_environment_module_details_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentModuleDetails,
                "endpoint_path": "/admin/v1/environments/{environmentName}/modules/{moduleName}/details",
                "http_method": "GET",
                "operation_id": "get_environment_module_details",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "module_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "moduleName",
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
                "endpoint_path": "/admin/v1/environments/{environmentName}/modules",
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
        self._get_environment_module_logs_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentModuleLogs,
                "endpoint_path": "/admin/v1/environments/{environmentName}/modules/{moduleName}/pods/{podName}/logs",
                "http_method": "GET",
                "operation_id": "get_environment_module_logs",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "module_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "moduleName",
                },
                "pod_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "podName",
                },
                "container_name": {
                    "location": "query",
                    "attribute": "containerName",
                },
                "since_seconds": {
                    "location": "query",
                    "attribute": "sinceSeconds",
                },
                "since_time": {
                    "location": "query",
                    "attribute": "sinceTime",
                },
                "tail_lines": {
                    "location": "query",
                    "attribute": "tailLines",
                },
                "search": {
                    "location": "query",
                    "attribute": "search",
                },
                "previous": {
                    "location": "query",
                    "attribute": "previous",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_environment_provisioning_progress_endpoint = _Endpoint(
            settings={
                "response_type": JsonBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/progress",
                "http_method": "GET",
                "operation_id": "get_environment_provisioning_progress",
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
        self._get_environment_status_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentStatus,
                "endpoint_path": "/admin/v1/environments/{environmentName}/status",
                "http_method": "GET",
                "operation_id": "get_environment_status",
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
        self._get_environment_status_history_endpoint = _Endpoint(
            settings={
                "response_type": List[EnvironmentStatusHistory],
                "endpoint_path": "/admin/v1/environments/{environmentName}/statusHistory",
                "http_method": "GET",
                "operation_id": "get_environment_status_history",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "start_time": {
                    "location": "query",
                    "attribute": "startTime",
                },
                "end_time": {
                    "location": "query",
                    "attribute": "endTime",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_latest_env_module_version_endpoint = _Endpoint(
            settings={
                "response_type": EnvModuleVersion,
                "endpoint_path": "/admin/v1/latestEnvModuleVersion",
                "http_method": "GET",
                "operation_id": "get_latest_env_module_version",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_node_endpoint = _Endpoint(
            settings={
                "response_type": JsonBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}",
                "http_method": "GET",
                "operation_id": "get_node",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_optional_environment_modules_endpoint = _Endpoint(
            settings={
                "response_type": List[EnvironmentModule],
                "endpoint_path": "/admin/v1/environments/optional-modules",
                "http_method": "GET",
                "operation_id": "get_optional_environment_modules",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_workflow_endpoint = _Endpoint(
            settings={
                "response_type": Workflow,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow/{workflowName}",
                "http_method": "GET",
                "operation_id": "get_workflow",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "workflow_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "workflowName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_workflow_list_endpoint = _Endpoint(
            settings={
                "response_type": WorkflowList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow",
                "http_method": "GET",
                "operation_id": "get_workflow_list",
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
        self._get_workflow_log_endpoint = _Endpoint(
            settings={
                "response_type": str,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow/{workflowName}/log",
                "http_method": "GET",
                "operation_id": "get_workflow_log",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "workflow_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "workflowName",
                },
            },
            headers_map={
                "accept": ["text/plain"],
            },
            api_client=api_client,
        )
        self._list_env_node_zone_endpoint = _Endpoint(
            settings={
                "response_type": List[str],
                "endpoint_path": "/admin/v1/environments/{environmentName}/availableZones",
                "http_method": "GET",
                "operation_id": "list_env_node_zone",
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
        self._list_environment_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentList,
                "endpoint_path": "/admin/v1/environments",
                "http_method": "GET",
                "operation_id": "list_environment",
            },
            params_map={
                "org_name": {
                    "location": "query",
                    "attribute": "orgName",
                },
                "cloud_provider": {
                    "location": "query",
                    "attribute": "cloudProvider",
                },
                "cloud_region": {
                    "location": "query",
                    "attribute": "cloudRegion",
                },
                "environment_type": {
                    "location": "query",
                    "attribute": "environmentType",
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
        self._list_environment_object_storage_endpoint = _Endpoint(
            settings={
                "response_type": EnvironmentObjectStorage,
                "endpoint_path": "/admin/v1/environmentObjectStorage",
                "http_method": "POST",
                "operation_id": "list_environment_object_storage",
            },
            params_map={
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
        self._list_kubernetes_node_endpoint = _Endpoint(
            settings={
                "response_type": NodeList,
                "endpoint_path": "/admin/v1/kubernetes/nodes",
                "http_method": "POST",
                "operation_id": "list_kubernetes_node",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
                "region": {
                    "location": "query",
                    "attribute": "region",
                },
                "zone": {
                    "location": "query",
                    "attribute": "zone",
                },
                "op": {
                    "location": "query",
                    "attribute": "op",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_kubernetes_storage_class_endpoint = _Endpoint(
            settings={
                "response_type": StorageClassList,
                "endpoint_path": "/admin/v1/kubernetes/storageclasses",
                "http_method": "POST",
                "operation_id": "list_kubernetes_storage_class",
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
        self._list_node_groups_endpoint = _Endpoint(
            settings={
                "response_type": List[NodeGroup],
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodeGroups",
                "http_method": "GET",
                "operation_id": "list_node_groups",
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
        self._list_node_pod_endpoint = _Endpoint(
            settings={
                "response_type": List[JsonBody],
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/pods",
                "http_method": "GET",
                "operation_id": "list_node_pod",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
                "type_": {
                    "required": True,
                    "location": "query",
                    "attribute": "type",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_nodes_endpoint = _Endpoint(
            settings={
                "response_type": NodeList,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes",
                "http_method": "GET",
                "operation_id": "list_nodes",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "host_name": {
                    "location": "query",
                    "attribute": "hostName",
                },
                "out_of_topology_range": {
                    "location": "query",
                    "attribute": "outOfTopologyRange",
                },
                "label_key": {
                    "location": "query",
                    "attribute": "labelKey",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_environment_endpoint = _Endpoint(
            settings={
                "response_type": Environment,
                "endpoint_path": "/admin/v1/environments/{environmentName}",
                "http_method": "PATCH",
                "operation_id": "patch_environment",
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
        self._patch_node_group_endpoint = _Endpoint(
            settings={
                "response_type": NodeGroup,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodeGroups/{nodeGroupName}",
                "http_method": "PATCH",
                "operation_id": "patch_node_group",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_group_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeGroupName",
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
        self._preflight_environment_endpoint = _Endpoint(
            settings={
                "response_type": PreflightList,
                "endpoint_path": "/admin/v1/environments/preflight",
                "http_method": "POST",
                "operation_id": "preflight_environment",
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
        self._remove_node_maintenance_mode_endpoint = _Endpoint(
            settings={
                "response_type": JsonBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/maintenance/off",
                "http_method": "PATCH",
                "operation_id": "remove_node_maintenance_mode",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._resubmit_workflow_endpoint = _Endpoint(
            settings={
                "response_type": Workflow,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow/{workflowName}/resubmit",
                "http_method": "POST",
                "operation_id": "resubmit_workflow",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "workflow_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "workflowName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._retry_workflow_endpoint = _Endpoint(
            settings={
                "response_type": Workflow,
                "endpoint_path": "/admin/v1/environments/{environmentName}/workflow/{workflowName}/retry",
                "http_method": "POST",
                "operation_id": "retry_workflow",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "workflow_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "workflowName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._scale_down_environment_nodes_endpoint = _Endpoint(
            settings={
                "response_type": Task,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/scalein",
                "http_method": "POST",
                "operation_id": "scale_down_environment_nodes",
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
        self._scale_out_environment_nodes_endpoint = _Endpoint(
            settings={
                "response_type": Task,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/scaleout",
                "http_method": "POST",
                "operation_id": "scale_out_environment_nodes",
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
        self._set_node_maintenance_mode_endpoint = _Endpoint(
            settings={
                "response_type": JsonBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/maintenance/on",
                "http_method": "PATCH",
                "operation_id": "set_node_maintenance_mode",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._uncordon_environment_node_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/environments/{environmentName}/nodes/{nodeName}/uncordon",
                "http_method": "PATCH",
                "operation_id": "uncordon_environment_node",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
                },
                "node_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "nodeName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_environment_kubeconfig_endpoint = _Endpoint(
            settings={
                "response_type": HttpBody,
                "endpoint_path": "/admin/v1/environments/{environmentName}/kubeconfig",
                "http_method": "POST",
                "operation_id": "update_environment_kubeconfig",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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
        self._update_environment_module_endpoint = _Endpoint(
            settings={
                "response_type": Workflow,
                "endpoint_path": "/admin/v1/environments/{environmentName}/modules",
                "http_method": "PATCH",
                "operation_id": "update_environment_module",
            },
            params_map={
                "environment_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "environmentName",
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


    def add_nodes(
        self,
        environment_name: str,
        body: List[NodePoolNode],
    ) -> List[NodePoolNode]:
        """Add nodes to environment.

        Add nodes to environment
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: List[NodePoolNode]
        :rtype: List[NodePoolNode]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._add_nodes_endpoint.call_with_http_info(**kwargs)

    def check_kubeconfig(
        self,
        *,
        body: Union[str, UnsetType] = unset,
    ) -> HttpBody:
        """check kubeconfig.
        :type body: str, optional
        :rtype: HttpBody
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._check_kubeconfig_endpoint.call_with_http_info(**kwargs)

    def check_node_ssh_config(
        self,
        body: SshConfigCheckRequest,
    ) -> SshConfigCheckResponse:
        """Check nodes ssh config.

        Check ssh config of provided IP addresses
        :type body: SshConfigCheckRequest
        :rtype: SshConfigCheckResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._check_node_ssh_config_endpoint.call_with_http_info(**kwargs)

    def cordon_environment_node(
        self,
        environment_name: str,
        node_name: str,
    ) -> APIErrorResponse:
        """Cordon environment node.

        cordon the specified Environment node
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._cordon_environment_node_endpoint.call_with_http_info(**kwargs)

    def create_environment(
        self,
        body: EnvironmentCreate,
    ) -> Environment:
        """Create environment.
        :type body: EnvironmentCreate
        :rtype: Environment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_environment_endpoint.call_with_http_info(**kwargs)

    def create_node_group(
        self,
        environment_name: str,
        body: NodeGroup,
    ) -> NodeGroup:
        """Create environment node group.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: NodeGroup
        :rtype: NodeGroup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._create_node_group_endpoint.call_with_http_info(**kwargs)

    def create_workflow(
        self,
        environment_name: str,
        *,
        body: Union[WorkflowCreate, UnsetType] = unset,
    ) -> Workflow:
        """create component management workflow, used to upgrade kubeblocks/gemini.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: WorkflowCreate, optional
        :rtype: Workflow
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if body is not unset:
            kwargs["body"] = body
        return self._create_workflow_endpoint.call_with_http_info(**kwargs)

    def delete_environment(
        self,
        environment_name: str,
        *,
        body: Union[EnvironmentDelete, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Delete environment.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: EnvironmentDelete, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if body is not unset:
            kwargs["body"] = body
        return self._delete_environment_endpoint.call_with_http_info(**kwargs)

    def delete_node_group(
        self,
        environment_name: str,
        node_group_name: str,
    ) -> APIErrorResponse:
        """Delete environment node group.
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_group_name: name of the node group
        :type node_group_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_group_name"] = node_group_name
        return self._delete_node_group_endpoint.call_with_http_info(**kwargs)

    def get_environment(
        self,
        environment_name: str,
    ) -> Environment:
        """Get environment.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: Environment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_endpoint.call_with_http_info(**kwargs)

    def get_environment_backup_repo(
        self,
        *,
        body: Union[str, UnsetType] = unset,
    ) -> EnvironmentBackupRepo:
        """get environment backup repo.
        :type body: str, optional
        :rtype: EnvironmentBackupRepo
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._get_environment_backup_repo_endpoint.call_with_http_info(**kwargs)

    def get_environment_bootstrap_manifests(
        self,
        environment_name: str,
    ) -> HttpBody:
        """Get bootstrap manifests of an environment.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: HttpBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_bootstrap_manifests_endpoint.call_with_http_info(**kwargs)

    def get_environment_kubeconfig(
        self,
        environment_name: str,
    ) -> HttpBody:
        """Get environment kubeconfig.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: HttpBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_kubeconfig_endpoint.call_with_http_info(**kwargs)

    def get_environment_metrics_monitor_stats(
        self,
        environment_name: str,
    ) -> JsonBody:
        """Get environment MetricsMonitorStats.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: JsonBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_metrics_monitor_stats_endpoint.call_with_http_info(**kwargs)

    def get_environment_module_details(
        self,
        environment_name: str,
        module_name: str,
    ) -> EnvironmentModuleDetails:
        """Get details information for an environment module.
        :param environment_name: Environment Name
        :type environment_name: str
        :param module_name: Environment module name
        :type module_name: str
        :rtype: EnvironmentModuleDetails
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["module_name"] = module_name
        return self._get_environment_module_details_endpoint.call_with_http_info(**kwargs)

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

    def get_environment_module_logs(
        self,
        environment_name: str,
        module_name: str,
        pod_name: str,
        *,
        container_name: Union[str, UnsetType] = unset,
        since_seconds: Union[int, UnsetType] = unset,
        since_time: Union[datetime, UnsetType] = unset,
        tail_lines: Union[int, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        previous: Union[bool, UnsetType] = unset,
    ) -> EnvironmentModuleLogs:
        """Get logs for an environment module pod. When no parameters other than containerName and search are provided, start streaming logs in real-time..
        :param environment_name: Environment Name
        :type environment_name: str
        :param module_name: Environment module name
        :type module_name: str
        :param pod_name: Pod name
        :type pod_name: str
        :param container_name: Container name
        :type container_name: str, optional
        :param since_seconds: Get logs from the last n seconds
        :type since_seconds: int, optional
        :param since_time: Get logs since this time (RFC3339 format)
        :type since_time: datetime, optional
        :param tail_lines: Number of lines to return from the end
        :type tail_lines: int, optional
        :param search: Search keyword in logs
        :type search: str, optional
        :param previous: Get previous terminated container logs
        :type previous: bool, optional
        :rtype: EnvironmentModuleLogs
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["module_name"] = module_name
        kwargs["pod_name"] = pod_name
        if container_name is not unset:
            kwargs["container_name"] = container_name
        if since_seconds is not unset:
            kwargs["since_seconds"] = since_seconds
        if since_time is not unset:
            kwargs["since_time"] = since_time
        if tail_lines is not unset:
            kwargs["tail_lines"] = tail_lines
        if search is not unset:
            kwargs["search"] = search
        if previous is not unset:
            kwargs["previous"] = previous
        return self._get_environment_module_logs_endpoint.call_with_http_info(**kwargs)

    def get_environment_provisioning_progress(
        self,
        environment_name: str,
    ) -> JsonBody:
        """Get environment provisioning progress.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: JsonBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_provisioning_progress_endpoint.call_with_http_info(**kwargs)

    def get_environment_status(
        self,
        environment_name: str,
    ) -> EnvironmentStatus:
        """Get environment status.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: EnvironmentStatus
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_environment_status_endpoint.call_with_http_info(**kwargs)

    def get_environment_status_history(
        self,
        environment_name: str,
        *,
        start_time: Union[datetime, UnsetType] = unset,
        end_time: Union[datetime, UnsetType] = unset,
    ) -> List[EnvironmentStatusHistory]:
        """Get environment status history.
        :param environment_name: name of the environment
        :type environment_name: str
        :param start_time: start time of the query range (nano seconds)
        :type start_time: datetime, optional
        :param end_time: end time of the query range(nano seconds)
        :type end_time: datetime, optional
        :rtype: List[EnvironmentStatusHistory]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if start_time is not unset:
            kwargs["start_time"] = start_time
        if end_time is not unset:
            kwargs["end_time"] = end_time
        return self._get_environment_status_history_endpoint.call_with_http_info(**kwargs)

    def get_latest_env_module_version(
        self,
    ) -> EnvModuleVersion:
        """Get environment module latest version.
        :rtype: EnvModuleVersion
        """
        kwargs: Dict[str, Any] = {}
        return self._get_latest_env_module_version_endpoint.call_with_http_info(**kwargs)

    def get_node(
        self,
        environment_name: str,
        node_name: str,
    ) -> JsonBody:
        """Get node info.

        Get specified node info for environment
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :rtype: JsonBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._get_node_endpoint.call_with_http_info(**kwargs)

    def get_optional_environment_modules(
        self,
    ) -> List[EnvironmentModule]:
        """get option environment module info.
        :rtype: List[EnvironmentModule]
        """
        kwargs: Dict[str, Any] = {}
        return self._get_optional_environment_modules_endpoint.call_with_http_info(**kwargs)

    def get_workflow(
        self,
        environment_name: str,
        workflow_name: str,
    ) -> Workflow:
        """Get component management workflows.
        :param environment_name: name of the environment
        :type environment_name: str
        :param workflow_name: workflow name
        :type workflow_name: str
        :rtype: Workflow
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["workflow_name"] = workflow_name
        return self._get_workflow_endpoint.call_with_http_info(**kwargs)

    def get_workflow_list(
        self,
        environment_name: str,
    ) -> WorkflowList:
        """Get component management workflow list.
        :param environment_name: name of the environment
        :type environment_name: str
        :rtype: WorkflowList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._get_workflow_list_endpoint.call_with_http_info(**kwargs)

    def get_workflow_log(
        self,
        environment_name: str,
        workflow_name: str,
    ) -> str:
        """Get component management workflow log.
        :param environment_name: name of the environment
        :type environment_name: str
        :param workflow_name: workflow name
        :type workflow_name: str
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["workflow_name"] = workflow_name
        return self._get_workflow_log_endpoint.call_with_http_info(**kwargs)

    def list_env_node_zone(
        self,
        environment_name: str,
    ) -> List[str]:
        """List the availability zones where the environment's nodes are located.

        List available zones of an environment
        :param environment_name: name of the Environment
        :type environment_name: str
        :rtype: List[str]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        return self._list_env_node_zone_endpoint.call_with_http_info(**kwargs)

    def list_environment(
        self,
        *,
        org_name: Union[str, UnsetType] = unset,
        cloud_provider: Union[str, UnsetType] = unset,
        cloud_region: Union[str, UnsetType] = unset,
        environment_type: Union[EnvironmentType, UnsetType] = unset,
        engine: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
    ) -> EnvironmentList:
        """List environments.

        List environments
        :param org_name: name of the Org
        :type org_name: str, optional
        :param cloud_provider: cloud provider of the Environment
        :type cloud_provider: str, optional
        :param cloud_region: cloud region of the Environment
        :type cloud_region: str, optional
        :param environment_type: type of the Environment
        :type environment_type: EnvironmentType, optional
        :param engine: engine name
        :type engine: str, optional
        :param version: version of the engine
        :type version: str, optional
        :rtype: EnvironmentList
        """
        kwargs: Dict[str, Any] = {}
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if cloud_provider is not unset:
            kwargs["cloud_provider"] = cloud_provider
        if cloud_region is not unset:
            kwargs["cloud_region"] = cloud_region
        if environment_type is not unset:
            kwargs["environment_type"] = environment_type
        if engine is not unset:
            kwargs["engine"] = engine
        if version is not unset:
            kwargs["version"] = version
        return self._list_environment_endpoint.call_with_http_info(**kwargs)

    def list_environment_object_storage(
        self,
        *,
        body: Union[str, UnsetType] = unset,
    ) -> EnvironmentObjectStorage:
        """List environment object storage.

        List environment object storage
        :type body: str, optional
        :rtype: EnvironmentObjectStorage
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._list_environment_object_storage_endpoint.call_with_http_info(**kwargs)

    def list_kubernetes_node(
        self,
        body: Kubeconfig,
        *,
        region: Union[str, UnsetType] = unset,
        zone: Union[str, UnsetType] = unset,
        op: Union[ListKubernetesNodeOpType, UnsetType] = unset,
    ) -> NodeList:
        """List Kubernetes nodes.

        List Kubernetes nodes before registered as environment
        :type body: Kubeconfig
        :param region: region of Kubernetes node
        :type region: str, optional
        :param zone: zone of Kubernetes node
        :type zone: str, optional
        :param op: operation of this query, either in or notin
        :type op: ListKubernetesNodeOpType, optional
        :rtype: NodeList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        if region is not unset:
            kwargs["region"] = region
        if zone is not unset:
            kwargs["zone"] = zone
        if op is not unset:
            kwargs["op"] = op
        return self._list_kubernetes_node_endpoint.call_with_http_info(**kwargs)

    def list_kubernetes_storage_class(
        self,
        body: Kubeconfig,
    ) -> StorageClassList:
        """List Kubernetes storageclass.

        List Kubernetes storageclass before registered as environment
        :type body: Kubeconfig
        :rtype: StorageClassList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._list_kubernetes_storage_class_endpoint.call_with_http_info(**kwargs)

    def list_node_groups(
        self,
        environment_name: str,
        *,
        zones: Union[List[str], UnsetType] = unset,
    ) -> List[NodeGroup]:
        """List environment node groups.
        :param environment_name: name of the environment
        :type environment_name: str
        :param zones: available zones for filtering node groups
        :type zones: List[str], optional
        :rtype: List[NodeGroup]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if zones is not unset:
            kwargs["zones"] = zones
        return self._list_node_groups_endpoint.call_with_http_info(**kwargs)

    def list_node_pod(
        self,
        environment_name: str,
        node_name: str,
        type_: str,
    ) -> List[JsonBody]:
        """List Pod in the environment node.

        List Pod in the environment node
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :param type_: filter Pods by type, supported types [all, kube-system, kb-system, cluster], default all if not provided
        :type type_: str
        :rtype: List[JsonBody]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        kwargs["type_"] = type_
        return self._list_node_pod_endpoint.call_with_http_info(**kwargs)

    def list_nodes(
        self,
        environment_name: str,
        *,
        host_name: Union[str, UnsetType] = unset,
        out_of_topology_range: Union[bool, UnsetType] = unset,
        label_key: Union[str, UnsetType] = unset,
    ) -> NodeList:
        """List Kubernetes nodes in an environment.

        List Kubernetes nodes in an environment
        :param environment_name: name of the environment
        :type environment_name: str
        :param host_name: Hostname to filter by
        :type host_name: str, optional
        :param out_of_topology_range: List nodes with invalid region & zone labels
        :type out_of_topology_range: bool, optional
        :param label_key: List nodes with label
        :type label_key: str, optional
        :rtype: NodeList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if host_name is not unset:
            kwargs["host_name"] = host_name
        if out_of_topology_range is not unset:
            kwargs["out_of_topology_range"] = out_of_topology_range
        if label_key is not unset:
            kwargs["label_key"] = label_key
        return self._list_nodes_endpoint.call_with_http_info(**kwargs)

    def patch_environment(
        self,
        environment_name: str,
        body: EnvironmentUpdate,
    ) -> Environment:
        """Update environment.

        partially update the specified Environment
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: EnvironmentUpdate
        :rtype: Environment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._patch_environment_endpoint.call_with_http_info(**kwargs)

    def patch_node_group(
        self,
        environment_name: str,
        node_group_name: str,
        body: NodeGroupUpdate,
    ) -> NodeGroup:
        """Patch node group.

        partially update the specified NodeGroup
        :param environment_name: name of the NodeGroup
        :type environment_name: str
        :param node_group_name: name of the node group
        :type node_group_name: str
        :type body: NodeGroupUpdate
        :rtype: NodeGroup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_group_name"] = node_group_name
        kwargs["body"] = body
        return self._patch_node_group_endpoint.call_with_http_info(**kwargs)

    def preflight_environment(
        self,
        body: Kubeconfig,
    ) -> PreflightList:
        """Preflight check before create Environment.
        :type body: Kubeconfig
        :rtype: PreflightList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._preflight_environment_endpoint.call_with_http_info(**kwargs)

    def remove_node_maintenance_mode(
        self,
        environment_name: str,
        node_name: str,
    ) -> JsonBody:
        """Remove the node from maintenance mode.

        Remove the node from maintenance mode. This action restores the node to its normal operational state, allowing it to resume handling workloads.
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :rtype: JsonBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._remove_node_maintenance_mode_endpoint.call_with_http_info(**kwargs)

    def resubmit_workflow(
        self,
        environment_name: str,
        workflow_name: str,
    ) -> Workflow:
        """retry workflow from failed.
        :param environment_name: name of the environment
        :type environment_name: str
        :param workflow_name: workflow name
        :type workflow_name: str
        :rtype: Workflow
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["workflow_name"] = workflow_name
        return self._resubmit_workflow_endpoint.call_with_http_info(**kwargs)

    def retry_workflow(
        self,
        environment_name: str,
        workflow_name: str,
    ) -> Workflow:
        """retry workflow.
        :param environment_name: name of the environment
        :type environment_name: str
        :param workflow_name: workflow name
        :type workflow_name: str
        :rtype: Workflow
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["workflow_name"] = workflow_name
        return self._retry_workflow_endpoint.call_with_http_info(**kwargs)

    def scale_down_environment_nodes(
        self,
        environment_name: str,
        body: NodeScaleInRequest,
    ) -> Task:
        """Scale in environment nodes.

        Scale in environment by removing nodes using sealos
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: NodeScaleInRequest
        :rtype: Task
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._scale_down_environment_nodes_endpoint.call_with_http_info(**kwargs)

    def scale_out_environment_nodes(
        self,
        environment_name: str,
        body: NodeScaleRequest,
    ) -> Task:
        """Scale out environment nodes.

        Scale out environment by adding new nodes using sealos
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: NodeScaleRequest
        :rtype: Task
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["body"] = body
        return self._scale_out_environment_nodes_endpoint.call_with_http_info(**kwargs)

    def set_node_maintenance_mode(
        self,
        environment_name: str,
        node_name: str,
    ) -> JsonBody:
        """Set the node to maintenance mode.

        Set the node to maintenance mode. This action temporarily disables the node for maintenance activities, ensuring no new workloads are scheduled on it.
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :rtype: JsonBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._set_node_maintenance_mode_endpoint.call_with_http_info(**kwargs)

    def uncordon_environment_node(
        self,
        environment_name: str,
        node_name: str,
    ) -> APIErrorResponse:
        """Cordon environment node.

        cordon the specified Environment node
        :param environment_name: name of the environment
        :type environment_name: str
        :param node_name: name of the environment node
        :type node_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        kwargs["node_name"] = node_name
        return self._uncordon_environment_node_endpoint.call_with_http_info(**kwargs)

    def update_environment_kubeconfig(
        self,
        environment_name: str,
        *,
        body: Union[str, UnsetType] = unset,
    ) -> HttpBody:
        """update environment kubeconfig.
        :param environment_name: name of the environment
        :type environment_name: str
        :type body: str, optional
        :rtype: HttpBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if body is not unset:
            kwargs["body"] = body
        return self._update_environment_kubeconfig_endpoint.call_with_http_info(**kwargs)

    def update_environment_module(
        self,
        environment_name: str,
        *,
        body: Union[EnvironmentModuleUpdate, UnsetType] = unset,
    ) -> Workflow:
        """update environment module.
        :param environment_name: Environment Name
        :type environment_name: str
        :type body: EnvironmentModuleUpdate, optional
        :rtype: Workflow
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_name"] = environment_name
        if body is not unset:
            kwargs["body"] = body
        return self._update_environment_module_endpoint.call_with_http_info(**kwargs)
