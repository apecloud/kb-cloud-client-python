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
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules",
                "http_method": "POST",
                "operation_id": "create_alert_rule",
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
        self._delete_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/{alertName}",
                "http_method": "DELETE",
                "operation_id": "delete_alert_rule",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/config",
                "http_method": "GET",
                "operation_id": "download_org_alert_rule_file",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/x-yaml", "application/json"],
            },
            api_client=api_client,
        )
        self._get_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": AlertRule,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/{alertName}",
                "http_method": "GET",
                "operation_id": "get_alert_rule",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "alert_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "alertName",
                },
            },
            headers_map={
                "accept": ["*/*", "application/json"],
            },
            api_client=api_client,
        )
        self._list_alert_rules_endpoint = _Endpoint(
            settings={
                "response_type": AlertRuleList,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules",
                "http_method": "GET",
                "operation_id": "list_alert_rules",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/config/restore",
                "http_method": "POST",
                "operation_id": "restore_org_alert_rule_to_default",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_alert_rule_endpoint = _Endpoint(
            settings={
                "response_type": AlertRule,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/{alertName}",
                "http_method": "PATCH",
                "operation_id": "update_alert_rule",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "alert_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "alertName",
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
        self._update_rule_config_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/api/v1/organizations/{orgName}/alerts/rules/config",
                "http_method": "PUT",
                "operation_id": "update_rule_config",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
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
        org_name: str,
        body: AlertRule,
    ) -> AlertRule:
        """Create alert rule.
        :param org_name: name of the Org
        :type org_name: str
        :type body: AlertRule
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_alert_rule_endpoint.call_with_http_info(**kwargs)

    def delete_alert_rule(
        self,
        org_name: str,
        alert_name: str,
    ) -> Dict[str, Any]:
        """Delete alert rule.
        :param org_name: name of the Org
        :type org_name: str
        :param alert_name: id of the alert rules
        :type alert_name: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["alert_name"] = alert_name
        return self._delete_alert_rule_endpoint.call_with_http_info(**kwargs)

    def download_org_alert_rule_file(
        self,
        org_name: str,
    ) -> bytes:
        """Download organization-specific alert rule configuration file.

        Downloads the current alert rule configuration for a specific organization as a YAML file.
        :param org_name: The name of the organization.
        :type org_name: str
        :rtype: bytes
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._download_org_alert_rule_file_endpoint.call_with_http_info(**kwargs)

    def get_alert_rule(
        self,
        org_name: str,
        alert_name: str,
    ) -> AlertRule:
        """getAlertRule.
        :param org_name: name of the Org
        :type org_name: str
        :param alert_name: name of the alert
        :type alert_name: str
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["alert_name"] = alert_name
        return self._get_alert_rule_endpoint.call_with_http_info(**kwargs)

    def list_alert_rules(
        self,
        org_name: str,
        *,
        disabled: Union[bool, UnsetType] = unset,
    ) -> AlertRuleList:
        """List alert rules.
        :param org_name: name of the Org
        :type org_name: str
        :param disabled: disabled status
        :type disabled: bool, optional
        :rtype: AlertRuleList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if disabled is not unset:
            kwargs["disabled"] = disabled
        return self._list_alert_rules_endpoint.call_with_http_info(**kwargs)

    def restore_org_alert_rule_to_default(
        self,
        org_name: str,
    ) -> Dict[str, Any]:
        """Restore organization's alert rule configuration to defaults.

        Restores the alert rule configuration for a specific organization to the system default settings.
        :param org_name: The name of the organization.
        :type org_name: str
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        return self._restore_org_alert_rule_to_default_endpoint.call_with_http_info(**kwargs)

    def update_alert_rule(
        self,
        org_name: str,
        alert_name: str,
        body: AlertRule,
    ) -> AlertRule:
        """Update alert rule.
        :param org_name: name of the Org
        :type org_name: str
        :param alert_name: id of the alert rules
        :type alert_name: str
        :type body: AlertRule
        :rtype: AlertRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["alert_name"] = alert_name
        kwargs["body"] = body
        return self._update_alert_rule_endpoint.call_with_http_info(**kwargs)

    def update_rule_config(
        self,
        org_name: str,
        *,
        content: Union[bytes, UnsetType] = unset,
    ) -> APIErrorResponse:
        """Update alert rule configuration via YAML upload.

        Replaces the entire alert rule configuration with the content of the uploaded YAML file.
        :param org_name: The name of the organization.
        :type org_name: str
        :param content: YAML file content containing the new alert rule configuration
        :type content: bytes, optional
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if content is not unset:
            kwargs["content"] = content
        return self._update_rule_config_endpoint.call_with_http_info(**kwargs)
