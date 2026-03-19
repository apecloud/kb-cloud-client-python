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


class FeatureApi:
    """Feature API client.

    Provides methods for the feature endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._list_feature_endpoint = _Endpoint(
            settings={
                "response_type": FeatureList,
                "endpoint_path": "/api/v1/features",
                "http_method": "GET",
                "operation_id": "list_feature",
            },
            params_map={
                "group": {
                    "location": "query",
                    "attribute": "group",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._read_feature_endpoint = _Endpoint(
            settings={
                "response_type": Feature,
                "endpoint_path": "/api/v1/features/{featureName}",
                "http_method": "GET",
                "operation_id": "read_feature",
            },
            params_map={
                "feature_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "featureName",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def list_feature(
        self,
        *,
        group: Union[str, UnsetType] = unset,
    ) -> FeatureList:
        """Get feature list.

        Get feature list
        :param group: name of the feature group
        :type group: str, optional
        :rtype: FeatureList
        """
        kwargs: Dict[str, Any] = {}
        if group is not unset:
            kwargs["group"] = group
        return self._list_feature_endpoint.call_with_http_info(**kwargs)

    def read_feature(
        self,
        feature_name: str,
    ) -> Feature:
        """Get feature.

        Get feature
        :param feature_name: name of the feature
        :type feature_name: str
        :rtype: Feature
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_name"] = feature_name
        return self._read_feature_endpoint.call_with_http_info(**kwargs)
