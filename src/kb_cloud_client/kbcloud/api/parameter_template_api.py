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


class ParametertemplateApi:
    """ParameterTemplate API client.

    Provides methods for the parameterTemplate endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": ParamTplListItem,
                "endpoint_path": "/api/v1/organizations/{orgName}/parameterTemplates",
                "http_method": "POST",
                "operation_id": "create_parameter_template",
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
        self._delete_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/parameterTemplate/{parameterTemplateName}",
                "http_method": "DELETE",
                "operation_id": "delete_parameter_template",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "parameter_template_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "parameterTemplateName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._export_parameter_template_from_cluster_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate",
                "http_method": "POST",
                "operation_id": "export_parameter_template_from_cluster",
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
        self._get_cluster_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": ParamTplApplyToClusterList,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate",
                "http_method": "GET",
                "operation_id": "get_cluster_parameter_template",
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
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
                "engine_name": {
                    "location": "query",
                    "attribute": "engineName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_parameter_templates_endpoint = _Endpoint(
            settings={
                "response_type": ParamTplList,
                "endpoint_path": "/api/v1/organizations/{orgName}/parameterTemplates",
                "http_method": "GET",
                "operation_id": "list_parameter_templates",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "partition": {
                    "location": "query",
                    "attribute": "partition",
                },
                "version": {
                    "location": "query",
                    "attribute": "version",
                },
                "component": {
                    "location": "query",
                    "attribute": "component",
                },
                "engine_name": {
                    "location": "query",
                    "attribute": "engineName",
                },
                "engine_mode": {
                    "location": "query",
                    "attribute": "engineMode",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": ParamTplListItem,
                "endpoint_path": "/api/v1/organizations/{orgName}/parameterTemplate/{parameterTemplateName}",
                "http_method": "PATCH",
                "operation_id": "patch_parameter_template",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "parameter_template_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "parameterTemplateName",
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
        self._read_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": ParameterList,
                "endpoint_path": "/api/v1/organizations/{orgName}/parameterTemplate/{parameterTemplateName}",
                "http_method": "GET",
                "operation_id": "read_parameter_template",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "parameter_template_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "parameterTemplateName",
                },
                "partition": {
                    "location": "query",
                    "attribute": "partition",
                },
                "raw_content": {
                    "location": "query",
                    "attribute": "rawContent",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_cluster_parameter_template_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate",
                "http_method": "PATCH",
                "operation_id": "update_cluster_parameter_template",
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
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )


    def create_parameter_template(
        self,
        org_name: str,
        body: ParamTplCreate,
    ) -> ParamTplListItem:
        """Create parameter template.
        :param org_name: name of the Org
        :type org_name: str
        :type body: ParamTplCreate
        :rtype: ParamTplListItem
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_parameter_template_endpoint.call_with_http_info(**kwargs)

    def delete_parameter_template(
        self,
        org_name: str,
        parameter_template_name: str,
    ) -> APIErrorResponse:
        """Delete parameter template.
        :param org_name: name of the Org
        :type org_name: str
        :param parameter_template_name: name of the parameter template
        :type parameter_template_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["parameter_template_name"] = parameter_template_name
        return self._delete_parameter_template_endpoint.call_with_http_info(**kwargs)

    def export_parameter_template_from_cluster(
        self,
        org_name: str,
        cluster_name: str,
        body: ParamTplCreateFromCluster,
    ) -> APIErrorResponse:
        """Export parameter template from cluster.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: ParamTplCreateFromCluster
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._export_parameter_template_from_cluster_endpoint.call_with_http_info(**kwargs)

    def get_cluster_parameter_template(
        self,
        org_name: str,
        cluster_name: str,
        *,
        component: Union[str, UnsetType] = unset,
        engine_name: Union[str, UnsetType] = unset,
    ) -> ParamTplApplyToClusterList:
        """Get cluster parameter template.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :param component: component type
        :type component: str, optional
        :param engine_name: engine name
        :type engine_name: str, optional
        :rtype: ParamTplApplyToClusterList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        if component is not unset:
            kwargs["component"] = component
        if engine_name is not unset:
            kwargs["engine_name"] = engine_name
        return self._get_cluster_parameter_template_endpoint.call_with_http_info(**kwargs)

    def list_parameter_templates(
        self,
        org_name: str,
        *,
        partition: Union[ParameterTemplatePartition, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        component: Union[str, UnsetType] = unset,
        engine_name: Union[str, UnsetType] = unset,
        engine_mode: Union[str, UnsetType] = unset,
    ) -> ParamTplList:
        """List parameter templates in an Org.
        :param org_name: name of the Org
        :type org_name: str
        :param partition: the template partition in listParamTpl request
        :type partition: ParameterTemplatePartition, optional
        :param version: Cluster Application Version
        :type version: str, optional
        :param component: component type
        :type component: str, optional
        :param engine_name: engine Name
        :type engine_name: str, optional
        :param engine_mode: engine mode
        :type engine_mode: str, optional
        :rtype: ParamTplList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if partition is not unset:
            kwargs["partition"] = partition
        if version is not unset:
            kwargs["version"] = version
        if component is not unset:
            kwargs["component"] = component
        if engine_name is not unset:
            kwargs["engine_name"] = engine_name
        if engine_mode is not unset:
            kwargs["engine_mode"] = engine_mode
        return self._list_parameter_templates_endpoint.call_with_http_info(**kwargs)

    def patch_parameter_template(
        self,
        org_name: str,
        parameter_template_name: str,
        body: ParamTplUpdate,
    ) -> ParamTplListItem:
        """Update parameter template.
        :param org_name: name of the Org
        :type org_name: str
        :param parameter_template_name: name of the parameter template
        :type parameter_template_name: str
        :type body: ParamTplUpdate
        :rtype: ParamTplListItem
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["parameter_template_name"] = parameter_template_name
        kwargs["body"] = body
        return self._patch_parameter_template_endpoint.call_with_http_info(**kwargs)

    def read_parameter_template(
        self,
        org_name: str,
        parameter_template_name: str,
        *,
        partition: Union[ParameterTemplatePartition, UnsetType] = unset,
        raw_content: Union[bool, UnsetType] = unset,
    ) -> ParameterList:
        """Get parameter template details.
        :param org_name: name of the Org
        :type org_name: str
        :param parameter_template_name: name of the parameter template
        :type parameter_template_name: str
        :param partition: the template partition in read paramTpl request
        :type partition: ParameterTemplatePartition, optional
        :param raw_content: whether to return the raw template content
        :type raw_content: bool, optional
        :rtype: ParameterList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["parameter_template_name"] = parameter_template_name
        if partition is not unset:
            kwargs["partition"] = partition
        if raw_content is not unset:
            kwargs["raw_content"] = raw_content
        return self._read_parameter_template_endpoint.call_with_http_info(**kwargs)

    def update_cluster_parameter_template(
        self,
        org_name: str,
        cluster_name: str,
        body: List[ParamTplsItem],
    ) -> APIErrorResponse:
        """Update cluster parameter template.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster_name: name of the cluster
        :type cluster_name: str
        :type body: List[ParamTplsItem]
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["cluster_name"] = cluster_name
        kwargs["body"] = body
        return self._update_cluster_parameter_template_endpoint.call_with_http_info(**kwargs)
