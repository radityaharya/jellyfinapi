# -*- coding: utf-8 -*-


from enum import Enum
import logging
import sys

from jellyfinapi.http.requests_client import RequestsClient

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Environment(Enum):
    """An enum for SDK environments"""

    PRODUCTION = 0
    CUSTOM = 0


class Server(Enum):
    """An enum for API servers"""

    DEFAULT = 0


class Configuration(object):
    """A class used for configuring the SDK by a user."""

    @property
    def http_client(self):
        return self._http_client

    @property
    def http_client_instance(self):
        return self._http_client_instance

    @property
    def override_http_client_configuration(self):
        return self._override_http_client_configuration

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def timeout(self):
        return self._timeout

    @property
    def max_retries(self):
        return self._max_retries

    @property
    def backoff_factor(self):
        return self._backoff_factor

    @property
    def retry_statuses(self):
        return self._retry_statuses

    @property
    def retry_methods(self):
        return self._retry_methods

    @property
    def environment(self):
        return self._environment

    @property
    def x_emby_token(self):
        return self._x_emby_token

    def __init__(
        self,
        http_client_instance=None,
        override_http_client_configuration=False,
        http_call_back=None,
        timeout=60,
        max_retries=0,
        backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=["GET", "PUT"],
        environment=None,
        server_url=None,
        x_emby_token=None,
    ):
        # The Http Client passed from the sdk user for making requests
        self._http_client_instance = http_client_instance

        # The value which determines to override properties of the passed Http Client from the sdk user
        self._override_http_client_configuration = override_http_client_configuration

        #  The callback value that is invoked before and after an HTTP call is made to an endpoint
        self._http_call_back = http_call_back

        # The value to use for connection timeout
        self._timeout = timeout

        # The number of times to retry an endpoint call if it fails
        self._max_retries = max_retries

        # A backoff factor to apply between attempts after the second try.
        # urllib3 will sleep for:
        # `{backoff factor} * (2 ** ({number of total retries} - 1))`
        self._backoff_factor = backoff_factor

        # The http statuses on which retry is to be done
        self._retry_statuses = retry_statuses

        # The http methods on which retry is to be done
        self._retry_methods = retry_methods

        # Current API environment
        self._environment = environment
        
        if server_url is not None:
            self._server_url = server_url
            self.environments[Environment.CUSTOM] = {Server.DEFAULT: server_url}

        # API key header parameter
        self._x_emby_token = x_emby_token

        # The Http Client to use for making requests.
        self._http_client = self.create_http_client()

    def clone_with(
        self,
        http_client_instance=None,
        override_http_client_configuration=None,
        http_call_back=None,
        timeout=None,
        max_retries=None,
        backoff_factor=None,
        retry_statuses=None,
        retry_methods=None,
        environment=None,
        x_emby_token=None,
    ):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = (
            override_http_client_configuration
            or self.override_http_client_configuration
        )
        http_call_back = http_call_back or self.http_call_back
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        x_emby_token = x_emby_token or self.x_emby_token

        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back,
            timeout=timeout,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            retry_statuses=retry_statuses,
            retry_methods=retry_methods,
            environment=environment,
            x_emby_token=x_emby_token,
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout,
            max_retries=self.max_retries,
            backoff_factor=self.backoff_factor,
            retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
        )

    # All the environments the SDK can run in
    environments = {Environment.PRODUCTION: {Server.DEFAULT: "http://localhost:8096"}}

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]

    @classmethod
    def disable_logging(cls):
        """Disable all logging in the SDK"""
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    @classmethod
    def enable_logging(cls):
        """Enable logging in the SDK"""
        cls.disable_logging()  # clear previously set logging info
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
