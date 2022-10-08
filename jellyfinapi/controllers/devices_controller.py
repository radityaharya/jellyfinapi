# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.device_info_query_result import DeviceInfoQueryResult
from jellyfinapi.models.device_info import DeviceInfo
from jellyfinapi.models.device_options import DeviceOptions
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class DevicesController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(DevicesController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_devices(self, supports_sync=None, user_id=None):
        """Does a GET request to /Devices.

        Get Devices.

        Args:
            supports_sync (bool, optional): Gets or sets a value indicating
                whether [supports synchronize].
            user_id (uuid|string, optional): Gets or sets the user
                identifier.

        Returns:
            DeviceInfoQueryResult: Response from the API. Devices retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_devices called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_devices.")
            _url_path = "/Devices"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"supportsSync": supports_sync, "userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_devices.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_devices.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_devices")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_devices.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceInfoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_device(self, id):
        """Does a DELETE request to /Devices.

        Deletes a device.

        Args:
            id (string): Device Id.

        Returns:
            void: Response from the API. Device deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_device called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_device.")
            _url_path = "/Devices"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_device.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_device")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_device.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_device_info(self, id):
        """Does a GET request to /Devices/Info.

        Get info for a device.

        Args:
            id (string): Device Id.

        Returns:
            DeviceInfo: Response from the API. Device info retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_device_info called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_device_info.")
            _url_path = "/Devices/Info"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_device_info.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_device_info.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_device_info")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_device_info.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_device_options(self, id):
        """Does a GET request to /Devices/Options.

        Get options for a device.

        Args:
            id (string): Device Id.

        Returns:
            DeviceOptions: Response from the API. Device options retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_device_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_device_options.")
            _url_path = "/Devices/Options"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_device_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_device_options.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_device_options")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_device_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Device not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, DeviceOptions.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_device_options(self, id, body):
        """Does a POST request to /Devices/Options.

        Update device options.

        Args:
            id (string): Device Id.
            body (DeviceOptionsDto): Device Options.

        Returns:
            void: Response from the API. Device options updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_device_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_device_options.")
            _url_path = "/Devices/Options"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_device_options.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_device_options."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_device_options")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_device_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
