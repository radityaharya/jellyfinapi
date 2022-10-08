# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.api_exception import APIException


class UniversalAudioController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(UniversalAudioController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_universal_audio_stream(
        self,
        item_id,
        container=None,
        media_source_id=None,
        device_id=None,
        user_id=None,
        audio_codec=None,
        max_audio_channels=None,
        transcoding_audio_channels=None,
        max_streaming_bitrate=None,
        audio_bit_rate=None,
        start_time_ticks=None,
        transcoding_container=None,
        transcoding_protocol=None,
        max_audio_sample_rate=None,
        max_audio_bit_depth=None,
        enable_remote_media=None,
        break_on_non_key_frames=False,
        enable_redirection=True,
    ):
        """Does a GET request to /Audio/{itemId}/universal.

        Gets an audio stream.

        Args:
            item_id (uuid|string): The item id.
            container (list of string, optional): Optional. The audio
                container.
            media_source_id (string, optional): The media version id, if
                playing an alternate version.
            device_id (string, optional): The device id of the client
                requesting. Used to stop encoding processes when needed.
            user_id (uuid|string, optional): Optional. The user id.
            audio_codec (string, optional): Optional. The audio codec to
                transcode to.
            max_audio_channels (int, optional): Optional. The maximum number
                of audio channels.
            transcoding_audio_channels (int, optional): Optional. The number
                of how many audio channels to transcode to.
            max_streaming_bitrate (int, optional): Optional. The maximum
                streaming bitrate.
            audio_bit_rate (int, optional): Optional. Specify an audio bitrate
                to encode to, e.g. 128000. If omitted this will be left to
                encoder defaults.
            start_time_ticks (long|int, optional): Optional. Specify a
                starting offset, in ticks. 1 tick = 10000 ms.
            transcoding_container (string, optional): Optional. The container
                to transcode to.
            transcoding_protocol (string, optional): Optional. The transcoding
                protocol.
            max_audio_sample_rate (int, optional): Optional. The maximum audio
                sample rate.
            max_audio_bit_depth (int, optional): Optional. The maximum audio
                bit depth.
            enable_remote_media (bool, optional): Optional. Whether to enable
                remote media.
            break_on_non_key_frames (bool, optional): Optional. Whether to
                break on non key frames.
            enable_redirection (bool, optional): Whether to enable
                redirection. Defaults to true.

        Returns:
            mixed: Response from the API. Audio stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_universal_audio_stream called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_universal_audio_stream.")
            _url_path = "/Audio/{itemId}/universal"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "container": container,
                "mediaSourceId": media_source_id,
                "deviceId": device_id,
                "userId": user_id,
                "audioCodec": audio_codec,
                "maxAudioChannels": max_audio_channels,
                "transcodingAudioChannels": transcoding_audio_channels,
                "maxStreamingBitrate": max_streaming_bitrate,
                "audioBitRate": audio_bit_rate,
                "startTimeTicks": start_time_ticks,
                "transcodingContainer": transcoding_container,
                "transcodingProtocol": transcoding_protocol,
                "maxAudioSampleRate": max_audio_sample_rate,
                "maxAudioBitDepth": max_audio_bit_depth,
                "enableRemoteMedia": enable_remote_media,
                "breakOnNonKeyFrames": break_on_non_key_frames,
                "enableRedirection": enable_redirection,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_universal_audio_stream.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_universal_audio_stream."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_universal_audio_stream"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_universal_audio_stream.")
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
