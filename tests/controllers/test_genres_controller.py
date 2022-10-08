# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class GenresControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(GenresControllerTests, cls).setUpClass()
        cls.controller = cls.client.genres
        cls.response_catcher = cls.controller.http_call_back

    # Gets all genres from a given item, folder, or the entire library.
    def test_get_genres(self):
        # Parameters for the API call
        start_index = None
        limit = None
        search_term = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        is_favorite = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        sort_by = None
        sort_order = None
        enable_images = True
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_genres(
            start_index,
            limit,
            search_term,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            is_favorite,
            image_type_limit,
            enable_image_types,
            user_id,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            sort_by,
            sort_order,
            enable_images,
            enable_total_record_count,
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

    # Gets all genres from a given item, folder, or the entire library.
    def test_get_genres_1(self):
        # Parameters for the API call
        start_index = None
        limit = None
        search_term = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        is_favorite = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        sort_by = None
        sort_order = None
        enable_images = True
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_genres(
            start_index,
            limit,
            search_term,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            is_favorite,
            image_type_limit,
            enable_image_types,
            user_id,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            sort_by,
            sort_order,
            enable_images,
            enable_total_record_count,
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

    # Gets all genres from a given item, folder, or the entire library.
    def test_get_genres_2(self):
        # Parameters for the API call
        start_index = None
        limit = None
        search_term = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        is_favorite = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        name_starts_with_or_greater = None
        name_starts_with = None
        name_less_than = None
        sort_by = None
        sort_order = None
        enable_images = True
        enable_total_record_count = True

        # Perform the API call through the SDK function
        result = self.controller.get_genres(
            start_index,
            limit,
            search_term,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            is_favorite,
            image_type_limit,
            enable_image_types,
            user_id,
            name_starts_with_or_greater,
            name_starts_with,
            name_less_than,
            sort_by,
            sort_order,
            enable_images,
            enable_total_record_count,
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
