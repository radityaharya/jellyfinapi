# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.task_info import TaskInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ScheduledTasksController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ScheduledTasksController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_tasks(self, is_hidden=None, is_enabled=None):
        """Does a GET request to /ScheduledTasks.

        Get tasks.

        Args:
            is_hidden (bool, optional): Optional filter tasks that are hidden,
                or not.
            is_enabled (bool, optional): Optional filter tasks that are
                enabled, or not.

        Returns:
            list of TaskInfo: Response from the API. Scheduled tasks
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_tasks called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_tasks.")
            _url_path = "/ScheduledTasks"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"isHidden": is_hidden, "isEnabled": is_enabled}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_tasks.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_tasks.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_tasks")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_tasks.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TaskInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_task(self, task_id):
        """Does a GET request to /ScheduledTasks/{taskId}.

        Get task by id.

        Args:
            task_id (string): Task Id.

        Returns:
            TaskInfo: Response from the API. Task retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_task called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_task.")
            _url_path = "/ScheduledTasks/{taskId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"taskId": {"value": task_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_task.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_task.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_task")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_task.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Task not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, TaskInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_task(self, task_id, body):
        """Does a POST request to /ScheduledTasks/{taskId}/Triggers.

        Update specified task triggers.

        Args:
            task_id (string): Task Id.
            body (list of TaskTriggerInfo): Triggers.

        Returns:
            void: Response from the API. Task triggers updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_task called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_task.")
            _url_path = "/ScheduledTasks/{taskId}/Triggers"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"taskId": {"value": task_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_task.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_task.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_task")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_task.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Task not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def start_task(self, task_id):
        """Does a POST request to /ScheduledTasks/Running/{taskId}.

        Start specified task.

        Args:
            task_id (string): Task Id.

        Returns:
            void: Response from the API. Task started.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("start_task called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for start_task.")
            _url_path = "/ScheduledTasks/Running/{taskId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"taskId": {"value": task_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for start_task.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="start_task")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for start_task.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Task not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def stop_task(self, task_id):
        """Does a DELETE request to /ScheduledTasks/Running/{taskId}.

        Stop specified task.

        Args:
            task_id (string): Task Id.

        Returns:
            void: Response from the API. Task stopped.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("stop_task called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for stop_task.")
            _url_path = "/ScheduledTasks/Running/{taskId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"taskId": {"value": task_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for stop_task.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="stop_task")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for stop_task.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Task not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
