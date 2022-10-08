# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.device_profile import DeviceProfile


class DlnaControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(DlnaControllerTests, cls).setUpClass()
        cls.controller = cls.client.dlna
        cls.response_catcher = cls.controller.http_call_back

    # Get profile infos.
    def test_get_profile_infos(self):

        # Perform the API call through the SDK function
        result = self.controller.get_profile_infos()

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

    # Get profile infos.
    def test_get_profile_infos_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_profile_infos()

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

    # Get profile infos.
    def test_get_profile_infos_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_profile_infos()

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

    # Creates a profile.
    def test_create_profile(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.create_profile(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the default profile.
    def test_get_default_profile(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_profile()

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

    # Gets the default profile.
    def test_get_default_profile_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_profile()

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

    # Gets the default profile.
    def test_get_default_profile_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_profile()

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
