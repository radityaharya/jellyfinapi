# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class EnvironmentControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(EnvironmentControllerTests, cls).setUpClass()
        cls.controller = cls.client.environment
        cls.response_catcher = cls.controller.http_call_back

    # Get Default directory browser.
    def test_get_default_directory_browser(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_directory_browser()

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

    # Get Default directory browser.
    def test_get_default_directory_browser_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_directory_browser()

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

    # Get Default directory browser.
    def test_get_default_directory_browser_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_directory_browser()

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

    # Gets available drives from the server's file system.
    def test_get_drives(self):

        # Perform the API call through the SDK function
        result = self.controller.get_drives()

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

    # Gets available drives from the server's file system.
    def test_get_drives_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_drives()

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

    # Gets available drives from the server's file system.
    def test_get_drives_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_drives()

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

    # Gets network paths.
    def test_get_network_shares(self):

        # Perform the API call through the SDK function
        result = self.controller.get_network_shares()

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

    # Gets network paths.
    def test_get_network_shares_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_network_shares()

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

    # Gets network paths.
    def test_get_network_shares_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_network_shares()

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
