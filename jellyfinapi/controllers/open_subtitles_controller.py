# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException
from jellyfinapi.exceptions.api_exception import APIException


class OpenSubtitlesController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(OpenSubtitlesController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def validate_login_info(self, body=None):
        """Does a POST request to /Jellyfin.Plugin.OpenSubtitles/ValidateLoginInfo.

        TODO: type endpoint description here.

        Args:
            body (LoginInfoInput, optional): TODO: type description here.

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("validate_login_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for validate_login_info.")
            _url_path = "/Jellyfin.Plugin.OpenSubtitles/ValidateLoginInfo"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for validate_login_info.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for validate_login_info.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="validate_login_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for validate_login_info.")
            if _response.status_code == 400:
                raise ProblemDetailsException("Bad Request", _response)
            elif _response.status_code == 401:
                raise ProblemDetailsException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
