# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ScheduledTasksControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ScheduledTasksControllerTests, cls).setUpClass()
        cls.controller = cls.client.scheduled_tasks
        cls.response_catcher = cls.controller.http_call_back

    # Get tasks.
    def test_get_tasks(self):
        # Parameters for the API call
        is_hidden = None
        is_enabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_tasks(is_hidden, is_enabled)

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

    # Get tasks.
    def test_get_tasks_1(self):
        # Parameters for the API call
        is_hidden = None
        is_enabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_tasks(is_hidden, is_enabled)

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

    # Get tasks.
    def test_get_tasks_2(self):
        # Parameters for the API call
        is_hidden = None
        is_enabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_tasks(is_hidden, is_enabled)

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
