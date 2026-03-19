# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd

from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from requests.auth import HTTPDigestAuth
from urllib3.util.retry import Retry

from ._version import __version__ as _VERSION
from .configuration import Configuration
from .exceptions import ApiException, raise_from_response

T = TypeVar("T")


# ---------------------------------------------------------------------------
# Sentinel for "parameter not provided" – mirrors DataDog's `unset`
# ---------------------------------------------------------------------------

class _Unset:
    """Sentinel singleton that distinguishes 'not provided' from ``None``."""

    _instance: Optional["_Unset"] = None

    def __new__(cls) -> "_Unset":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "unset"

    def __bool__(self) -> bool:
        return False


unset = _Unset()
UnsetType = _Unset


# ---------------------------------------------------------------------------
# Datetime helper
# ---------------------------------------------------------------------------

def _parse_datetime(value: Any) -> Any:
    """Parse an ISO-8601 datetime string, handling the ``Z`` UTC suffix (Python 3.10 compat)."""
    if not isinstance(value, str):
        return value
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return value


# ---------------------------------------------------------------------------
# Endpoint – declarative API operation descriptor (mirrors DataDog's pattern)
# ---------------------------------------------------------------------------

class Endpoint:
    """Encapsulates all metadata for a single API operation.

    Generated API classes create one ``Endpoint`` instance per operation in
    their ``__init__``, then each method simply builds a ``kwargs`` dict and
    calls :meth:`call_with_http_info`.

    :param settings: Operation-level settings.
        - ``response_type``: Python type to deserialize the response into, or ``None``.
        - ``endpoint_path``: URL path template (e.g. ``/v1/organizations/{orgName}/clusters``).
        - ``http_method``: HTTP verb (``GET``, ``POST``, …).
        - ``operation_id``: snake_case operation name.
        - ``deprecated``: ``True`` if the operation is deprecated.
    :param params_map: Maps **Python** parameter name → parameter metadata dict.
        Each entry contains:
        - ``location``: ``"path"``, ``"query"``, ``"header"``, or ``"body"``.
        - ``attribute``: Original camelCase name used in the URL / query string.
        - ``collection_format``: (optional) ``"csv"``, ``"multi"``, etc.
        - ``required``: (optional) ``True`` if the parameter is required.
    :param headers_map: ``{"accept": [...], "content_type": [...]}``
    :param api_client: The :class:`ApiClient` used to execute the request.
    """

    def __init__(
        self,
        settings: Dict[str, Any],
        params_map: Dict[str, Any],
        headers_map: Dict[str, List[str]],
        api_client: "ApiClient",
    ):
        self.settings = settings
        self.params_map = params_map
        self.headers_map = headers_map
        self.api_client = api_client

    def call_with_http_info(self, **kwargs: Any) -> Any:
        """Execute the API operation with the provided keyword arguments."""
        path_params: Dict[str, Any] = {}
        query_params: Dict[str, Any] = {}
        header_params: Dict[str, str] = {}
        body: Any = None
        collection_formats: Dict[str, str] = {}

        for name, value in kwargs.items():
            param_info = self.params_map.get(name, {})
            location = param_info.get("location", "query")
            # Use the original API attribute name for path/query (camelCase)
            attr = param_info.get("attribute", name)

            if location == "path":
                path_params[attr] = value
            elif location == "query":
                query_params[attr] = value
            elif location == "header":
                header_params[attr] = value
            elif location == "body":
                body = value

            if "collection_format" in param_info:
                collection_formats[attr] = param_info["collection_format"]

        accept_list = self.headers_map.get("accept", [])
        if accept_list:
            header_params["Accept"] = accept_list[0]
        content_type_list = self.headers_map.get("content_type", [])
        if content_type_list and body is not None:
            header_params["Content-Type"] = content_type_list[0]

        return self.api_client.call_api(
            method=self.settings["http_method"],
            path=self.settings["endpoint_path"],
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            response_type=self.settings.get("response_type"),
            collection_formats=collection_formats,
        )


# ---------------------------------------------------------------------------
# ApiClient
# ---------------------------------------------------------------------------

class ApiClient:
    """HTTP client for the KubeBlocks Cloud API.

    :param configuration: Client configuration. Reads from environment
        variables when omitted.

    Example::

        from kb_cloud_client import ApiClient, Configuration

        with ApiClient(Configuration()) as client:
            api = ClusterApi(client)
            clusters = api.list_cluster(org_name="my-org")
    """

    def __init__(self, configuration: Optional[Configuration] = None):
        if configuration is None:
            configuration = Configuration.default()
        self.configuration = configuration
        self._session: Optional[requests.Session] = None

    def __enter__(self) -> "ApiClient":
        self._session = self._create_session()
        return self

    def __exit__(self, *args: Any) -> None:
        if self._session:
            self._session.close()
            self._session = None

    def _create_session(self) -> requests.Session:
        session = requests.Session()

        cfg = self.configuration
        if cfg.api_key_name and cfg.api_key_secret:
            session.auth = HTTPDigestAuth(cfg.api_key_name, cfg.api_key_secret)

        session.verify = cfg.ssl_ca_cert if cfg.ssl_ca_cert else cfg.verify_ssl

        if cfg.proxy:
            session.proxies = {"http": cfg.proxy, "https": cfg.proxy}

        if cfg.enable_retry:
            retry = Retry(
                total=cfg.max_retries,
                backoff_factor=cfg.retry_backoff_factor,
                status_forcelist=[429, 500, 502, 503, 504],
                # Only retry idempotent methods; retrying POST/DELETE/PATCH on
                # 5xx could cause duplicate resource creation or deletion.
                allowed_methods=["GET", "HEAD", "OPTIONS", "PUT"],
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount("http://", adapter)
            session.mount("https://", adapter)

        session.headers.update({
            "User-Agent": f"kb-cloud-client-python/{_VERSION}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            **cfg.default_headers,
        })

        return session

    @property
    def session(self) -> requests.Session:
        if self._session is None:
            self._session = self._create_session()
        return self._session

    def call_api(
        self,
        method: str,
        path: str,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        header_params: Optional[Dict[str, str]] = None,
        body: Optional[Any] = None,
        files: Optional[Dict[str, Any]] = None,
        response_type: Optional[Any] = None,
        collection_formats: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Execute an HTTP request and return the deserialized response.

        When ``configuration.return_http_data_only`` is ``False``, returns a
        ``(data, status_code, headers)`` tuple instead of just the data.
        """
        url = self._build_url(path, path_params)
        params = self._sanitize_params(query_params or {}, collection_formats or {})
        headers: Dict[str, str] = {}
        if header_params:
            headers.update(header_params)

        request_body = None
        if body is not None:
            request_body = self._serialize(body)

        cfg = self.configuration
        if cfg.debug:
            cfg.logger.debug(f"{method} {url} params={params}")

        resp = self.session.request(
            method=method.upper(),
            url=url,
            params=params or None,
            data=request_body,
            files=files,
            headers=headers,
            timeout=cfg.request_timeout,
        )

        if cfg.debug:
            cfg.logger.debug(f"Response {resp.status_code}: {resp.text[:200]}")

        if resp.status_code >= 300:
            raise_from_response(resp)

        if response_type is None or resp.status_code == 204:
            data = None
        else:
            data = self._deserialize(resp, response_type)

        if cfg.return_http_data_only:
            return data
        return data, resp.status_code, dict(resp.headers)

    def _build_url(self, path: str, path_params: Optional[Dict[str, Any]] = None) -> str:
        url = self.configuration.host + path
        if path_params:
            for k, v in path_params.items():
                url = url.replace(f"{{{k}}}", quote(str(v), safe=""))
        return url

    def _sanitize_params(
        self,
        params: Dict[str, Any],
        collection_formats: Dict[str, str],
    ) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, list):
                fmt = collection_formats.get(k, "multi")
                if fmt == "csv":
                    result[k] = ",".join(str(i) for i in v)
                elif fmt == "ssv":
                    result[k] = " ".join(str(i) for i in v)
                elif fmt == "tsv":
                    result[k] = "\t".join(str(i) for i in v)
                elif fmt == "pipes":
                    result[k] = "|".join(str(i) for i in v)
                else:
                    result[k] = v
            else:
                result[k] = v
        return result

    def _serialize(self, obj: Any) -> Optional[str]:
        if obj is None:
            return None
        if isinstance(obj, (str, bytes)):
            return obj
        if hasattr(obj, "to_dict"):
            return json.dumps(obj.to_dict())
        return json.dumps(obj)

    def _deserialize(self, resp: requests.Response, response_type: Any) -> Any:
        try:
            data = resp.json()
        except Exception:
            return resp.text
        return _deserialize_value(data, response_type)


def _deserialize_value(data: Any, type_hint: Any) -> Any:
    """Recursively deserialize ``data`` into an instance of ``type_hint``.

    Handles ``List``, ``Dict``, ``Union`` (``Optional``), model classes with
    ``from_dict``, enums, and primitives. Falls back to raw data on failure.
    """
    if data is None:
        return None
    if type_hint is None or type_hint is Any:
        return data

    origin = getattr(type_hint, "__origin__", None)

    if origin is list:
        item_type = (type_hint.__args__ or (Any,))[0]
        if isinstance(data, list):
            return [_deserialize_value(item, item_type) for item in data]
        return data

    if origin is dict:
        val_type = (type_hint.__args__ or (str, Any))[1]
        if isinstance(data, dict):
            return {k: _deserialize_value(v, val_type) for k, v in data.items()}
        return data

    if origin is Union:
        for t in type_hint.__args__:
            if t is type(None):
                continue
            try:
                return _deserialize_value(data, t)
            except Exception:
                continue
        return data

    if hasattr(type_hint, "from_dict") and isinstance(data, dict):
        return type_hint.from_dict(data)

    if hasattr(type_hint, "__mro__") and any(
        c.__name__ in ("Enum", "IntEnum") for c in type_hint.__mro__
    ):
        try:
            return type_hint(data)
        except (ValueError, KeyError):
            return data

    try:
        if isinstance(data, type_hint):
            return data
        return type_hint(data)
    except Exception:
        return data
