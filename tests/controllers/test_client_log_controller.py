# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ClientLogControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ClientLogControllerTests, cls).setUpClass()
        cls.controller = cls.client.client_log
        cls.response_catcher = cls.controller.http_call_back

    # Upload a document.
    def test_log_file(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.log_file(body)

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

    # Upload a document.
    def test_log_file_1(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.log_file(body)

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

    # Upload a document.
    def test_log_file_2(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.log_file(body)

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
