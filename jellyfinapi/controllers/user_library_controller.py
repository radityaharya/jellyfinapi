# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.user_item_data_dto import UserItemDataDto
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException


class UserLibraryController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(UserLibraryController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def mark_favorite_item(self, user_id, item_id):
        """Does a POST request to /Users/{userId}/FavoriteItems/{itemId}.

        Marks an item as a favorite.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            UserItemDataDto: Response from the API. Item marked as favorite.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("mark_favorite_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for mark_favorite_item.")
            _url_path = "/Users/{userId}/FavoriteItems/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for mark_favorite_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for mark_favorite_item.")
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="mark_favorite_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for mark_favorite_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserItemDataDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def unmark_favorite_item(self, user_id, item_id):
        """Does a DELETE request to /Users/{userId}/FavoriteItems/{itemId}.

        Unmarks item as a favorite.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            UserItemDataDto: Response from the API. Item unmarked as
                favorite.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("unmark_favorite_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for unmark_favorite_item.")
            _url_path = "/Users/{userId}/FavoriteItems/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for unmark_favorite_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for unmark_favorite_item."
            )
            _request = self.config.http_client.delete(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="unmark_favorite_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for unmark_favorite_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserItemDataDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item(self, user_id, item_id):
        """Does a GET request to /Users/{userId}/Items/{itemId}.

        Gets an item from a user's library.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            BaseItemDto: Response from the API. Item returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item.")
            _url_path = "/Users/{userId}/Items/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_item.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item.")
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

    def get_intros(self, user_id, item_id):
        """Does a GET request to /Users/{userId}/Items/{itemId}/Intros.

        Gets intros to play before the main media item plays.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Intros returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_intros called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_intros.")
            _url_path = "/Users/{userId}/Items/{itemId}/Intros"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_intros.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_intros.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_intros")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_intros.")
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

    def get_local_trailers(self, user_id, item_id):
        """Does a GET request to /Users/{userId}/Items/{itemId}/LocalTrailers.

        Gets local trailers for an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            list of BaseItemDto: Response from the API. An
                Microsoft.AspNetCore.Mvc.OkResult containing the item's local
                trailers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_local_trailers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_local_trailers.")
            _url_path = "/Users/{userId}/Items/{itemId}/LocalTrailers"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_local_trailers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_local_trailers.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_local_trailers")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_local_trailers.")
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

    def delete_user_item_rating(self, user_id, item_id):
        """Does a DELETE request to /Users/{userId}/Items/{itemId}/Rating.

        Deletes a user's saved personal rating for an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            UserItemDataDto: Response from the API. Personal rating removed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_user_item_rating called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_user_item_rating.")
            _url_path = "/Users/{userId}/Items/{itemId}/Rating"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for delete_user_item_rating.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for delete_user_item_rating."
            )
            _request = self.config.http_client.delete(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_user_item_rating")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_user_item_rating.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserItemDataDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user_item_rating(self, user_id, item_id, likes=None):
        """Does a POST request to /Users/{userId}/Items/{itemId}/Rating.

        Updates a user's rating for an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.
            likes (bool, optional): Whether this
                M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItem
                Rating(System.Guid,System.Guid,System.Nullable{System.Boolean})
                is likes.

        Returns:
            UserItemDataDto: Response from the API. Item rating updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user_item_rating called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user_item_rating.")
            _url_path = "/Users/{userId}/Items/{itemId}/Rating"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"likes": likes}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user_item_rating.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_user_item_rating."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user_item_rating")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user_item_rating.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserItemDataDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_special_features(self, user_id, item_id):
        """Does a GET request to /Users/{userId}/Items/{itemId}/SpecialFeatures.

        Gets special features for an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            list of BaseItemDto: Response from the API. Special features
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_special_features called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_special_features.")
            _url_path = "/Users/{userId}/Items/{itemId}/SpecialFeatures"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_special_features.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_special_features."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_special_features")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_special_features.")
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

    def get_latest_media(
        self,
        user_id,
        parent_id=None,
        fields=None,
        include_item_types=None,
        is_played=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
        limit=20,
        group_items=True,
    ):
        """Does a GET request to /Users/{userId}/Items/Latest.

        Gets latest media.

        Args:
            user_id (uuid|string): User id.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be filtered based on item type.
                This allows multiple, comma delimited.
            is_played (bool, optional): Filter by items that are played, or
                not.
            enable_images (bool, optional): Optional. include image
                information in output.
            image_type_limit (int, optional): Optional. the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. include user data.
            limit (int, optional): Return item limit.
            group_items (bool, optional): Whether or not to group items into a
                parent container.

        Returns:
            list of BaseItemDto: Response from the API. Latest media
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_latest_media called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_latest_media.")
            _url_path = "/Users/{userId}/Items/Latest"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "parentId": parent_id,
                "fields": fields,
                "includeItemTypes": include_item_types,
                "isPlayed": is_played,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
                "limit": limit,
                "groupItems": group_items,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_latest_media.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_latest_media.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_latest_media")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_latest_media.")
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

    def get_root_folder(self, user_id):
        """Does a GET request to /Users/{userId}/Items/Root.

        Gets the root folder from a user's library.

        Args:
            user_id (uuid|string): User id.

        Returns:
            BaseItemDto: Response from the API. Root folder returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_root_folder called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_root_folder.")
            _url_path = "/Users/{userId}/Items/Root"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_root_folder.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_root_folder.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_root_folder")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_root_folder.")
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
