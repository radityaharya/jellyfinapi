# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.search_hint_result import SearchHintResult
from jellyfinapi.exceptions.api_exception import APIException


class SearchController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SearchController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get(
        self,
        search_term,
        start_index=None,
        limit=None,
        user_id=None,
        include_item_types=None,
        exclude_item_types=None,
        media_types=None,
        parent_id=None,
        is_movie=None,
        is_series=None,
        is_news=None,
        is_kids=None,
        is_sports=None,
        include_people=True,
        include_media=True,
        include_genres=True,
        include_studios=True,
        include_artists=True,
    ):
        """Does a GET request to /Search/Hints.

        Gets the search hint result.

        Args:
            search_term (string): The search term to filter on.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            user_id (uuid|string, optional): Optional. Supply a user id to
                search within a user's library or omit to search all.
            include_item_types (list of BaseItemKindEnum, optional): If
                specified, only results with the specified item types are
                returned. This allows multiple, comma delimeted.
            exclude_item_types (list of BaseItemKindEnum, optional): If
                specified, results with these item types are filtered out.
                This allows multiple, comma delimeted.
            media_types (list of string, optional): If specified, only results
                with the specified media types are returned. This allows
                multiple, comma delimeted.
            parent_id (uuid|string, optional): If specified, only children of
                the parent are returned.
            is_movie (bool, optional): Optional filter for movies.
            is_series (bool, optional): Optional filter for series.
            is_news (bool, optional): Optional filter for news.
            is_kids (bool, optional): Optional filter for kids.
            is_sports (bool, optional): Optional filter for sports.
            include_people (bool, optional): Optional filter whether to
                include people.
            include_media (bool, optional): Optional filter whether to include
                media.
            include_genres (bool, optional): Optional filter whether to
                include genres.
            include_studios (bool, optional): Optional filter whether to
                include studios.
            include_artists (bool, optional): Optional filter whether to
                include artists.

        Returns:
            SearchHintResult: Response from the API. Search hint returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get.")
            _url_path = "/Search/Hints"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "searchTerm": search_term,
                "startIndex": start_index,
                "limit": limit,
                "userId": user_id,
                "includeItemTypes": include_item_types,
                "excludeItemTypes": exclude_item_types,
                "mediaTypes": media_types,
                "parentId": parent_id,
                "isMovie": is_movie,
                "isSeries": is_series,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "includePeople": include_people,
                "includeMedia": include_media,
                "includeGenres": include_genres,
                "includeStudios": include_studios,
                "includeArtists": include_artists,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SearchHintResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
