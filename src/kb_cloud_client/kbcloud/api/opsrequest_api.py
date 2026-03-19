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


class OpsrequestApi:
    """Opsrequest API client.

    Provides methods for the opsrequest endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._cancel_ops_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/opsrequests/{opsName}/cancel",
                "http_method": "POST",
                "operation_id": "cancel_ops",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "ops_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "opsName",
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
        self._cluster_volume_expand_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/volume-expand",
                "http_method": "POST",
                "operation_id": "cluster_volume_expand",
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
        self._custom_ops_endpoint = _Endpoint(
            settings={
                "response_type": ClusterTask,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/custom-ops",
                "http_method": "POST",
                "operation_id": "custom_ops",
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
        self._expose_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/expose",
                "http_method": "POST",
                "operation_id": "expose_cluster",
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
        self._horizontal_scale_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/hscale",
                "http_method": "POST",
                "operation_id": "horizontal_scale_cluster",
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
        self._list_available_nodes_endpoint = _Endpoint(
            settings={
                "response_type": NodeList,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/rebuildInstance/availableNodes",
                "http_method": "GET",
                "operation_id": "list_available_nodes",
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
                "name": {
                    "required": True,
                    "location": "query",
                    "attribute": "name",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._promote_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/promote",
                "http_method": "POST",
                "operation_id": "promote_cluster",
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
        self._rebuild_instance_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/rebuildInstance",
                "http_method": "POST",
                "operation_id": "rebuild_instance",
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
        self._reconfigure_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/reconfigure",
                "http_method": "POST",
                "operation_id": "reconfigure_cluster",
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
        self._restart_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/restart",
                "http_method": "POST",
                "operation_id": "restart_cluster",
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
        self._specify_cluster_io_quotas_endpoint = _Endpoint(
            settings={
                "response_type": OpsIoQuotas,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/volumes/io-quotas",
                "http_method": "POST",
                "operation_id": "specify_cluster_io_quotas",
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
        self._start_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/start",
                "http_method": "POST",
                "operation_id": "start_cluster",
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
        self._stop_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/stop",
                "http_method": "POST",
                "operation_id": "stop_cluster",
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
        self._update_cluster_license_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/updateLicense",
                "http_method": "POST",
                "operation_id": "update_cluster_license",
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
        self._upgrade_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/upgrade",
                "http_method": "POST",
                "operation_id": "upgrade_cluster",
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
        self._vertical_scale_cluster_endpoint = _Endpoint(
            settings={
                "response_type": OpsRequestName,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/vscale",
                "http_method": "POST",
                "operation_id": "vertical_scale_cluster",
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


    def cancel_ops(
        self,
        org_name: str,
        ops_name: str,
        cluster_name: str,
    ) -> APIErrorResponse:
        """Cancel OpsRequest.

        cancel a OpsRequest
        :param org_name: name of the Org
        :type org_name: str
        :param ops_name: name of the OpsRequest
        :type ops_name: str
        :param cluster_name: name of the Cluster
        :type cluster_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["ops_name"] = ops_name
        kwargs["cluster_name"] = cluster_name
        return self._cancel_ops_endpoint.call_with_http_info(**kwargs)

    def cluster_volume_expand(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsVolumeExpand,
    ) -> OpsRequestName:
        """Expand cluster volume size.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsVolumeExpand
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._cluster_volume_expand_endpoint.call_with_http_info(**kwargs)

    def custom_ops(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsCustom,
    ) -> ClusterTask:
        """Create custom OpsRequest.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsCustom
        :rtype: ClusterTask
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._custom_ops_endpoint.call_with_http_info(**kwargs)

    def expose_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsExpose,
    ) -> OpsRequestName:
        """Expose cluster loadbalancer endpoint.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsExpose
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._expose_cluster_endpoint.call_with_http_info(**kwargs)

    def horizontal_scale_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsHScale,
    ) -> OpsRequestName:
        """Horizontal scale cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsHScale
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._horizontal_scale_cluster_endpoint.call_with_http_info(**kwargs)

    def list_available_nodes(
        self,
        org_name: str,
        cluster_name: str,
        name: str,
    ) -> NodeList:
        """List available nodes for rebuilding instance.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :param name: name of the instance to be rebuilt
        :type name: str
        :rtype: NodeList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["name"] = name
        return self._list_available_nodes_endpoint.call_with_http_info(**kwargs)

    def promote_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsPromote,
    ) -> OpsRequestName:
        """Promote cluster intance to primary.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsPromote
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._promote_cluster_endpoint.call_with_http_info(**kwargs)

    def rebuild_instance(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsRebuildInstance,
    ) -> OpsRequestName:
        """rebuild the instance.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsRebuildInstance
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._rebuild_instance_endpoint.call_with_http_info(**kwargs)

    def reconfigure_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: ReconfigureCreate,
    ) -> OpsRequestName:
        """Update cluster configuration.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: ReconfigureCreate
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._reconfigure_cluster_endpoint.call_with_http_info(**kwargs)

    def restart_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsRestart,
    ) -> OpsRequestName:
        """Restart cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsRestart
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._restart_cluster_endpoint.call_with_http_info(**kwargs)

    def specify_cluster_io_quotas(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsIoQuotas,
    ) -> OpsIoQuotas:
        """Specify IOPS and BPS of cluster volumes.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsIoQuotas
        :rtype: OpsIoQuotas
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._specify_cluster_io_quotas_endpoint.call_with_http_info(**kwargs)

    def start_cluster(
        self,
        org_name: str,
        cluster_name: str,
    ) -> OpsRequestName:
        """Start cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._start_cluster_endpoint.call_with_http_info(**kwargs)

    def stop_cluster(
        self,
        org_name: str,
        cluster_name: str,
    ) -> OpsRequestName:
        """Stop cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        return self._stop_cluster_endpoint.call_with_http_info(**kwargs)

    def update_cluster_license(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsLicense,
    ) -> OpsRequestName:
        """Update the cluster license.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsLicense
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._update_cluster_license_endpoint.call_with_http_info(**kwargs)

    def upgrade_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsUpgrade,
    ) -> OpsRequestName:
        """Upgrade cluster version.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsUpgrade
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._upgrade_cluster_endpoint.call_with_http_info(**kwargs)

    def vertical_scale_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: OpsVScale,
    ) -> OpsRequestName:
        """Vertical scale cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the KubeBlocks cluster
        :type cluster_name: str
        :type body: OpsVScale
        :rtype: OpsRequestName
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._vertical_scale_cluster_endpoint.call_with_http_info(**kwargs)
