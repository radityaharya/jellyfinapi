# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class EndpointsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(EndpointsControllerTests, cls).setUpClass()
        cls.controller = cls.client.endpoints
        cls.response_catcher = cls.controller.http_call_back

    # Testcase for testing endpoint GetPin
    def test_get_pin(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

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

    # Testcase for testing endpoint GetPin
    def test_get_pin_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

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

    # Testcase for testing endpoint GetPin
    def test_get_pin_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

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

    # Testcase for testing endpoint GetPin
    def test_get_pin_3(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "text/plain"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Testcase for testing endpoint GetPin
    def test_get_pin_4(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "text/json"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Testcase for testing endpoint GetPin
    def test_get_pin_5(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "text/css"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )

    # Testcase for testing endpoint GetPin
    def test_get_pin_6(self):

        # Perform the API call through the SDK function
        result = self.controller.get_pin()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers["content-type"] = "text/xml"

        self.assertTrue(
            TestHelper.match_headers(
                expected_headers, self.response_catcher.response.headers
            )
        )
