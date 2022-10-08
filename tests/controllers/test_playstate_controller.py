# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.playback_start_info import PlaybackStartInfo
from jellyfinapi.models.playback_progress_info import PlaybackProgressInfo
from jellyfinapi.models.playback_stop_info import PlaybackStopInfo


class PlaystateControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(PlaystateControllerTests, cls).setUpClass()
        cls.controller = cls.client.playstate
        cls.response_catcher = cls.controller.http_call_back

    # Reports playback has started within a session.
    def test_report_playback_start(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.report_playback_start(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports playback progress within a session.
    def test_report_playback_progress(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.report_playback_progress(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports playback has stopped within a session.
    def test_report_playback_stopped(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.report_playback_stopped(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
