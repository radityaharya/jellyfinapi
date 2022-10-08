# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class TvShowsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(TvShowsControllerTests, cls).setUpClass()
        cls.controller = cls.client.tv_shows
        cls.response_catcher = cls.controller.http_call_back

    # Gets a list of next up episodes.
    def test_get_next_up(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        series_id = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        next_up_date_cutoff = None
        enable_total_record_count = True
        disable_first_episode = False
        enable_rewatching = False

        # Perform the API call through the SDK function
        result = self.controller.get_next_up(
            user_id,
            start_index,
            limit,
            fields,
            series_id,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            next_up_date_cutoff,
            enable_total_record_count,
            disable_first_episode,
            enable_rewatching,
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

    # Gets a list of next up episodes.
    def test_get_next_up_1(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        series_id = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        next_up_date_cutoff = None
        enable_total_record_count = True
        disable_first_episode = False
        enable_rewatching = False

        # Perform the API call through the SDK function
        result = self.controller.get_next_up(
            user_id,
            start_index,
            limit,
            fields,
            series_id,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            next_up_date_cutoff,
            enable_total_record_count,
            disable_first_episode,
            enable_rewatching,
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

    # Gets a list of next up episodes.
    def test_get_next_up_2(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        series_id = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None
        next_up_date_cutoff = None
        enable_total_record_count = True
        disable_first_episode = False
        enable_rewatching = False

        # Perform the API call through the SDK function
        result = self.controller.get_next_up(
            user_id,
            start_index,
            limit,
            fields,
            series_id,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            next_up_date_cutoff,
            enable_total_record_count,
            disable_first_episode,
            enable_rewatching,
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

    # Gets a list of upcoming episodes.
    def test_get_upcoming_episodes(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None

        # Perform the API call through the SDK function
        result = self.controller.get_upcoming_episodes(
            user_id,
            start_index,
            limit,
            fields,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
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

    # Gets a list of upcoming episodes.
    def test_get_upcoming_episodes_1(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None

        # Perform the API call through the SDK function
        result = self.controller.get_upcoming_episodes(
            user_id,
            start_index,
            limit,
            fields,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
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

    # Gets a list of upcoming episodes.
    def test_get_upcoming_episodes_2(self):
        # Parameters for the API call
        user_id = None
        start_index = None
        limit = None
        fields = None
        parent_id = None
        enable_images = None
        image_type_limit = None
        enable_image_types = None
        enable_user_data = None

        # Perform the API call through the SDK function
        result = self.controller.get_upcoming_episodes(
            user_id,
            start_index,
            limit,
            fields,
            parent_id,
            enable_images,
            image_type_limit,
            enable_image_types,
            enable_user_data,
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
