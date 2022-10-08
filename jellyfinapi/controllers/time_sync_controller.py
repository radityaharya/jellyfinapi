# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.utc_time_response import UtcTimeResponse


class TimeSyncController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(TimeSyncController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_utc_time(self):
        """Does a GET request to /GetUtcTime.

        Gets the current UTC time.

        Returns:
            UtcTimeResponse: Response from the API. Time returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_utc_time called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_utc_time.")
            _url_path = "/GetUtcTime"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_utc_time.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_utc_time.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_utc_time")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UtcTimeResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
