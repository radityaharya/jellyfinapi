# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.login_info_input import LoginInfoInput


class OpenSubtitlesControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(OpenSubtitlesControllerTests, cls).setUpClass()
        cls.controller = cls.client.open_subtitles
        cls.response_catcher = cls.controller.http_call_back

    # Testcase for testing endpoint ValidateLoginInfo
    def test_validate_login_info(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.validate_login_info(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
