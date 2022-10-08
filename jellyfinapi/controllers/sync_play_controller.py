# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.group_info_dto import GroupInfoDto
from jellyfinapi.exceptions.api_exception import APIException


class SyncPlayController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SyncPlayController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def sync_play_buffering(self, body):
        """Does a POST request to /SyncPlay/Buffering.

        Notify SyncPlay group that member is buffering.

        Args:
            body (BufferRequestDto): The player status.

        Returns:
            void: Response from the API. Group state update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_buffering called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_buffering.")
            _url_path = "/SyncPlay/Buffering"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_buffering.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_buffering.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_buffering")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_buffering.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_join_group(self, body):
        """Does a POST request to /SyncPlay/Join.

        Join an existing SyncPlay group.

        Args:
            body (JoinGroupRequestDto): The group to join.

        Returns:
            void: Response from the API. Group join successful.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_join_group called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_join_group.")
            _url_path = "/SyncPlay/Join"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_join_group.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_join_group."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_join_group")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_join_group.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_leave_group(self):
        """Does a POST request to /SyncPlay/Leave.

        Leave the joined SyncPlay group.

        Returns:
            void: Response from the API. Group leave successful.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_leave_group called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_leave_group.")
            _url_path = "/SyncPlay/Leave"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_leave_group."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_leave_group")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_leave_group.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_get_groups(self):
        """Does a GET request to /SyncPlay/List.

        Gets all SyncPlay groups.

        Returns:
            list of GroupInfoDto: Response from the API. Groups returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_get_groups called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_get_groups.")
            _url_path = "/SyncPlay/List"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_get_groups.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_get_groups."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_get_groups")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_get_groups.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, GroupInfoDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_move_playlist_item(self, body):
        """Does a POST request to /SyncPlay/MovePlaylistItem.

        Request to move an item in the playlist in SyncPlay group.

        Args:
            body (MovePlaylistItemRequestDto): The new position for the item.

        Returns:
            void: Response from the API. Queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_move_playlist_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_move_playlist_item.")
            _url_path = "/SyncPlay/MovePlaylistItem"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_move_playlist_item.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_move_playlist_item."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="sync_play_move_playlist_item"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_move_playlist_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_create_group(self, body):
        """Does a POST request to /SyncPlay/New.

        Create a new SyncPlay group.

        Args:
            body (NewGroupRequestDto): The settings of the new group.

        Returns:
            void: Response from the API. New group created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_create_group called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_create_group.")
            _url_path = "/SyncPlay/New"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_create_group.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_create_group."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_create_group")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_create_group.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_next_item(self, body):
        """Does a POST request to /SyncPlay/NextItem.

        Request next item in SyncPlay group.

        Args:
            body (NextItemRequestDto): The current item information.

        Returns:
            void: Response from the API. Next item update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_next_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_next_item.")
            _url_path = "/SyncPlay/NextItem"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_next_item.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_next_item.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_next_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_next_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_pause(self):
        """Does a POST request to /SyncPlay/Pause.

        Request pause in SyncPlay group.

        Returns:
            void: Response from the API. Pause update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_pause called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_pause.")
            _url_path = "/SyncPlay/Pause"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_pause.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_pause")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_pause.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_ping(self, body):
        """Does a POST request to /SyncPlay/Ping.

        Update session ping.

        Args:
            body (PingRequestDto): The new ping.

        Returns:
            void: Response from the API. Ping updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_ping called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_ping.")
            _url_path = "/SyncPlay/Ping"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_ping.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_ping.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_ping")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_ping.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_previous_item(self, body):
        """Does a POST request to /SyncPlay/PreviousItem.

        Request previous item in SyncPlay group.

        Args:
            body (PreviousItemRequestDto): The current item information.

        Returns:
            void: Response from the API. Previous item update sent to all
                group members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_previous_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_previous_item.")
            _url_path = "/SyncPlay/PreviousItem"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_previous_item.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_previous_item."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_previous_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_previous_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_queue(self, body):
        """Does a POST request to /SyncPlay/Queue.

        Request to queue items to the playlist of a SyncPlay group.

        Args:
            body (QueueRequestDto): The items to add.

        Returns:
            void: Response from the API. Queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_queue called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_queue.")
            _url_path = "/SyncPlay/Queue"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_queue.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_queue.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_queue")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_queue.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_ready(self, body):
        """Does a POST request to /SyncPlay/Ready.

        Notify SyncPlay group that member is ready for playback.

        Args:
            body (ReadyRequestDto): The player status.

        Returns:
            void: Response from the API. Group state update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_ready called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_ready.")
            _url_path = "/SyncPlay/Ready"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_ready.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_ready.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_ready")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_ready.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_remove_from_playlist(self, body):
        """Does a POST request to /SyncPlay/RemoveFromPlaylist.

        Request to remove items from the playlist in SyncPlay group.

        Args:
            body (RemoveFromPlaylistRequestDto): The items to remove.

        Returns:
            void: Response from the API. Queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_remove_from_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_remove_from_playlist.")
            _url_path = "/SyncPlay/RemoveFromPlaylist"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_remove_from_playlist.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_remove_from_playlist."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="sync_play_remove_from_playlist"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_remove_from_playlist.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_seek(self, body):
        """Does a POST request to /SyncPlay/Seek.

        Request seek in SyncPlay group.

        Args:
            body (SeekRequestDto): The new playback position.

        Returns:
            void: Response from the API. Seek update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_seek called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_seek.")
            _url_path = "/SyncPlay/Seek"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_seek.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_seek.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_seek")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_seek.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_set_ignore_wait(self, body):
        """Does a POST request to /SyncPlay/SetIgnoreWait.

        Request SyncPlay group to ignore member during group-wait.

        Args:
            body (IgnoreWaitRequestDto): The settings to set.

        Returns:
            void: Response from the API. Member state updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_set_ignore_wait called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_set_ignore_wait.")
            _url_path = "/SyncPlay/SetIgnoreWait"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_set_ignore_wait.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_set_ignore_wait."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_set_ignore_wait")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_set_ignore_wait.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_set_new_queue(self, body):
        """Does a POST request to /SyncPlay/SetNewQueue.

        Request to set new playlist in SyncPlay group.

        Args:
            body (PlayRequestDto): The new playlist to play in the group.

        Returns:
            void: Response from the API. Queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_set_new_queue called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_set_new_queue.")
            _url_path = "/SyncPlay/SetNewQueue"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_set_new_queue.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_set_new_queue."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_set_new_queue")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_set_new_queue.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_set_playlist_item(self, body):
        """Does a POST request to /SyncPlay/SetPlaylistItem.

        Request to change playlist item in SyncPlay group.

        Args:
            body (SetPlaylistItemRequestDto): The new item to play.

        Returns:
            void: Response from the API. Queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_set_playlist_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_set_playlist_item.")
            _url_path = "/SyncPlay/SetPlaylistItem"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_set_playlist_item.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_set_playlist_item."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="sync_play_set_playlist_item"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_set_playlist_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_set_repeat_mode(self, body):
        """Does a POST request to /SyncPlay/SetRepeatMode.

        Request to set repeat mode in SyncPlay group.

        Args:
            body (SetRepeatModeRequestDto): The new repeat mode.

        Returns:
            void: Response from the API. Play queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_set_repeat_mode called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_set_repeat_mode.")
            _url_path = "/SyncPlay/SetRepeatMode"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_set_repeat_mode.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_set_repeat_mode."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_set_repeat_mode")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_set_repeat_mode.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_set_shuffle_mode(self, body):
        """Does a POST request to /SyncPlay/SetShuffleMode.

        Request to set shuffle mode in SyncPlay group.

        Args:
            body (SetShuffleModeRequestDto): The new shuffle mode.

        Returns:
            void: Response from the API. Play queue update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_set_shuffle_mode called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_set_shuffle_mode.")
            _url_path = "/SyncPlay/SetShuffleMode"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for sync_play_set_shuffle_mode.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for sync_play_set_shuffle_mode."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="sync_play_set_shuffle_mode"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_set_shuffle_mode.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_stop(self):
        """Does a POST request to /SyncPlay/Stop.

        Request stop in SyncPlay group.

        Returns:
            void: Response from the API. Stop update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_stop called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_stop.")
            _url_path = "/SyncPlay/Stop"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_stop.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_stop")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_stop.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def sync_play_unpause(self):
        """Does a POST request to /SyncPlay/Unpause.

        Request unpause in SyncPlay group.

        Returns:
            void: Response from the API. Unpause update sent to all group
                members.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("sync_play_unpause called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for sync_play_unpause.")
            _url_path = "/SyncPlay/Unpause"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for sync_play_unpause.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="sync_play_unpause")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for sync_play_unpause.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
