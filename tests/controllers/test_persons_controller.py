# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class PersonsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(PersonsControllerTests, cls).setUpClass()
        cls.controller = cls.client.persons
        cls.response_catcher = cls.controller.http_call_back

    # Gets all persons.
    def test_get_persons(self):
        # Parameters for the API call
        limit = None
        search_term = None
        fields = None
        filters = None
        is_favorite = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        exclude_person_types = None
        person_types = None
        appears_in_item_id = None
        user_id = None
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_persons(
            limit,
            search_term,
            fields,
            filters,
            is_favorite,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            exclude_person_types,
            person_types,
            appears_in_item_id,
            user_id,
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

    # Gets all persons.
    def test_get_persons_1(self):
        # Parameters for the API call
        limit = None
        search_term = None
        fields = None
        filters = None
        is_favorite = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        exclude_person_types = None
        person_types = None
        appears_in_item_id = None
        user_id = None
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_persons(
            limit,
            search_term,
            fields,
            filters,
            is_favorite,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            exclude_person_types,
            person_types,
            appears_in_item_id,
            user_id,
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

    # Gets all persons.
    def test_get_persons_2(self):
        # Parameters for the API call
        limit = None
        search_term = None
        fields = None
        filters = None
        is_favorite = None
        enable_user_data = None
        image_type_limit = None
        enable_image_types = None
        exclude_person_types = None
        person_types = None
        appears_in_item_id = None
        user_id = None
        enable_images = True

        # Perform the API call through the SDK function
        result = self.controller.get_persons(
            limit,
            search_term,
            fields,
            filters,
            is_favorite,
            enable_user_data,
            image_type_limit,
            enable_image_types,
            exclude_person_types,
            person_types,
            appears_in_item_id,
            user_id,
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
