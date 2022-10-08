# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ConfigurationControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ConfigurationControllerTests, cls).setUpClass()
        cls.controller = cls.client.configuration
        cls.response_catcher = cls.controller.http_call_back

    # Gets application configuration.
    def test_get_configuration(self):

        # Perform the API call through the SDK function
        result = self.controller.get_configuration()

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

    # Gets application configuration.
    def test_get_configuration_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_configuration()

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

    # Gets application configuration.
    def test_get_configuration_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_configuration()

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

    # Gets a default MetadataOptions object.
    def test_get_default_metadata_options(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_metadata_options()

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

    # Gets a default MetadataOptions object.
    def test_get_default_metadata_options_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_metadata_options()

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

    # Gets a default MetadataOptions object.
    def test_get_default_metadata_options_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_default_metadata_options()

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
