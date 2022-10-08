# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class TmdbControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(TmdbControllerTests, cls).setUpClass()
        cls.controller = cls.client.tmdb
        cls.response_catcher = cls.controller.http_call_back

    # Gets the TMDb image configuration options.
    def test_tmdb_client_configuration(self):

        # Perform the API call through the SDK function
        result = self.controller.tmdb_client_configuration()

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
