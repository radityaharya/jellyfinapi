# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.user_dto import UserDto
from jellyfinapi.models.authentication_result import AuthenticationResult
from jellyfinapi.models.forgot_password_result import ForgotPasswordResult
from jellyfinapi.models.pin_redeem_result import PinRedeemResult
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class UserController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(UserController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_users(self, is_hidden=None, is_disabled=None):
        """Does a GET request to /Users.

        Gets a list of users.

        Args:
            is_hidden (bool, optional): Optional filter by IsHidden=true or
                false.
            is_disabled (bool, optional): Optional filter by IsDisabled=true
                or false.

        Returns:
            list of UserDto: Response from the API. Users returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_users called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_users.")
            _url_path = "/Users"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"isHidden": is_hidden, "isDisabled": is_disabled}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_users.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_users.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_users")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_users.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_user_by_id(self, user_id):
        """Does a GET request to /Users/{userId}.

        Gets a user by Id.

        Args:
            user_id (uuid|string): The user id.

        Returns:
            UserDto: Response from the API. User returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_user_by_id called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_user_by_id.")
            _url_path = "/Users/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_user_by_id.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_user_by_id.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_user_by_id")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_user_by_id.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_user(self, user_id):
        """Does a DELETE request to /Users/{userId}.

        Deletes a user.

        Args:
            user_id (uuid|string): The user id.

        Returns:
            void: Response from the API. User deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_user.")
            _url_path = "/Users/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_user.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_user.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user(self, user_id, body):
        """Does a POST request to /Users/{userId}.

        Updates a user.

        Args:
            user_id (uuid|string): The user id.
            body (UserDto): The updated user model.

        Returns:
            void: Response from the API. User updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user.")
            _url_path = "/Users/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_user.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user.")
            if _response.status_code == 400:
                raise ProblemDetailsException(
                    "User information was not supplied.", _response
                )
            elif _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException("User update forbidden.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def authenticate_user(self, user_id, pw, password=None):
        """Does a POST request to /Users/{userId}/Authenticate.

        Authenticates a user.

        Args:
            user_id (uuid|string): The user id.
            pw (string): The password as plain text.
            password (string, optional): The password sha1-hash.

        Returns:
            AuthenticationResult: Response from the API. User authenticated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("authenticate_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for authenticate_user.")
            _url_path = "/Users/{userId}/Authenticate"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"pw": pw, "password": password}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for authenticate_user.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for authenticate_user.")
            _request = self.config.http_client.post(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="authenticate_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for authenticate_user.")
            if _response.status_code == 403:
                raise ProblemDetailsException(
                    "Sha1-hashed password only is not allowed.", _response
                )
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, AuthenticationResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user_configuration(self, user_id, body):
        """Does a POST request to /Users/{userId}/Configuration.

        Updates a user configuration.

        Args:
            user_id (uuid|string): The user id.
            body (UserConfiguration): The new user configuration.

        Returns:
            void: Response from the API. User configuration updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user_configuration called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user_configuration.")
            _url_path = "/Users/{userId}/Configuration"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user_configuration.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_user_configuration."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user_configuration")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user_configuration.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User configuration update forbidden.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user_easy_password(self, user_id, body):
        """Does a POST request to /Users/{userId}/EasyPassword.

        Updates a user's easy password.

        Args:
            user_id (uuid|string): The user id.
            body (UpdateUserEasyPassword): The
                M:Jellyfin.Api.Controllers.UserController.UpdateUserEasyPasswor
                d(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserEasyPasswo
                rd) request.

        Returns:
            void: Response from the API. Password successfully reset.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user_easy_password called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user_easy_password.")
            _url_path = "/Users/{userId}/EasyPassword"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user_easy_password.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_user_easy_password."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user_easy_password")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user_easy_password.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User is not allowed to update the password.", _response
                )
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user_password(self, user_id, body):
        """Does a POST request to /Users/{userId}/Password.

        Updates a user's password.

        Args:
            user_id (uuid|string): The user id.
            body (UpdateUserPassword): The
                M:Jellyfin.Api.Controllers.UserController.UpdateUserPassword(Sy
                stem.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserPassword)
                request.

        Returns:
            void: Response from the API. Password successfully reset.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user_password called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user_password.")
            _url_path = "/Users/{userId}/Password"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user_password.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_user_password."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user_password")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user_password.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User is not allowed to update the password.", _response
                )
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_user_policy(self, user_id, body):
        """Does a POST request to /Users/{userId}/Policy.

        Updates a user policy.

        Args:
            user_id (uuid|string): The user id.
            body (UserPolicy): The new user policy.

        Returns:
            void: Response from the API. User policy updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_user_policy called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_user_policy.")
            _url_path = "/Users/{userId}/Policy"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_user_policy.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_user_policy.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_user_policy")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_user_policy.")
            if _response.status_code == 400:
                raise ProblemDetailsException(
                    "User policy was not supplied.", _response
                )
            elif _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User policy update forbidden.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def authenticate_user_by_name(self, body):
        """Does a POST request to /Users/AuthenticateByName.

        Authenticates a user by name.

        Args:
            body (AuthenticateUserByName): The
                M:Jellyfin.Api.Controllers.UserController.AuthenticateUserByNam
                e(Jellyfin.Api.Models.UserDtos.AuthenticateUserByName)
                request.

        Returns:
            AuthenticationResult: Response from the API. User authenticated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("authenticate_user_by_name called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for authenticate_user_by_name.")
            _url_path = "/Users/AuthenticateByName"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for authenticate_user_by_name.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for authenticate_user_by_name."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="authenticate_user_by_name")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, AuthenticationResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def authenticate_with_quick_connect(self, body):
        """Does a POST request to /Users/AuthenticateWithQuickConnect.

        Authenticates a user with quick connect.

        Args:
            body (QuickConnectDto): The
                Jellyfin.Api.Models.UserDtos.QuickConnectDto request.

        Returns:
            AuthenticationResult: Response from the API. User authenticated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("authenticate_with_quick_connect called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for authenticate_with_quick_connect.")
            _url_path = "/Users/AuthenticateWithQuickConnect"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for authenticate_with_quick_connect.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for authenticate_with_quick_connect."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="authenticate_with_quick_connect"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for authenticate_with_quick_connect.")
            if _response.status_code == 400:
                raise APIException("Missing token.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, AuthenticationResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def forgot_password(self, body):
        """Does a POST request to /Users/ForgotPassword.

        Initiates the forgot password process for a local user.

        Args:
            body (ForgotPasswordDto): The forgot password request containing
                the entered username.

        Returns:
            ForgotPasswordResult: Response from the API. Password reset
                process started.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("forgot_password called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for forgot_password.")
            _url_path = "/Users/ForgotPassword"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for forgot_password.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for forgot_password.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="forgot_password")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ForgotPasswordResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def forgot_password_pin(self, body):
        """Does a POST request to /Users/ForgotPassword/Pin.

        Redeems a forgot password pin.

        Args:
            body (ForgotPasswordPinDto): The forgot password pin request
                containing the entered pin.

        Returns:
            PinRedeemResult: Response from the API. Pin reset process
                started.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("forgot_password_pin called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for forgot_password_pin.")
            _url_path = "/Users/ForgotPassword/Pin"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for forgot_password_pin.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for forgot_password_pin.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="forgot_password_pin")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, PinRedeemResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_current_user(self):
        """Does a GET request to /Users/Me.

        Gets the user based on auth token.

        Returns:
            UserDto: Response from the API. User returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_current_user called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_current_user.")
            _url_path = "/Users/Me"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_current_user.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_current_user.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_current_user")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_current_user.")
            if _response.status_code == 400:
                raise ProblemDetailsException(
                    "Token is not owned by a user.", _response
                )
            elif _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_user_by_name(self, body):
        """Does a POST request to /Users/New.

        Creates a user.

        Args:
            body (CreateUserByName): The create user by name request body.

        Returns:
            UserDto: Response from the API. User created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("create_user_by_name called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for create_user_by_name.")
            _url_path = "/Users/New"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for create_user_by_name.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info("Preparing and executing request for create_user_by_name.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="create_user_by_name")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for create_user_by_name.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_public_users(self):
        """Does a GET request to /Users/Public.

        Gets a list of publicly visible users for display on a login screen.

        Returns:
            list of UserDto: Response from the API. Public users returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_public_users called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_public_users.")
            _url_path = "/Users/Public"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_public_users.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_public_users.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_public_users")
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, UserDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
