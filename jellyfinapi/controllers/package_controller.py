# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.package_info import PackageInfo
from jellyfinapi.models.repository_info import RepositoryInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class PackageController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(PackageController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_packages(self):
        """Does a GET request to /Packages.

        Gets available packages.

        Returns:
            list of PackageInfo: Response from the API. Available packages
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_packages called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_packages.")
            _url_path = "/Packages"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_packages.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_packages.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_packages")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_packages.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PackageInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_package_info(self, name, assembly_guid=None):
        """Does a GET request to /Packages/{name}.

        Gets a package by name or assembly GUID.

        Args:
            name (string): The name of the package.
            assembly_guid (uuid|string, optional): The GUID of the associated
                assembly.

        Returns:
            PackageInfo: Response from the API. Package retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_package_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_package_info.")
            _url_path = "/Packages/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"assemblyGuid": assembly_guid}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_package_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_package_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_package_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_package_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PackageInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def install_package(
        self, name, assembly_guid=None, version=None, repository_url=None
    ):
        """Does a POST request to /Packages/Installed/{name}.

        Installs a package.

        Args:
            name (string): Package name.
            assembly_guid (uuid|string, optional): GUID of the associated
                assembly.
            version (string, optional): Optional version. Defaults to latest
                version.
            repository_url (string, optional): Optional. Specify the
                repository to install from.

        Returns:
            void: Response from the API. Package found.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("install_package called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for install_package.")
            _url_path = "/Packages/Installed/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "assemblyGuid": assembly_guid,
                "version": version,
                "repositoryUrl": repository_url,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for install_package.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="install_package")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for install_package.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Package not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def cancel_package_installation(self, package_id):
        """Does a DELETE request to /Packages/Installing/{packageId}.

        Cancels a package installation.

        Args:
            package_id (uuid|string): Installation Id.

        Returns:
            void: Response from the API. Installation cancelled.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("cancel_package_installation called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for cancel_package_installation.")
            _url_path = "/Packages/Installing/{packageId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"packageId": {"value": package_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for cancel_package_installation."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="cancel_package_installation"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for cancel_package_installation.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_repositories(self):
        """Does a GET request to /Repositories.

        Gets all package repositories.

        Returns:
            list of RepositoryInfo: Response from the API. Package
                repositories returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_repositories called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_repositories.")
            _url_path = "/Repositories"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_repositories.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_repositories.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_repositories")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_repositories.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RepositoryInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_repositories(self, body):
        """Does a POST request to /Repositories.

        Sets the enabled and existing package repositories.

        Args:
            body (list of RepositoryInfo): The list of package repositories.

        Returns:
            void: Response from the API. Package repositories saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_repositories called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_repositories.")
            _url_path = "/Repositories"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for set_repositories.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_repositories.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_repositories")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_repositories.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
