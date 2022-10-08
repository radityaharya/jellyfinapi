# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.default_directory_browser_info_dto import (
    DefaultDirectoryBrowserInfoDto,
)
from jellyfinapi.models.file_system_entry_info import FileSystemEntryInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class EnvironmentController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(EnvironmentController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_default_directory_browser(self):
        """Does a GET request to /Environment/DefaultDirectoryBrowser.

        Get Default directory browser.

        Returns:
            DefaultDirectoryBrowserInfoDto: Response from the API. Default
                directory browser returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_default_directory_browser called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_default_directory_browser.")
            _url_path = "/Environment/DefaultDirectoryBrowser"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_default_directory_browser.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_default_directory_browser."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_default_directory_browser"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_default_directory_browser.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DefaultDirectoryBrowserInfoDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_directory_contents(
        self, path, include_files=False, include_directories=False
    ):
        """Does a GET request to /Environment/DirectoryContents.

        Gets the contents of a given directory in the file system.

        Args:
            path (string): The path.
            include_files (bool, optional): An optional filter to include or
                exclude files from the results. true/false.
            include_directories (bool, optional): An optional filter to
                include or exclude folders from the results. true/false.

        Returns:
            list of FileSystemEntryInfo: Response from the API. Directory
                contents returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_directory_contents called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_directory_contents.")
            _url_path = "/Environment/DirectoryContents"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "path": path,
                "includeFiles": include_files,
                "includeDirectories": include_directories,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_directory_contents.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_directory_contents."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_directory_contents")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_directory_contents.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, FileSystemEntryInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_drives(self):
        """Does a GET request to /Environment/Drives.

        Gets available drives from the server's file system.

        Returns:
            list of FileSystemEntryInfo: Response from the API. List of
                entries returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_drives called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_drives.")
            _url_path = "/Environment/Drives"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_drives.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_drives.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_drives")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_drives.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, FileSystemEntryInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    @deprecated()
    def get_network_shares(self):
        """Does a GET request to /Environment/NetworkShares.

        Gets network paths.

        Returns:
            list of FileSystemEntryInfo: Response from the API. Empty array
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_network_shares called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_network_shares.")
            _url_path = "/Environment/NetworkShares"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_network_shares.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_network_shares.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_network_shares")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_network_shares.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, FileSystemEntryInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_parent_path(self, path):
        """Does a GET request to /Environment/ParentPath.

        Gets the parent path of a given path.

        Args:
            path (string): The path.

        Returns:
            string: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_parent_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_parent_path.")
            _url_path = "/Environment/ParentPath"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"path": path}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_parent_path.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_parent_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_parent_path.")
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

    def validate_path(self, body):
        """Does a POST request to /Environment/ValidatePath.

        Validates path.

        Args:
            body (ValidatePathDto): Validate request object.

        Returns:
            void: Response from the API. Path validated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("validate_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for validate_path.")
            _url_path = "/Environment/ValidatePath"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for validate_path.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for validate_path.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="validate_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for validate_path.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Path not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
