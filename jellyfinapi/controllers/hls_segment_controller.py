# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException
from jellyfinapi.exceptions.api_exception import APIException


class HlsSegmentController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(HlsSegmentController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_hls_audio_segment_legacy_aac(self, item_id, segment_id):
        """Does a GET request to /Audio/{itemId}/hls/{segmentId}/stream.aac.

        Gets the specified audio segment for an audio item.

        Args:
            item_id (string): The item id.
            segment_id (string): The segment id.

        Returns:
            mixed: Response from the API. Hls audio segment returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_hls_audio_segment_legacy_aac called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_hls_audio_segment_legacy_aac."
            )
            _url_path = "/Audio/{itemId}/hls/{segmentId}/stream.aac"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "segmentId": {"value": segment_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_hls_audio_segment_legacy_aac.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_hls_audio_segment_legacy_aac."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_hls_audio_segment_legacy_aac"
            )
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_hls_audio_segment_legacy_mp_3(self, item_id, segment_id):
        """Does a GET request to /Audio/{itemId}/hls/{segmentId}/stream.mp3.

        Gets the specified audio segment for an audio item.

        Args:
            item_id (string): The item id.
            segment_id (string): The segment id.

        Returns:
            mixed: Response from the API. Hls audio segment returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_hls_audio_segment_legacy_mp_3 called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_hls_audio_segment_legacy_mp_3."
            )
            _url_path = "/Audio/{itemId}/hls/{segmentId}/stream.mp3"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "segmentId": {"value": segment_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_hls_audio_segment_legacy_mp_3.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_hls_audio_segment_legacy_mp_3."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_hls_audio_segment_legacy_mp_3"
            )
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_hls_video_segment_legacy(
        self, item_id, playlist_id, segment_id, segment_container
    ):
        """Does a GET request to /Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer}.

        Gets a hls video segment.

        Args:
            item_id (string): The item id.
            playlist_id (string): The playlist id.
            segment_id (string): The segment id.
            segment_container (string): The segment container.

        Returns:
            mixed: Response from the API. Hls video segment returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_hls_video_segment_legacy called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_hls_video_segment_legacy.")
            _url_path = (
                "/Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer}"
            )
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "playlistId": {"value": playlist_id, "encode": True},
                    "segmentId": {"value": segment_id, "encode": True},
                    "segmentContainer": {"value": segment_container, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_hls_video_segment_legacy.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_hls_video_segment_legacy."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_hls_video_segment_legacy"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_hls_video_segment_legacy.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Hls segment not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_hls_playlist_legacy(self, item_id, playlist_id):
        """Does a GET request to /Videos/{itemId}/hls/{playlistId}/stream.m3u8.

        Gets a hls video playlist.

        Args:
            item_id (string): The video id.
            playlist_id (string): The playlist id.

        Returns:
            mixed: Response from the API. Hls video playlist returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_hls_playlist_legacy called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_hls_playlist_legacy.")
            _url_path = "/Videos/{itemId}/hls/{playlistId}/stream.m3u8"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "playlistId": {"value": playlist_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_hls_playlist_legacy.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_hls_playlist_legacy."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_hls_playlist_legacy")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_hls_playlist_legacy.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def stop_encoding_process(self, device_id, play_session_id):
        """Does a DELETE request to /Videos/ActiveEncodings.

        Stops an active encoding.

        Args:
            device_id (string): The device id of the client requesting. Used
                to stop encoding processes when needed.
            play_session_id (string): The play session id.

        Returns:
            void: Response from the API. Encoding stopped successfully.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("stop_encoding_process called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for stop_encoding_process.")
            _url_path = "/Videos/ActiveEncodings"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "deviceId": device_id,
                "playSessionId": play_session_id,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for stop_encoding_process."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="stop_encoding_process")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for stop_encoding_process.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
