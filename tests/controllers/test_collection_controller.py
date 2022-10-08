# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class CollectionControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(CollectionControllerTests, cls).setUpClass()
        cls.controller = cls.client.collection
        cls.response_catcher = cls.controller.http_call_back

    # Creates a new collection.
    def test_create_collection(self):
        # Parameters for the API call
        name = None
        ids = None
        parent_id = None
        is_locked = False

        # Perform the API call through the SDK function
        result = self.controller.create_collection(name, ids, parent_id, is_locked)

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

    # Creates a new collection.
    def test_create_collection_1(self):
        # Parameters for the API call
        name = None
        ids = None
        parent_id = None
        is_locked = False

        # Perform the API call through the SDK function
        result = self.controller.create_collection(name, ids, parent_id, is_locked)

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

    # Creates a new collection.
    def test_create_collection_2(self):
        # Parameters for the API call
        name = None
        ids = None
        parent_id = None
        is_locked = False

        # Perform the API call through the SDK function
        result = self.controller.create_collection(name, ids, parent_id, is_locked)

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
