# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.name_id_pair import NameIdPair
from jellyfinapi.models.session_info import SessionInfo
from jellyfinapi.exceptions.api_exception import APIException


class SessionController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SessionController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_password_reset_providers(self):
        """Does a GET request to /Auth/PasswordResetProviders.

        Get all password reset providers.

        Returns:
            list of NameIdPair: Response from the API. Password reset
                providers retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_password_reset_providers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_password_reset_providers.")
            _url_path = "/Auth/PasswordResetProviders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_password_reset_providers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_password_reset_providers."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_password_reset_providers"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_password_reset_providers.")
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

    def get_auth_providers(self):
        """Does a GET request to /Auth/Providers.

        Get all auth providers.

        Returns:
            list of NameIdPair: Response from the API. Auth providers
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_auth_providers called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_auth_providers.")
            _url_path = "/Auth/Providers"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_auth_providers.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_auth_providers.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_auth_providers")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_auth_providers.")
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

    def get_sessions(
        self, controllable_by_user_id=None, device_id=None, active_within_seconds=None
    ):
        """Does a GET request to /Sessions.

        Gets a list of sessions.

        Args:
            controllable_by_user_id (uuid|string, optional): Filter by
                sessions that a given user is allowed to remote control.
            device_id (string, optional): Filter by device Id.
            active_within_seconds (int, optional): Optional. Filter by
                sessions that were active in the last n seconds.

        Returns:
            list of SessionInfo: Response from the API. List of sessions
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_sessions called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_sessions.")
            _url_path = "/Sessions"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "controllableByUserId": controllable_by_user_id,
                "deviceId": device_id,
                "activeWithinSeconds": active_within_seconds,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_sessions.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_sessions.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_sessions")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_sessions.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SessionInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def send_full_general_command(self, session_id, body):
        """Does a POST request to /Sessions/{sessionId}/Command.

        Issues a full general command to a client.

        Args:
            session_id (string): The session id.
            body (GeneralCommand): The
                MediaBrowser.Model.Session.GeneralCommand.

        Returns:
            void: Response from the API. Full general command sent to
                session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("send_full_general_command called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for send_full_general_command.")
            _url_path = "/Sessions/{sessionId}/Command"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"sessionId": {"value": session_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for send_full_general_command.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for send_full_general_command."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="send_full_general_command")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for send_full_general_command.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def send_general_command(self, session_id, command):
        """Does a POST request to /Sessions/{sessionId}/Command/{command}.

        Issues a general command to a client.

        Args:
            session_id (string): The session id.
            command (GeneralCommandTypeEnum): The command to send.

        Returns:
            void: Response from the API. General command sent to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("send_general_command called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for send_general_command.")
            _url_path = "/Sessions/{sessionId}/Command/{command}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "sessionId": {"value": session_id, "encode": True},
                    "command": {"value": command, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for send_general_command."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="send_general_command")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for send_general_command.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def send_message_command(self, session_id, body):
        """Does a POST request to /Sessions/{sessionId}/Message.

        Issues a command to a client to display a message to the user.

        Args:
            session_id (string): The session id.
            body (MessageCommand): The
                MediaBrowser.Model.Session.MessageCommand object containing
                Header, Message Text, and TimeoutMs.

        Returns:
            void: Response from the API. Message sent.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("send_message_command called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for send_message_command.")
            _url_path = "/Sessions/{sessionId}/Message"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"sessionId": {"value": session_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for send_message_command.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for send_message_command."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="send_message_command")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for send_message_command.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def play(
        self,
        session_id,
        play_command,
        item_ids,
        start_position_ticks=None,
        media_source_id=None,
        audio_stream_index=None,
        subtitle_stream_index=None,
        start_index=None,
    ):
        """Does a POST request to /Sessions/{sessionId}/Playing.

        Instructs a session to play an item.

        Args:
            session_id (string): The session id.
            play_command (PlayCommandEnum): The type of play command to issue
                (PlayNow, PlayNext, PlayLast). Clients who have not yet
                implemented play next and play last may play now.
            item_ids (list of uuid|string): The ids of the items to play,
                comma delimited.
            start_position_ticks (long|int, optional): The starting position
                of the first item.
            media_source_id (string, optional): Optional. The media source
                id.
            audio_stream_index (int, optional): Optional. The index of the
                audio stream to play.
            subtitle_stream_index (int, optional): Optional. The index of the
                subtitle stream to play.
            start_index (int, optional): Optional. The start index.

        Returns:
            void: Response from the API. Instruction sent to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("play called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for play.")
            _url_path = "/Sessions/{sessionId}/Playing"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"sessionId": {"value": session_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "playCommand": play_command,
                "itemIds": item_ids,
                "startPositionTicks": start_position_ticks,
                "mediaSourceId": media_source_id,
                "audioStreamIndex": audio_stream_index,
                "subtitleStreamIndex": subtitle_stream_index,
                "startIndex": start_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for play.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="play")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for play.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def send_playstate_command(
        self, session_id, command, seek_position_ticks=None, controlling_user_id=None
    ):
        """Does a POST request to /Sessions/{sessionId}/Playing/{command}.

        Issues a playstate command to a client.

        Args:
            session_id (string): The session id.
            command (PlaystateCommandEnum): The
                MediaBrowser.Model.Session.PlaystateCommand.
            seek_position_ticks (long|int, optional): The optional position
                ticks.
            controlling_user_id (string, optional): The optional controlling
                user id.

        Returns:
            void: Response from the API. Playstate command sent to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("send_playstate_command called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for send_playstate_command.")
            _url_path = "/Sessions/{sessionId}/Playing/{command}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "sessionId": {"value": session_id, "encode": True},
                    "command": {"value": command, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "seekPositionTicks": seek_position_ticks,
                "controllingUserId": controlling_user_id,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for send_playstate_command."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="send_playstate_command")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for send_playstate_command.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def send_system_command(self, session_id, command):
        """Does a POST request to /Sessions/{sessionId}/System/{command}.

        Issues a system command to a client.

        Args:
            session_id (string): The session id.
            command (GeneralCommandTypeEnum): The command to send.

        Returns:
            void: Response from the API. System command sent to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("send_system_command called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for send_system_command.")
            _url_path = "/Sessions/{sessionId}/System/{command}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "sessionId": {"value": session_id, "encode": True},
                    "command": {"value": command, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for send_system_command.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="send_system_command")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for send_system_command.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_user_to_session(self, session_id, user_id):
        """Does a POST request to /Sessions/{sessionId}/User/{userId}.

        Adds an additional user to a session.

        Args:
            session_id (string): The session id.
            user_id (uuid|string): The user id.

        Returns:
            void: Response from the API. User added to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_user_to_session called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_user_to_session.")
            _url_path = "/Sessions/{sessionId}/User/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "sessionId": {"value": session_id, "encode": True},
                    "userId": {"value": user_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_user_to_session.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_user_to_session")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_user_to_session.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_user_from_session(self, session_id, user_id):
        """Does a DELETE request to /Sessions/{sessionId}/User/{userId}.

        Removes an additional user from a session.

        Args:
            session_id (string): The session id.
            user_id (uuid|string): The user id.

        Returns:
            void: Response from the API. User removed from session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("remove_user_from_session called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for remove_user_from_session.")
            _url_path = "/Sessions/{sessionId}/User/{userId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "sessionId": {"value": session_id, "encode": True},
                    "userId": {"value": user_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for remove_user_from_session."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="remove_user_from_session")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for remove_user_from_session.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def display_content(self, session_id, item_type, item_id, item_name):
        """Does a POST request to /Sessions/{sessionId}/Viewing.

        Instructs a session to browse to an item or view.

        Args:
            session_id (string): The session Id.
            item_type (BaseItemKindEnum): The type of item to browse to.
            item_id (string): The Id of the item.
            item_name (string): The name of the item.

        Returns:
            void: Response from the API. Instruction sent to session.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("display_content called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for display_content.")
            _url_path = "/Sessions/{sessionId}/Viewing"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"sessionId": {"value": session_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "itemType": item_type,
                "itemId": item_id,
                "itemName": item_name,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for display_content.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="display_content")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for display_content.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_capabilities(
        self,
        id=None,
        playable_media_types=None,
        supported_commands=None,
        supports_media_control=False,
        supports_sync=False,
        supports_persistent_identifier=True,
    ):
        """Does a POST request to /Sessions/Capabilities.

        Updates capabilities for a device.

        Args:
            id (string, optional): The session id.
            playable_media_types (list of string, optional): A list of
                playable media types, comma delimited. Audio, Video, Book,
                Photo.
            supported_commands (list of GeneralCommandTypeEnum, optional): A
                list of supported remote control commands, comma delimited.
            supports_media_control (bool, optional): Determines whether media
                can be played remotely..
            supports_sync (bool, optional): Determines whether sync is
                supported.
            supports_persistent_identifier (bool, optional): Determines
                whether the device supports a unique identifier.

        Returns:
            void: Response from the API. Capabilities posted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_capabilities called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_capabilities.")
            _url_path = "/Sessions/Capabilities"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "id": id,
                "playableMediaTypes": playable_media_types,
                "supportedCommands": supported_commands,
                "supportsMediaControl": supports_media_control,
                "supportsSync": supports_sync,
                "supportsPersistentIdentifier": supports_persistent_identifier,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_capabilities.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_capabilities")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_capabilities.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_full_capabilities(self, body, id=None):
        """Does a POST request to /Sessions/Capabilities/Full.

        Updates capabilities for a device.

        Args:
            body (ClientCapabilitiesDto): The
                MediaBrowser.Model.Session.ClientCapabilities.
            id (string, optional): The session id.

        Returns:
            void: Response from the API. Capabilities updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_full_capabilities called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_full_capabilities.")
            _url_path = "/Sessions/Capabilities/Full"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"id": id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for post_full_capabilities.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for post_full_capabilities."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_full_capabilities")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_full_capabilities.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def report_session_ended(self):
        """Does a POST request to /Sessions/Logout.

        Reports that a session has ended.

        Returns:
            void: Response from the API. Session end reported to server.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("report_session_ended called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for report_session_ended.")
            _url_path = "/Sessions/Logout"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for report_session_ended."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="report_session_ended")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for report_session_ended.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def report_viewing(self, item_id, session_id=None):
        """Does a POST request to /Sessions/Viewing.

        Reports that a session is viewing an item.

        Args:
            item_id (string): The item id.
            session_id (string, optional): The session id.

        Returns:
            void: Response from the API. Session reported to server.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("report_viewing called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for report_viewing.")
            _url_path = "/Sessions/Viewing"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"itemId": item_id, "sessionId": session_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for report_viewing.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="report_viewing")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for report_viewing.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
