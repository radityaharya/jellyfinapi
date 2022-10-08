# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.user_item_data_dto import UserItemDataDto
from jellyfinapi.exceptions.api_exception import APIException


class PlaystateController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(PlaystateController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def report_playback_start(self, body=None):
        """Does a POST request to /Sessions/Playing.

        Reports playback has started within a session.

        Args:
            body (PlaybackStartInfo, optional): The playback start info.

        Returns:
            void: Response from the API. Playback start recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("report_playback_start called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for report_playback_start.")
            _url_path = "/Sessions/Playing"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for report_playback_start.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for report_playback_start."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="report_playback_start")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for report_playback_start.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def ping_playback_session(self, play_session_id):
        """Does a POST request to /Sessions/Playing/Ping.

        Pings a playback session.

        Args:
            play_session_id (string): Playback session id.

        Returns:
            void: Response from the API. Playback session pinged.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("ping_playback_session called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for ping_playback_session.")
            _url_path = "/Sessions/Playing/Ping"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"playSessionId": play_session_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for ping_playback_session."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="ping_playback_session")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for ping_playback_session.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def report_playback_progress(self, body=None):
        """Does a POST request to /Sessions/Playing/Progress.

        Reports playback progress within a session.

        Args:
            body (PlaybackProgressInfo, optional): The playback progress
                info.

        Returns:
            void: Response from the API. Playback progress recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("report_playback_progress called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for report_playback_progress.")
            _url_path = "/Sessions/Playing/Progress"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for report_playback_progress.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for report_playback_progress."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="report_playback_progress")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for report_playback_progress.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def report_playback_stopped(self, body=None):
        """Does a POST request to /Sessions/Playing/Stopped.

        Reports playback has stopped within a session.

        Args:
            body (PlaybackStopInfo, optional): The playback stop info.

        Returns:
            void: Response from the API. Playback stop recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("report_playback_stopped called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for report_playback_stopped.")
            _url_path = "/Sessions/Playing/Stopped"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for report_playback_stopped.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for report_playback_stopped."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="report_playback_stopped")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for report_playback_stopped.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def mark_played_item(self, user_id, item_id, date_played=None):
        """Does a POST request to /Users/{userId}/PlayedItems/{itemId}.

        Marks an item as played for user.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.
            date_played (datetime, optional): Optional. The date the item was
                played.

        Returns:
            UserItemDataDto: Response from the API. Item marked as played.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("mark_played_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for mark_played_item.")
            _url_path = "/Users/{userId}/PlayedItems/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "datePlayed": APIHelper.when_defined(
                    APIHelper.RFC3339DateTime, date_played
                )
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for mark_played_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for mark_played_item.")
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="mark_played_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for mark_played_item.")
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

    def mark_unplayed_item(self, user_id, item_id):
        """Does a DELETE request to /Users/{userId}/PlayedItems/{itemId}.

        Marks an item as unplayed for user.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.

        Returns:
            UserItemDataDto: Response from the API. Item marked as unplayed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("mark_unplayed_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for mark_unplayed_item.")
            _url_path = "/Users/{userId}/PlayedItems/{itemId}"
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
            self.logger.info("Preparing headers for mark_unplayed_item.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for mark_unplayed_item.")
            _request = self.config.http_client.delete(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="mark_unplayed_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for mark_unplayed_item.")
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

    def on_playback_start(
        self,
        user_id,
        item_id,
        media_source_id=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        play_method=None,
        live_stream_id=None,
        play_session_id=None,
        can_seek=False,
    ):
        """Does a POST request to /Users/{userId}/PlayingItems/{itemId}.

        Reports that a user has begun playing an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.
            media_source_id (string, optional): The id of the MediaSource.
            audio_stream_index (int, optional): The audio stream index.
            subtitle_stream_index (int, optional): The subtitle stream index.
            play_method (PlayMethodEnum, optional): The play method.
            live_stream_id (string, optional): The live stream id.
            play_session_id (string, optional): The play session id.
            can_seek (bool, optional): Indicates if the client can seek.

        Returns:
            void: Response from the API. Play start recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("on_playback_start called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for on_playback_start.")
            _url_path = "/Users/{userId}/PlayingItems/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "mediaSourceId": media_source_id,
                "audioStreamIndex": audio_stream_index,
                "subtitleStreamIndex": subtitle_stream_index,
                "playMethod": play_method,
                "liveStreamId": live_stream_id,
                "playSessionId": play_session_id,
                "canSeek": can_seek,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for on_playback_start.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="on_playback_start")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for on_playback_start.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def on_playback_stopped(
        self,
        user_id,
        item_id,
        media_source_id=None,
        next_media_type=None,
        position_ticks=None,
        live_stream_id=None,
        play_session_id=None,
    ):
        """Does a DELETE request to /Users/{userId}/PlayingItems/{itemId}.

        Reports that a user has stopped playing an item.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.
            media_source_id (string, optional): The id of the MediaSource.
            next_media_type (string, optional): The next media type that will
                play.
            position_ticks (long|int, optional): Optional. The position, in
                ticks, where playback stopped. 1 tick = 10000 ms.
            live_stream_id (string, optional): The live stream id.
            play_session_id (string, optional): The play session id.

        Returns:
            void: Response from the API. Playback stop recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("on_playback_stopped called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for on_playback_stopped.")
            _url_path = "/Users/{userId}/PlayingItems/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "mediaSourceId": media_source_id,
                "nextMediaType": next_media_type,
                "positionTicks": position_ticks,
                "liveStreamId": live_stream_id,
                "playSessionId": play_session_id,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for on_playback_stopped.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="on_playback_stopped")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for on_playback_stopped.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def on_playback_progress(
        self,
        user_id,
        item_id,
        media_source_id=None,
        position_ticks=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        volume_level=None,
        play_method=None,
        live_stream_id=None,
        play_session_id=None,
        repeat_mode=None,
        is_paused=False,
        is_muted=False,
    ):
        """Does a POST request to /Users/{userId}/PlayingItems/{itemId}/Progress.

        Reports a user's playback progress.

        Args:
            user_id (uuid|string): User id.
            item_id (uuid|string): Item id.
            media_source_id (string, optional): The id of the MediaSource.
            position_ticks (long|int, optional): Optional. The current
                position, in ticks. 1 tick = 10000 ms.
            audio_stream_index (int, optional): The audio stream index.
            subtitle_stream_index (int, optional): The subtitle stream index.
            volume_level (int, optional): Scale of 0-100.
            play_method (PlayMethodEnum, optional): The play method.
            live_stream_id (string, optional): The live stream id.
            play_session_id (string, optional): The play session id.
            repeat_mode (RepeatModeEnum, optional): The repeat mode.
            is_paused (bool, optional): Indicates if the player is paused.
            is_muted (bool, optional): Indicates if the player is muted.

        Returns:
            void: Response from the API. Play progress recorded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("on_playback_progress called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for on_playback_progress.")
            _url_path = "/Users/{userId}/PlayingItems/{itemId}/Progress"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "itemId": {"value": item_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "mediaSourceId": media_source_id,
                "positionTicks": position_ticks,
                "audioStreamIndex": audio_stream_index,
                "subtitleStreamIndex": subtitle_stream_index,
                "volumeLevel": volume_level,
                "playMethod": play_method,
                "liveStreamId": live_stream_id,
                "playSessionId": play_session_id,
                "repeatMode": repeat_mode,
                "isPaused": is_paused,
                "isMuted": is_muted,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for on_playback_progress."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="on_playback_progress")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for on_playback_progress.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
