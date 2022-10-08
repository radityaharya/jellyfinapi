# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ActivityLogControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ActivityLogControllerTests, cls).setUpClass()
        cls.controller = cls.client.activity_log
        cls.response_catcher = cls.controller.http_call_back

    # Gets activity log entries.
    def test_get_log_entries(self):
        # Parameters for the API call
        start_index = None
        limit = None
        min_date = None
        has_user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_log_entries(
            start_index, limit, min_date, has_user_id
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

    # Gets activity log entries.
    def test_get_log_entries_1(self):
        # Parameters for the API call
        start_index = None
        limit = None
        min_date = None
        has_user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_log_entries(
            start_index, limit, min_date, has_user_id
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

    # Gets activity log entries.
    def test_get_log_entries_2(self):
        # Parameters for the API call
        start_index = None
        limit = None
        min_date = None
        has_user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_log_entries(
            start_index, limit, min_date, has_user_id
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
