# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.startup_user_dto import StartupUserDto


class StartupControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(StartupControllerTests, cls).setUpClass()
        cls.controller = cls.client.startup
        cls.response_catcher = cls.controller.http_call_back

    # Completes the startup wizard.
    def test_complete_wizard(self):

        # Perform the API call through the SDK function
        self.controller.complete_wizard()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the initial startup wizard configuration.
    def test_get_startup_configuration(self):

        # Perform the API call through the SDK function
        result = self.controller.get_startup_configuration()

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

    # Gets the initial startup wizard configuration.
    def test_get_startup_configuration_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_startup_configuration()

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

    # Gets the initial startup wizard configuration.
    def test_get_startup_configuration_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_startup_configuration()

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

    # Gets the first user.
    def test_get_first_user_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user_2()

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

    # Gets the first user.
    def test_get_first_user_21(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user_2()

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

    # Gets the first user.
    def test_get_first_user_22(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user_2()

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

    # Gets the first user.
    def test_get_first_user(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user()

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

    # Gets the first user.
    def test_get_first_user_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user()

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

    # Gets the first user.
    def test_get_first_user_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_first_user()

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

    # Sets the user name and password.
    def test_update_startup_user(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.update_startup_user(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
