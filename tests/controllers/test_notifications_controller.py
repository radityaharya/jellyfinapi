# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class NotificationsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(NotificationsControllerTests, cls).setUpClass()
        cls.controller = cls.client.notifications
        cls.response_catcher = cls.controller.http_call_back

    # Gets notification services.
    def test_get_notification_services(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_services()

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

    # Gets notification services.
    def test_get_notification_services_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_services()

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

    # Gets notification services.
    def test_get_notification_services_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_services()

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

    # Gets notification types.
    def test_get_notification_types(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_types()

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

    # Gets notification types.
    def test_get_notification_types_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_types()

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

    # Gets notification types.
    def test_get_notification_types_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_notification_types()

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
