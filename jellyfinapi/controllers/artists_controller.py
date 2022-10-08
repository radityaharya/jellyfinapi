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


class ArtistsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ArtistsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_artists(
        self,
        min_community_rating=None,
        start_index=None,
        limit=None,
        search_term=None,
        parent_id=None,
        fields=None,
        exclude_item_types=None,
        include_item_types=None,
        filters=None,
        is_favorite=None,
        media_types=None,
        genres=None,
        genre_ids=None,
        official_ratings=None,
        tags=None,
        years=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
        person=None,
        person_ids=None,
        person_types=None,
        studios=None,
        studio_ids=None,
        user_id=None,
        name_starts_with_or_greater=None,
        name_starts_with=None,
        name_less_than=None,
        sort_by=None,
        sort_order=None,
        enable_images=True,
        enable_total_record_count=True,
    ):
        """Does a GET request to /Artists.

        Gets all artists from a given item, folder, or the entire library.

        Args:
            min_community_rating (float, optional): Optional filter by minimum
                community rating.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            search_term (string, optional): Optional. Search term.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered out based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not.
            media_types (list of string, optional): Optional filter by
                MediaType. Allows multiple, comma delimited.
            genres (list of string, optional): Optional. If specified, results
                will be filtered based on genre. This allows multiple, pipe
                delimited.
            genre_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on genre id. This allows
                multiple, pipe delimited.
            official_ratings (list of string, optional): Optional. If
                specified, results will be filtered based on OfficialRating.
                This allows multiple, pipe delimited.
            tags (list of string, optional): Optional. If specified, results
                will be filtered based on tag. This allows multiple, pipe
                delimited.
            years (list of int, optional): Optional. If specified, results
                will be filtered based on production year. This allows
                multiple, comma delimited.
            enable_user_data (bool, optional): Optional, include user data.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            person (string, optional): Optional. If specified, results will be
                filtered to include only those containing the specified
                person.
            person_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified person ids.
            person_types (list of string, optional): Optional. If specified,
                along with Person, results will be filtered to include only
                those containing the specified person and PersonType. Allows
                multiple, comma-delimited.
            studios (list of string, optional): Optional. If specified,
                results will be filtered based on studio. This allows
                multiple, pipe delimited.
            studio_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on studio id. This
                allows multiple, pipe delimited.
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
            enable_total_record_count (bool, optional): Total record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Artists returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_artists called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_artists.")
            _url_path = "/Artists"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "minCommunityRating": min_community_rating,
                "startIndex": start_index,
                "limit": limit,
                "searchTerm": search_term,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "filters": filters,
                "isFavorite": is_favorite,
                "mediaTypes": media_types,
                "genres": genres,
                "genreIds": genre_ids,
                "officialRatings": official_ratings,
                "tags": tags,
                "years": years,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "person": person,
                "personIds": person_ids,
                "personTypes": person_types,
                "studios": studios,
                "studioIds": studio_ids,
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
            self.logger.info("Preparing headers for get_artists.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_artists.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_artists")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_artists.")
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

    def get_artist_by_name(self, name, user_id=None):
        """Does a GET request to /Artists/{name}.

        Gets an artist by name.

        Args:
            name (string): Studio name.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.

        Returns:
            BaseItemDto: Response from the API. Artist returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_artist_by_name called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_artist_by_name.")
            _url_path = "/Artists/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_artist_by_name.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_artist_by_name.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_artist_by_name")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_artist_by_name.")
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

    def get_album_artists(
        self,
        min_community_rating=None,
        start_index=None,
        limit=None,
        search_term=None,
        parent_id=None,
        fields=None,
        exclude_item_types=None,
        include_item_types=None,
        filters=None,
        is_favorite=None,
        media_types=None,
        genres=None,
        genre_ids=None,
        official_ratings=None,
        tags=None,
        years=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
        person=None,
        person_ids=None,
        person_types=None,
        studios=None,
        studio_ids=None,
        user_id=None,
        name_starts_with_or_greater=None,
        name_starts_with=None,
        name_less_than=None,
        sort_by=None,
        sort_order=None,
        enable_images=True,
        enable_total_record_count=True,
    ):
        """Does a GET request to /Artists/AlbumArtists.

        Gets all album artists from a given item, folder, or the entire
        library.

        Args:
            min_community_rating (float, optional): Optional filter by minimum
                community rating.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            search_term (string, optional): Optional. Search term.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered out based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not.
            media_types (list of string, optional): Optional filter by
                MediaType. Allows multiple, comma delimited.
            genres (list of string, optional): Optional. If specified, results
                will be filtered based on genre. This allows multiple, pipe
                delimited.
            genre_ids (list of uuid|string, optional): Optional. If specified,
                results will be filtered based on genre id. This allows
                multiple, pipe delimited.
            official_ratings (list of string, optional): Optional. If
                specified, results will be filtered based on OfficialRating.
                This allows multiple, pipe delimited.
            tags (list of string, optional): Optional. If specified, results
                will be filtered based on tag. This allows multiple, pipe
                delimited.
            years (list of int, optional): Optional. If specified, results
                will be filtered based on production year. This allows
                multiple, comma delimited.
            enable_user_data (bool, optional): Optional, include user data.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            person (string, optional): Optional. If specified, results will be
                filtered to include only those containing the specified
                person.
            person_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered to include only those
                containing the specified person ids.
            person_types (list of string, optional): Optional. If specified,
                along with Person, results will be filtered to include only
                those containing the specified person and PersonType. Allows
                multiple, comma-delimited.
            studios (list of string, optional): Optional. If specified,
                results will be filtered based on studio. This allows
                multiple, pipe delimited.
            studio_ids (list of uuid|string, optional): Optional. If
                specified, results will be filtered based on studio id. This
                allows multiple, pipe delimited.
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
            enable_total_record_count (bool, optional): Total record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Album artists
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_album_artists called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_album_artists.")
            _url_path = "/Artists/AlbumArtists"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "minCommunityRating": min_community_rating,
                "startIndex": start_index,
                "limit": limit,
                "searchTerm": search_term,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "filters": filters,
                "isFavorite": is_favorite,
                "mediaTypes": media_types,
                "genres": genres,
                "genreIds": genre_ids,
                "officialRatings": official_ratings,
                "tags": tags,
                "years": years,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "person": person,
                "personIds": person_ids,
                "personTypes": person_types,
                "studios": studios,
                "studioIds": studio_ids,
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
            self.logger.info("Preparing headers for get_album_artists.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_album_artists.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_album_artists")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_album_artists.")
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
