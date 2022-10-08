# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class PackageControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(PackageControllerTests, cls).setUpClass()
        cls.controller = cls.client.package
        cls.response_catcher = cls.controller.http_call_back

    # Gets available packages.
    def test_get_packages(self):

        # Perform the API call through the SDK function
        result = self.controller.get_packages()

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

    # Gets available packages.
    def test_get_packages_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_packages()

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

    # Gets available packages.
    def test_get_packages_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_packages()

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

    # Gets all package repositories.
    def test_get_repositories(self):

        # Perform the API call through the SDK function
        result = self.controller.get_repositories()

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

    # Gets all package repositories.
    def test_get_repositories_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_repositories()

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

    # Gets all package repositories.
    def test_get_repositories_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_repositories()

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
