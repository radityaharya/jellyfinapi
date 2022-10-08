# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.notification_result_dto import NotificationResultDto
from jellyfinapi.models.notifications_summary_dto import NotificationsSummaryDto
from jellyfinapi.models.name_id_pair import NameIdPair
from jellyfinapi.models.notification_type_info import NotificationTypeInfo
from jellyfinapi.exceptions.api_exception import APIException


class NotificationsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(NotificationsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_notifications(self, user_id):
        """Does a GET request to /Notifications/{userId}.

        Gets a user's notifications.

        Args:
            user_id (string): TODO: type description here.

        Returns:
            NotificationResultDto: Response from the API. Notifications
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_notifications called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_notifications.")
            _url_path = "/Notifications/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_notifications.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_notifications.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_notifications")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_notifications.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NotificationResultDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_read(self, user_id):
        """Does a POST request to /Notifications/{userId}/Read.

        Sets notifications as read.

        Args:
            user_id (string): TODO: type description here.

        Returns:
            void: Response from the API. Notifications set as read.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_read called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_read.")
            _url_path = "/Notifications/{userId}/Read"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_read.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_read")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_read.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_notifications_summary(self, user_id):
        """Does a GET request to /Notifications/{userId}/Summary.

        Gets a user's notification summary.

        Args:
            user_id (string): TODO: type description here.

        Returns:
            NotificationsSummaryDto: Response from the API. Summary of user's
                notifications returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_notifications_summary called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_notifications_summary.")
            _url_path = "/Notifications/{userId}/Summary"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_notifications_summary.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_notifications_summary."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_notifications_summary")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_notifications_summary.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NotificationsSummaryDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_unread(self, user_id):
        """Does a POST request to /Notifications/{userId}/Unread.

        Sets notifications as unread.

        Args:
            user_id (string): TODO: type description here.

        Returns:
            void: Response from the API. Notifications set as unread.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_unread called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_unread.")
            _url_path = "/Notifications/{userId}/Unread"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_unread.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_unread")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_unread.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_admin_notification(self, body):
        """Does a POST request to /Notifications/Admin.

        Sends a notification to all admins.

        Args:
            body (AdminNotificationDto): The notification request.

        Returns:
            void: Response from the API. Notification sent.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_admin_notification called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_admin_notification.")
            _url_path = "/Notifications/Admin"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_admin_notification.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for create_admin_notification."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_admin_notification")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_admin_notification.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_notification_services(self):
        """Does a GET request to /Notifications/Services.

        Gets notification services.

        Returns:
            list of NameIdPair: Response from the API. All notification
                services returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_notification_services called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_notification_services.")
            _url_path = "/Notifications/Services"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_notification_services.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_notification_services."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_notification_services")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_notification_services.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NameIdPair.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_notification_types(self):
        """Does a GET request to /Notifications/Types.

        Gets notification types.

        Returns:
            list of NotificationTypeInfo: Response from the API. All
                notification types returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_notification_types called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_notification_types.")
            _url_path = "/Notifications/Types"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_notification_types.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_notification_types."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_notification_types")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_notification_types.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, NotificationTypeInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
