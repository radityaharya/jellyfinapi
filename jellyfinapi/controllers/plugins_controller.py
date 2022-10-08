# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from deprecation import deprecated
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.plugin_info import PluginInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class PluginsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(PluginsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_plugins(self):
        """Does a GET request to /Plugins.

        Gets a list of currently installed plugins.

        Returns:
            list of PluginInfo: Response from the API. Installed plugins
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_plugins called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_plugins.")
            _url_path = "/Plugins"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_plugins.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_plugins.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_plugins")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_plugins.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PluginInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    @deprecated()
    def uninstall_plugin(self, plugin_id):
        """Does a DELETE request to /Plugins/{pluginId}.

        Uninstalls a plugin.

        Args:
            plugin_id (uuid|string): Plugin id.

        Returns:
            void: Response from the API. Plugin uninstalled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("uninstall_plugin called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for uninstall_plugin.")
            _url_path = "/Plugins/{pluginId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"pluginId": {"value": plugin_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for uninstall_plugin.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="uninstall_plugin")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for uninstall_plugin.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Plugin not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def uninstall_plugin_by_version(self, plugin_id, version):
        """Does a DELETE request to /Plugins/{pluginId}/{version}.

        Uninstalls a plugin by version.

        Args:
            plugin_id (uuid|string): Plugin id.
            version (string): Plugin version.

        Returns:
            void: Response from the API. Plugin uninstalled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("uninstall_plugin_by_version called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for uninstall_plugin_by_version.")
            _url_path = "/Plugins/{pluginId}/{version}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "pluginId": {"value": plugin_id, "encode": True},
                    "version": {"value": version, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for uninstall_plugin_by_version."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="uninstall_plugin_by_version"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for uninstall_plugin_by_version.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Plugin not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def disable_plugin(self, plugin_id, version):
        """Does a POST request to /Plugins/{pluginId}/{version}/Disable.

        Disable a plugin.

        Args:
            plugin_id (uuid|string): Plugin id.
            version (string): Plugin version.

        Returns:
            void: Response from the API. Plugin disabled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("disable_plugin called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for disable_plugin.")
            _url_path = "/Plugins/{pluginId}/{version}/Disable"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "pluginId": {"value": plugin_id, "encode": True},
                    "version": {"value": version, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for disable_plugin.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="disable_plugin")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for disable_plugin.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Plugin not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def enable_plugin(self, plugin_id, version):
        """Does a POST request to /Plugins/{pluginId}/{version}/Enable.

        Enables a disabled plugin.

        Args:
            plugin_id (uuid|string): Plugin id.
            version (string): Plugin version.

        Returns:
            void: Response from the API. Plugin enabled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("enable_plugin called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for enable_plugin.")
            _url_path = "/Plugins/{pluginId}/{version}/Enable"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "pluginId": {"value": plugin_id, "encode": True},
                    "version": {"value": version, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for enable_plugin.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="enable_plugin")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for enable_plugin.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Plugin not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_plugin_image(self, plugin_id, version):
        """Does a GET request to /Plugins/{pluginId}/{version}/Image.

        Gets a plugin's image.

        Args:
            plugin_id (uuid|string): Plugin id.
            version (string): Plugin version.

        Returns:
            mixed: Response from the API. Plugin image returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_plugin_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_plugin_image.")
            _url_path = "/Plugins/{pluginId}/{version}/Image"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "pluginId": {"value": plugin_id, "encode": True},
                    "version": {"value": version, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_plugin_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_plugin_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_plugin_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_plugin_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_plugin_configuration(self, plugin_id):
        """Does a GET request to /Plugins/{pluginId}/Configuration.

        Gets plugin configuration.

        Args:
            plugin_id (uuid|string): Plugin id.

        Returns:
            object: Response from the API. Plugin configuration returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_plugin_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_plugin_configuration.")
            _url_path = "/Plugins/{pluginId}/Configuration"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"pluginId": {"value": plugin_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_plugin_configuration.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_plugin_configuration."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_plugin_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_plugin_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException(
                    "Plugin not found or plugin configuration not found.", _response
                )
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_plugin_configuration(self, plugin_id):
        """Does a POST request to /Plugins/{pluginId}/Configuration.

        Accepts plugin configuration as JSON body.

        Args:
            plugin_id (uuid|string): Plugin id.

        Returns:
            void: Response from the API. Plugin configuration updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_plugin_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_plugin_configuration.")
            _url_path = "/Plugins/{pluginId}/Configuration"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"pluginId": {"value": plugin_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_plugin_configuration."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="update_plugin_configuration"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_plugin_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException(
                    "Plugin not found or plugin does not have configuration.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_plugin_manifest(self, plugin_id):
        """Does a POST request to /Plugins/{pluginId}/Manifest.

        Gets a plugin's manifest.

        Args:
            plugin_id (uuid|string): Plugin id.

        Returns:
            void: Response from the API. Plugin manifest returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_plugin_manifest called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_plugin_manifest.")
            _url_path = "/Plugins/{pluginId}/Manifest"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"pluginId": {"value": plugin_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_plugin_manifest.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_plugin_manifest")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_plugin_manifest.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Plugin not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
