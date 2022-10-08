# -*- coding: utf-8 -*-


import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from jellyfinapi.api_helper import APIHelper


class SystemControllerTests(ControllerTestBase):
    @classmethod
    def setUpClass(cls):
        super(SystemControllerTests, cls).setUpClass()
        cls.controller = cls.client.system
        cls.response_catcher = cls.controller.http_call_back

    # Gets information about the request endpoint.
    def test_get_endpoint_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_endpoint_info()

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

    # Gets information about the request endpoint.
    def test_get_endpoint_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_endpoint_info()

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

    # Gets information about the request endpoint.
    def test_get_endpoint_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_endpoint_info()

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

    # Gets information about the server.
    def test_get_system_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_system_info()

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

    # Gets information about the server.
    def test_get_system_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_system_info()

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

    # Gets information about the server.
    def test_get_system_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_system_info()

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

    # Gets public information about the server.
    def test_get_public_system_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_system_info()

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

    # Gets public information about the server.
    def test_get_public_system_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_system_info()

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

    # Gets public information about the server.
    def test_get_public_system_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_public_system_info()

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

    # Gets a list of available server log files.
    def test_get_server_logs(self):

        # Perform the API call through the SDK function
        result = self.controller.get_server_logs()

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

    # Gets a list of available server log files.
    def test_get_server_logs_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_server_logs()

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

    # Gets a list of available server log files.
    def test_get_server_logs_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_server_logs()

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

    # Pings the system.
    def test_get_ping_system(self):

        # Perform the API call through the SDK function
        result = self.controller.get_ping_system()

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

    # Pings the system.
    def test_get_ping_system_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_ping_system()

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

    # Pings the system.
    def test_get_ping_system_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_ping_system()

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

    # Pings the system.
    def test_post_ping_system(self):

        # Perform the API call through the SDK function
        result = self.controller.post_ping_system()

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

    # Pings the system.
    def test_post_ping_system_1(self):

        # Perform the API call through the SDK function
        result = self.controller.post_ping_system()

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

    # Pings the system.
    def test_post_ping_system_2(self):

        # Perform the API call through the SDK function
        result = self.controller.post_ping_system()

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

    # Restarts the application.
    def test_restart_application(self):

        # Perform the API call through the SDK function
        self.controller.restart_application()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Shuts down the application.
    def test_shutdown_application(self):

        # Perform the API call through the SDK function
        self.controller.shutdown_application()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets wake on lan information.
    def test_get_wake_on_lan_info(self):

        # Perform the API call through the SDK function
        result = self.controller.get_wake_on_lan_info()

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

    # Gets wake on lan information.
    def test_get_wake_on_lan_info_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_wake_on_lan_info()

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

    # Gets wake on lan information.
    def test_get_wake_on_lan_info_2(self):

        # Perform the API call through the SDK function
        result = self.controller.get_wake_on_lan_info()

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
