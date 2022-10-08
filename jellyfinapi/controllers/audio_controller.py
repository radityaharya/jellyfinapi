# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController


class AudioController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(AudioController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_audio_stream(
        self,
        item_id,
        container=None,
        static=None,
        params=None,
        tag=None,
        device_profile_id=None,
        play_session_id=None,
        segment_container=None,
        segment_length=None,
        min_segments=None,
        media_source_id=None,
        device_id=None,
        audio_codec=None,
        enable_auto_stream_copy=None,
        allow_video_stream_copy=None,
        allow_audio_stream_copy=None,
        break_on_non_key_frames=None,
        audio_sample_rate=None,
        max_audio_bit_depth=None,
        audio_bit_rate=None,
        audio_channels=None,
        max_audio_channels=None,
        profile=None,
        level=None,
        framerate=None,
        max_framerate=None,
        copy_timestamps=None,
        start_time_ticks=None,
        width=None,
        height=None,
        video_bit_rate=None,
        subtitle_stream_index=None,
        subtitle_method=None,
        max_ref_frames=None,
        max_video_bit_depth=None,
        require_avc=None,
        de_interlace=None,
        require_non_anamorphic=None,
        transcoding_max_audio_channels=None,
        cpu_core_limit=None,
        live_stream_id=None,
        enable_mpegts_m_2_ts_mode=None,
        video_codec=None,
        subtitle_codec=None,
        transcode_reasons=None,
        audio_stream_index=None,
        video_stream_index=None,
        context=None,
        stream_options=None,
    ):
        """Does a GET request to /Audio/{itemId}/stream.

        Gets an audio stream.

        Args:
            item_id (uuid|string): The item id.
            container (string, optional): The audio container.
            static (bool, optional): Optional. If true, the original file will
                be streamed statically without any encoding. Use either no url
                extension or the original file extension. true/false.
            params (string, optional): The streaming parameters.
            tag (string, optional): The tag.
            device_profile_id (string, optional): Optional. The dlna device
                profile id to utilize.
            play_session_id (string, optional): The play session id.
            segment_container (string, optional): The segment container.
            segment_length (int, optional): The segment length.
            min_segments (int, optional): The minimum number of segments.
            media_source_id (string, optional): The media version id, if
                playing an alternate version.
            device_id (string, optional): The device id of the client
                requesting. Used to stop encoding processes when needed.
            audio_codec (string, optional): Optional. Specify a audio codec to
                encode to, e.g. mp3. If omitted the server will auto-select
                using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool, optional): Whether or not to allow
                automatic stream copy if requested values match the original
                source. Defaults to true.
            allow_video_stream_copy (bool, optional): Whether or not to allow
                copying of the video stream url.
            allow_audio_stream_copy (bool, optional): Whether or not to allow
                copying of the audio stream url.
            break_on_non_key_frames (bool, optional): Optional. Whether to
                break on non key frames.
            audio_sample_rate (int, optional): Optional. Specify a specific
                audio sample rate, e.g. 44100.
            max_audio_bit_depth (int, optional): Optional. The maximum audio
                bit depth.
            audio_bit_rate (int, optional): Optional. Specify an audio bitrate
                to encode to, e.g. 128000. If omitted this will be left to
                encoder defaults.
            audio_channels (int, optional): Optional. Specify a specific
                number of audio channels to encode to, e.g. 2.
            max_audio_channels (int, optional): Optional. Specify a maximum
                number of audio channels to encode to, e.g. 2.
            profile (string, optional): Optional. Specify a specific an
                encoder profile (varies by encoder), e.g. main, baseline,
                high.
            level (string, optional): Optional. Specify a level for the
                encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float, optional): Optional. A specific video framerate
                to encode to, e.g. 23.976. Generally this should be omitted
                unless the device has specific requirements.
            max_framerate (float, optional): Optional. A specific maximum
                video framerate to encode to, e.g. 23.976. Generally this
                should be omitted unless the device has specific
                requirements.
            copy_timestamps (bool, optional): Whether or not to copy
                timestamps when transcoding with an offset. Defaults to
                false.
            start_time_ticks (long|int, optional): Optional. Specify a
                starting offset, in ticks. 1 tick = 10000 ms.
            width (int, optional): Optional. The fixed horizontal resolution
                of the encoded video.
            height (int, optional): Optional. The fixed vertical resolution of
                the encoded video.
            video_bit_rate (int, optional): Optional. Specify a video bitrate
                to encode to, e.g. 500000. If omitted this will be left to
                encoder defaults.
            subtitle_stream_index (int, optional): Optional. The index of the
                subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethodEnum, optional): Optional.
                Specify the subtitle delivery method.
            max_ref_frames (int, optional): Optional.
            max_video_bit_depth (int, optional): Optional. The maximum video
                bit depth.
            require_avc (bool, optional): Optional. Whether to require avc.
            de_interlace (bool, optional): Optional. Whether to deinterlace
                the video.
            require_non_anamorphic (bool, optional): Optional. Whether to
                require a non anamorphic stream.
            transcoding_max_audio_channels (int, optional): Optional. The
                maximum number of audio channels to transcode.
            cpu_core_limit (int, optional): Optional. The limit of how many
                cpu cores to use.
            live_stream_id (string, optional): The live stream id.
            enable_mpegts_m_2_ts_mode (bool, optional): Optional. Whether to
                enable the MpegtsM2Ts mode.
            video_codec (string, optional): Optional. Specify a video codec to
                encode to, e.g. h264. If omitted the server will auto-select
                using the url's extension. Options: h265, h264, mpeg4, theora,
                vp8, vp9, vpx (deprecated), wmv.
            subtitle_codec (string, optional): Optional. Specify a subtitle
                codec to encode to.
            transcode_reasons (string, optional): Optional. The transcoding
                reason.
            audio_stream_index (int, optional): Optional. The index of the
                audio stream to use. If omitted the first audio stream will be
                used.
            video_stream_index (int, optional): Optional. The index of the
                video stream to use. If omitted the first video stream will be
                used.
            context (EncodingContextEnum, optional): Optional. The
                MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (dict, optional): Optional. The streaming options.

        Returns:
            mixed: Response from the API. Audio stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_audio_stream called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_audio_stream.")
            _url_path = "/Audio/{itemId}/stream"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "container": container,
                "static": static,
                "params": params,
                "tag": tag,
                "deviceProfileId": device_profile_id,
                "playSessionId": play_session_id,
                "segmentContainer": segment_container,
                "segmentLength": segment_length,
                "minSegments": min_segments,
                "mediaSourceId": media_source_id,
                "deviceId": device_id,
                "audioCodec": audio_codec,
                "enableAutoStreamCopy": enable_auto_stream_copy,
                "allowVideoStreamCopy": allow_video_stream_copy,
                "allowAudioStreamCopy": allow_audio_stream_copy,
                "breakOnNonKeyFrames": break_on_non_key_frames,
                "audioSampleRate": audio_sample_rate,
                "maxAudioBitDepth": max_audio_bit_depth,
                "audioBitRate": audio_bit_rate,
                "audioChannels": audio_channels,
                "maxAudioChannels": max_audio_channels,
                "profile": profile,
                "level": level,
                "framerate": framerate,
                "maxFramerate": max_framerate,
                "copyTimestamps": copy_timestamps,
                "startTimeTicks": start_time_ticks,
                "width": width,
                "height": height,
                "videoBitRate": video_bit_rate,
                "subtitleStreamIndex": subtitle_stream_index,
                "subtitleMethod": subtitle_method,
                "maxRefFrames": max_ref_frames,
                "maxVideoBitDepth": max_video_bit_depth,
                "requireAvc": require_avc,
                "deInterlace": de_interlace,
                "requireNonAnamorphic": require_non_anamorphic,
                "transcodingMaxAudioChannels": transcoding_max_audio_channels,
                "cpuCoreLimit": cpu_core_limit,
                "liveStreamId": live_stream_id,
                "enableMpegtsM2TsMode": enable_mpegts_m_2_ts_mode,
                "videoCodec": video_codec,
                "subtitleCodec": subtitle_codec,
                "transcodeReasons": transcode_reasons,
                "audioStreamIndex": audio_stream_index,
                "videoStreamIndex": video_stream_index,
                "context": context,
                "streamOptions": stream_options,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_audio_stream.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_audio_stream.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_audio_stream")
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_audio_stream_by_container(
        self,
        item_id,
        container,
        static=None,
        params=None,
        tag=None,
        device_profile_id=None,
        play_session_id=None,
        segment_container=None,
        segment_length=None,
        min_segments=None,
        media_source_id=None,
        device_id=None,
        audio_codec=None,
        enable_auto_stream_copy=None,
        allow_video_stream_copy=None,
        allow_audio_stream_copy=None,
        break_on_non_key_frames=None,
        audio_sample_rate=None,
        max_audio_bit_depth=None,
        audio_bit_rate=None,
        audio_channels=None,
        max_audio_channels=None,
        profile=None,
        level=None,
        framerate=None,
        max_framerate=None,
        copy_timestamps=None,
        start_time_ticks=None,
        width=None,
        height=None,
        video_bit_rate=None,
        subtitle_stream_index=None,
        subtitle_method=None,
        max_ref_frames=None,
        max_video_bit_depth=None,
        require_avc=None,
        de_interlace=None,
        require_non_anamorphic=None,
        transcoding_max_audio_channels=None,
        cpu_core_limit=None,
        live_stream_id=None,
        enable_mpegts_m_2_ts_mode=None,
        video_codec=None,
        subtitle_codec=None,
        transcode_reasons=None,
        audio_stream_index=None,
        video_stream_index=None,
        context=None,
        stream_options=None,
    ):
        """Does a GET request to /Audio/{itemId}/stream.{container}.

        Gets an audio stream.

        Args:
            item_id (uuid|string): The item id.
            container (string): The audio container.
            static (bool, optional): Optional. If true, the original file will
                be streamed statically without any encoding. Use either no url
                extension or the original file extension. true/false.
            params (string, optional): The streaming parameters.
            tag (string, optional): The tag.
            device_profile_id (string, optional): Optional. The dlna device
                profile id to utilize.
            play_session_id (string, optional): The play session id.
            segment_container (string, optional): The segment container.
            segment_length (int, optional): The segment lenght.
            min_segments (int, optional): The minimum number of segments.
            media_source_id (string, optional): The media version id, if
                playing an alternate version.
            device_id (string, optional): The device id of the client
                requesting. Used to stop encoding processes when needed.
            audio_codec (string, optional): Optional. Specify a audio codec to
                encode to, e.g. mp3. If omitted the server will auto-select
                using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool, optional): Whether or not to allow
                automatic stream copy if requested values match the original
                source. Defaults to true.
            allow_video_stream_copy (bool, optional): Whether or not to allow
                copying of the video stream url.
            allow_audio_stream_copy (bool, optional): Whether or not to allow
                copying of the audio stream url.
            break_on_non_key_frames (bool, optional): Optional. Whether to
                break on non key frames.
            audio_sample_rate (int, optional): Optional. Specify a specific
                audio sample rate, e.g. 44100.
            max_audio_bit_depth (int, optional): Optional. The maximum audio
                bit depth.
            audio_bit_rate (int, optional): Optional. Specify an audio bitrate
                to encode to, e.g. 128000. If omitted this will be left to
                encoder defaults.
            audio_channels (int, optional): Optional. Specify a specific
                number of audio channels to encode to, e.g. 2.
            max_audio_channels (int, optional): Optional. Specify a maximum
                number of audio channels to encode to, e.g. 2.
            profile (string, optional): Optional. Specify a specific an
                encoder profile (varies by encoder), e.g. main, baseline,
                high.
            level (string, optional): Optional. Specify a level for the
                encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float, optional): Optional. A specific video framerate
                to encode to, e.g. 23.976. Generally this should be omitted
                unless the device has specific requirements.
            max_framerate (float, optional): Optional. A specific maximum
                video framerate to encode to, e.g. 23.976. Generally this
                should be omitted unless the device has specific
                requirements.
            copy_timestamps (bool, optional): Whether or not to copy
                timestamps when transcoding with an offset. Defaults to
                false.
            start_time_ticks (long|int, optional): Optional. Specify a
                starting offset, in ticks. 1 tick = 10000 ms.
            width (int, optional): Optional. The fixed horizontal resolution
                of the encoded video.
            height (int, optional): Optional. The fixed vertical resolution of
                the encoded video.
            video_bit_rate (int, optional): Optional. Specify a video bitrate
                to encode to, e.g. 500000. If omitted this will be left to
                encoder defaults.
            subtitle_stream_index (int, optional): Optional. The index of the
                subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethodEnum, optional): Optional.
                Specify the subtitle delivery method.
            max_ref_frames (int, optional): Optional.
            max_video_bit_depth (int, optional): Optional. The maximum video
                bit depth.
            require_avc (bool, optional): Optional. Whether to require avc.
            de_interlace (bool, optional): Optional. Whether to deinterlace
                the video.
            require_non_anamorphic (bool, optional): Optional. Whether to
                require a non anamporphic stream.
            transcoding_max_audio_channels (int, optional): Optional. The
                maximum number of audio channels to transcode.
            cpu_core_limit (int, optional): Optional. The limit of how many
                cpu cores to use.
            live_stream_id (string, optional): The live stream id.
            enable_mpegts_m_2_ts_mode (bool, optional): Optional. Whether to
                enable the MpegtsM2Ts mode.
            video_codec (string, optional): Optional. Specify a video codec to
                encode to, e.g. h264. If omitted the server will auto-select
                using the url's extension. Options: h265, h264, mpeg4, theora,
                vp8, vp9, vpx (deprecated), wmv.
            subtitle_codec (string, optional): Optional. Specify a subtitle
                codec to encode to.
            transcode_reasons (string, optional): Optional. The transcoding
                reason.
            audio_stream_index (int, optional): Optional. The index of the
                audio stream to use. If omitted the first audio stream will be
                used.
            video_stream_index (int, optional): Optional. The index of the
                video stream to use. If omitted the first video stream will be
                used.
            context (EncodingContextEnum, optional): Optional. The
                MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (dict, optional): Optional. The streaming options.

        Returns:
            mixed: Response from the API. Audio stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_audio_stream_by_container called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_audio_stream_by_container.")
            _url_path = "/Audio/{itemId}/stream.{container}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "container": {"value": container, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "static": static,
                "params": params,
                "tag": tag,
                "deviceProfileId": device_profile_id,
                "playSessionId": play_session_id,
                "segmentContainer": segment_container,
                "segmentLength": segment_length,
                "minSegments": min_segments,
                "mediaSourceId": media_source_id,
                "deviceId": device_id,
                "audioCodec": audio_codec,
                "enableAutoStreamCopy": enable_auto_stream_copy,
                "allowVideoStreamCopy": allow_video_stream_copy,
                "allowAudioStreamCopy": allow_audio_stream_copy,
                "breakOnNonKeyFrames": break_on_non_key_frames,
                "audioSampleRate": audio_sample_rate,
                "maxAudioBitDepth": max_audio_bit_depth,
                "audioBitRate": audio_bit_rate,
                "audioChannels": audio_channels,
                "maxAudioChannels": max_audio_channels,
                "profile": profile,
                "level": level,
                "framerate": framerate,
                "maxFramerate": max_framerate,
                "copyTimestamps": copy_timestamps,
                "startTimeTicks": start_time_ticks,
                "width": width,
                "height": height,
                "videoBitRate": video_bit_rate,
                "subtitleStreamIndex": subtitle_stream_index,
                "subtitleMethod": subtitle_method,
                "maxRefFrames": max_ref_frames,
                "maxVideoBitDepth": max_video_bit_depth,
                "requireAvc": require_avc,
                "deInterlace": de_interlace,
                "requireNonAnamorphic": require_non_anamorphic,
                "transcodingMaxAudioChannels": transcoding_max_audio_channels,
                "cpuCoreLimit": cpu_core_limit,
                "liveStreamId": live_stream_id,
                "enableMpegtsM2TsMode": enable_mpegts_m_2_ts_mode,
                "videoCodec": video_codec,
                "subtitleCodec": subtitle_codec,
                "transcodeReasons": transcode_reasons,
                "audioStreamIndex": audio_stream_index,
                "videoStreamIndex": video_stream_index,
                "context": context,
                "streamOptions": stream_options,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_audio_stream_by_container.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_audio_stream_by_container."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_audio_stream_by_container"
            )
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
