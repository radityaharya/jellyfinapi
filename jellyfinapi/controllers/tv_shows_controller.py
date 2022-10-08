# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class TvShowsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(TvShowsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_episodes(
        self,
        series_id,
        user_id=None,
        fields=None,
        season=None,
        season_id=None,
        is_missing=None,
        adjacent_to=None,
        start_item_id=None,
        start_index=None,
        limit=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
        sort_by=None,
    ):
        """Does a GET request to /Shows/{seriesId}/Episodes.

        Gets episodes for a tv season.

        Args:
            series_id (uuid|string): The series id.
            user_id (uuid|string, optional): The user id.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.
            season (int, optional): Optional filter by season number.
            season_id (uuid|string, optional): Optional. Filter by season id.
            is_missing (bool, optional): Optional. Filter by items that are
                missing episodes or not.
            adjacent_to (string, optional): Optional. Return items that are
                siblings of a supplied item.
            start_item_id (uuid|string, optional): Optional. Skip through the
                list until a given item is found.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            enable_images (bool, optional): Optional, include image
                information in output.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            sort_by (string, optional): Optional. Specify one or more sort
                orders, comma delimited. Options: Album, AlbumArtist, Artist,
                Budget, CommunityRating, CriticRating, DateCreated,
                DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName,
                Random, Revenue, Runtime.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_episodes called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_episodes.")
            _url_path = "/Shows/{seriesId}/Episodes"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"seriesId": {"value": series_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "fields": fields,
                "season": season,
                "seasonId": season_id,
                "isMissing": is_missing,
                "adjacentTo": adjacent_to,
                "startItemId": start_item_id,
                "startIndex": start_index,
                "limit": limit,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
                "sortBy": sort_by,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_episodes.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_episodes.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_episodes")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_episodes.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_seasons(
        self,
        series_id,
        user_id=None,
        fields=None,
        is_special_season=None,
        is_missing=None,
        adjacent_to=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
    ):
        """Does a GET request to /Shows/{seriesId}/Seasons.

        Gets seasons for a tv series.

        Args:
            series_id (uuid|string): The series id.
            user_id (uuid|string, optional): The user id.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.
            is_special_season (bool, optional): Optional. Filter by special
                season.
            is_missing (bool, optional): Optional. Filter by items that are
                missing episodes or not.
            adjacent_to (string, optional): Optional. Return items that are
                siblings of a supplied item.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. Include user data.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_seasons called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_seasons.")
            _url_path = "/Shows/{seriesId}/Seasons"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"seriesId": {"value": series_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "fields": fields,
                "isSpecialSeason": is_special_season,
                "isMissing": is_missing,
                "adjacentTo": adjacent_to,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_seasons.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_seasons.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_seasons")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_seasons.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_next_up(
        self,
        user_id=None,
        start_index=None,
        limit=None,
        fields=None,
        series_id=None,
        parent_id=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
        next_up_date_cutoff=None,
        enable_total_record_count=True,
        disable_first_episode=False,
        enable_rewatching=False,
    ):
        """Does a GET request to /Shows/NextUp.

        Gets a list of next up episodes.

        Args:
            user_id (uuid|string, optional): The user id of the user to get
                the next up episodes for.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            series_id (string, optional): Optional. Filter by series id.
            parent_id (uuid|string, optional): Optional. Specify this to
                localize the search to a specific item or folder. Omit to use
                the root.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            next_up_date_cutoff (datetime, optional): Optional. Starting date
                of shows to show in Next Up section.
            enable_total_record_count (bool, optional): Whether to enable the
                total records count. Defaults to true.
            disable_first_episode (bool, optional): Whether to disable sending
                the first episode in a series as next up.
            enable_rewatching (bool, optional): Whether to include watched
                episode in next up results.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_next_up called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_next_up.")
            _url_path = "/Shows/NextUp"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "fields": fields,
                "seriesId": series_id,
                "parentId": parent_id,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
                "nextUpDateCutoff": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, next_up_date_cutoff
                ),
                "enableTotalRecordCount": enable_total_record_count,
                "disableFirstEpisode": disable_first_episode,
                "enableRewatching": enable_rewatching,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_next_up.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_next_up.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_next_up")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_next_up.")
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

    def get_upcoming_episodes(
        self,
        user_id=None,
        start_index=None,
        limit=None,
        fields=None,
        parent_id=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
    ):
        """Does a GET request to /Shows/Upcoming.

        Gets a list of upcoming episodes.

        Args:
            user_id (uuid|string, optional): The user id of the user to get
                the upcoming episodes for.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            parent_id (uuid|string, optional): Optional. Specify this to
                localize the search to a specific item or folder. Omit to use
                the root.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. Include user data.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_upcoming_episodes called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_upcoming_episodes.")
            _url_path = "/Shows/Upcoming"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "fields": fields,
                "parentId": parent_id,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_upcoming_episodes.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_upcoming_episodes."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_upcoming_episodes")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_upcoming_episodes.")
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
