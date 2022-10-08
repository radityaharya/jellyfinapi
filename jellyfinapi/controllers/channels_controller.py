# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.models.channel_features import ChannelFeatures
from jellyfinapi.exceptions.api_exception import APIException


class ChannelsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ChannelsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_channels(
        self,
        user_id=None,
        start_index=None,
        limit=None,
        supports_latest_items=None,
        supports_media_deletion=None,
        is_favorite=None,
    ):
        """Does a GET request to /Channels.

        Gets available channels.

        Args:
            user_id (uuid|string, optional): User Id to filter by. Use
                System.Guid.Empty to not filter by user.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            supports_latest_items (bool, optional): Optional. Filter by
                channels that support getting latest items.
            supports_media_deletion (bool, optional): Optional. Filter by
                channels that support media deletion.
            is_favorite (bool, optional): Optional. Filter by channels that
                are favorite.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Channels returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_channels called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_channels.")
            _url_path = "/Channels"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "supportsLatestItems": supports_latest_items,
                "supportsMediaDeletion": supports_media_deletion,
                "isFavorite": is_favorite,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_channels.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_channels.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_channels")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_channels.")
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

    def get_channel_features(self, channel_id):
        """Does a GET request to /Channels/{channelId}/Features.

        Get channel features.

        Args:
            channel_id (uuid|string): Channel id.

        Returns:
            ChannelFeatures: Response from the API. Channel features
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_channel_features called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_channel_features.")
            _url_path = "/Channels/{channelId}/Features"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"channelId": {"value": channel_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_channel_features.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_channel_features."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_channel_features")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_channel_features.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ChannelFeatures.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_channel_items(
        self,
        channel_id,
        folder_id=None,
        user_id=None,
        start_index=None,
        limit=None,
        sort_order=None,
        filters=None,
        sort_by=None,
        fields=None,
    ):
        """Does a GET request to /Channels/{channelId}/Items.

        Get channel items.

        Args:
            channel_id (uuid|string): Channel Id.
            folder_id (uuid|string, optional): Optional. Folder Id.
            user_id (uuid|string, optional): Optional. User Id.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            sort_order (list of SortOrderEnum, optional): Optional. Sort Order
                - Ascending,Descending.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited. Options: Album, AlbumArtist,
                Artist, Budget, CommunityRating, CriticRating, DateCreated,
                DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName,
                Random, Revenue, Runtime.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Channel items
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_channel_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_channel_items.")
            _url_path = "/Channels/{channelId}/Items"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"channelId": {"value": channel_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "folderId": folder_id,
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "sortOrder": sort_order,
                "filters": filters,
                "sortBy": sort_by,
                "fields": fields,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_channel_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_channel_items.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_channel_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_channel_items.")
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

    def get_all_channel_features(self):
        """Does a GET request to /Channels/Features.

        Get all channel features.

        Returns:
            list of ChannelFeatures: Response from the API. All channel
                features returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_all_channel_features called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_all_channel_features.")
            _url_path = "/Channels/Features"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_all_channel_features.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_all_channel_features."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_all_channel_features")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_all_channel_features.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ChannelFeatures.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_latest_channel_items(
        self,
        user_id=None,
        start_index=None,
        limit=None,
        filters=None,
        fields=None,
        channel_ids=None,
    ):
        """Does a GET request to /Channels/Items/Latest.

        Gets latest channel items.

        Args:
            user_id (uuid|string, optional): Optional. User Id.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            channel_ids (list of uuid|string, optional): Optional. Specify one
                or more channel id's, comma delimited.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Latest channel
                items returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_latest_channel_items called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_latest_channel_items.")
            _url_path = "/Channels/Items/Latest"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "filters": filters,
                "fields": fields,
                "channelIds": channel_ids,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_latest_channel_items.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_latest_channel_items."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_latest_channel_items")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_latest_channel_items.")
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
