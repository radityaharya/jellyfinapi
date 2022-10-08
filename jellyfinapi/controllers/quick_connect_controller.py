# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.quick_connect_result import QuickConnectResult
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class QuickConnectController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(QuickConnectController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def authorize(self, code):
        """Does a POST request to /QuickConnect/Authorize.

        Authorizes a pending quick connect request.

        Args:
            code (string): Quick connect code to authorize.

        Returns:
            bool: Response from the API. Quick connect result authorized
                successfully.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("authorize called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for authorize.")
            _url_path = "/QuickConnect/Authorize"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"code": code}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for authorize.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="authorize")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for authorize.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException("Unknown user id.", _response)
            self.validate_response(_response)

            decoded = _response.text == "true"

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def connect(self, secret):
        """Does a GET request to /QuickConnect/Connect.

        Attempts to retrieve authentication information.

        Args:
            secret (string): Secret previously returned from the Initiate
                endpoint.

        Returns:
            QuickConnectResult: Response from the API. Quick connect result
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("connect called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for connect.")
            _url_path = "/QuickConnect/Connect"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"secret": secret}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for connect.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for connect.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="connect")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for connect.")
            if _response.status_code == 404:
                raise ProblemDetailsException(
                    "Unknown quick connect secret.", _response
                )
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, QuickConnectResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_enabled(self):
        """Does a GET request to /QuickConnect/Enabled.

        Gets the current quick connect state.

        Returns:
            bool: Response from the API. Quick connect state returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_enabled called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_enabled.")
            _url_path = "/QuickConnect/Enabled"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_enabled.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_enabled")
            self.validate_response(_response)

            decoded = _response.text == "true"

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def initiate(self):
        """Does a GET request to /QuickConnect/Initiate.

        Initiate a new quick connect request.

        Returns:
            QuickConnectResult: Response from the API. Quick connect request
                successfully created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("initiate called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for initiate.")
            _url_path = "/QuickConnect/Initiate"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for initiate.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for initiate.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="initiate")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for initiate.")
            if _response.status_code == 401:
                raise APIException(
                    "Quick connect is not active on this server.", _response
                )
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, QuickConnectResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
