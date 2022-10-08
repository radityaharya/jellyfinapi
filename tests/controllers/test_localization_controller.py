# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class LocalizationControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(LocalizationControllerTests, cls).setUpClass()
        cls.controller = cls.client.localization
        cls.response_catcher = cls.controller.http_call_back

    # Gets known countries.
    def test_get_countries(self):

        # Perform the API call through the SDK function
        result = self.controller.get_countries()

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

    # Gets known countries.
    def test_get_countries_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_countries()

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

    # Gets known countries.
    def test_get_countries_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_countries()

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

    # Gets known cultures.
    def test_get_cultures(self):

        # Perform the API call through the SDK function
        result = self.controller.get_cultures()

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

    # Gets known cultures.
    def test_get_cultures_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_cultures()

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

    # Gets known cultures.
    def test_get_cultures_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_cultures()

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

    # Gets localization options.
    def test_get_localization_options(self):

        # Perform the API call through the SDK function
        result = self.controller.get_localization_options()

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

    # Gets localization options.
    def test_get_localization_options_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_localization_options()

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

    # Gets localization options.
    def test_get_localization_options_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_localization_options()

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

    # Gets known parental ratings.
    def test_get_parental_ratings(self):

        # Perform the API call through the SDK function
        result = self.controller.get_parental_ratings()

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

    # Gets known parental ratings.
    def test_get_parental_ratings_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_parental_ratings()

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

    # Gets known parental ratings.
    def test_get_parental_ratings_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_parental_ratings()

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
