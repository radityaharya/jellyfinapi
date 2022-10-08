# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.channel_mapping_options_dto import ChannelMappingOptionsDto
from jellyfinapi.models.tuner_channel_mapping import TunerChannelMapping
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.guide_info import GuideInfo
from jellyfinapi.models.live_tv_info import LiveTvInfo
from jellyfinapi.models.listings_provider_info import ListingsProviderInfo
from jellyfinapi.models.name_id_pair import NameIdPair
from jellyfinapi.models.series_timer_info_dto_query_result import (
    SeriesTimerInfoDtoQueryResult,
)
from jellyfinapi.models.series_timer_info_dto import SeriesTimerInfoDto
from jellyfinapi.models.timer_info_dto_query_result import TimerInfoDtoQueryResult
from jellyfinapi.models.timer_info_dto import TimerInfoDto
from jellyfinapi.models.tuner_host_info import TunerHostInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class LiveTvController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(LiveTvController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_channel_mapping_options(self, provider_id=None):
        """Does a GET request to /LiveTv/ChannelMappingOptions.

        Get channel mapping options.

        Args:
            provider_id (string, optional): Provider id.

        Returns:
            ChannelMappingOptionsDto: Response from the API. Channel mapping
                options returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_channel_mapping_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_channel_mapping_options.")
            _url_path = "/LiveTv/ChannelMappingOptions"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"providerId": provider_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_channel_mapping_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_channel_mapping_options."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_channel_mapping_options"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_channel_mapping_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ChannelMappingOptionsDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_channel_mapping(self, body):
        """Does a POST request to /LiveTv/ChannelMappings.

        Set channel mappings.

        Args:
            body (SetChannelMappingDto): The set channel mapping dto.

        Returns:
            TunerChannelMapping: Response from the API. Created channel
                mapping returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_channel_mapping called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_channel_mapping.")
            _url_path = "/LiveTv/ChannelMappings"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for set_channel_mapping.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_channel_mapping.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_channel_mapping")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_channel_mapping.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TunerChannelMapping.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_live_tv_channels(
        self,
        mtype=None,
        user_id=None,
        start_index=None,
        is_movie=None,
        is_series=None,
        is_news=None,
        is_kids=None,
        is_sports=None,
        limit=None,
        is_favorite=None,
        is_liked=None,
        is_disliked=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        fields=None,
        enable_user_data=None,
        sort_by=None,
        sort_order=None,
        enable_favorite_sorting=False,
        add_current_program=True,
    ):
        """Does a GET request to /LiveTv/Channels.

        Gets available live tv channels.

        Args:
            mtype (ChannelTypeEnum, optional): Optional. Filter by channel
                type.
            user_id (uuid|string, optional): Optional. Filter by user and
                attach user data.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            is_movie (bool, optional): Optional. Filter for movies.
            is_series (bool, optional): Optional. Filter for series.
            is_news (bool, optional): Optional. Filter for news.
            is_kids (bool, optional): Optional. Filter for kids.
            is_sports (bool, optional): Optional. Filter for sports.
            limit (int, optional): Optional. The maximum number of records to
                return.
            is_favorite (bool, optional): Optional. Filter by channels that
                are favorites, or not.
            is_liked (bool, optional): Optional. Filter by channels that are
                liked, or not.
            is_disliked (bool, optional): Optional. Filter by channels that
                are disliked, or not.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): "Optional.
                The image types to include in the output.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            sort_by (list of string, optional): Optional. Key to sort by.
            sort_order (SortOrderEnum, optional): Optional. Sort order.
            enable_favorite_sorting (bool, optional): Optional. Incorporate
                favorite and like status into channel sorting.
            add_current_program (bool, optional): Optional. Adds current
                program info to each channel.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Available live tv
                channels returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_live_tv_channels called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_live_tv_channels.")
            _url_path = "/LiveTv/Channels"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "type": mtype,
                "userId": user_id,
                "startIndex": start_index,
                "isMovie": is_movie,
                "isSeries": is_series,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "limit": limit,
                "isFavorite": is_favorite,
                "isLiked": is_liked,
                "isDisliked": is_disliked,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "fields": fields,
                "enableUserData": enable_user_data,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "enableFavoriteSorting": enable_favorite_sorting,
                "addCurrentProgram": add_current_program,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_live_tv_channels.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_live_tv_channels."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_live_tv_channels")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_live_tv_channels.")
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

    def get_channel(self, channel_id, user_id=None):
        """Does a GET request to /LiveTv/Channels/{channelId}.

        Gets a live tv channel.

        Args:
            channel_id (uuid|string): Channel id.
            user_id (uuid|string, optional): Optional. Attach user data.

        Returns:
            BaseItemDto: Response from the API. Live tv channel returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_channel called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_channel.")
            _url_path = "/LiveTv/Channels/{channelId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"channelId": {"value": channel_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_channel.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_channel.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_channel")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_channel.")
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

    def get_guide_info(self):
        """Does a GET request to /LiveTv/GuideInfo.

        Get guid info.

        Returns:
            GuideInfo: Response from the API. Guid info returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_guide_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_guide_info.")
            _url_path = "/LiveTv/GuideInfo"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_guide_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_guide_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_guide_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_guide_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, GuideInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_live_tv_info(self):
        """Does a GET request to /LiveTv/Info.

        Gets available live tv services.

        Returns:
            LiveTvInfo: Response from the API. Available live tv services
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_live_tv_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_live_tv_info.")
            _url_path = "/LiveTv/Info"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_live_tv_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_live_tv_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_live_tv_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_live_tv_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, LiveTvInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_listing_provider(
        self, pw=None, validate_listings=False, validate_login=False, body=None
    ):
        """Does a POST request to /LiveTv/ListingProviders.

        Adds a listings provider.

        Args:
            pw (string, optional): Password.
            validate_listings (bool, optional): Validate listings.
            validate_login (bool, optional): Validate login.
            body (ListingsProviderInfo, optional): New listings info.

        Returns:
            ListingsProviderInfo: Response from the API. Created listings
                provider returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_listing_provider called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_listing_provider.")
            _url_path = "/LiveTv/ListingProviders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "pw": pw,
                "validateListings": validate_listings,
                "validateLogin": validate_login,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for add_listing_provider.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for add_listing_provider."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_listing_provider")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_listing_provider.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ListingsProviderInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_listing_provider(self, id=None):
        """Does a DELETE request to /LiveTv/ListingProviders.

        Delete listing provider.

        Args:
            id (string, optional): Listing provider id.

        Returns:
            void: Response from the API. Listing provider deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_listing_provider called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_listing_provider.")
            _url_path = "/LiveTv/ListingProviders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for delete_listing_provider."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_listing_provider")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_listing_provider.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_default_listing_provider(self):
        """Does a GET request to /LiveTv/ListingProviders/Default.

        Gets default listings provider info.

        Returns:
            ListingsProviderInfo: Response from the API. Default listings
                provider info returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_default_listing_provider called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_default_listing_provider.")
            _url_path = "/LiveTv/ListingProviders/Default"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_default_listing_provider.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_default_listing_provider."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_default_listing_provider"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_default_listing_provider.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ListingsProviderInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_lineups(self, id=None, mtype=None, location=None, country=None):
        """Does a GET request to /LiveTv/ListingProviders/Lineups.

        Gets available lineups.

        Args:
            id (string, optional): Provider id.
            mtype (string, optional): Provider type.
            location (string, optional): Location.
            country (string, optional): Country.

        Returns:
            list of NameIdPair: Response from the API. Available lineups
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_lineups called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_lineups.")
            _url_path = "/LiveTv/ListingProviders/Lineups"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "id": id,
                "type": mtype,
                "location": location,
                "country": country,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_lineups.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_lineups.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_lineups")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_lineups.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NameIdPair.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_schedules_direct_countries(self):
        """Does a GET request to /LiveTv/ListingProviders/SchedulesDirect/Countries.

        Gets available countries.

        Returns:
            binary: Response from the API. Available countries returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_schedules_direct_countries called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_schedules_direct_countries.")
            _url_path = "/LiveTv/ListingProviders/SchedulesDirect/Countries"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_schedules_direct_countries."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_schedules_direct_countries"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_schedules_direct_countries.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_live_recording_file(self, recording_id):
        """Does a GET request to /LiveTv/LiveRecordings/{recordingId}/stream.

        Gets a live tv recording stream.

        Args:
            recording_id (string): Recording id.

        Returns:
            mixed: Response from the API. Recording stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_live_recording_file called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_live_recording_file.")
            _url_path = "/LiveTv/LiveRecordings/{recordingId}/stream"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"recordingId": {"value": recording_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_live_recording_file.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_live_recording_file."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_live_recording_file")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_live_recording_file.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Recording not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_live_stream_file(self, stream_id, container):
        """Does a GET request to /LiveTv/LiveStreamFiles/{streamId}/stream.{container}.

        Gets a live tv channel stream.

        Args:
            stream_id (string): Stream id.
            container (string): Container type.

        Returns:
            mixed: Response from the API. Stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_live_stream_file called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_live_stream_file.")
            _url_path = "/LiveTv/LiveStreamFiles/{streamId}/stream.{container}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "streamId": {"value": stream_id, "encode": True},
                    "container": {"value": container, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_live_stream_file.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_live_stream_file."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_live_stream_file")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_live_stream_file.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Stream not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_live_tv_programs(
        self,
        channel_ids=None,
        user_id=None,
        min_start_date=None,
        has_aired=None,
        is_airing=None,
        max_start_date=None,
        min_end_date=None,
        max_end_date=None,
        is_movie=None,
        is_series=None,
        is_news=None,
        is_kids=None,
        is_sports=None,
        start_index=None,
        limit=None,
        sort_by=None,
        sort_order=None,
        genres=None,
        genre_ids=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        enable_user_data=None,
        series_timer_id=None,
        library_series_id=None,
        fields=None,
        enable_total_record_count=True,
    ):
        """Does a GET request to /LiveTv/Programs.

        Gets available live tv epgs.

        Args:
            channel_ids (list of uuid|string, optional): The channels to
                return guide information for.
            user_id (uuid|string, optional): Optional. Filter by user id.
            min_start_date (datetime, optional): Optional. The minimum
                premiere start date.
            has_aired (bool, optional): Optional. Filter by programs that have
                completed airing, or not.
            is_airing (bool, optional): Optional. Filter by programs that are
                currently airing, or not.
            max_start_date (datetime, optional): Optional. The maximum
                premiere start date.
            min_end_date (datetime, optional): Optional. The minimum premiere
                end date.
            max_end_date (datetime, optional): Optional. The maximum premiere
                end date.
            is_movie (bool, optional): Optional. Filter for movies.
            is_series (bool, optional): Optional. Filter for series.
            is_news (bool, optional): Optional. Filter for news.
            is_kids (bool, optional): Optional. Filter for kids.
            is_sports (bool, optional): Optional. Filter for sports.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited. Options: Name, StartDate.
            sort_order (list of SortOrderEnum, optional): Sort Order -
                Ascending,Descending.
            genres (list of string, optional): The genres to return guide
                information for.
            genre_ids (list of uuid|string, optional): The genre ids to return
                guide information for.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            series_timer_id (string, optional): Optional. Filter by series
                timer id.
            library_series_id (uuid|string, optional): Optional. Filter by
                library series id.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_total_record_count (bool, optional): Retrieve total record
                count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Live tv epgs
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_live_tv_programs called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_live_tv_programs.")
            _url_path = "/LiveTv/Programs"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "channelIds": channel_ids,
                "userId": user_id,
                "minStartDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_start_date
                ),
                "hasAired": has_aired,
                "isAiring": is_airing,
                "maxStartDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, max_start_date
                ),
                "minEndDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, min_end_date
                ),
                "maxEndDate": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, max_end_date
                ),
                "isMovie": is_movie,
                "isSeries": is_series,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "startIndex": start_index,
                "limit": limit,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "genres": genres,
                "genreIds": genre_ids,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "enableUserData": enable_user_data,
                "seriesTimerId": series_timer_id,
                "librarySeriesId": library_series_id,
                "fields": fields,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_live_tv_programs.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_live_tv_programs."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_live_tv_programs")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_live_tv_programs.")
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

    def get_programs(self, body=None):
        """Does a POST request to /LiveTv/Programs.

        Gets available live tv epgs.

        Args:
            body (GetProgramsDto, optional): Request body.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Live tv epgs
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_programs called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_programs.")
            _url_path = "/LiveTv/Programs"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_programs.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_programs.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_programs")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_programs.")
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

    def get_program(self, program_id, user_id=None):
        """Does a GET request to /LiveTv/Programs/{programId}.

        Gets a live tv program.

        Args:
            program_id (string): Program id.
            user_id (uuid|string, optional): Optional. Attach user data.

        Returns:
            BaseItemDto: Response from the API. Program returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_program called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_program.")
            _url_path = "/LiveTv/Programs/{programId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"programId": {"value": program_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_program.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_program.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_program")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_program.")
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

    def get_recommended_programs(
        self,
        user_id=None,
        limit=None,
        is_airing=None,
        has_aired=None,
        is_series=None,
        is_movie=None,
        is_news=None,
        is_kids=None,
        is_sports=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        genre_ids=None,
        fields=None,
        enable_user_data=None,
        enable_total_record_count=True,
    ):
        """Does a GET request to /LiveTv/Programs/Recommended.

        Gets recommended live tv epgs.

        Args:
            user_id (uuid|string, optional): Optional. filter by user id.
            limit (int, optional): Optional. The maximum number of records to
                return.
            is_airing (bool, optional): Optional. Filter by programs that are
                currently airing, or not.
            has_aired (bool, optional): Optional. Filter by programs that have
                completed airing, or not.
            is_series (bool, optional): Optional. Filter for series.
            is_movie (bool, optional): Optional. Filter for movies.
            is_news (bool, optional): Optional. Filter for news.
            is_kids (bool, optional): Optional. Filter for kids.
            is_sports (bool, optional): Optional. Filter for sports.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            genre_ids (list of uuid|string, optional): The genres to return
                guide information for.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_user_data (bool, optional): Optional. include user data.
            enable_total_record_count (bool, optional): Retrieve total record
                count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Recommended epgs
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recommended_programs called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recommended_programs.")
            _url_path = "/LiveTv/Programs/Recommended"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "limit": limit,
                "isAiring": is_airing,
                "hasAired": has_aired,
                "isSeries": is_series,
                "isMovie": is_movie,
                "isNews": is_news,
                "isKids": is_kids,
                "isSports": is_sports,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "genreIds": genre_ids,
                "fields": fields,
                "enableUserData": enable_user_data,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recommended_programs.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_recommended_programs."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recommended_programs")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recommended_programs.")
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

    def get_recordings(
        self,
        channel_id=None,
        user_id=None,
        start_index=None,
        limit=None,
        status=None,
        is_in_progress=None,
        series_timer_id=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        fields=None,
        enable_user_data=None,
        is_movie=None,
        is_series=None,
        is_kids=None,
        is_sports=None,
        is_news=None,
        is_library_item=None,
        enable_total_record_count=True,
    ):
        """Does a GET request to /LiveTv/Recordings.

        Gets live tv recordings.

        Args:
            channel_id (string, optional): Optional. Filter by channel id.
            user_id (uuid|string, optional): Optional. Filter by user and
                attach user data.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            status (RecordingStatusEnum, optional): Optional. Filter by
                recording status.
            is_in_progress (bool, optional): Optional. Filter by recordings
                that are in progress, or not.
            series_timer_id (string, optional): Optional. Filter by recordings
                belonging to a series timer.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            is_movie (bool, optional): Optional. Filter for movies.
            is_series (bool, optional): Optional. Filter for series.
            is_kids (bool, optional): Optional. Filter for kids.
            is_sports (bool, optional): Optional. Filter for sports.
            is_news (bool, optional): Optional. Filter for news.
            is_library_item (bool, optional): Optional. Filter for is library
                item.
            enable_total_record_count (bool, optional): Optional. Return total
                record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Live tv recordings
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recordings called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recordings.")
            _url_path = "/LiveTv/Recordings"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "channelId": channel_id,
                "userId": user_id,
                "startIndex": start_index,
                "limit": limit,
                "status": status,
                "isInProgress": is_in_progress,
                "seriesTimerId": series_timer_id,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "fields": fields,
                "enableUserData": enable_user_data,
                "isMovie": is_movie,
                "isSeries": is_series,
                "isKids": is_kids,
                "isSports": is_sports,
                "isNews": is_news,
                "isLibraryItem": is_library_item,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recordings.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_recordings.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recordings")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recordings.")
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

    def get_recording(self, recording_id, user_id=None):
        """Does a GET request to /LiveTv/Recordings/{recordingId}.

        Gets a live tv recording.

        Args:
            recording_id (uuid|string): Recording id.
            user_id (uuid|string, optional): Optional. Attach user data.

        Returns:
            BaseItemDto: Response from the API. Recording returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recording called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recording.")
            _url_path = "/LiveTv/Recordings/{recordingId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"recordingId": {"value": recording_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recording.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_recording.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recording")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recording.")
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

    def delete_recording(self, recording_id):
        """Does a DELETE request to /LiveTv/Recordings/{recordingId}.

        Deletes a live tv recording.

        Args:
            recording_id (uuid|string): Recording id.

        Returns:
            void: Response from the API. Recording deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_recording called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_recording.")
            _url_path = "/LiveTv/Recordings/{recordingId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"recordingId": {"value": recording_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_recording.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_recording")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_recording.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_recording_folders(self, user_id=None):
        """Does a GET request to /LiveTv/Recordings/Folders.

        Gets recording folders.

        Args:
            user_id (uuid|string, optional): Optional. Filter by user and
                attach user data.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Recording folders
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recording_folders called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recording_folders.")
            _url_path = "/LiveTv/Recordings/Folders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recording_folders.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_recording_folders."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recording_folders")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recording_folders.")
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
    def get_recording_groups(self, user_id=None):
        """Does a GET request to /LiveTv/Recordings/Groups.

        Gets live tv recording groups.

        Args:
            user_id (uuid|string, optional): Optional. Filter by user and
                attach user data.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Recording groups
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recording_groups called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recording_groups.")
            _url_path = "/LiveTv/Recordings/Groups"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recording_groups.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_recording_groups."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recording_groups")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recording_groups.")
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
    def get_recording_group(self, group_id):
        """Does a GET request to /LiveTv/Recordings/Groups/{groupId}.

        Get recording group.

        Args:
            group_id (uuid|string): Group id.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recording_group called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recording_group.")
            _url_path = "/LiveTv/Recordings/Groups/{groupId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"groupId": {"value": group_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_recording_group.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recording_group")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recording_group.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    @deprecated()
    def get_recordings_series(
        self,
        channel_id=None,
        user_id=None,
        group_id=None,
        start_index=None,
        limit=None,
        status=None,
        is_in_progress=None,
        series_timer_id=None,
        enable_images=None,
        image_type_limit=None,
        enable_image_types=None,
        fields=None,
        enable_user_data=None,
        enable_total_record_count=True,
    ):
        """Does a GET request to /LiveTv/Recordings/Series.

        Gets live tv recording series.

        Args:
            channel_id (string, optional): Optional. Filter by channel id.
            user_id (uuid|string, optional): Optional. Filter by user and
                attach user data.
            group_id (string, optional): Optional. Filter by recording group.
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            status (RecordingStatusEnum, optional): Optional. Filter by
                recording status.
            is_in_progress (bool, optional): Optional. Filter by recordings
                that are in progress, or not.
            series_timer_id (string, optional): Optional. Filter by recordings
                belonging to a series timer.
            enable_images (bool, optional): Optional. Include image
                information in output.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            enable_user_data (bool, optional): Optional. Include user data.
            enable_total_record_count (bool, optional): Optional. Return total
                record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Live tv recordings
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_recordings_series called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_recordings_series.")
            _url_path = "/LiveTv/Recordings/Series"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "channelId": channel_id,
                "userId": user_id,
                "groupId": group_id,
                "startIndex": start_index,
                "limit": limit,
                "status": status,
                "isInProgress": is_in_progress,
                "seriesTimerId": series_timer_id,
                "enableImages": enable_images,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "fields": fields,
                "enableUserData": enable_user_data,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_recordings_series.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_recordings_series."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_recordings_series")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_recordings_series.")
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

    def get_series_timers(self, sort_by=None, sort_order=None):
        """Does a GET request to /LiveTv/SeriesTimers.

        Gets live tv series timers.

        Args:
            sort_by (string, optional): Optional. Sort by SortName or
                Priority.
            sort_order (SortOrderEnum, optional): Optional. Sort in Ascending
                or Descending order.

        Returns:
            SeriesTimerInfoDtoQueryResult: Response from the API. Timers
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_series_timers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_series_timers.")
            _url_path = "/LiveTv/SeriesTimers"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"sortBy": sort_by, "sortOrder": sort_order}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_series_timers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_series_timers.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_series_timers")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_series_timers.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SeriesTimerInfoDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_series_timer(self, body=None):
        """Does a POST request to /LiveTv/SeriesTimers.

        Creates a live tv series timer.

        Args:
            body (SeriesTimerInfoDto, optional): New series timer info.

        Returns:
            void: Response from the API. Series timer info created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_series_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_series_timer.")
            _url_path = "/LiveTv/SeriesTimers"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_series_timer.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_series_timer.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_series_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_series_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_series_timer(self, timer_id):
        """Does a GET request to /LiveTv/SeriesTimers/{timerId}.

        Gets a live tv series timer.

        Args:
            timer_id (string): Timer id.

        Returns:
            SeriesTimerInfoDto: Response from the API. Series timer returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_series_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_series_timer.")
            _url_path = "/LiveTv/SeriesTimers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_series_timer.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_series_timer.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_series_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_series_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Series timer not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SeriesTimerInfoDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def cancel_series_timer(self, timer_id):
        """Does a DELETE request to /LiveTv/SeriesTimers/{timerId}.

        Cancels a live tv series timer.

        Args:
            timer_id (string): Timer id.

        Returns:
            void: Response from the API. Timer cancelled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("cancel_series_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for cancel_series_timer.")
            _url_path = "/LiveTv/SeriesTimers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for cancel_series_timer.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="cancel_series_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for cancel_series_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_series_timer(self, timer_id, body=None):
        """Does a POST request to /LiveTv/SeriesTimers/{timerId}.

        Updates a live tv series timer.

        Args:
            timer_id (string): Timer id.
            body (SeriesTimerInfoDto, optional): New series timer info.

        Returns:
            void: Response from the API. Series timer updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_series_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_series_timer.")
            _url_path = "/LiveTv/SeriesTimers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_series_timer.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_series_timer.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_series_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_series_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_timers(
        self, channel_id=None, series_timer_id=None, is_active=None, is_scheduled=None
    ):
        """Does a GET request to /LiveTv/Timers.

        Gets the live tv timers.

        Args:
            channel_id (string, optional): Optional. Filter by channel id.
            series_timer_id (string, optional): Optional. Filter by timers
                belonging to a series timer.
            is_active (bool, optional): Optional. Filter by timers that are
                active.
            is_scheduled (bool, optional): Optional. Filter by timers that are
                scheduled.

        Returns:
            TimerInfoDtoQueryResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_timers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_timers.")
            _url_path = "/LiveTv/Timers"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "channelId": channel_id,
                "seriesTimerId": series_timer_id,
                "isActive": is_active,
                "isScheduled": is_scheduled,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_timers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_timers.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_timers")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_timers.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TimerInfoDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_timer(self, body=None):
        """Does a POST request to /LiveTv/Timers.

        Creates a live tv timer.

        Args:
            body (TimerInfoDto, optional): New timer info.

        Returns:
            void: Response from the API. Timer created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_timer.")
            _url_path = "/LiveTv/Timers"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_timer.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_timer.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_timer(self, timer_id):
        """Does a GET request to /LiveTv/Timers/{timerId}.

        Gets a timer.

        Args:
            timer_id (string): Timer id.

        Returns:
            TimerInfoDto: Response from the API. Timer returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_timer.")
            _url_path = "/LiveTv/Timers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_timer.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_timer.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TimerInfoDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def cancel_timer(self, timer_id):
        """Does a DELETE request to /LiveTv/Timers/{timerId}.

        Cancels a live tv timer.

        Args:
            timer_id (string): Timer id.

        Returns:
            void: Response from the API. Timer deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("cancel_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for cancel_timer.")
            _url_path = "/LiveTv/Timers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for cancel_timer.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="cancel_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for cancel_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_timer(self, timer_id, body=None):
        """Does a POST request to /LiveTv/Timers/{timerId}.

        Updates a live tv timer.

        Args:
            timer_id (string): Timer id.
            body (TimerInfoDto, optional): New timer info.

        Returns:
            void: Response from the API. Timer updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_timer.")
            _url_path = "/LiveTv/Timers/{timerId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"timerId": {"value": timer_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_timer.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_timer.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_default_timer(self, program_id=None):
        """Does a GET request to /LiveTv/Timers/Defaults.

        Gets the default values for a new timer.

        Args:
            program_id (string, optional): Optional. To attach default values
                based on a program.

        Returns:
            SeriesTimerInfoDto: Response from the API. Default values
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_default_timer called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_default_timer.")
            _url_path = "/LiveTv/Timers/Defaults"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"programId": program_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_default_timer.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_default_timer.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_default_timer")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_default_timer.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SeriesTimerInfoDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_tuner_host(self, body=None):
        """Does a POST request to /LiveTv/TunerHosts.

        Adds a tuner host.

        Args:
            body (TunerHostInfo, optional): New tuner host.

        Returns:
            TunerHostInfo: Response from the API. Created tuner host
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_tuner_host called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_tuner_host.")
            _url_path = "/LiveTv/TunerHosts"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for add_tuner_host.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_tuner_host.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_tuner_host")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_tuner_host.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TunerHostInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_tuner_host(self, id=None):
        """Does a DELETE request to /LiveTv/TunerHosts.

        Deletes a tuner host.

        Args:
            id (string, optional): Tuner host id.

        Returns:
            void: Response from the API. Tuner host deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_tuner_host called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_tuner_host.")
            _url_path = "/LiveTv/TunerHosts"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_tuner_host.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_tuner_host")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_tuner_host.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_tuner_host_types(self):
        """Does a GET request to /LiveTv/TunerHosts/Types.

        Get tuner host types.

        Returns:
            list of NameIdPair: Response from the API. Tuner host types
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_tuner_host_types called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_tuner_host_types.")
            _url_path = "/LiveTv/TunerHosts/Types"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_tuner_host_types.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_tuner_host_types."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_tuner_host_types")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_tuner_host_types.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NameIdPair.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def reset_tuner(self, tuner_id):
        """Does a POST request to /LiveTv/Tuners/{tunerId}/Reset.

        Resets a tv tuner.

        Args:
            tuner_id (string): Tuner id.

        Returns:
            void: Response from the API. Tuner reset.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("reset_tuner called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for reset_tuner.")
            _url_path = "/LiveTv/Tuners/{tunerId}/Reset"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"tunerId": {"value": tuner_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for reset_tuner.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="reset_tuner")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for reset_tuner.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def discover_tuners(self, new_devices_only=False):
        """Does a GET request to /LiveTv/Tuners/Discover.

        Discover tuners.

        Args:
            new_devices_only (bool, optional): Only discover new tuners.

        Returns:
            list of TunerHostInfo: Response from the API. Tuners returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("discover_tuners called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for discover_tuners.")
            _url_path = "/LiveTv/Tuners/Discover"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"newDevicesOnly": new_devices_only}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for discover_tuners.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for discover_tuners.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="discover_tuners")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for discover_tuners.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TunerHostInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def discvover_tuners(self, new_devices_only=False):
        """Does a GET request to /LiveTv/Tuners/Discvover.

        Discover tuners.

        Args:
            new_devices_only (bool, optional): Only discover new tuners.

        Returns:
            list of TunerHostInfo: Response from the API. Tuners returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("discvover_tuners called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for discvover_tuners.")
            _url_path = "/LiveTv/Tuners/Discvover"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"newDevicesOnly": new_devices_only}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for discvover_tuners.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for discvover_tuners.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="discvover_tuners")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for discvover_tuners.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TunerHostInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
