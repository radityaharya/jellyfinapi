# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class PluginsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(PluginsControllerTests, cls).setUpClass()
        cls.controller = cls.client.plugins
        cls.response_catcher = cls.controller.http_call_back

    # Gets a list of currently installed plugins.
    def test_get_plugins(self):

        # Perform the API call through the SDK function
        result = self.controller.get_plugins()

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

    # Gets a list of currently installed plugins.
    def test_get_plugins_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_plugins()

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

    # Gets a list of currently installed plugins.
    def test_get_plugins_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_plugins()

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
