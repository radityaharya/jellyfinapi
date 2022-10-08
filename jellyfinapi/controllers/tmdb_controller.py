# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.config_image_types import ConfigImageTypes
from jellyfinapi.exceptions.api_exception import APIException


class TmdbController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(TmdbController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def tmdb_client_configuration(self):
        """Does a GET request to /Tmdb/ClientConfiguration.

        Gets the TMDb image configuration options.

        Returns:
            ConfigImageTypes: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("tmdb_client_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for tmdb_client_configuration.")
            _url_path = "/Tmdb/ClientConfiguration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for tmdb_client_configuration.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for tmdb_client_configuration."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="tmdb_client_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for tmdb_client_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ConfigImageTypes.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
