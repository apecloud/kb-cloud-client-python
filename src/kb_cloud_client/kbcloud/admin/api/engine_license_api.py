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


class EnginelicenseApi:
    """EngineLicense API client.

    Provides methods for the engineLicense endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_engine_license_endpoint = _Endpoint(
            settings={
                "response_type": EngineLicense,
                "endpoint_path": "/admin/v1/engineLicense",
                "http_method": "POST",
                "operation_id": "create_engine_license",
            },
            params_map={
                "body": {
                    "required": True,
                    "location": "body",
                },
                "license_file": {
                    "required": True,
                    "location": "form",
                    "attribute": "licenseFile",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json", "multipart/form-data"],
            },
            api_client=api_client,
        )
        self._delete_engine_license_endpoint = _Endpoint(
            settings={
                "response_type": APIErrorResponse,
                "endpoint_path": "/admin/v1/engineLicense",
                "http_method": "DELETE",
                "operation_id": "delete_engine_license",
            },
            params_map={
                "license_id": {
                    "required": True,
                    "location": "query",
                    "attribute": "licenseId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._engine_license_endpoint = _Endpoint(
            settings={
                "response_type": EngineLicense,
                "endpoint_path": "/admin/v1/engineLicense",
                "http_method": "GET",
                "operation_id": "engine_license",
            },
            params_map={
                "license_id": {
                    "required": True,
                    "location": "query",
                    "attribute": "licenseId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_engine_licenses_endpoint = _Endpoint(
            settings={
                "response_type": EngineLicenseList,
                "endpoint_path": "/admin/v1/engineLicenses",
                "http_method": "GET",
                "operation_id": "list_engine_licenses",
            },
            params_map={
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


    def create_engine_license(
        self,
        body: EngineLicenseCreate,
        license_file: bytes,
    ) -> EngineLicense:
        """Create engineLicense.

        Create a new engineLicense
        :type body: EngineLicenseCreate
        :param license_file: The license file to upload
        :type license_file: bytes
        :rtype: EngineLicense
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body
        kwargs["license_file"] = license_file
        return self._create_engine_license_endpoint.call_with_http_info(**kwargs)

    def delete_engine_license(
        self,
        license_id: int,
    ) -> APIErrorResponse:
        """Delete engine license.

        delete an engine license
        :param license_id: license id
        :type license_id: int
        :rtype: APIErrorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["license_id"] = license_id
        return self._delete_engine_license_endpoint.call_with_http_info(**kwargs)

    def engine_license(
        self,
        license_id: int,
    ) -> EngineLicense:
        """Get engineLicense.

        Get a engineLicense detail
        :param license_id: license id
        :type license_id: int
        :rtype: EngineLicense
        """
        kwargs: Dict[str, Any] = {}
        kwargs["license_id"] = license_id
        return self._engine_license_endpoint.call_with_http_info(**kwargs)

    def list_engine_licenses(
        self,
        *,
        engine_name: Union[str, UnsetType] = unset,
    ) -> EngineLicenseList:
        """List all engineLicenses.

        list all engineLicenses
        :param engine_name: engine name
        :type engine_name: str, optional
        :rtype: EngineLicenseList
        """
        kwargs: Dict[str, Any] = {}
        if engine_name is not unset:
            kwargs["engine_name"] = engine_name
        return self._list_engine_licenses_endpoint.call_with_http_info(**kwargs)
