# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.server_configuration import ServerConfiguration
from jellyfinapi.models.metadata_options import MetadataOptions
from jellyfinapi.exceptions.api_exception import APIException


class ConfigurationController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ConfigurationController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_configuration(self):
        """Does a GET request to /System/Configuration.

        Gets application configuration.

        Returns:
            ServerConfiguration: Response from the API. Application
                configuration returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_configuration.")
            _url_path = "/System/Configuration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_configuration.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_configuration.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ServerConfiguration.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_configuration(self, body):
        """Does a POST request to /System/Configuration.

        Updates application configuration.

        Args:
            body (ServerConfiguration): Configuration.

        Returns:
            void: Response from the API. Configuration updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_configuration.")
            _url_path = "/System/Configuration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_configuration.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_configuration."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_named_configuration(self, key):
        """Does a GET request to /System/Configuration/{key}.

        Gets a named configuration.

        Args:
            key (string): Configuration key.

        Returns:
            binary: Response from the API. Configuration returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_named_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_named_configuration.")
            _url_path = "/System/Configuration/{key}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"key": {"value": key, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_named_configuration."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_named_configuration"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_named_configuration.")
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

    def update_named_configuration(self, key, body):
        """Does a POST request to /System/Configuration/{key}.

        Updates named configuration.

        Args:
            key (string): Configuration key.
            body (object): Configuration.

        Returns:
            void: Response from the API. Named configuration updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_named_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_named_configuration.")
            _url_path = "/System/Configuration/{key}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"key": {"value": key, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_named_configuration.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_named_configuration."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="update_named_configuration"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_named_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_default_metadata_options(self):
        """Does a GET request to /System/Configuration/MetadataOptions/Default.

        Gets a default MetadataOptions object.

        Returns:
            MetadataOptions: Response from the API. Metadata options
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_default_metadata_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_default_metadata_options.")
            _url_path = "/System/Configuration/MetadataOptions/Default"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_default_metadata_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_default_metadata_options."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_default_metadata_options"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_default_metadata_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, MetadataOptions.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_media_encoder_path(self, body):
        """Does a POST request to /System/MediaEncoder/Path.

        Updates the path to the media encoder.

        Args:
            body (MediaEncoderPathDto): Media encoder path form body.

        Returns:
            void: Response from the API. Media encoder path updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_media_encoder_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_media_encoder_path.")
            _url_path = "/System/MediaEncoder/Path"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_media_encoder_path.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_media_encoder_path."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_media_encoder_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_media_encoder_path.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
