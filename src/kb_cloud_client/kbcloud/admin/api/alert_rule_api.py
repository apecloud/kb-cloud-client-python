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


class AlertruleApi:
    """AlertRule API client.

    Provides methods for the alertRule endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": AlertRule,
                "endpoint_path": "/admin/v1/alerts/rules",
                "http_method": "POST",
                "operation_id": "create_alert_rule",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
                "disabled": {
                    "location": "query",
                    "attribute": "disabled",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self._delete_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/alerts/rules/{alertName}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_rule",
            },
            params_map={
                "alert_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "alertName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._download_org_alert_rule_file_endpoint = _Endpoint(
            settings={
                "response_type": bytes,
                "endpoint_path": "/admin/v1/alerts/rules/download",
                "http_method": "GET",
                "operation_id": "download_org_alert_rule_file",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/x-yaml", "application/json"],
            },
            api_client=api_client,
        )
        self._get_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": AlertRule,
                "endpoint_path": "/admin/v1/alerts/rules/{alertName}",
                "http_method": "GET",
                "operation_id": "get_alert_rule",
            },
            params_map={
                "alert_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "alertName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_rules_endpoint = _Endpoint(
            settings={
                "response_type": AlertRuleList,
                "endpoint_path": "/admin/v1/alerts/rules",
                "http_method": "GET",
                "operation_id": "list_alert_rules",
            },
            params_map={
                "disabled": {
                    "location": "query",
                    "attribute": "disabled",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._restore_org_alert_rule_to_default_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/admin/v1/alerts/rules/reset",
                "http_method": "POST",
                "operation_id": "restore_org_alert_rule_to_default",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": AlertRule,
                "endpoint_path": "/admin/v1/alerts/rules",
                "http_method": "PATCH",
                "operation_id": "update_alert_rule",
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
        self._update_rule_config_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/alerts/rules/upload",
                "http_method": "PUT",
                "operation_id": "update_rule_config",
            },
            params_map={
                "content": {
                    "location": "form",
                    "attribute": "content",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": ["multipart/form-data"],
            },
            api_client=api_client,
        )


    def create_alert_rule(
        self,
        body: AlertRule,
        *,
        disabled: Union[bool, UnsetType] = unset,
    ) -> AlertRule:
        """Create alert rule.
        :type body: AlertRule
        :param disabled: disabled status
        :type disabled: bool, optional
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        if disabled is not unset:
            kwargs["disabled"] = disabled
        return self._create_alert_rule_endpoint.call_with_http_info(**kwargs)

    def delete_alert_rule(
        self,
        alert_name: str,
    ) -> APIErrorResponse:
        """Delete alert rule.
        :param alert_name: name of the alert rule
        :type alert_name: str
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["alert_name"] = alert_name
        return self._delete_alert_rule_endpoint.call_with_http_info(**kwargs)

    def download_org_alert_rule_file(
        self,
    ) -> bytes:
        """Download organization-specific alert rule configuration file.

        Downloads the current alert rule configuration for a specific organization as a YAML file.
        :rtype: bytes
        """
        kwargs: Dict[str, Any] = {}
        return self._download_org_alert_rule_file_endpoint.call_with_http_info(**kwargs)

    def get_alert_rule(
        self,
        alert_name: str,
    ) -> AlertRule:
        """Get alert rule.
        :param alert_name: name of the alert rule
        :type alert_name: str
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["alert_name"] = alert_name
        return self._get_alert_rule_endpoint.call_with_http_info(**kwargs)

    def list_alert_rules(
        self,
        *,
        disabled: Union[bool, UnsetType] = unset,
    ) -> AlertRuleList:
        """List alert rules.
        :param disabled: disabled status
        :type disabled: bool, optional
        :rtype: AlertRuleList
        """
        kwargs: Dict[str, Any] = {}
        if disabled is not unset:
            kwargs["disabled"] = disabled
        return self._list_alert_rules_endpoint.call_with_http_info(**kwargs)

    def restore_org_alert_rule_to_default(
        self,
    ) -> Dict[str, Any]:
        """Restore organization's alert rule configuration to defaults.

        Restores the alert rule configuration for a specific organization to the system default settings.
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        return self._restore_org_alert_rule_to_default_endpoint.call_with_http_info(**kwargs)

    def update_alert_rule(
        self,
        body: AlertRule,
    ) -> AlertRule:
        """updateAlertRule.
        :type body: AlertRule
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        return self._update_alert_rule_endpoint.call_with_http_info(**kwargs)

    def update_rule_config(
        self,
        *,
        content: Union[bytes, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Update alert rule configuration via YAML upload.

        Replaces the entire alert rule configuration with the content of the uploaded YAML file.
        :param content: YAML file content containing the new alert rule configuration
        :type content: bytes, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        if content is not unset:
            kwargs["content"] = content
        return self._update_rule_config_endpoint.call_with_http_info(**kwargs)
