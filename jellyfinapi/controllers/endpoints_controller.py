# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.code_response import CodeResponse
from jellyfinapi.models.code_status_response import CodeStatusResponse
from jellyfinapi.models.user_settings import UserSettings
from jellyfinapi.exceptions.api_exception import APIException


class EndpointsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(EndpointsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_pin(self):
        """Does a GET request to /Simkl/oauth/pin.

        TODO: type endpoint description here.

        Returns:
            CodeResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_pin called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_pin.")
            _url_path = "/Simkl/oauth/pin"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_pin.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_pin.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_pin")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_pin.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, CodeResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_pin_status(self, user_code):
        """Does a GET request to /Simkl/oauth/pin/{userCode}.

        TODO: type endpoint description here.

        Args:
            user_code (string): TODO: type description here.

        Returns:
            CodeStatusResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_pin_status called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_pin_status.")
            _url_path = "/Simkl/oauth/pin/{userCode}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userCode": {"value": user_code, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_pin_status.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_pin_status.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_pin_status")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_pin_status.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, CodeStatusResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_user_settings(self, user_id):
        """Does a GET request to /Simkl/users/settings/{userId}.

        TODO: type endpoint description here.

        Args:
            user_id (uuid|string): TODO: type description here.

        Returns:
            UserSettings: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_user_settings called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_user_settings.")
            _url_path = "/Simkl/users/settings/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_user_settings.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_user_settings.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_user_settings")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_user_settings.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserSettings.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
