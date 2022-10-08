# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.startup_configuration_dto import StartupConfigurationDto
from jellyfinapi.models.startup_user_dto import StartupUserDto
from jellyfinapi.exceptions.api_exception import APIException


class StartupController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(StartupController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def complete_wizard(self):
        """Does a POST request to /Startup/Complete.

        Completes the startup wizard.

        Returns:
            void: Response from the API. Startup wizard completed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("complete_wizard called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for complete_wizard.")
            _url_path = "/Startup/Complete"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for complete_wizard.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="complete_wizard")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for complete_wizard.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_startup_configuration(self):
        """Does a GET request to /Startup/Configuration.

        Gets the initial startup wizard configuration.

        Returns:
            StartupConfigurationDto: Response from the API. Initial startup
                wizard configuration retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_startup_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_startup_configuration.")
            _url_path = "/Startup/Configuration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_startup_configuration.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_startup_configuration."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_startup_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_startup_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, StartupConfigurationDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_initial_configuration(self, body):
        """Does a POST request to /Startup/Configuration.

        Sets the initial startup wizard configuration.

        Args:
            body (StartupConfigurationDto): The updated startup
                configuration.

        Returns:
            void: Response from the API. Configuration saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_initial_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_initial_configuration.")
            _url_path = "/Startup/Configuration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_initial_configuration.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_initial_configuration."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="update_initial_configuration"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_initial_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_first_user_2(self):
        """Does a GET request to /Startup/FirstUser.

        Gets the first user.

        Returns:
            StartupUserDto: Response from the API. Initial user retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_first_user_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_first_user_2.")
            _url_path = "/Startup/FirstUser"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_first_user_2.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_first_user_2.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_first_user_2")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_first_user_2.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, StartupUserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_remote_access(self, body):
        """Does a POST request to /Startup/RemoteAccess.

        Sets remote access and UPnP.

        Args:
            body (StartupRemoteAccessDto): The startup remote access dto.

        Returns:
            void: Response from the API. Configuration saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_remote_access called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_remote_access.")
            _url_path = "/Startup/RemoteAccess"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for set_remote_access.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_remote_access.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_remote_access")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_remote_access.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_first_user(self):
        """Does a GET request to /Startup/User.

        Gets the first user.

        Returns:
            StartupUserDto: Response from the API. Initial user retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_first_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_first_user.")
            _url_path = "/Startup/User"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_first_user.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_first_user.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_first_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_first_user.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, StartupUserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_startup_user(self, body=None):
        """Does a POST request to /Startup/User.

        Sets the user name and password.

        Args:
            body (StartupUserDto, optional): The DTO containing username and
                password.

        Returns:
            void: Response from the API. Updated user name and password.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_startup_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_startup_user.")
            _url_path = "/Startup/User"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_startup_user.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_startup_user.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_startup_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_startup_user.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
