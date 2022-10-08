# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class DlnaServerController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(DlnaServerController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_connection_manager(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ConnectionManager.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_connection_manager called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_connection_manager.")
            _url_path = "/Dlna/{serverId}/ConnectionManager"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_connection_manager.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_connection_manager."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_connection_manager"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_connection_manager.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_connection_manager_2(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ConnectionManager/ConnectionManager.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_connection_manager_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_connection_manager_2.")
            _url_path = "/Dlna/{serverId}/ConnectionManager/ConnectionManager"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_connection_manager_2.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_connection_manager_2."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_connection_manager_2"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_connection_manager_2.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_connection_manager_3(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ConnectionManager/ConnectionManager.xml.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_connection_manager_3 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_connection_manager_3.")
            _url_path = "/Dlna/{serverId}/ConnectionManager/ConnectionManager.xml"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_connection_manager_3.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_connection_manager_3."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_connection_manager_3"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_connection_manager_3.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def process_connection_manager_control_request(self, server_id):
        """Does a POST request to /Dlna/{serverId}/ConnectionManager/Control.

        Process a connection manager control request.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Request processed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("process_connection_manager_control_request called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for process_connection_manager_control_request."
            )
            _url_path = "/Dlna/{serverId}/ConnectionManager/Control"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for process_connection_manager_control_request."
            )
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for process_connection_manager_control_request."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="process_connection_manager_control_request"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for process_connection_manager_control_request."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_content_directory(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ContentDirectory.

        Gets Dlna content directory xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna content directory returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_content_directory called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_content_directory.")
            _url_path = "/Dlna/{serverId}/ContentDirectory"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_content_directory.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_content_directory."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_content_directory"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_content_directory.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_content_directory_2(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ContentDirectory/ContentDirectory.

        Gets Dlna content directory xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna content directory returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_content_directory_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_content_directory_2.")
            _url_path = "/Dlna/{serverId}/ContentDirectory/ContentDirectory"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_content_directory_2.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_content_directory_2."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_content_directory_2"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_content_directory_2.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_content_directory_3(self, server_id):
        """Does a GET request to /Dlna/{serverId}/ContentDirectory/ContentDirectory.xml.

        Gets Dlna content directory xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna content directory returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_content_directory_3 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_content_directory_3.")
            _url_path = "/Dlna/{serverId}/ContentDirectory/ContentDirectory.xml"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_content_directory_3.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_content_directory_3."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_content_directory_3"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_content_directory_3.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def process_content_directory_control_request(self, server_id):
        """Does a POST request to /Dlna/{serverId}/ContentDirectory/Control.

        Process a content directory control request.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Request processed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("process_content_directory_control_request called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for process_content_directory_control_request."
            )
            _url_path = "/Dlna/{serverId}/ContentDirectory/Control"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for process_content_directory_control_request."
            )
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for process_content_directory_control_request."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="process_content_directory_control_request"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for process_content_directory_control_request."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_description_xml(self, server_id):
        """Does a GET request to /Dlna/{serverId}/description.

        Get Description Xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Description xml returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_description_xml called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_description_xml.")
            _url_path = "/Dlna/{serverId}/description"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_description_xml.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_description_xml.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_description_xml"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_description_xml.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_description_xml_2(self, server_id):
        """Does a GET request to /Dlna/{serverId}/description.xml.

        Get Description Xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Description xml returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_description_xml_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_description_xml_2.")
            _url_path = "/Dlna/{serverId}/description.xml"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_description_xml_2.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_description_xml_2."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_description_xml_2"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_description_xml_2.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_icon_id(self, server_id, file_name):
        """Does a GET request to /Dlna/{serverId}/icons/{fileName}.

        Gets a server icon.

        Args:
            server_id (string): Server UUID.
            file_name (string): The icon filename.

        Returns:
            mixed: Response from the API. Request processed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_icon_id called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_icon_id.")
            _url_path = "/Dlna/{serverId}/icons/{fileName}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "serverId": {"value": server_id, "encode": True},
                    "fileName": {"value": file_name, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_icon_id.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_icon_id.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_icon_id")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_icon_id.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found.", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_receiver_registrar(self, server_id):
        """Does a GET request to /Dlna/{serverId}/MediaReceiverRegistrar.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_receiver_registrar called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_receiver_registrar.")
            _url_path = "/Dlna/{serverId}/MediaReceiverRegistrar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_receiver_registrar.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_media_receiver_registrar."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_media_receiver_registrar"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_receiver_registrar.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def process_media_receiver_registrar_control_request(self, server_id):
        """Does a POST request to /Dlna/{serverId}/MediaReceiverRegistrar/Control.

        Process a media receiver registrar control request.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Request processed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("process_media_receiver_registrar_control_request called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for process_media_receiver_registrar_control_request."
            )
            _url_path = "/Dlna/{serverId}/MediaReceiverRegistrar/Control"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for process_media_receiver_registrar_control_request."
            )
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for process_media_receiver_registrar_control_request."
            )
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request,
                binary=True,
                name="process_media_receiver_registrar_control_request",
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for process_media_receiver_registrar_control_request."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_receiver_registrar_2(self, server_id):
        """Does a GET request to /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_receiver_registrar_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_receiver_registrar_2.")
            _url_path = "/Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_receiver_registrar_2.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_media_receiver_registrar_2."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_media_receiver_registrar_2"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_receiver_registrar_2.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_media_receiver_registrar_3(self, server_id):
        """Does a GET request to /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml.

        Gets Dlna media receiver registrar xml.

        Args:
            server_id (string): Server UUID.

        Returns:
            binary: Response from the API. Dlna media receiver registrar xml
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_media_receiver_registrar_3 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_media_receiver_registrar_3.")
            _url_path = (
                "/Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml"
            )
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"serverId": {"value": server_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_media_receiver_registrar_3.")
            _headers = {"accept": "application/xml"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_media_receiver_registrar_3."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_media_receiver_registrar_3"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_media_receiver_registrar_3.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)

            decoded = XmlUtilities.deserialize_xml(_response.text, "response", str)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_icon(self, file_name):
        """Does a GET request to /Dlna/icons/{fileName}.

        Gets a server icon.

        Args:
            file_name (string): The icon filename.

        Returns:
            mixed: Response from the API. Request processed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_icon called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_icon.")
            _url_path = "/Dlna/icons/{fileName}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"fileName": {"value": file_name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_icon.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_icon.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_icon")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_icon.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Not Found.", _response)
            elif _response.status_code == 503:
                raise APIException("DLNA is disabled.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
