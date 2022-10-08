# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class SyncPlayControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(SyncPlayControllerTests, cls).setUpClass()
        cls.controller = cls.client.sync_play
        cls.response_catcher = cls.controller.http_call_back

    # Leave the joined SyncPlay group.
    def test_sync_play_leave_group(self):

        # Perform the API call through the SDK function
        self.controller.sync_play_leave_group()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets all SyncPlay groups.
    def test_sync_play_get_groups(self):

        # Perform the API call through the SDK function
        result = self.controller.sync_play_get_groups()

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

    # Gets all SyncPlay groups.
    def test_sync_play_get_groups_1(self):

        # Perform the API call through the SDK function
        result = self.controller.sync_play_get_groups()

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

    # Gets all SyncPlay groups.
    def test_sync_play_get_groups_2(self):

        # Perform the API call through the SDK function
        result = self.controller.sync_play_get_groups()

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

    # Request pause in SyncPlay group.
    def test_sync_play_pause(self):

        # Perform the API call through the SDK function
        self.controller.sync_play_pause()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Request stop in SyncPlay group.
    def test_sync_play_stop(self):

        # Perform the API call through the SDK function
        self.controller.sync_play_stop()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Request unpause in SyncPlay group.
    def test_sync_play_unpause(self):

        # Perform the API call through the SDK function
        self.controller.sync_play_unpause()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
