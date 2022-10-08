# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class MoviesControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(MoviesControllerTests, cls).setUpClass()
        cls.controller = cls.client.movies
        cls.response_catcher = cls.controller.http_call_back

    # Gets movie recommendations.
    def test_get_movie_recommendations(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        fields = None
        category_limit = 5
        item_limit = 8

        # Perform the API call through the SDK function
        result = self.controller.get_movie_recommendations(
            user_id, parent_id, fields, category_limit, item_limit
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

    # Gets movie recommendations.
    def test_get_movie_recommendations_1(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        fields = None
        category_limit = 5
        item_limit = 8

        # Perform the API call through the SDK function
        result = self.controller.get_movie_recommendations(
            user_id, parent_id, fields, category_limit, item_limit
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

    # Gets movie recommendations.
    def test_get_movie_recommendations_2(self):
        # Parameters for the API call
        user_id = None
        parent_id = None
        fields = None
        category_limit = 5
        item_limit = 8

        # Perform the API call through the SDK function
        result = self.controller.get_movie_recommendations(
            user_id, parent_id, fields, category_limit, item_limit
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
