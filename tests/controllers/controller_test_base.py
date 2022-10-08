# -*- coding: utf-8 -*-


import unittest
from tests.http_response_catcher import HttpResponseCatcher
from jellyfinapi.configuration import Configuration
from jellyfinapi.configuration import Environment
from jellyfinapi.jellyfinapi_client import JellyfinapiClient


class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ControllerTestBase.create_configuration()
        cls.client = JellyfinapiClient(config=cls.config)
        cls.auth_managers = cls.client.auth_managers

    @staticmethod
    def create_configuration():
        return Configuration(http_call_back=HttpResponseCatcher())
