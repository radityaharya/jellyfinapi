# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class TimeSyncControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(TimeSyncControllerTests, cls).setUpClass()
        cls.controller = cls.client.time_sync
        cls.response_catcher = cls.controller.http_call_back

    # Gets the current UTC time.
    def test_get_utc_time(self):

        # Perform the API call through the SDK function
        result = self.controller.get_utc_time()

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

    # Gets the current UTC time.
    def test_get_utc_time_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_utc_time()

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

    # Gets the current UTC time.
    def test_get_utc_time_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_utc_time()

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
