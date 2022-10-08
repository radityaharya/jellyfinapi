# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class SessionControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(SessionControllerTests, cls).setUpClass()
        cls.controller = cls.client.session
        cls.response_catcher = cls.controller.http_call_back

    # Get all password reset providers.
    def test_get_password_reset_providers(self):

        # Perform the API call through the SDK function
        result = self.controller.get_password_reset_providers()

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

    # Get all password reset providers.
    def test_get_password_reset_providers_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_password_reset_providers()

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

    # Get all password reset providers.
    def test_get_password_reset_providers_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_password_reset_providers()

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

    # Get all auth providers.
    def test_get_auth_providers(self):

        # Perform the API call through the SDK function
        result = self.controller.get_auth_providers()

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

    # Get all auth providers.
    def test_get_auth_providers_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_auth_providers()

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

    # Get all auth providers.
    def test_get_auth_providers_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_auth_providers()

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

    # Gets a list of sessions.
    def test_get_sessions(self):
        # Parameters for the API call
        controllable_by_user_id = None
        device_id = None
        active_within_seconds = None

        # Perform the API call through the SDK function
        result = self.controller.get_sessions(
            controllable_by_user_id, device_id, active_within_seconds
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

    # Gets a list of sessions.
    def test_get_sessions_1(self):
        # Parameters for the API call
        controllable_by_user_id = None
        device_id = None
        active_within_seconds = None

        # Perform the API call through the SDK function
        result = self.controller.get_sessions(
            controllable_by_user_id, device_id, active_within_seconds
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

    # Gets a list of sessions.
    def test_get_sessions_2(self):
        # Parameters for the API call
        controllable_by_user_id = None
        device_id = None
        active_within_seconds = None

        # Perform the API call through the SDK function
        result = self.controller.get_sessions(
            controllable_by_user_id, device_id, active_within_seconds
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

    # Updates capabilities for a device.
    def test_post_capabilities(self):
        # Parameters for the API call
        id = None
        playable_media_types = None
        supported_commands = None
        supports_media_control = False
        supports_sync = False
        supports_persistent_identifier = True

        # Perform the API call through the SDK function
        self.controller.post_capabilities(
            id,
            playable_media_types,
            supported_commands,
            supports_media_control,
            supports_sync,
            supports_persistent_identifier,
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports that a session has ended.
    def test_report_session_ended(self):

        # Perform the API call through the SDK function
        self.controller.report_session_ended()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
