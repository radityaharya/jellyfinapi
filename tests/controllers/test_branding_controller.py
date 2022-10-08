# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class BrandingControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(BrandingControllerTests, cls).setUpClass()
        cls.controller = cls.client.branding
        cls.response_catcher = cls.controller.http_call_back

    # Gets branding configuration.
    def test_get_branding_options(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_options()

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

    # Gets branding configuration.
    def test_get_branding_options_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_options()

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

    # Gets branding configuration.
    def test_get_branding_options_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_options()

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

    # Gets branding css.
    def test_get_branding_css(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css()

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

    # Gets branding css.
    def test_get_branding_css_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css()

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

    # Gets branding css.
    def test_get_branding_css_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css()

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

    # Gets branding css.
    def test_get_branding_css_3(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css()

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

    # Gets branding css.
    def test_get_branding_css_4(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets branding css.
    def test_get_branding_css_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css_2()

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

    # Gets branding css.
    def test_get_branding_css_21(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css_2()

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

    # Gets branding css.
    def test_get_branding_css_22(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css_2()

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

    # Gets branding css.
    def test_get_branding_css_23(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css_2()

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

    # Gets branding css.
    def test_get_branding_css_24(self):

        # Perform the API call through the SDK function
        result = self.controller.get_branding_css_2()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
