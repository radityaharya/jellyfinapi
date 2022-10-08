# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ImageControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ImageControllerTests, cls).setUpClass()
        cls.controller = cls.client.image
        cls.response_catcher = cls.controller.http_call_back

    # Generates or gets the splashscreen.
    def test_get_splashscreen(self):
        # Parameters for the API call
        tag = None
        format = None
        max_width = None
        max_height = None
        width = None
        height = None
        fill_width = None
        fill_height = None
        blur = None
        background_color = None
        foreground_layer = None
        quality = 90

        # Perform the API call through the SDK function
        result = self.controller.get_splashscreen(
            tag,
            format,
            max_width,
            max_height,
            width,
            height,
            fill_width,
            fill_height,
            blur,
            background_color,
            foreground_layer,
            quality,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # Uploads a custom splashscreen.
    # The body is expected to the image contents base64 encoded.
    def test_upload_custom_splashscreen(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.upload_custom_splashscreen(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Delete a custom splashscreen.
    def test_delete_custom_splashscreen(self):

        # Perform the API call through the SDK function
        self.controller.delete_custom_splashscreen()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
