# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at ApeCloud (https://www.apecloud.com/).
# Copyright 2022-Present ApeCloud Co., Ltd

from __future__ import annotations

import logging
import os
from typing import Any, Dict, Optional


DEFAULT_HOST = "https://api.apecloud.com"


class Configuration:
    """Configuration for the KubeBlocks Cloud API client.

    :param host: Base URL for the API. Defaults to ``https://api.apecloud.com``.
        Can also be set via the ``KB_CLOUD_SITE`` environment variable.
    :type host: str
    :param api_key_name: API key name (username for Digest auth).
        Can also be set via the ``KB_CLOUD_API_KEY_NAME`` environment variable.
    :type api_key_name: str
    :param api_key_secret: API key secret (password for Digest auth).
        Can also be set via the ``KB_CLOUD_API_KEY_SECRET`` environment variable.
    :type api_key_secret: str
    :param verify_ssl: Whether to verify SSL certificates. Defaults to ``True``.
    :type verify_ssl: bool
    :param ssl_ca_cert: Path to a CA certificate file for SSL verification.
    :type ssl_ca_cert: str
    :param debug: Enable debug logging. Defaults to ``False``.
    :type debug: bool
    :param proxy: HTTP proxy URL (e.g. ``http://proxy.example.com:8080``).
    :type proxy: str
    :param request_timeout: Request timeout in seconds. Can be a float or a
        ``(connect_timeout, read_timeout)`` tuple. Defaults to ``None`` (no timeout).
    :type request_timeout: float or tuple
    :param enable_retry: Retry requests on transient errors (5xx and 429).
        Defaults to ``False``.
    :type enable_retry: bool
    :param max_retries: Maximum number of retries. Defaults to ``3``.
    :type max_retries: int
    :param retry_backoff_factor: Backoff factor between retries. Defaults to ``2``.
    :type retry_backoff_factor: float
    :param return_http_data_only: When ``True`` (default), API methods return only
        the deserialized response body. When ``False``, they return a
        ``(data, status_code, headers)`` tuple — mirrors DataDog's option.
    :type return_http_data_only: bool
    :param unstable_operations: Dict of operation names that are enabled despite
        being marked unstable/preview. Set an operation's key to ``True`` to
        enable it. Example: ``{"list_cluster": True}``.
    :type unstable_operations: dict
    """

    def __init__(
        self,
        host: Optional[str] = None,
        api_key_name: Optional[str] = None,
        api_key_secret: Optional[str] = None,
        verify_ssl: bool = True,
        ssl_ca_cert: Optional[str] = None,
        debug: bool = False,
        proxy: Optional[str] = None,
        request_timeout: Optional[float] = None,
        enable_retry: bool = False,
        max_retries: int = 3,
        retry_backoff_factor: float = 2.0,
        return_http_data_only: bool = True,
        unstable_operations: Optional[Dict[str, bool]] = None,
    ):
        self._host = host
        self.verify_ssl = verify_ssl
        self.ssl_ca_cert = ssl_ca_cert
        self.debug = debug
        self.proxy = proxy
        self.request_timeout = request_timeout
        self.enable_retry = enable_retry
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor
        self.return_http_data_only = return_http_data_only
        self.unstable_operations: Dict[str, bool] = unstable_operations or {}

        # Authentication
        self._api_key_name = api_key_name
        self._api_key_secret = api_key_secret

        # Logger
        self.logger = logging.getLogger("kb_cloud_client")
        if debug:
            self.logger.setLevel(logging.DEBUG)

        # Default headers sent with every request
        self.default_headers: Dict[str, str] = {}

    @property
    def host(self) -> str:
        """Return the base URL for the API."""
        if self._host is not None:
            return self._host.rstrip("/")
        site = os.environ.get("KB_CLOUD_SITE")
        if site:
            return site.rstrip("/")
        return DEFAULT_HOST

    @host.setter
    def host(self, value: str) -> None:
        self._host = value

    @property
    def api_key_name(self) -> Optional[str]:
        """Return the API key name."""
        if self._api_key_name is not None:
            return self._api_key_name
        return os.environ.get("KB_CLOUD_API_KEY_NAME")

    @api_key_name.setter
    def api_key_name(self, value: str) -> None:
        self._api_key_name = value

    @property
    def api_key_secret(self) -> Optional[str]:
        """Return the API key secret."""
        if self._api_key_secret is not None:
            return self._api_key_secret
        return os.environ.get("KB_CLOUD_API_KEY_SECRET")

    @api_key_secret.setter
    def api_key_secret(self, value: str) -> None:
        self._api_key_secret = value

    def add_default_header(self, header_name: str, header_value: str) -> None:
        """Add a default header that is sent with every request.

        :param header_name: Header name.
        :param header_value: Header value.
        """
        self.default_headers[header_name] = header_value

    @classmethod
    def default(cls) -> "Configuration":
        """Create a Configuration from environment variables.

        Reads ``KB_CLOUD_API_KEY_NAME``, ``KB_CLOUD_API_KEY_SECRET``,
        and ``KB_CLOUD_SITE`` from the environment.
        """
        return cls()
