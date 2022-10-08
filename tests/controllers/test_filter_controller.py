# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class FilterControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(FilterControllerTests, cls).setUpClass()
        cls.controller = cls.client.filter
        cls.response_catcher = cls.controller.http_call_back

    # Gets legacy query filters.
    def test_get_query_filters_legacy(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        media_types = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters_legacy(
            user_id, parent_id, include_item_types, media_types
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

    # Gets legacy query filters.
    def test_get_query_filters_legacy_1(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        media_types = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters_legacy(
            user_id, parent_id, include_item_types, media_types
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

    # Gets legacy query filters.
    def test_get_query_filters_legacy_2(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        media_types = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters_legacy(
            user_id, parent_id, include_item_types, media_types
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

    # Gets query filters.
    def test_get_query_filters(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        is_airing = None
        is_movie = None
        is_sports = None
        is_kids = None
        is_news = None
        is_series = None
        recursive = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters(
            user_id,
            parent_id,
            include_item_types,
            is_airing,
            is_movie,
            is_sports,
            is_kids,
            is_news,
            is_series,
            recursive,
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

    # Gets query filters.
    def test_get_query_filters_1(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        is_airing = None
        is_movie = None
        is_sports = None
        is_kids = None
        is_news = None
        is_series = None
        recursive = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters(
            user_id,
            parent_id,
            include_item_types,
            is_airing,
            is_movie,
            is_sports,
            is_kids,
            is_news,
            is_series,
            recursive,
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

    # Gets query filters.
    def test_get_query_filters_2(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        include_item_types = None
        is_airing = None
        is_movie = None
        is_sports = None
        is_kids = None
        is_news = None
        is_series = None
        recursive = None

        # Perform the API call through the SDK function
        result = self.controller.get_query_filters(
            user_id,
            parent_id,
            include_item_types,
            is_airing,
            is_movie,
            is_sports,
            is_kids,
            is_news,
            is_series,
            recursive,
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
