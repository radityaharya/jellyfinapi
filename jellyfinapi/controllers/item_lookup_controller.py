# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.external_id_info import ExternalIdInfo
from jellyfinapi.models.remote_search_result import RemoteSearchResult
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ItemLookupController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ItemLookupController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_external_id_infos(self, item_id):
        """Does a GET request to /Items/{itemId}/ExternalIdInfos.

        Get the item's external id info.

        Args:
            item_id (uuid|string): Item id.

        Returns:
            list of ExternalIdInfo: Response from the API. External id info
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_external_id_infos called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_external_id_infos.")
            _url_path = "/Items/{itemId}/ExternalIdInfos"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_external_id_infos.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_external_id_infos."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_external_id_infos")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_external_id_infos.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ExternalIdInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def apply_search_criteria(self, item_id, body, replace_all_images=True):
        """Does a POST request to /Items/RemoteSearch/Apply/{itemId}.

        Applies search criteria to an item and refreshes metadata.

        Args:
            item_id (uuid|string): Item id.
            body (RemoteSearchResult): The remote search result.
            replace_all_images (bool, optional): Optional. Whether or not to
                replace all images. Default: True.

        Returns:
            void: Response from the API. Item metadata refreshed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("apply_search_criteria called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for apply_search_criteria.")
            _url_path = "/Items/RemoteSearch/Apply/{itemId}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"replaceAllImages": replace_all_images}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for apply_search_criteria.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for apply_search_criteria."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="apply_search_criteria")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for apply_search_criteria.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_book_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/Book.

        Get book remote search.

        Args:
            body (BookInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Book remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_book_remote_search_results called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_book_remote_search_results.")
            _url_path = "/Items/RemoteSearch/Book"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_book_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_book_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_book_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_book_remote_search_results.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_box_set_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/BoxSet.

        Get box set remote search.

        Args:
            body (BoxSetInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Box set remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_box_set_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_box_set_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/BoxSet"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_box_set_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_box_set_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_box_set_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_box_set_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_movie_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/Movie.

        Get movie remote search.

        Args:
            body (MovieInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Movie remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_movie_remote_search_results called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_movie_remote_search_results.")
            _url_path = "/Items/RemoteSearch/Movie"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_movie_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_movie_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_movie_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_movie_remote_search_results.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_music_album_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/MusicAlbum.

        Get music album remote search.

        Args:
            body (AlbumInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Music album
                remote search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_music_album_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_music_album_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/MusicAlbum"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for get_music_album_remote_search_results."
            )
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_music_album_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_music_album_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_music_album_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_music_artist_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/MusicArtist.

        Get music artist remote search.

        Args:
            body (ArtistInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Music artist
                remote search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_music_artist_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_music_artist_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/MusicArtist"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for get_music_artist_remote_search_results."
            )
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_music_artist_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_music_artist_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_music_artist_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_music_video_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/MusicVideo.

        Get music video remote search.

        Args:
            body (MusicVideoInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Music video
                remote search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_music_video_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_music_video_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/MusicVideo"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info(
                "Preparing headers for get_music_video_remote_search_results."
            )
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_music_video_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_music_video_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_music_video_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_person_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/Person.

        Get person remote search.

        Args:
            body (PersonLookupInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Person remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_person_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_person_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/Person"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_person_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_person_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_person_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_person_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_series_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/Series.

        Get series remote search.

        Args:
            body (SeriesInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Series remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_series_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_series_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/Series"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_series_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_series_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_series_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_series_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_trailer_remote_search_results(self, body):
        """Does a POST request to /Items/RemoteSearch/Trailer.

        Get trailer remote search.

        Args:
            body (TrailerInfoRemoteSearchQuery): Remote search query.

        Returns:
            list of RemoteSearchResult: Response from the API. Trailer remote
                search executed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_trailer_remote_search_results called.")

            # Prepare query URL
            self.logger.info(
                "Preparing query URL for get_trailer_remote_search_results."
            )
            _url_path = "/Items/RemoteSearch/Trailer"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_trailer_remote_search_results.")
            _headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_trailer_remote_search_results."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_trailer_remote_search_results"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                "Validating response for get_trailer_remote_search_results."
            )
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RemoteSearchResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
