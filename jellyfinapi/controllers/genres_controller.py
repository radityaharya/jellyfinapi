# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.exceptions.api_exception import APIException


class GenresController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(GenresController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_genres(
        self,
        start_index=None,
        limit=None,
        search_term=None,
        parent_id=None,
        fields=None,
        exclude_item_types=None,
        include_item_types=None,
        is_favorite=None,
        image_type_limit=None,
        enable_image_types=None,
        user_id=None,
        name_starts_with_or_greater=None,
        name_starts_with=None,
        name_less_than=None,
        sort_by=None,
        sort_order=None,
        enable_images=True,
        enable_total_record_count=True,
    ):
        """Does a GET request to /Genres.

        Gets all genres from a given item, folder, or the entire library.

        Args:
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            search_term (string, optional): The search term.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered out based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered in based on item type.
                This allows multiple, comma delimited.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            user_id (uuid|string, optional): User id.
            name_starts_with_or_greater (string, optional): Optional filter by
                items whose name is sorted equally or greater than a given
                input string.
            name_starts_with (string, optional): Optional filter by items
                whose name is sorted equally than a given input string.
            name_less_than (string, optional): Optional filter by items whose
                name is equally or lesser than a given input string.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited.
            sort_order (list of SortOrderEnum, optional): Sort Order -
                Ascending,Descending.
            enable_images (bool, optional): Optional, include image
                information in output.
            enable_total_record_count (bool, optional): Optional. Include
                total record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Genres returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_genres called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_genres.")
            _url_path = "/Genres"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "startIndex": start_index,
                "limit": limit,
                "searchTerm": search_term,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "isFavorite": is_favorite,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "userId": user_id,
                "nameStartsWithOrGreater": name_starts_with_or_greater,
                "nameStartsWith": name_starts_with,
                "nameLessThan": name_less_than,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "enableImages": enable_images,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_genres.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_genres.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_genres")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_genres.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_genre(self, genre_name, user_id=None):
        """Does a GET request to /Genres/{genreName}.

        Gets a genre, by name.

        Args:
            genre_name (string): The genre name.
            user_id (uuid|string, optional): The user id.

        Returns:
            BaseItemDto: Response from the API. Genres returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_genre called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_genre.")
            _url_path = "/Genres/{genreName}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"genreName": {"value": genre_name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_genre.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_genre.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_genre")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_genre.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
