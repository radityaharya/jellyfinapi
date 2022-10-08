# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.branding_options import BrandingOptions


class BrandingController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(BrandingController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_branding_options(self):
        """Does a GET request to /Branding/Configuration.

        Gets branding configuration.

        Returns:
            BrandingOptions: Response from the API. Branding configuration
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_branding_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_branding_options.")
            _url_path = "/Branding/Configuration"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_branding_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_branding_options."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_branding_options")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BrandingOptions.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_branding_css(self):
        """Does a GET request to /Branding/Css.

        Gets branding css.

        Returns:
            string: Response from the API. Branding css returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_branding_css called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_branding_css.")
            _url_path = "/Branding/Css"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_branding_css.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_branding_css")
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_branding_css_2(self):
        """Does a GET request to /Branding/Css.css.

        Gets branding css.

        Returns:
            string: Response from the API. Branding css returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_branding_css_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_branding_css_2.")
            _url_path = "/Branding/Css.css"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_branding_css_2.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_branding_css_2")
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
