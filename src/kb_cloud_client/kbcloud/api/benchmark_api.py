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


class BenchmarkApi:
    """Benchmark API client.

    Provides methods for the benchmark endpoints of the KubeBlocks Cloud API.
    """

    def __init__(self, api_client: Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient(Configuration.default())
        self.api_client = api_client

        # ── Endpoint descriptors ──────────────────────────────────────────────
        self._create_pgbench_endpoint = _Endpoint(
            settings={
                "response_type": Benchmark,
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark/pgbench",
                "http_method": "POST",
                "operation_id": "create_pgbench",
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
        self._create_sysbench_endpoint = _Endpoint(
            settings={
                "response_type": Benchmark,
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark/sysbench",
                "http_method": "POST",
                "operation_id": "create_sysbench",
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
        self._create_tpcc_endpoint = _Endpoint(
            settings={
                "response_type": Benchmark,
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark/tpcc",
                "http_method": "POST",
                "operation_id": "create_tpcc",
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
        self._create_ycsb_endpoint = _Endpoint(
            settings={
                "response_type": Benchmark,
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark/ycsb",
                "http_method": "POST",
                "operation_id": "create_ycsb",
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
        self._delete_benchmark_endpoint = _Endpoint(
            settings={
                "response_type": Dict[str, Any],
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark",
                "http_method": "DELETE",
                "operation_id": "delete_benchmark",
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
        self._get_benchmark_endpoint = _Endpoint(
            settings={
                "response_type": Benchmark,
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark/{benchmarkId}",
                "http_method": "GET",
                "operation_id": "get_benchmark",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "benchmark_id": {
                    "required": True,
                    "location": "path",
                    "attribute": "benchmarkId",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )
        self._list_benchmark_endpoint = _Endpoint(
            settings={
                "response_type": List[Benchmark],
                "endpoint_path": "/api/v1/organizations/{orgName}/benchmark",
                "http_method": "GET",
                "operation_id": "list_benchmark",
            },
            params_map={
                "org_name": {
                    "required": True,
                    "location": "path",
                    "attribute": "orgName",
                },
                "cluster": {
                    "location": "query",
                    "attribute": "cluster",
                },
                "bench_type": {
                    "location": "query",
                    "attribute": "benchType",
                },
                "cluster_id": {
                    "location": "query",
                    "attribute": "clusterID",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )


    def create_pgbench(
        self,
        org_name: str,
        body: Pgbench,
    ) -> Benchmark:
        """Create a pgbench benchmark task.
        :param org_name: name of the Org
        :type org_name: str
        :type body: Pgbench
        :rtype: Benchmark
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_pgbench_endpoint.call_with_http_info(**kwargs)

    def create_sysbench(
        self,
        org_name: str,
        body: Sysbench,
    ) -> Benchmark:
        """Create a sysbench benchmark task.
        :param org_name: name of the Org
        :type org_name: str
        :type body: Sysbench
        :rtype: Benchmark
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_sysbench_endpoint.call_with_http_info(**kwargs)

    def create_tpcc(
        self,
        org_name: str,
        body: Tpcc,
    ) -> Benchmark:
        """Create a tpcc benchmark task.
        :param org_name: name of the Org
        :type org_name: str
        :type body: Tpcc
        :rtype: Benchmark
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_tpcc_endpoint.call_with_http_info(**kwargs)

    def create_ycsb(
        self,
        org_name: str,
        body: Ycsb,
    ) -> Benchmark:
        """Create a ycsb benchmark task.
        :param org_name: name of the Org
        :type org_name: str
        :type body: Ycsb
        :rtype: Benchmark
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._create_ycsb_endpoint.call_with_http_info(**kwargs)

    def delete_benchmark(
        self,
        org_name: str,
        body: DeleteBenchOption,
    ) -> Dict[str, Any]:
        """Delete benchmark tasks.
        :param org_name: name of the Org
        :type org_name: str
        :param body: ids of the benchmark
        :type body: DeleteBenchOption
        :rtype: Dict[str, Any]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["body"] = body
        return self._delete_benchmark_endpoint.call_with_http_info(**kwargs)

    def get_benchmark(
        self,
        org_name: str,
        benchmark_id: str,
    ) -> Benchmark:
        """Get benchmark task info.
        :param org_name: name of the Org
        :type org_name: str
        :param benchmark_id: id of the benchmark
        :type benchmark_id: str
        :rtype: Benchmark
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        kwargs["benchmark_id"] = benchmark_id
        return self._get_benchmark_endpoint.call_with_http_info(**kwargs)

    def list_benchmark(
        self,
        org_name: str,
        *,
        cluster: Union[str, UnsetType] = unset,
        bench_type: Union[str, UnsetType] = unset,
        cluster_id: Union[str, UnsetType] = unset,
    ) -> List[Benchmark]:
        """List benchmark tasks.
        :param org_name: name of the Org
        :type org_name: str
        :param cluster: name of the cluster
        :type cluster: str, optional
        :param bench_type: type of the benchmark
        :type bench_type: str, optional
        :param cluster_id: id of the cluster
        :type cluster_id: str, optional
        :rtype: List[Benchmark]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_name"] = org_name
        if cluster is not unset:
            kwargs["cluster"] = cluster
        if bench_type is not unset:
            kwargs["bench_type"] = bench_type
        if cluster_id is not unset:
            kwargs["cluster_id"] = cluster_id
        return self._list_benchmark_endpoint.call_with_http_info(**kwargs)
