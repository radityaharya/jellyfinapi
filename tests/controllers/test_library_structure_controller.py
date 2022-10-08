# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.add_virtual_folder_dto import AddVirtualFolderDto
from jellyfinapi.models.update_library_options_dto import UpdateLibraryOptionsDto


class LibraryStructureControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(LibraryStructureControllerTests, cls).setUpClass()
        cls.controller = cls.client.library_structure
        cls.response_catcher = cls.controller.http_call_back

    # Gets all virtual folders.
    def test_get_virtual_folders(self):

        # Perform the API call through the SDK function
        result = self.controller.get_virtual_folders()

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

    # Gets all virtual folders.
    def test_get_virtual_folders_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_virtual_folders()

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

    # Gets all virtual folders.
    def test_get_virtual_folders_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_virtual_folders()

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

    # Adds a virtual folder.
    def test_add_virtual_folder(self):
        # Parameters for the API call
        name = None
        collection_type = None
        paths = None
        refresh_library = False
        body = None

        # Perform the API call through the SDK function
        self.controller.add_virtual_folder(
            name, collection_type, paths, refresh_library, body
        )

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Removes a virtual folder.
    def test_remove_virtual_folder(self):
        # Parameters for the API call
        name = None
        refresh_library = False

        # Perform the API call through the SDK function
        self.controller.remove_virtual_folder(name, refresh_library)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Update library options.
    def test_update_library_options(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.update_library_options(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Renames a virtual folder.
    def test_rename_virtual_folder(self):
        # Parameters for the API call
        name = None
        new_name = None
        refresh_library = False

        # Perform the API call through the SDK function
        self.controller.rename_virtual_folder(name, new_name, refresh_library)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Remove a media path.
    def test_remove_media_path(self):
        # Parameters for the API call
        name = None
        path = None
        refresh_library = False

        # Perform the API call through the SDK function
        self.controller.remove_media_path(name, path, refresh_library)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
