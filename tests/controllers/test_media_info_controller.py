# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.open_live_stream_dto import OpenLiveStreamDto


class MediaInfoControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(MediaInfoControllerTests, cls).setUpClass()
        cls.controller = cls.client.media_info
        cls.response_catcher = cls.controller.http_call_back

    # Opens a media source.
    def test_open_live_stream(self):
        # Parameters for the API call
        open_token = None
        user_id = None
        play_session_id = None
        max_streaming_bitrate = None
        start_time_ticks = None
        audio_stream_index = None
        subtitle_stream_index = None
        max_audio_channels = None
        item_id = None
        enable_direct_play = None
        enable_direct_stream = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.open_live_stream(
            open_token,
            user_id,
            play_session_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            item_id,
            enable_direct_play,
            enable_direct_stream,
            body,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "application/json"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Opens a media source.
    def test_open_live_stream_1(self):
        # Parameters for the API call
        open_token = None
        user_id = None
        play_session_id = None
        max_streaming_bitrate = None
        start_time_ticks = None
        audio_stream_index = None
        subtitle_stream_index = None
        max_audio_channels = None
        item_id = None
        enable_direct_play = None
        enable_direct_stream = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.open_live_stream(
            open_token,
            user_id,
            play_session_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            item_id,
            enable_direct_play,
            enable_direct_stream,
            body,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = 'application/json; profile="CamelCase"'

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Opens a media source.
    def test_open_live_stream_2(self):
        # Parameters for the API call
        open_token = None
        user_id = None
        play_session_id = None
        max_streaming_bitrate = None
        start_time_ticks = None
        audio_stream_index = None
        subtitle_stream_index = None
        max_audio_channels = None
        item_id = None
        enable_direct_play = None
        enable_direct_stream = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.open_live_stream(
            open_token,
            user_id,
            play_session_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            item_id,
            enable_direct_play,
            enable_direct_stream,
            body,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = 'application/json; profile="PascalCase"'

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Tests the network with a request with the size of the bitrate.
    def test_get_bitrate_test_bytes(self):
        # Parameters for the API call
        size = 102400

        # Perform the API call through the SDK function
        result = self.controller.get_bitrate_test_bytes(size)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "application/octet-stream"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )
