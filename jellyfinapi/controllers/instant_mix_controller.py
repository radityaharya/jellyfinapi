# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException


class InstantMixController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(InstantMixController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_instant_mix_from_album(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Albums/{id}/InstantMix.

        Creates an instant playlist based on a given album.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_album called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_album.")
            _url_path = "/Albums/{id}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_album.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_album."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_album"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_album.")
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

    def get_instant_mix_from_artists(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Artists/{id}/InstantMix.

        Creates an instant playlist based on a given artist.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_artists called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_artists.")
            _url_path = "/Artists/{id}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_artists.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_artists."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_artists"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_artists.")
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

    @deprecated()
    def get_instant_mix_from_artists_2(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Artists/InstantMix.

        Creates an instant playlist based on a given artist.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_artists_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_artists_2.")
            _url_path = "/Artists/InstantMix"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "id": id,
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_artists_2.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_artists_2."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_artists_2"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_artists_2.")
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

    def get_instant_mix_from_item(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Items/{id}/InstantMix.

        Creates an instant playlist based on a given item.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_item.")
            _url_path = "/Items/{id}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_item."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_instant_mix_from_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_item.")
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

    def get_instant_mix_from_music_genre_by_name(
        self,
        name,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /MusicGenres/{name}/InstantMix.

        Creates an instant playlist based on a given genre.

        Args:
            name (string): The genre name.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_music_genre_by_name called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_instant_mix_from_music_genre_by_name."
            )
            _url_path = "/MusicGenres/{name}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info(
                "Preparing headers for get_instant_mix_from_music_genre_by_name."
            )
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_music_genre_by_name."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_music_genre_by_name"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_instant_mix_from_music_genre_by_name."
            )
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

    def get_instant_mix_from_music_genre_by_id(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /MusicGenres/InstantMix.

        Creates an instant playlist based on a given genre.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_music_genre_by_id called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_instant_mix_from_music_genre_by_id."
            )
            _url_path = "/MusicGenres/InstantMix"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "id": id,
                "userId": user_id,
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
            self.logger.info(
                "Preparing headers for get_instant_mix_from_music_genre_by_id."
            )
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_music_genre_by_id."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_music_genre_by_id"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_instant_mix_from_music_genre_by_id."
            )
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

    def get_instant_mix_from_playlist(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Playlists/{id}/InstantMix.

        Creates an instant playlist based on a given playlist.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_playlist.")
            _url_path = "/Playlists/{id}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_playlist.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_playlist."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_instant_mix_from_playlist"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_playlist.")
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

    def get_instant_mix_from_song(
        self,
        id,
        user_id=None,
        limit=None,
        fields=None,
        enable_images=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
    ):
        """Does a GET request to /Songs/{id}/InstantMix.

        Creates an instant playlist based on a given song.

        Args:
            id (uuid|string): The item id.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
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
            BaseItemDtoQueryResult: Response from the API. Instant playlist
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_instant_mix_from_song called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_instant_mix_from_song.")
            _url_path = "/Songs/{id}/InstantMix"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
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
            self.logger.info("Preparing headers for get_instant_mix_from_song.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_instant_mix_from_song."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_instant_mix_from_song")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_instant_mix_from_song.")
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
