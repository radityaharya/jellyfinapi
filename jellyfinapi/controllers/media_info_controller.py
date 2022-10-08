# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.playback_info_response import PlaybackInfoResponse
from jellyfinapi.models.live_stream_response import LiveStreamResponse
from jellyfinapi.exceptions.api_exception import APIException


class MediaInfoController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(MediaInfoController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_playback_info(self, item_id, user_id):
        """Does a GET request to /Items/{itemId}/PlaybackInfo.

        Gets live playback media info for an item.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string): The user id.

        Returns:
            PlaybackInfoResponse: Response from the API. Playback info
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_playback_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_playback_info.")
            _url_path = "/Items/{itemId}/PlaybackInfo"
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
            self.logger.info("Preparing headers for get_playback_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_playback_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_playback_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_playback_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PlaybackInfoResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_posted_playback_info(
        self,
        item_id,
        user_id=None,
        max_streaming_bitrate=None,
        start_time_ticks=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        max_audio_channels=None,
        media_source_id=None,
        live_stream_id=None,
        auto_open_live_stream=None,
        enable_direct_play=None,
        enable_direct_stream=None,
        enable_transcoding=None,
        allow_video_stream_copy=None,
        allow_audio_stream_copy=None,
        body=None,
    ):
        """Does a POST request to /Items/{itemId}/PlaybackInfo.

        For backwards compatibility parameters can be sent via Query or Body,
        with Query having higher precedence.
        Query parameters are obsolete.

        Args:
            item_id (uuid|string): The item id.
            user_id (uuid|string, optional): The user id.
            max_streaming_bitrate (int, optional): The maximum streaming
                bitrate.
            start_time_ticks (long|int, optional): The start time in ticks.
            audio_stream_index (int, optional): The audio stream index.
            subtitle_stream_index (int, optional): The subtitle stream index.
            max_audio_channels (int, optional): The maximum number of audio
                channels.
            media_source_id (string, optional): The media source id.
            live_stream_id (string, optional): The livestream id.
            auto_open_live_stream (bool, optional): Whether to auto open the
                livestream.
            enable_direct_play (bool, optional): Whether to enable direct
                play. Default: true.
            enable_direct_stream (bool, optional): Whether to enable direct
                stream. Default: true.
            enable_transcoding (bool, optional): Whether to enable
                transcoding. Default: true.
            allow_video_stream_copy (bool, optional): Whether to allow to copy
                the video stream. Default: true.
            allow_audio_stream_copy (bool, optional): Whether to allow to copy
                the audio stream. Default: true.
            body (PlaybackInfoDto, optional): The playback info.

        Returns:
            PlaybackInfoResponse: Response from the API. Playback info
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_posted_playback_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_posted_playback_info.")
            _url_path = "/Items/{itemId}/PlaybackInfo"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "maxStreamingBitrate": max_streaming_bitrate,
                "startTimeTicks": start_time_ticks,
                "audioStreamIndex": audio_stream_index,
                "subtitleStreamIndex": subtitle_stream_index,
                "maxAudioChannels": max_audio_channels,
                "mediaSourceId": media_source_id,
                "liveStreamId": live_stream_id,
                "autoOpenLiveStream": auto_open_live_stream,
                "enableDirectPlay": enable_direct_play,
                "enableDirectStream": enable_direct_stream,
                "enableTranscoding": enable_transcoding,
                "allowVideoStreamCopy": allow_video_stream_copy,
                "allowAudioStreamCopy": allow_audio_stream_copy,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_posted_playback_info.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_posted_playback_info."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_posted_playback_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_posted_playback_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PlaybackInfoResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def close_live_stream(self, live_stream_id):
        """Does a POST request to /LiveStreams/Close.

        Closes a media source.

        Args:
            live_stream_id (string): The livestream id.

        Returns:
            void: Response from the API. Livestream closed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("close_live_stream called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for close_live_stream.")
            _url_path = "/LiveStreams/Close"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"liveStreamId": live_stream_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for close_live_stream.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="close_live_stream")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for close_live_stream.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def open_live_stream(
        self,
        open_token=None,
        user_id=None,
        play_session_id=None,
        max_streaming_bitrate=None,
        start_time_ticks=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        max_audio_channels=None,
        item_id=None,
        enable_direct_play=None,
        enable_direct_stream=None,
        body=None,
    ):
        """Does a POST request to /LiveStreams/Open.

        Opens a media source.

        Args:
            open_token (string, optional): The open token.
            user_id (uuid|string, optional): The user id.
            play_session_id (string, optional): The play session id.
            max_streaming_bitrate (int, optional): The maximum streaming
                bitrate.
            start_time_ticks (long|int, optional): The start time in ticks.
            audio_stream_index (int, optional): The audio stream index.
            subtitle_stream_index (int, optional): The subtitle stream index.
            max_audio_channels (int, optional): The maximum number of audio
                channels.
            item_id (uuid|string, optional): The item id.
            enable_direct_play (bool, optional): Whether to enable direct
                play. Default: true.
            enable_direct_stream (bool, optional): Whether to enable direct
                stream. Default: true.
            body (OpenLiveStreamDto, optional): The open live stream dto.

        Returns:
            LiveStreamResponse: Response from the API. Media source opened.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("open_live_stream called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for open_live_stream.")
            _url_path = "/LiveStreams/Open"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "openToken": open_token,
                "userId": user_id,
                "playSessionId": play_session_id,
                "maxStreamingBitrate": max_streaming_bitrate,
                "startTimeTicks": start_time_ticks,
                "audioStreamIndex": audio_stream_index,
                "subtitleStreamIndex": subtitle_stream_index,
                "maxAudioChannels": max_audio_channels,
                "itemId": item_id,
                "enableDirectPlay": enable_direct_play,
                "enableDirectStream": enable_direct_stream,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for open_live_stream.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for open_live_stream.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="open_live_stream")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for open_live_stream.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, LiveStreamResponse.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_bitrate_test_bytes(self, size=102400):
        """Does a GET request to /Playback/BitrateTest.

        Tests the network with a request with the size of the bitrate.

        Args:
            size (int, optional): The bitrate. Defaults to 102400.

        Returns:
            binary: Response from the API. Test buffer returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_bitrate_test_bytes called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_bitrate_test_bytes.")
            _url_path = "/Playback/BitrateTest"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"size": size}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_bitrate_test_bytes."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_bitrate_test_bytes"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_bitrate_test_bytes.")
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
