# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.end_point_info import EndPointInfo
from jellyfinapi.models.system_info import SystemInfo
from jellyfinapi.models.public_system_info import PublicSystemInfo
from jellyfinapi.models.log_file import LogFile
from jellyfinapi.models.wake_on_lan_info import WakeOnLanInfo
from jellyfinapi.exceptions.api_exception import APIException


class SystemController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SystemController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_endpoint_info(self):
        """Does a GET request to /System/Endpoint.

        Gets information about the request endpoint.

        Returns:
            EndPointInfo: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_endpoint_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_endpoint_info.")
            _url_path = "/System/Endpoint"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_endpoint_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_endpoint_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_endpoint_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_endpoint_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, EndPointInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_system_info(self):
        """Does a GET request to /System/Info.

        Gets information about the server.

        Returns:
            SystemInfo: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_system_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_system_info.")
            _url_path = "/System/Info"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_system_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_system_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_system_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_system_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SystemInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_public_system_info(self):
        """Does a GET request to /System/Info/Public.

        Gets public information about the server.

        Returns:
            PublicSystemInfo: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_public_system_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_public_system_info.")
            _url_path = "/System/Info/Public"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_public_system_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_public_system_info."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_public_system_info")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PublicSystemInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_server_logs(self):
        """Does a GET request to /System/Logs.

        Gets a list of available server log files.

        Returns:
            list of LogFile: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_server_logs called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_server_logs.")
            _url_path = "/System/Logs"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_server_logs.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_server_logs.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_server_logs")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_server_logs.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, LogFile.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_log_file(self, name):
        """Does a GET request to /System/Logs/Log.

        Gets a log file.

        Args:
            name (string): The name of the log file to get.

        Returns:
            binary: Response from the API. Log file retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_log_file called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_log_file.")
            _url_path = "/System/Logs/Log"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"name": name}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_log_file.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, binary=True, name="get_log_file")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_log_file.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_ping_system(self):
        """Does a GET request to /System/Ping.

        Pings the system.

        Returns:
            string: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_ping_system called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_ping_system.")
            _url_path = "/System/Ping"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_ping_system.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_ping_system")
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_ping_system(self):
        """Does a POST request to /System/Ping.

        Pings the system.

        Returns:
            string: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_ping_system called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_ping_system.")
            _url_path = "/System/Ping"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_ping_system.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_ping_system")
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def restart_application(self):
        """Does a POST request to /System/Restart.

        Restarts the application.

        Returns:
            void: Response from the API. Server restarted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("restart_application called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for restart_application.")
            _url_path = "/System/Restart"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for restart_application.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="restart_application")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for restart_application.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def shutdown_application(self):
        """Does a POST request to /System/Shutdown.

        Shuts down the application.

        Returns:
            void: Response from the API. Server shut down.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("shutdown_application called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for shutdown_application.")
            _url_path = "/System/Shutdown"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for shutdown_application."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="shutdown_application")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for shutdown_application.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    @deprecated()
    def get_wake_on_lan_info(self):
        """Does a GET request to /System/WakeOnLanInfo.

        Gets wake on lan information.

        Returns:
            list of WakeOnLanInfo: Response from the API. Information
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_wake_on_lan_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_wake_on_lan_info.")
            _url_path = "/System/WakeOnLanInfo"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_wake_on_lan_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_wake_on_lan_info."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_wake_on_lan_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_wake_on_lan_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, WakeOnLanInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
