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


class AlerttemplateApi:
    """AlertTemplate API client.

    Provides methods for the alertTemplate endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_alert_template_endpoint = _Endpoint(
            settings={
                "response_type": AlertTemplate,
                "endpoint_path": "/admin/v1/alertTemplates",
                "http_method": "POST",
                "operation_id": "create_alert_template",
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
        self._delete_alert_template_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/alertTemplates/{templateId}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_template",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "templateId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._get_alert_template_endpoint = _Endpoint(
            settings={
                "response_type": AlertTemplate,
                "endpoint_path": "/admin/v1/alertTemplates/{templateId}",
                "http_method": "GET",
                "operation_id": "get_alert_template",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "templateId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_templates_endpoint = _Endpoint(
            settings={
                "response_type": AlertTemplateList,
                "endpoint_path": "/admin/v1/alertTemplates",
                "http_method": "GET",
                "operation_id": "list_alert_templates",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._patch_alert_template_endpoint = _Endpoint(
            settings={
                "response_type": AlertTemplate,
                "endpoint_path": "/admin/v1/alertTemplates/{templateId}",
                "http_method": "PATCH",
                "operation_id": "patch_alert_template",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "templateId",
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


    def create_alert_template(
        self,
        body: AlertTemplate,
    ) -> AlertTemplate:
        """Create alert template.
        :type body: AlertTemplate
        :rtype: AlertTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._create_alert_template_endpoint.call_with_http_info(**kwargs)

    def delete_alert_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """Delete alert template.
        :param template_id: id of the alert tmpl configuration
        :type template_id: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id
        return self._delete_alert_template_endpoint.call_with_http_info(**kwargs)

    def get_alert_template(
        self,
        template_id: str,
    ) -> AlertTemplate:
        """Get alert template.
        :param template_id: id of the alert tmpl configuration
        :type template_id: str
        :rtype: AlertTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id
        return self._get_alert_template_endpoint.call_with_http_info(**kwargs)

    def list_alert_templates(
        self,
    ) -> AlertTemplateList:
        """List alert templates.
        :rtype: AlertTemplateList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_alert_templates_endpoint.call_with_http_info(**kwargs)

    def patch_alert_template(
        self,
        template_id: str,
        body: AlertTemplate,
    ) -> AlertTemplate:
        """Update alert template.

        partially update the alert receiver
        :param template_id: id of the alert tmpl configuration
        :type template_id: str
        :type body: AlertTemplate
        :rtype: AlertTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id
        kwargs["body"] = body
        return self._patch_alert_template_endpoint.call_with_http_info(**kwargs)
