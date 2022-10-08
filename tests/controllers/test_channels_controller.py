# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class ChannelsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(ChannelsControllerTests, cls).setUpClass()
        cls.controller = cls.client.channels
        cls.response_catcher = cls.controller.http_call_back

    # Gets available channels.
    def test_get_channels(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        supports_latest_items = None
        supports_media_deletion = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_channels(
            user_id,
            start_index,
            limit,
            supports_latest_items,
            supports_media_deletion,
            is_favorite,
        )

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

    # Gets available channels.
    def test_get_channels_1(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        supports_latest_items = None
        supports_media_deletion = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_channels(
            user_id,
            start_index,
            limit,
            supports_latest_items,
            supports_media_deletion,
            is_favorite,
        )

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

    # Gets available channels.
    def test_get_channels_2(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        supports_latest_items = None
        supports_media_deletion = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_channels(
            user_id,
            start_index,
            limit,
            supports_latest_items,
            supports_media_deletion,
            is_favorite,
        )

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

    # Get all channel features.
    def test_get_all_channel_features(self):

        # Perform the API call through the SDK function
        result = self.controller.get_all_channel_features()

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

    # Get all channel features.
    def test_get_all_channel_features_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_all_channel_features()

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

    # Get all channel features.
    def test_get_all_channel_features_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_all_channel_features()

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

    # Gets latest channel items.
    def test_get_latest_channel_items(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        filters = None
        fields = None
        channel_ids = None

        # Perform the API call through the SDK function
        result = self.controller.get_latest_channel_items(
            user_id, start_index, limit, filters, fields, channel_ids
        )

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

    # Gets latest channel items.
    def test_get_latest_channel_items_1(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        filters = None
        fields = None
        channel_ids = None

        # Perform the API call through the SDK function
        result = self.controller.get_latest_channel_items(
            user_id, start_index, limit, filters, fields, channel_ids
        )

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

    # Gets latest channel items.
    def test_get_latest_channel_items_2(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        filters = None
        fields = None
        channel_ids = None

        # Perform the API call through the SDK function
        result = self.controller.get_latest_channel_items(
            user_id, start_index, limit, filters, fields, channel_ids
        )

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
