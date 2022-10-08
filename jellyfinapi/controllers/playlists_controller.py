# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.playlist_creation_result import PlaylistCreationResult
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException


class PlaylistsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(PlaylistsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def create_playlist(
        self, name=None, ids=None, user_id=None, media_type=None, body=None
    ):
        """Does a POST request to /Playlists.

        For backwards compatibility parameters can be sent via Query or Body,
        with Query having higher precedence.
        Query parameters are obsolete.

        Args:
            name (string, optional): The playlist name.
            ids (list of uuid|string, optional): The item ids.
            user_id (uuid|string, optional): The user id.
            media_type (string, optional): The media type.
            body (CreatePlaylistDto, optional): The create playlist payload.

        Returns:
            PlaylistCreationResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_playlist.")
            _url_path = "/Playlists"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "name": name,
                "ids": ids,
                "userId": user_id,
                "mediaType": media_type,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_playlist.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_playlist.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_playlist")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_playlist.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PlaylistCreationResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_to_playlist(self, playlist_id, ids=None, user_id=None):
        """Does a POST request to /Playlists/{playlistId}/Items.

        Adds items to a playlist.

        Args:
            playlist_id (uuid|string): The playlist id.
            ids (list of uuid|string, optional): Item id, comma delimited.
            user_id (uuid|string, optional): The userId.

        Returns:
            void: Response from the API. Items added to playlist.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_to_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_to_playlist.")
            _url_path = "/Playlists/{playlistId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"playlistId": {"value": playlist_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"ids": ids, "userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_to_playlist.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_to_playlist")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_to_playlist.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_from_playlist(self, playlist_id, entry_ids=None):
        """Does a DELETE request to /Playlists/{playlistId}/Items.

        Removes items from a playlist.

        Args:
            playlist_id (string): The playlist id.
            entry_ids (list of string, optional): The item ids, comma
                delimited.

        Returns:
            void: Response from the API. Items removed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("remove_from_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for remove_from_playlist.")
            _url_path = "/Playlists/{playlistId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"playlistId": {"value": playlist_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"entryIds": entry_ids}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for remove_from_playlist."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="remove_from_playlist")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for remove_from_playlist.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_playlist_items(
        self,
        playlist_id,
        user_id,
        start_index=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Playlists/{playlistId}/Items.

        Gets the original items of a playlist.

        Args:
            playlist_id (uuid|string): The playlist id.
            user_id (uuid|string): User id.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_images (bool, optional): Optional. Include image
                information in output.
            enable_user_data (bool, optional): Optional. Include user data.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Original playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_playlist_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_playlist_items.")
            _url_path = "/Playlists/{playlistId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"playlistId": {"value": playlist_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "fields": fields,
                "enableImages": enable_images,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_playlist_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_playlist_items.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_playlist_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_playlist_items.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise APIException("Playlist not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def move_item(self, playlist_id, item_id, new_index):
        """Does a POST request to /Playlists/{playlistId}/Items/{itemId}/Move/{newIndex}.

        Moves a playlist item.

        Args:
            playlist_id (string): The playlist id.
            item_id (string): The item id.
            new_index (int): The new index.

        Returns:
            void: Response from the API. Item moved to new index.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("move_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for move_item.")
            _url_path = "/Playlists/{playlistId}/Items/{itemId}/Move/{newIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "playlistId": {"value": playlist_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                    "newIndex": {"value": new_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for move_item.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="move_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for move_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
