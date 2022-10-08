# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class DevicesControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(DevicesControllerTests, cls).setUpClass()
        cls.controller = cls.client.devices
        cls.response_catcher = cls.controller.http_call_back

    # Get Devices.
    def test_get_devices(self):
        # Parameters for the API call
        supports_sync = None
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_devices(supports_sync, user_id)

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

    # Get Devices.
    def test_get_devices_1(self):
        # Parameters for the API call
        supports_sync = None
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_devices(supports_sync, user_id)

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

    # Get Devices.
    def test_get_devices_2(self):
        # Parameters for the API call
        supports_sync = None
        user_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_devices(supports_sync, user_id)

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
