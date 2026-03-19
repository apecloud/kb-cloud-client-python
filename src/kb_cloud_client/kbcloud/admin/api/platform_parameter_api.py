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


class PlatformparameterApi:
    """PlatformParameter API client.

    Provides methods for the platformParameter endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._get_platform_parameter_endpoint = _Endpoint(
            settings={
                "response_type": PlatformParameter,
                "endpoint_path": "/admin/v1/platformParameters/{platformParameterName}",
                "http_method": "GET",
                "operation_id": "get_platform_parameter",
            },
            params_map={
                "platform_parameter_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "platformParameterName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_platform_parameters_endpoint = _Endpoint(
            settings={
                "response_type": PlatformParameterList,
                "endpoint_path": "/admin/v1/platformParameters",
                "http_method": "GET",
                "operation_id": "list_platform_parameters",
            },
            params_map={
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._update_platform_parameters_endpoint = _Endpoint(
            settings={
                "response_type": List[PlatformParameter],
                "endpoint_path": "/admin/v1/platformParameters",
                "http_method": "PATCH",
                "operation_id": "update_platform_parameters",
            },
            params_map={
                "body": {
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


    def get_platform_parameter(
        self,
        platform_parameter_name: str,
    ) -> PlatformParameter:
        """get platformParameter by name.
        :param platform_parameter_name: name of the platformParameter
        :type platform_parameter_name: str
        :rtype: PlatformParameter
        """
        kwargs: Dict[str, Any] = {}
        kwargs["platform_parameter_name"] = platform_parameter_name
        return self._get_platform_parameter_endpoint.call_with_http_info(**kwargs)

    def list_platform_parameters(
        self,
    ) -> PlatformParameterList:
        """list platformParameters.
        :rtype: PlatformParameterList
        """
        kwargs: Dict[str, Any] = {}
        return self._list_platform_parameters_endpoint.call_with_http_info(**kwargs)

    def update_platform_parameters(
        self,
        *,
        body: Union[List[PlatformParameterUpdate], UnsetType] = unset,
    ) -> List[PlatformParameter]:
        """update platformParameters.
        :type body: List[PlatformParameterUpdate], optional
        :rtype: List[PlatformParameter]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body
        return self._update_platform_parameters_endpoint.call_with_http_info(**kwargs)
