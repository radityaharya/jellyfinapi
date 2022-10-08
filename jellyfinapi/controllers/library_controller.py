# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.all_theme_media_result import AllThemeMediaResult
from jellyfinapi.models.theme_media_result import ThemeMediaResult
from jellyfinapi.models.item_counts import ItemCounts
from jellyfinapi.models.library_options_result_dto import LibraryOptionsResultDto
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException
from jellyfinapi.exceptions.api_exception import APIException


class LibraryController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(LibraryController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def delete_items(self, ids=None):
        """Does a DELETE request to /Items.

        Deletes items from the library and filesystem.

        Args:
            ids (list of uuid|string, optional): The item ids.

        Returns:
            void: Response from the API. Items deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_items.")
            _url_path = "/Items"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"ids": ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_items.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_items.")
            if _response.status_code == 401:
                raise ProblemDetailsException("Unauthorized access.", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_item(self, item_id):
        """Does a DELETE request to /Items/{itemId}.

        Deletes an item from the library and filesystem.

        Args:
            item_id (uuid|string): The item id.

        Returns:
            void: Response from the API. Item deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_item.")
            _url_path = "/Items/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_item.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_item.")
            if _response.status_code == 401:
                raise ProblemDetailsException("Unauthorized access.", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_similar_albums(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Albums/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_albums called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_albums.")
            _url_path = "/Albums/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_albums.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_similar_albums.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_albums")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_albums.")
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

    def get_similar_artists(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Artists/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_artists called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_artists.")
            _url_path = "/Artists/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_artists.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_similar_artists.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_artists")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_artists.")
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

    def get_ancestors(self, item_id, user_id=None):
        """Does a GET request to /Items/{itemId}/Ancestors.

        Gets all parents of an item.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.

        Returns:
            list of BaseItemDto: Response from the API. Item parents
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_ancestors called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_ancestors.")
            _url_path = "/Items/{itemId}/Ancestors"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_ancestors.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_ancestors.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_ancestors")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_ancestors.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    @deprecated()
    def get_critic_reviews(self, item_id):
        """Does a GET request to /Items/{itemId}/CriticReviews.

        Gets critic review for an item.

        Args:
            item_id (string): TODO: type description here.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Critic reviews
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_critic_reviews called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_critic_reviews.")
            _url_path = "/Items/{itemId}/CriticReviews"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_critic_reviews.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_critic_reviews.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_critic_reviews")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_critic_reviews.")
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

    def get_download(self, item_id):
        """Does a GET request to /Items/{itemId}/Download.

        Downloads item media.

        Args:
            item_id (uuid|string): The item id.

        Returns:
            mixed: Response from the API. Media downloaded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_download called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_download.")
            _url_path = "/Items/{itemId}/Download"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_download.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_download.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_download")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_download.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_file(self, item_id):
        """Does a GET request to /Items/{itemId}/File.

        Get the original file of an item.

        Args:
            item_id (uuid|string): The item id.

        Returns:
            mixed: Response from the API. File stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_file called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_file.")
            _url_path = "/Items/{itemId}/File"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_file.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_file.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_file")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_file.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_similar_items(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Items/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_items.")
            _url_path = "/Items/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_similar_items.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_items.")
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

    def get_theme_media(self, item_id, user_id=None, inherit_from_parent=False):
        """Does a GET request to /Items/{itemId}/ThemeMedia.

        Get theme songs and videos for an item.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            inherit_from_parent (bool, optional): Optional. Determines whether
                or not parent items should be searched for theme media.

        Returns:
            AllThemeMediaResult: Response from the API. Theme songs and videos
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_theme_media called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_theme_media.")
            _url_path = "/Items/{itemId}/ThemeMedia"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "inheritFromParent": inherit_from_parent,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_theme_media.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_theme_media.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_theme_media")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_theme_media.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise APIException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, AllThemeMediaResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_theme_songs(self, item_id, user_id=None, inherit_from_parent=False):
        """Does a GET request to /Items/{itemId}/ThemeSongs.

        Get theme songs for an item.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            inherit_from_parent (bool, optional): Optional. Determines whether
                or not parent items should be searched for theme media.

        Returns:
            ThemeMediaResult: Response from the API. Theme songs returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_theme_songs called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_theme_songs.")
            _url_path = "/Items/{itemId}/ThemeSongs"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "inheritFromParent": inherit_from_parent,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_theme_songs.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_theme_songs.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_theme_songs")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_theme_songs.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ThemeMediaResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_theme_videos(self, item_id, user_id=None, inherit_from_parent=False):
        """Does a GET request to /Items/{itemId}/ThemeVideos.

        Get theme videos for an item.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            inherit_from_parent (bool, optional): Optional. Determines whether
                or not parent items should be searched for theme media.

        Returns:
            ThemeMediaResult: Response from the API. Theme videos returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_theme_videos called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_theme_videos.")
            _url_path = "/Items/{itemId}/ThemeVideos"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "inheritFromParent": inherit_from_parent,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_theme_videos.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_theme_videos.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_theme_videos")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_theme_videos.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ThemeMediaResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item_counts(self, user_id=None, is_favorite=None):
        """Does a GET request to /Items/Counts.

        Get item counts.

        Args:
            user_id (uuid|string, optional): Optional. Get counts from a
                specific user's library.
            is_favorite (bool, optional): Optional. Get counts of favorite
                items.

        Returns:
            ItemCounts: Response from the API. Item counts returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item_counts called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item_counts.")
            _url_path = "/Items/Counts"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id, "isFavorite": is_favorite}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item_counts.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_item_counts.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item_counts")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item_counts.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ItemCounts.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_library_options_info(self, library_content_type=None, is_new_library=False):
        """Does a GET request to /Libraries/AvailableOptions.

        Gets the library options info.

        Args:
            library_content_type (string, optional): Library content type.
            is_new_library (bool, optional): Whether this is a new library.

        Returns:
            LibraryOptionsResultDto: Response from the API. Library options
                info returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_library_options_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_library_options_info.")
            _url_path = "/Libraries/AvailableOptions"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "libraryContentType": library_content_type,
                "isNewLibrary": is_new_library,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_library_options_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_library_options_info."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_library_options_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_library_options_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, LibraryOptionsResultDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_updated_media(self, body):
        """Does a POST request to /Library/Media/Updated.

        Reports that new movies have been added by an external source.

        Args:
            body (MediaUpdateInfoDto): The update paths.

        Returns:
            void: Response from the API. Report success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_updated_media called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_updated_media.")
            _url_path = "/Library/Media/Updated"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for post_updated_media.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_updated_media.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_updated_media")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_updated_media.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_folders(self, is_hidden=None):
        """Does a GET request to /Library/MediaFolders.

        Gets all user media folders.

        Args:
            is_hidden (bool, optional): Optional. Filter by folders that are
                marked hidden, or not.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Media folders
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_folders called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_folders.")
            _url_path = "/Library/MediaFolders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"isHidden": is_hidden}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_folders.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_media_folders.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_media_folders")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_folders.")
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

    def post_added_movies(self, tmdb_id=None, imdb_id=None):
        """Does a POST request to /Library/Movies/Added.

        Reports that new movies have been added by an external source.

        Args:
            tmdb_id (string, optional): The tmdbId.
            imdb_id (string, optional): The imdbId.

        Returns:
            void: Response from the API. Report success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_added_movies called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_added_movies.")
            _url_path = "/Library/Movies/Added"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"tmdbId": tmdb_id, "imdbId": imdb_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_added_movies.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_added_movies")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_added_movies.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_updated_movies(self, tmdb_id=None, imdb_id=None):
        """Does a POST request to /Library/Movies/Updated.

        Reports that new movies have been added by an external source.

        Args:
            tmdb_id (string, optional): The tmdbId.
            imdb_id (string, optional): The imdbId.

        Returns:
            void: Response from the API. Report success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_updated_movies called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_updated_movies.")
            _url_path = "/Library/Movies/Updated"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"tmdbId": tmdb_id, "imdbId": imdb_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_updated_movies.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_updated_movies")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_updated_movies.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_physical_paths(self):
        """Does a GET request to /Library/PhysicalPaths.

        Gets a list of physical paths from virtual folders.

        Returns:
            list of string: Response from the API. Physical paths returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_physical_paths called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_physical_paths.")
            _url_path = "/Library/PhysicalPaths"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_physical_paths.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_physical_paths.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_physical_paths")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_physical_paths.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def refresh_library(self):
        """Does a POST request to /Library/Refresh.

        Starts a library scan.

        Returns:
            void: Response from the API. Library scan started.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("refresh_library called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for refresh_library.")
            _url_path = "/Library/Refresh"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for refresh_library.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="refresh_library")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for refresh_library.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_added_series(self, tvdb_id=None):
        """Does a POST request to /Library/Series/Added.

        Reports that new episodes of a series have been added by an external
        source.

        Args:
            tvdb_id (string, optional): The tvdbId.

        Returns:
            void: Response from the API. Report success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_added_series called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_added_series.")
            _url_path = "/Library/Series/Added"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"tvdbId": tvdb_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_added_series.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_added_series")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_added_series.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_updated_series(self, tvdb_id=None):
        """Does a POST request to /Library/Series/Updated.

        Reports that new episodes of a series have been added by an external
        source.

        Args:
            tvdb_id (string, optional): The tvdbId.

        Returns:
            void: Response from the API. Report success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_updated_series called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_updated_series.")
            _url_path = "/Library/Series/Updated"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"tvdbId": tvdb_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_updated_series.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_updated_series")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_updated_series.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_similar_movies(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Movies/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_movies called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_movies.")
            _url_path = "/Movies/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_movies.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_similar_movies.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_movies")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_movies.")
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

    def get_similar_shows(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Shows/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_shows called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_shows.")
            _url_path = "/Shows/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_shows.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_similar_shows.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_shows")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_shows.")
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

    def get_similar_trailers(
        self, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None
    ):
        """Does a GET request to /Trailers/{itemId}/Similar.

        Gets similar items.

        Args:
            item_id (uuid|string): The item id.
            exclude_artist_ids (list of uuid|string, optional): Exclude artist
                ids.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output. This
                allows multiple, comma delimited. Options: Budget, Chapters,
                DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams,
                Overview, ParentId, Path, People, ProviderIds,
                PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines,
                TrailerUrls.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Similar items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_similar_trailers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_similar_trailers.")
            _url_path = "/Trailers/{itemId}/Similar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "excludeArtistIds": exclude_artist_ids,
                "userId": user_id,
                "limit": limit,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_similar_trailers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_similar_trailers."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_similar_trailers")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_similar_trailers.")
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
