# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.trakt_sync_response import TraktSyncResponse
from jellyfinapi.models.trakt_movie import TraktMovie
from jellyfinapi.models.trakt_show import TraktShow
from jellyfinapi.exceptions.api_exception import APIException


class TraktController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(TraktController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def trakt_device_authorization(self, user_guid):
        """Does a POST request to /Trakt/Users/{userGuid}/Authorize.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("trakt_device_authorization called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for trakt_device_authorization.")
            _url_path = "/Trakt/Users/{userGuid}/Authorize"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userGuid": {"value": user_guid, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for trakt_device_authorization."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="trakt_device_authorization"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for trakt_device_authorization.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def trakt_device_de_authorization(self, user_guid):
        """Does a POST request to /Trakt/Users/{userGuid}/Deauthorize.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.

        Returns:
            string: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("trakt_device_de_authorization called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for trakt_device_de_authorization.")
            _url_path = "/Trakt/Users/{userGuid}/Deauthorize"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userGuid": {"value": user_guid, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for trakt_device_de_authorization."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="trakt_device_de_authorization"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for trakt_device_de_authorization.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def trakt_rate_item(self, user_guid, item_id, rating=None):
        """Does a POST request to /Trakt/Users/{userGuid}/Items/{itemId}/Rate.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.
            item_id (uuid|string): TODO: type description here.
            rating (int, optional): TODO: type description here.

        Returns:
            TraktSyncResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("trakt_rate_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for trakt_rate_item.")
            _url_path = "/Trakt/Users/{userGuid}/Items/{itemId}/Rate"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userGuid": {"value": user_guid, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"rating": rating}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for trakt_rate_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for trakt_rate_item.")
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="trakt_rate_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for trakt_rate_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TraktSyncResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def trakt_poll_authorization_status(self, user_guid):
        """Does a GET request to /Trakt/Users/{userGuid}/PollAuthorizationStatus.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("trakt_poll_authorization_status called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for trakt_poll_authorization_status.")
            _url_path = "/Trakt/Users/{userGuid}/PollAuthorizationStatus"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userGuid": {"value": user_guid, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for trakt_poll_authorization_status."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="trakt_poll_authorization_status"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for trakt_poll_authorization_status.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def recommended_trakt_movies(self, user_guid):
        """Does a POST request to /Trakt/Users/{userGuid}/RecommendedMovies.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.

        Returns:
            list of TraktMovie: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("recommended_trakt_movies called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for recommended_trakt_movies.")
            _url_path = "/Trakt/Users/{userGuid}/RecommendedMovies"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userGuid": {"value": user_guid, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for recommended_trakt_movies.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for recommended_trakt_movies."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="recommended_trakt_movies")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for recommended_trakt_movies.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TraktMovie.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def recommended_trakt_shows(self, user_guid):
        """Does a POST request to /Trakt/Users/{userGuid}/RecommendedShows.

        TODO: type endpoint description here.

        Args:
            user_guid (uuid|string): TODO: type description here.

        Returns:
            list of TraktShow: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("recommended_trakt_shows called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for recommended_trakt_shows.")
            _url_path = "/Trakt/Users/{userGuid}/RecommendedShows"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userGuid": {"value": user_guid, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for recommended_trakt_shows.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for recommended_trakt_shows."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="recommended_trakt_shows")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for recommended_trakt_shows.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TraktShow.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
