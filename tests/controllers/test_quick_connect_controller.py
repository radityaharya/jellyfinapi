# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class QuickConnectControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(QuickConnectControllerTests, cls).setUpClass()
        cls.controller = cls.client.quick_connect
        cls.response_catcher = cls.controller.http_call_back

    # Gets the current quick connect state.
    def test_get_enabled(self):

        # Perform the API call through the SDK function
        result = self.controller.get_enabled()

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

    # Gets the current quick connect state.
    def test_get_enabled_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_enabled()

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

    # Gets the current quick connect state.
    def test_get_enabled_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_enabled()

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

    # Initiate a new quick connect request.
    def test_initiate(self):

        # Perform the API call through the SDK function
        result = self.controller.initiate()

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

    # Initiate a new quick connect request.
    def test_initiate_1(self):

        # Perform the API call through the SDK function
        result = self.controller.initiate()

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

    # Initiate a new quick connect request.
    def test_initiate_2(self):

        # Perform the API call through the SDK function
        result = self.controller.initiate()

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
