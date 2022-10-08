# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class DashboardControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(DashboardControllerTests, cls).setUpClass()
        cls.controller = cls.client.dashboard
        cls.response_catcher = cls.controller.http_call_back

    # Gets a dashboard configuration page.
    def test_get_dashboard_configuration_page(self):
        # Parameters for the API call
        name = None

        # Perform the API call through the SDK function
        result = self.controller.get_dashboard_configuration_page(name)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "text/html"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Gets a dashboard configuration page.
    def test_get_dashboard_configuration_page_1(self):
        # Parameters for the API call
        name = None

        # Perform the API call through the SDK function
        result = self.controller.get_dashboard_configuration_page(name)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "application/x-javascript"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Gets the configuration pages.
    def test_get_configuration_pages(self):
        # Parameters for the API call
        enable_in_main_menu = None

        # Perform the API call through the SDK function
        result = self.controller.get_configuration_pages(enable_in_main_menu)

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

    # Gets the configuration pages.
    def test_get_configuration_pages_1(self):
        # Parameters for the API call
        enable_in_main_menu = None

        # Perform the API call through the SDK function
        result = self.controller.get_configuration_pages(enable_in_main_menu)

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

    # Gets the configuration pages.
    def test_get_configuration_pages_2(self):
        # Parameters for the API call
        enable_in_main_menu = None

        # Perform the API call through the SDK function
        result = self.controller.get_configuration_pages(enable_in_main_menu)

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
