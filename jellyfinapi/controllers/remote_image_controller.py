# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.remote_image_result import RemoteImageResult
from jellyfinapi.models.image_provider_info import ImageProviderInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class RemoteImageController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(RemoteImageController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_remote_images(
        self,
        item_id,
        mtype=None,
        start_index=None,
        limit=None,
        provider_name=None,
        include_all_languages=False,
    ):
        """Does a GET request to /Items/{itemId}/RemoteImages.

        Gets available remote images for an item.

        Args:
            item_id (uuid|string): Item Id.
            mtype (ImageTypeEnum, optional): The image type.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            provider_name (string, optional): Optional. The image provider to
                use.
            include_all_languages (bool, optional): Optional. Include all
                languages.

        Returns:
            RemoteImageResult: Response from the API. Remote Images returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_remote_images called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_remote_images.")
            _url_path = "/Items/{itemId}/RemoteImages"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "type": mtype,
                "startIndex": start_index,
                "limit": limit,
                "providerName": provider_name,
                "includeAllLanguages": include_all_languages,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_remote_images.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_remote_images.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_remote_images")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_remote_images.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteImageResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def download_remote_image(self, item_id, mtype, image_url=None):
        """Does a POST request to /Items/{itemId}/RemoteImages/Download.

        Downloads a remote image for an item.

        Args:
            item_id (uuid|string): Item Id.
            mtype (ImageTypeEnum): The image type.
            image_url (string, optional): The image url.

        Returns:
            void: Response from the API. Remote image downloaded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("download_remote_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for download_remote_image.")
            _url_path = "/Items/{itemId}/RemoteImages/Download"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"type": mtype, "imageUrl": image_url}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for download_remote_image."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="download_remote_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for download_remote_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Remote image not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_remote_image_providers(self, item_id):
        """Does a GET request to /Items/{itemId}/RemoteImages/Providers.

        Gets available remote image providers for an item.

        Args:
            item_id (uuid|string): Item Id.

        Returns:
            list of ImageProviderInfo: Response from the API. Returned remote
                image providers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_remote_image_providers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_remote_image_providers.")
            _url_path = "/Items/{itemId}/RemoteImages/Providers"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_remote_image_providers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_remote_image_providers."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_remote_image_providers"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_remote_image_providers.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ImageProviderInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
