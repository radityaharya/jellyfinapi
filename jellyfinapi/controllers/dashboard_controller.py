# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.configuration_page_info import ConfigurationPageInfo
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException
from jellyfinapi.exceptions.api_exception import APIException


class DashboardController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(DashboardController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_dashboard_configuration_page(self, name=None):
        """Does a GET request to /web/ConfigurationPage.

        Gets a dashboard configuration page.

        Args:
            name (string, optional): The name of the page.

        Returns:
            binary: Response from the API. ConfigurationPage returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_dashboard_configuration_page called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_dashboard_configuration_page."
            )
            _url_path = "/web/ConfigurationPage"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"name": name}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_dashboard_configuration_page."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_dashboard_configuration_page"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_dashboard_configuration_page."
            )
            if _response.status_code == 404:
                raise ProblemDetailsException(
                    "Plugin configuration page not found.", _response
                )
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_configuration_pages(self, enable_in_main_menu=None):
        """Does a GET request to /web/ConfigurationPages.

        Gets the configuration pages.

        Args:
            enable_in_main_menu (bool, optional): Whether to enable in the
                main menu.

        Returns:
            list of ConfigurationPageInfo: Response from the API.
                ConfigurationPages returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_configuration_pages called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_configuration_pages.")
            _url_path = "/web/ConfigurationPages"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"enableInMainMenu": enable_in_main_menu}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_configuration_pages.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_configuration_pages."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_configuration_pages")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_configuration_pages.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Server still loading.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ConfigurationPageInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
