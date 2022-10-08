# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class UserControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(UserControllerTests, cls).setUpClass()
        cls.controller = cls.client.user
        cls.response_catcher = cls.controller.http_call_back

    # Gets a list of users.
    def test_get_users(self):
        # Parameters for the API call
        is_hidden = None
        is_disabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_users(is_hidden, is_disabled)

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

    # Gets a list of users.
    def test_get_users_1(self):
        # Parameters for the API call
        is_hidden = None
        is_disabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_users(is_hidden, is_disabled)

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

    # Gets a list of users.
    def test_get_users_2(self):
        # Parameters for the API call
        is_hidden = None
        is_disabled = None

        # Perform the API call through the SDK function
        result = self.controller.get_users(is_hidden, is_disabled)

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

    # Gets the user based on auth token.
    def test_get_current_user(self):

        # Perform the API call through the SDK function
        result = self.controller.get_current_user()

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

    # Gets the user based on auth token.
    def test_get_current_user_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_current_user()

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

    # Gets the user based on auth token.
    def test_get_current_user_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_current_user()

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

    # Gets a list of publicly visible users for display on a login screen.
    def test_get_public_users(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_users()

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

    # Gets a list of publicly visible users for display on a login screen.
    def test_get_public_users_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_users()

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

    # Gets a list of publicly visible users for display on a login screen.
    def test_get_public_users_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_users()

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
