# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.collection_creation_result import CollectionCreationResult
from jellyfinapi.exceptions.api_exception import APIException


class CollectionController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(CollectionController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def create_collection(self, name=None, ids=None, parent_id=None, is_locked=False):
        """Does a POST request to /Collections.

        Creates a new collection.

        Args:
            name (string, optional): The name of the collection.
            ids (list of string, optional): Item Ids to add to the
                collection.
            parent_id (uuid|string, optional): Optional. Create the collection
                within a specific folder.
            is_locked (bool, optional): Whether or not to lock the new
                collection.

        Returns:
            CollectionCreationResult: Response from the API. Collection
                created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_collection called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_collection.")
            _url_path = "/Collections"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "name": name,
                "ids": ids,
                "parentId": parent_id,
                "isLocked": is_locked,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_collection.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_collection.")
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_collection")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_collection.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, CollectionCreationResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_to_collection(self, collection_id, ids):
        """Does a POST request to /Collections/{collectionId}/Items.

        Adds items to a collection.

        Args:
            collection_id (uuid|string): The collection id.
            ids (list of uuid|string): Item ids, comma delimited.

        Returns:
            void: Response from the API. Items added to collection.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_to_collection called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_to_collection.")
            _url_path = "/Collections/{collectionId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"collectionId": {"value": collection_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"ids": ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_to_collection.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_to_collection")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_to_collection.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_from_collection(self, collection_id, ids):
        """Does a DELETE request to /Collections/{collectionId}/Items.

        Removes items from a collection.

        Args:
            collection_id (uuid|string): The collection id.
            ids (list of uuid|string): Item ids, comma delimited.

        Returns:
            void: Response from the API. Items removed from collection.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("remove_from_collection called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for remove_from_collection.")
            _url_path = "/Collections/{collectionId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"collectionId": {"value": collection_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"ids": ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for remove_from_collection."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="remove_from_collection")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for remove_from_collection.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
