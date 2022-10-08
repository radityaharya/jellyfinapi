# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.country_info import CountryInfo
from jellyfinapi.models.culture_dto import CultureDto
from jellyfinapi.models.localization_option import LocalizationOption
from jellyfinapi.models.parental_rating import ParentalRating
from jellyfinapi.exceptions.api_exception import APIException


class LocalizationController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(LocalizationController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_countries(self):
        """Does a GET request to /Localization/Countries.

        Gets known countries.

        Returns:
            list of CountryInfo: Response from the API. Known countries
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_countries called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_countries.")
            _url_path = "/Localization/Countries"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_countries.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_countries.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_countries")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_countries.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, CountryInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_cultures(self):
        """Does a GET request to /Localization/Cultures.

        Gets known cultures.

        Returns:
            list of CultureDto: Response from the API. Known cultures
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_cultures called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_cultures.")
            _url_path = "/Localization/Cultures"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_cultures.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_cultures.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_cultures")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_cultures.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, CultureDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_localization_options(self):
        """Does a GET request to /Localization/Options.

        Gets localization options.

        Returns:
            list of LocalizationOption: Response from the API. Localization
                options returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_localization_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_localization_options.")
            _url_path = "/Localization/Options"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_localization_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_localization_options."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_localization_options")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_localization_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, LocalizationOption.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_parental_ratings(self):
        """Does a GET request to /Localization/ParentalRatings.

        Gets known parental ratings.

        Returns:
            list of ParentalRating: Response from the API. Known parental
                ratings returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_parental_ratings called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_parental_ratings.")
            _url_path = "/Localization/ParentalRatings"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_parental_ratings.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_parental_ratings."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_parental_ratings")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_parental_ratings.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ParentalRating.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
