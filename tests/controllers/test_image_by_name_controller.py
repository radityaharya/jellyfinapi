# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ImageByNameControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ImageByNameControllerTests, cls).setUpClass()
        cls.controller = cls.client.image_by_name
        cls.response_catcher = cls.controller.http_call_back

    # Get all general images.
    def test_get_general_images(self):

        # Perform the API call through the SDK function
        result = self.controller.get_general_images()

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

    # Get all general images.
    def test_get_general_images_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_general_images()

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

    # Get all general images.
    def test_get_general_images_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_general_images()

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

    # Get all media info images.
    def test_get_media_info_images(self):

        # Perform the API call through the SDK function
        result = self.controller.get_media_info_images()

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

    # Get all media info images.
    def test_get_media_info_images_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_media_info_images()

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

    # Get all media info images.
    def test_get_media_info_images_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_media_info_images()

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

    # Get all general images.
    def test_get_rating_images(self):

        # Perform the API call through the SDK function
        result = self.controller.get_rating_images()

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

    # Get all general images.
    def test_get_rating_images_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_rating_images()

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

    # Get all general images.
    def test_get_rating_images_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_rating_images()

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
