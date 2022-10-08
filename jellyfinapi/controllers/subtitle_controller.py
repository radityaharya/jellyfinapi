# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.font_file import FontFile
from jellyfinapi.models.remote_subtitle_info import RemoteSubtitleInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class SubtitleController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SubtitleController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_fallback_font_list(self):
        """Does a GET request to /FallbackFont/Fonts.

        Gets a list of available fallback font files.

        Returns:
            list of FontFile: Response from the API. Information retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_fallback_font_list called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_fallback_font_list.")
            _url_path = "/FallbackFont/Fonts"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_fallback_font_list.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_fallback_font_list."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_fallback_font_list")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_fallback_font_list.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, FontFile.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_fallback_font(self, name):
        """Does a GET request to /FallbackFont/Fonts/{name}.

        Gets a fallback font file.

        Args:
            name (string): The name of the fallback font file to get.

        Returns:
            mixed: Response from the API. Fallback font file retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_fallback_font called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_fallback_font.")
            _url_path = "/FallbackFont/Fonts/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_fallback_font.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_fallback_font.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_fallback_font")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_fallback_font.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def search_remote_subtitles(self, item_id, language, is_perfect_match=None):
        """Does a GET request to /Items/{itemId}/RemoteSearch/Subtitles/{language}.

        Search remote subtitles.

        Args:
            item_id (uuid|string): The item id.
            language (string): The language of the subtitles.
            is_perfect_match (bool, optional): Optional. Only show subtitles
                which are a perfect match.

        Returns:
            list of RemoteSubtitleInfo: Response from the API. Subtitles
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("search_remote_subtitles called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for search_remote_subtitles.")
            _url_path = "/Items/{itemId}/RemoteSearch/Subtitles/{language}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "language": {"value": language, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"isPerfectMatch": is_perfect_match}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for search_remote_subtitles.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for search_remote_subtitles."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="search_remote_subtitles")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for search_remote_subtitles.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSubtitleInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def download_remote_subtitles(self, item_id, subtitle_id):
        """Does a POST request to /Items/{itemId}/RemoteSearch/Subtitles/{subtitleId}.

        Downloads a remote subtitle.

        Args:
            item_id (uuid|string): The item id.
            subtitle_id (string): The subtitle id.

        Returns:
            void: Response from the API. Subtitle downloaded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("download_remote_subtitles called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for download_remote_subtitles.")
            _url_path = "/Items/{itemId}/RemoteSearch/Subtitles/{subtitleId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "subtitleId": {"value": subtitle_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for download_remote_subtitles."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="download_remote_subtitles")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for download_remote_subtitles.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_remote_subtitles(self, id):
        """Does a GET request to /Providers/Subtitles/Subtitles/{id}.

        Gets the remote subtitles.

        Args:
            id (string): The item id.

        Returns:
            binary: Response from the API. File returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_remote_subtitles called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_remote_subtitles.")
            _url_path = "/Providers/Subtitles/Subtitles/{id}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"id": {"value": id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_remote_subtitles."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_remote_subtitles"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_remote_subtitles.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_subtitle_playlist(self, item_id, index, media_source_id, segment_length):
        """Does a GET request to /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8.

        Gets an HLS subtitle playlist.

        Args:
            item_id (uuid|string): The item id.
            index (int): The subtitle stream index.
            media_source_id (string): The media source id.
            segment_length (int): The subtitle segment length.

        Returns:
            mixed: Response from the API. Subtitle playlist retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_subtitle_playlist called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_subtitle_playlist.")
            _url_path = (
                "/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8"
            )
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "index": {"value": index, "encode": True},
                    "mediaSourceId": {"value": media_source_id, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"segmentLength": segment_length}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_subtitle_playlist.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_subtitle_playlist."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_subtitle_playlist")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_subtitle_playlist.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def upload_subtitle(self, item_id, body):
        """Does a POST request to /Videos/{itemId}/Subtitles.

        Upload an external subtitle file.

        Args:
            item_id (uuid|string): The item the subtitle belongs to.
            body (UploadSubtitleDto): The request body.

        Returns:
            void: Response from the API. Subtitle uploaded.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("upload_subtitle called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for upload_subtitle.")
            _url_path = "/Videos/{itemId}/Subtitles"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for upload_subtitle.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for upload_subtitle.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="upload_subtitle")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for upload_subtitle.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_subtitle(self, item_id, index):
        """Does a DELETE request to /Videos/{itemId}/Subtitles/{index}.

        Deletes an external subtitle file.

        Args:
            item_id (uuid|string): The item id.
            index (int): The index of the subtitle file.

        Returns:
            void: Response from the API. Subtitle deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_subtitle called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_subtitle.")
            _url_path = "/Videos/{itemId}/Subtitles/{index}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "index": {"value": index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_subtitle.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_subtitle")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_subtitle.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_subtitle_with_ticks(
        self,
        route_item_id,
        route_media_source_id,
        route_index,
        route_start_position_ticks,
        route_format,
        item_id=None,
        media_source_id=None,
        index=None,
        start_position_ticks=None,
        format=None,
        end_position_ticks=None,
        copy_timestamps=False,
        add_vtt_time_map=False,
    ):
        """Does a GET request to /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}.

        Gets subtitles in a specified format.

        Args:
            route_item_id (uuid|string): The (route) item id.
            route_media_source_id (string): The (route) media source id.
            route_index (int): The (route) subtitle stream index.
            route_start_position_ticks (long|int): The (route) start position
                of the subtitle in ticks.
            route_format (string): The (route) format of the returned
                subtitle.
            item_id (uuid|string, optional): The item id.
            media_source_id (string, optional): The media source id.
            index (int, optional): The subtitle stream index.
            start_position_ticks (long|int, optional): The start position of
                the subtitle in ticks.
            format (string, optional): The format of the returned subtitle.
            end_position_ticks (long|int, optional): Optional. The end
                position of the subtitle in ticks.
            copy_timestamps (bool, optional): Optional. Whether to copy the
                timestamps.
            add_vtt_time_map (bool, optional): Optional. Whether to add a VTT
                time map.

        Returns:
            binary: Response from the API. File returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_subtitle_with_ticks called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_subtitle_with_ticks.")
            _url_path = "/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "routeItemId": {"value": route_item_id, "encode": True},
                    "routeMediaSourceId": {
                        "value": route_media_source_id,
                        "encode": True,
                    },
                    "routeIndex": {"value": route_index, "encode": True},
                    "routeStartPositionTicks": {
                        "value": route_start_position_ticks,
                        "encode": True,
                    },
                    "routeFormat": {"value": route_format, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "itemId": item_id,
                "mediaSourceId": media_source_id,
                "index": index,
                "startPositionTicks": start_position_ticks,
                "format": format,
                "endPositionTicks": end_position_ticks,
                "copyTimestamps": copy_timestamps,
                "addVttTimeMap": add_vtt_time_map,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_subtitle_with_ticks."
            )
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_subtitle_with_ticks"
            )
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_subtitle(
        self,
        route_item_id,
        route_media_source_id,
        route_index,
        route_format,
        item_id=None,
        media_source_id=None,
        index=None,
        format=None,
        end_position_ticks=None,
        copy_timestamps=False,
        add_vtt_time_map=False,
        start_position_ticks=0,
    ):
        """Does a GET request to /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat}.

        Gets subtitles in a specified format.

        Args:
            route_item_id (uuid|string): The (route) item id.
            route_media_source_id (string): The (route) media source id.
            route_index (int): The (route) subtitle stream index.
            route_format (string): The (route) format of the returned
                subtitle.
            item_id (uuid|string, optional): The item id.
            media_source_id (string, optional): The media source id.
            index (int, optional): The subtitle stream index.
            format (string, optional): The format of the returned subtitle.
            end_position_ticks (long|int, optional): Optional. The end
                position of the subtitle in ticks.
            copy_timestamps (bool, optional): Optional. Whether to copy the
                timestamps.
            add_vtt_time_map (bool, optional): Optional. Whether to add a VTT
                time map.
            start_position_ticks (long|int, optional): The start position of
                the subtitle in ticks.

        Returns:
            binary: Response from the API. File returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_subtitle called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_subtitle.")
            _url_path = "/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "routeItemId": {"value": route_item_id, "encode": True},
                    "routeMediaSourceId": {
                        "value": route_media_source_id,
                        "encode": True,
                    },
                    "routeIndex": {"value": route_index, "encode": True},
                    "routeFormat": {"value": route_format, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "itemId": item_id,
                "mediaSourceId": media_source_id,
                "index": index,
                "format": format,
                "endPositionTicks": end_position_ticks,
                "copyTimestamps": copy_timestamps,
                "addVttTimeMap": add_vtt_time_map,
                "startPositionTicks": start_position_ticks,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_subtitle.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, binary=True, name="get_subtitle")
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
