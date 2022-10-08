# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.image_by_name_info import ImageByNameInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ImageByNameController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ImageByNameController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_general_images(self):
        """Does a GET request to /Images/General.

        Get all general images.

        Returns:
            list of ImageByNameInfo: Response from the API. Retrieved list of
                images.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_general_images called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_general_images.")
            _url_path = "/Images/General"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_general_images.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_general_images.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_general_images")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_general_images.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ImageByNameInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_general_image(self, name, mtype):
        """Does a GET request to /Images/General/{name}/{type}.

        Get General Image.

        Args:
            name (string): The name of the image.
            mtype (string): Image Type (primary, backdrop, logo, etc).

        Returns:
            mixed: Response from the API. Image stream retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_general_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_general_image.")
            _url_path = "/Images/General/{name}/{type}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "type": {"value": mtype, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_general_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_general_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_general_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_general_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Image not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_info_images(self):
        """Does a GET request to /Images/MediaInfo.

        Get all media info images.

        Returns:
            list of ImageByNameInfo: Response from the API. Image list
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_info_images called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_info_images.")
            _url_path = "/Images/MediaInfo"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_info_images.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_media_info_images."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_media_info_images")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_info_images.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ImageByNameInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_info_image(self, theme, name):
        """Does a GET request to /Images/MediaInfo/{theme}/{name}.

        Get media info image.

        Args:
            theme (string): The theme to get the image from.
            name (string): The name of the image.

        Returns:
            mixed: Response from the API. Image stream retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_info_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_info_image.")
            _url_path = "/Images/MediaInfo/{theme}/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "theme": {"value": theme, "encode": True},
                    "name": {"value": name, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_info_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_media_info_image."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_media_info_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_info_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Image not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_rating_images(self):
        """Does a GET request to /Images/Ratings.

        Get all general images.

        Returns:
            list of ImageByNameInfo: Response from the API. Retrieved list of
                images.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_rating_images called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_rating_images.")
            _url_path = "/Images/Ratings"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_rating_images.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_rating_images.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_rating_images")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_rating_images.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ImageByNameInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_rating_image(self, theme, name):
        """Does a GET request to /Images/Ratings/{theme}/{name}.

        Get rating image.

        Args:
            theme (string): The theme to get the image from.
            name (string): The name of the image.

        Returns:
            mixed: Response from the API. Image stream retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_rating_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_rating_image.")
            _url_path = "/Images/Ratings/{theme}/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "theme": {"value": theme, "encode": True},
                    "name": {"value": name, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_rating_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_rating_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_rating_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_rating_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Image not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
