# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.query_filters_legacy import QueryFiltersLegacy
from jellyfinapi.models.query_filters import QueryFilters
from jellyfinapi.exceptions.api_exception import APIException


class FilterController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(FilterController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_query_filters_legacy(
        self, user_id=None, parent_id=None, include_item_types=None, media_types=None
    ):
        """Does a GET request to /Items/Filters.

        Gets legacy query filters.

        Args:
            user_id (uuid|string, optional): Optional. User id.
            parent_id (uuid|string, optional): Optional. Parent id.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            media_types (list of string, optional): Optional. Filter by
                MediaType. Allows multiple, comma delimited.

        Returns:
            QueryFiltersLegacy: Response from the API. Legacy filters
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_query_filters_legacy called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_query_filters_legacy.")
            _url_path = "/Items/Filters"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "parentId": parent_id,
                "includeItemTypes": include_item_types,
                "mediaTypes": media_types,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_query_filters_legacy.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_query_filters_legacy."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_query_filters_legacy")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_query_filters_legacy.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, QueryFiltersLegacy.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_query_filters(
        self,
        user_id=None,
        parent_id=None,
        include_item_types=None,
        is_airing=None,
        is_movie=None,
        is_sports=None,
        is_kids=None,
        is_news=None,
        is_series=None,
        recursive=None,
    ):
        """Does a GET request to /Items/Filters2.

        Gets query filters.

        Args:
            user_id (uuid|string, optional): Optional. User id.
            parent_id (uuid|string, optional): Optional. Specify this to
                localize the search to a specific item or folder. Omit to use
                the root.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            is_airing (bool, optional): Optional. Is item airing.
            is_movie (bool, optional): Optional. Is item movie.
            is_sports (bool, optional): Optional. Is item sports.
            is_kids (bool, optional): Optional. Is item kids.
            is_news (bool, optional): Optional. Is item news.
            is_series (bool, optional): Optional. Is item series.
            recursive (bool, optional): Optional. Search recursive.

        Returns:
            QueryFilters: Response from the API. Filters retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_query_filters called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_query_filters.")
            _url_path = "/Items/Filters2"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "parentId": parent_id,
                "includeItemTypes": include_item_types,
                "isAiring": is_airing,
                "isMovie": is_movie,
                "isSports": is_sports,
                "isKids": is_kids,
                "isNews": is_news,
                "isSeries": is_series,
                "recursive": recursive,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_query_filters.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_query_filters.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_query_filters")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_query_filters.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, QueryFilters.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
