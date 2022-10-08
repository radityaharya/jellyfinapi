# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class LibraryControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(LibraryControllerTests, cls).setUpClass()
        cls.controller = cls.client.library
        cls.response_catcher = cls.controller.http_call_back

    # Deletes items from the library and filesystem.
    def test_delete_items(self):
        # Parameters for the API call
        ids = None

        # Perform the API call through the SDK function
        self.controller.delete_items(ids)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Get item counts.
    def test_get_item_counts(self):
        # Parameters for the API call
        user_id = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_item_counts(user_id, is_favorite)

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

    # Get item counts.
    def test_get_item_counts_1(self):
        # Parameters for the API call
        user_id = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_item_counts(user_id, is_favorite)

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

    # Get item counts.
    def test_get_item_counts_2(self):
        # Parameters for the API call
        user_id = None
        is_favorite = None

        # Perform the API call through the SDK function
        result = self.controller.get_item_counts(user_id, is_favorite)

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

    # Gets the library options info.
    def test_get_library_options_info(self):
        # Parameters for the API call
        library_content_type = None
        is_new_library = False

        # Perform the API call through the SDK function
        result = self.controller.get_library_options_info(
            library_content_type, is_new_library
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

    # Gets the library options info.
    def test_get_library_options_info_1(self):
        # Parameters for the API call
        library_content_type = None
        is_new_library = False

        # Perform the API call through the SDK function
        result = self.controller.get_library_options_info(
            library_content_type, is_new_library
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

    # Gets the library options info.
    def test_get_library_options_info_2(self):
        # Parameters for the API call
        library_content_type = None
        is_new_library = False

        # Perform the API call through the SDK function
        result = self.controller.get_library_options_info(
            library_content_type, is_new_library
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

    # Gets all user media folders.
    def test_get_media_folders(self):
        # Parameters for the API call
        is_hidden = None

        # Perform the API call through the SDK function
        result = self.controller.get_media_folders(is_hidden)

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

    # Gets all user media folders.
    def test_get_media_folders_1(self):
        # Parameters for the API call
        is_hidden = None

        # Perform the API call through the SDK function
        result = self.controller.get_media_folders(is_hidden)

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

    # Gets all user media folders.
    def test_get_media_folders_2(self):
        # Parameters for the API call
        is_hidden = None

        # Perform the API call through the SDK function
        result = self.controller.get_media_folders(is_hidden)

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

    # Reports that new movies have been added by an external source.
    def test_post_added_movies(self):
        # Parameters for the API call
        tmdb_id = None
        imdb_id = None

        # Perform the API call through the SDK function
        self.controller.post_added_movies(tmdb_id, imdb_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports that new movies have been added by an external source.
    def test_post_updated_movies(self):
        # Parameters for the API call
        tmdb_id = None
        imdb_id = None

        # Perform the API call through the SDK function
        self.controller.post_updated_movies(tmdb_id, imdb_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets a list of physical paths from virtual folders.
    def test_get_physical_paths(self):

        # Perform the API call through the SDK function
        result = self.controller.get_physical_paths()

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

    # Gets a list of physical paths from virtual folders.
    def test_get_physical_paths_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_physical_paths()

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

    # Gets a list of physical paths from virtual folders.
    def test_get_physical_paths_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_physical_paths()

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

    # Starts a library scan.
    def test_refresh_library(self):

        # Perform the API call through the SDK function
        self.controller.refresh_library()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports that new episodes of a series have been added by an external source.
    def test_post_added_series(self):
        # Parameters for the API call
        tvdb_id = None

        # Perform the API call through the SDK function
        self.controller.post_added_series(tvdb_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Reports that new episodes of a series have been added by an external source.
    def test_post_updated_series(self):
        # Parameters for the API call
        tvdb_id = None

        # Perform the API call through the SDK function
        self.controller.post_updated_series(tvdb_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
