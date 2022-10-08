# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.display_preferences_dto import DisplayPreferencesDto
from jellyfinapi.exceptions.api_exception import APIException


class DisplayPreferencesController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(DisplayPreferencesController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_display_preferences(self, display_preferences_id, user_id, client):
        """Does a GET request to /DisplayPreferences/{displayPreferencesId}.

        Get Display Preferences.

        Args:
            display_preferences_id (string): Display preferences id.
            user_id (uuid|string): User id.
            client (string): Client.

        Returns:
            DisplayPreferencesDto: Response from the API. Display preferences
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_display_preferences called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_display_preferences.")
            _url_path = "/DisplayPreferences/{displayPreferencesId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "displayPreferencesId": {
                        "value": display_preferences_id,
                        "encode": True,
                    }
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id, "client": client}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_display_preferences.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_display_preferences."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_display_preferences")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_display_preferences.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DisplayPreferencesDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_display_preferences(self, display_preferences_id, user_id, client, body):
        """Does a POST request to /DisplayPreferences/{displayPreferencesId}.

        Update Display Preferences.

        Args:
            display_preferences_id (string): Display preferences id.
            user_id (uuid|string): User Id.
            client (string): Client.
            body (DisplayPreferencesDto): New Display Preferences object.

        Returns:
            void: Response from the API. Display preferences updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_display_preferences called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_display_preferences.")
            _url_path = "/DisplayPreferences/{displayPreferencesId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "displayPreferencesId": {
                        "value": display_preferences_id,
                        "encode": True,
                    }
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id, "client": client}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_display_preferences.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_display_preferences."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="update_display_preferences"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_display_preferences.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
