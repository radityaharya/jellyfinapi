# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.authentication_info_query_result import (
    AuthenticationInfoQueryResult,
)
from jellyfinapi.exceptions.api_exception import APIException


class ApiKeyController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ApiKeyController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_keys(self):
        """Does a GET request to /Auth/Keys.

        Get all keys.

        Returns:
            AuthenticationInfoQueryResult: Response from the API. Api keys
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_keys called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_keys.")
            _url_path = "/Auth/Keys"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_keys.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_keys.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_keys")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_keys.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, AuthenticationInfoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_key(self, app):
        """Does a POST request to /Auth/Keys.

        Create a new api key.

        Args:
            app (string): Name of the app using the authentication key.

        Returns:
            void: Response from the API. Api key created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_key called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_key.")
            _url_path = "/Auth/Keys"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"app": app}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_key.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_key")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_key.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def revoke_key(self, key):
        """Does a DELETE request to /Auth/Keys/{key}.

        Remove an api key.

        Args:
            key (string): The access token to delete.

        Returns:
            void: Response from the API. Api key deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("revoke_key called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for revoke_key.")
            _url_path = "/Auth/Keys/{key}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"key": {"value": key, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for revoke_key.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="revoke_key")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for revoke_key.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
