# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.device_profile_info import DeviceProfileInfo
from jellyfinapi.models.device_profile import DeviceProfile
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class DlnaController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(DlnaController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_profile_infos(self):
        """Does a GET request to /Dlna/ProfileInfos.

        Get profile infos.

        Returns:
            list of DeviceProfileInfo: Response from the API. Device profile
                infos returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_profile_infos called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_profile_infos.")
            _url_path = "/Dlna/ProfileInfos"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_profile_infos.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_profile_infos.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_profile_infos")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_profile_infos.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceProfileInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_profile(self, body=None):
        """Does a POST request to /Dlna/Profiles.

        Creates a profile.

        Args:
            body (DeviceProfile, optional): Device profile.

        Returns:
            void: Response from the API. Device profile created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_profile called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_profile.")
            _url_path = "/Dlna/Profiles"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_profile.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_profile.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_profile")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_profile.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_profile(self, profile_id):
        """Does a GET request to /Dlna/Profiles/{profileId}.

        Gets a single profile.

        Args:
            profile_id (string): Profile Id.

        Returns:
            DeviceProfile: Response from the API. Device profile returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_profile called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_profile.")
            _url_path = "/Dlna/Profiles/{profileId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"profileId": {"value": profile_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_profile.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_profile.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_profile")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_profile.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device profile not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceProfile.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_profile(self, profile_id):
        """Does a DELETE request to /Dlna/Profiles/{profileId}.

        Deletes a profile.

        Args:
            profile_id (string): Profile id.

        Returns:
            void: Response from the API. Device profile deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_profile called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_profile.")
            _url_path = "/Dlna/Profiles/{profileId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"profileId": {"value": profile_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_profile.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_profile")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_profile.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device profile not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_profile(self, profile_id, body=None):
        """Does a POST request to /Dlna/Profiles/{profileId}.

        Updates a profile.

        Args:
            profile_id (string): Profile id.
            body (DeviceProfile, optional): Device profile.

        Returns:
            void: Response from the API. Device profile updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_profile called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_profile.")
            _url_path = "/Dlna/Profiles/{profileId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"profileId": {"value": profile_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_profile.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_profile.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_profile")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_profile.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device profile not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_default_profile(self):
        """Does a GET request to /Dlna/Profiles/Default.

        Gets the default profile.

        Returns:
            DeviceProfile: Response from the API. Default device profile
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_default_profile called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_default_profile.")
            _url_path = "/Dlna/Profiles/Default"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_default_profile.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_default_profile.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_default_profile")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_default_profile.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceProfile.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
