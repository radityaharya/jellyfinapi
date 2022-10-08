# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.virtual_folder_info import VirtualFolderInfo
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class LibraryStructureController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(LibraryStructureController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_virtual_folders(self):
        """Does a GET request to /Library/VirtualFolders.

        Gets all virtual folders.

        Returns:
            list of VirtualFolderInfo: Response from the API. Virtual folders
                retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_virtual_folders called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_virtual_folders.")
            _url_path = "/Library/VirtualFolders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_virtual_folders.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_virtual_folders.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_virtual_folders")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_virtual_folders.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, VirtualFolderInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_virtual_folder(
        self,
        name=None,
        collection_type=None,
        paths=None,
        refresh_library=False,
        body=None,
    ):
        """Does a POST request to /Library/VirtualFolders.

        Adds a virtual folder.

        Args:
            name (string, optional): The name of the virtual folder.
            collection_type (CollectionTypeOptionsEnum, optional): The type of
                the collection.
            paths (list of string, optional): The paths of the virtual
                folder.
            refresh_library (bool, optional): Whether to refresh the library.
            body (AddVirtualFolderDto, optional): The library options.

        Returns:
            void: Response from the API. Folder added.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_virtual_folder called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_virtual_folder.")
            _url_path = "/Library/VirtualFolders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "name": name,
                "collectionType": collection_type,
                "paths": paths,
                "refreshLibrary": refresh_library,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for add_virtual_folder.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_virtual_folder.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_virtual_folder")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_virtual_folder.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_virtual_folder(self, name=None, refresh_library=False):
        """Does a DELETE request to /Library/VirtualFolders.

        Removes a virtual folder.

        Args:
            name (string, optional): The name of the folder.
            refresh_library (bool, optional): Whether to refresh the library.

        Returns:
            void: Response from the API. Folder removed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("remove_virtual_folder called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for remove_virtual_folder.")
            _url_path = "/Library/VirtualFolders"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"name": name, "refreshLibrary": refresh_library}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for remove_virtual_folder."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="remove_virtual_folder")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for remove_virtual_folder.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_library_options(self, body=None):
        """Does a POST request to /Library/VirtualFolders/LibraryOptions.

        Update library options.

        Args:
            body (UpdateLibraryOptionsDto, optional): The library name and
                options.

        Returns:
            void: Response from the API. Library updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_library_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_library_options.")
            _url_path = "/Library/VirtualFolders/LibraryOptions"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_library_options.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_library_options."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_library_options")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_library_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def rename_virtual_folder(self, name=None, new_name=None, refresh_library=False):
        """Does a POST request to /Library/VirtualFolders/Name.

        Renames a virtual folder.

        Args:
            name (string, optional): The name of the virtual folder.
            new_name (string, optional): The new name.
            refresh_library (bool, optional): Whether to refresh the library.

        Returns:
            void: Response from the API. Folder renamed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("rename_virtual_folder called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for rename_virtual_folder.")
            _url_path = "/Library/VirtualFolders/Name"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "name": name,
                "newName": new_name,
                "refreshLibrary": refresh_library,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for rename_virtual_folder."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="rename_virtual_folder")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for rename_virtual_folder.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Library doesn't exist.", _response)
            elif _response.status_code == 409:
                raise ProblemDetailsException("Library already exists.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def add_media_path(self, body, refresh_library=False):
        """Does a POST request to /Library/VirtualFolders/Paths.

        Add a media path to a library.

        Args:
            body (MediaPathDto): The media path dto.
            refresh_library (bool, optional): Whether to refresh the library.

        Returns:
            void: Response from the API. Media path added.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("add_media_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for add_media_path.")
            _url_path = "/Library/VirtualFolders/Paths"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"refreshLibrary": refresh_library}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for add_media_path.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for add_media_path.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="add_media_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for add_media_path.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def remove_media_path(self, name=None, path=None, refresh_library=False):
        """Does a DELETE request to /Library/VirtualFolders/Paths.

        Remove a media path.

        Args:
            name (string, optional): The name of the library.
            path (string, optional): The path to remove.
            refresh_library (bool, optional): Whether to refresh the library.

        Returns:
            void: Response from the API. Media path removed.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("remove_media_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for remove_media_path.")
            _url_path = "/Library/VirtualFolders/Paths"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "name": name,
                "path": path,
                "refreshLibrary": refresh_library,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for remove_media_path.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="remove_media_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for remove_media_path.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_media_path(self, body):
        """Does a POST request to /Library/VirtualFolders/Paths/Update.

        Updates a media path.

        Args:
            body (UpdateMediaPathRequestDto): The name of the library and path
                infos.

        Returns:
            void: Response from the API. Media path updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_media_path called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_media_path.")
            _url_path = "/Library/VirtualFolders/Paths/Update"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for update_media_path.")
            _headers = {"Content-Type": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for update_media_path.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_media_path")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_media_path.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
