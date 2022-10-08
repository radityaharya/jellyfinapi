# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.create_playlist_dto import CreatePlaylistDto


class PlaylistsControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(PlaylistsControllerTests, cls).setUpClass()
        cls.controller = cls.client.playlists
        cls.response_catcher = cls.controller.http_call_back

    # For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
    # Query parameters are obsolete.
    def test_create_playlist(self):
        # Parameters for the API call
        name = None
        ids = None
        user_id = None
        media_type = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.create_playlist(name, ids, user_id, media_type, body)

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

    # For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
    # Query parameters are obsolete.
    def test_create_playlist_1(self):
        # Parameters for the API call
        name = None
        ids = None
        user_id = None
        media_type = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.create_playlist(name, ids, user_id, media_type, body)

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

    # For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
    # Query parameters are obsolete.
    def test_create_playlist_2(self):
        # Parameters for the API call
        name = None
        ids = None
        user_id = None
        media_type = None
        body = None

        # Perform the API call through the SDK function
        result = self.controller.create_playlist(name, ids, user_id, media_type, body)

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
