# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class YearsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(YearsControllerTests, cls).setUpClass()
        cls.controller = cls.client.years
        cls.response_catcher = cls.controller.http_call_back

    # Get years.
    def test_get_years(self):
        # Parameters for the API call
        start_index = None
        limit = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        media_types = None
        sort_by = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        recursive = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_years(
            start_index,
            limit,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            media_types,
            sort_by,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            user_id,
            recursive,
            enable_images,
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

    # Get years.
    def test_get_years_1(self):
        # Parameters for the API call
        start_index = None
        limit = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        media_types = None
        sort_by = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        recursive = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_years(
            start_index,
            limit,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            media_types,
            sort_by,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            user_id,
            recursive,
            enable_images,
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

    # Get years.
    def test_get_years_2(self):
        # Parameters for the API call
        start_index = None
        limit = None
        sort_order = None
        parent_id = None
        fields = None
        exclude_item_types = None
        include_item_types = None
        media_types = None
        sort_by = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        user_id = None
        recursive = True
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_years(
            start_index,
            limit,
            sort_order,
            parent_id,
            fields,
            exclude_item_types,
            include_item_types,
            media_types,
            sort_by,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            user_id,
            recursive,
            enable_images,
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
