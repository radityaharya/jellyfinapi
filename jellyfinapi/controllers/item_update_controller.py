# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.metadata_editor_info import MetadataEditorInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ItemUpdateController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ItemUpdateController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def update_item(self, item_id, body):
        """Does a POST request to /Items/{itemId}.

        Updates an item.

        Args:
            item_id (uuid|string): The item id.
            body (BaseItemDto): The new item properties.

        Returns:
            void: Response from the API. Item updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_item.")
            _url_path = "/Items/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_item.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_item.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_item_content_type(self, item_id, content_type=None):
        """Does a POST request to /Items/{itemId}/ContentType.

        Updates an item's content type.

        Args:
            item_id (uuid|string): The item id.
            content_type (string, optional): The content type of the item.

        Returns:
            void: Response from the API. Item content type updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_item_content_type called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_item_content_type.")
            _url_path = "/Items/{itemId}/ContentType"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"contentType": content_type}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_item_content_type."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_item_content_type")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_item_content_type.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_metadata_editor_info(self, item_id):
        """Does a GET request to /Items/{itemId}/MetadataEditor.

        Gets metadata editor info for an item.

        Args:
            item_id (uuid|string): The item id.

        Returns:
            MetadataEditorInfo: Response from the API. Item metadata editor
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_metadata_editor_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_metadata_editor_info.")
            _url_path = "/Items/{itemId}/MetadataEditor"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_metadata_editor_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_metadata_editor_info."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_metadata_editor_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_metadata_editor_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, MetadataEditorInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
