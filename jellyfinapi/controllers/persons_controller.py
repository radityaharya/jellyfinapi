# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class PersonsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(PersonsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_persons(
        self,
        limit=None,
        search_term=None,
        fields=None,
        filters=None,
        is_favorite=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
        exclude_person_types=None,
        person_types=None,
        appears_in_item_id=None,
        user_id=None,
        enable_images=True,
    ):
        """Does a GET request to /Persons.

        Gets all persons.

        Args:
            limit (int, optional): Optional. The maximum number of records to
                return.
            search_term (string, optional): The search term.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            filters (list of ItemFilterEnum, optional): Optional. Specify
                additional filters to apply.
            is_favorite (bool, optional): Optional filter by items that are
                marked as favorite, or not. userId is required.
            enable_user_data (bool, optional): Optional, include user data.
            image_type_limit (int, optional): Optional, the max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            exclude_person_types (list of string, optional): Optional. If
                specified results will be filtered to exclude those containing
                the specified PersonType. Allows multiple, comma-delimited.
            person_types (list of string, optional): Optional. If specified
                results will be filtered to include only those containing the
                specified PersonType. Allows multiple, comma-delimited.
            appears_in_item_id (uuid|string, optional): Optional. If
                specified, person results will be filtered on items related to
                said persons.
            user_id (uuid|string, optional): User id.
            enable_images (bool, optional): Optional, include image
                information in output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Persons returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_persons called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_persons.")
            _url_path = "/Persons"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "limit": limit,
                "searchTerm": search_term,
                "fields": fields,
                "filters": filters,
                "isFavorite": is_favorite,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "excludePersonTypes": exclude_person_types,
                "personTypes": person_types,
                "appearsInItemId": appears_in_item_id,
                "userId": user_id,
                "enableImages": enable_images,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_persons.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_persons.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_persons")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_persons.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDtoQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_person(self, name, user_id=None):
        """Does a GET request to /Persons/{name}.

        Get person by name.

        Args:
            name (string): Person name.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.

        Returns:
            BaseItemDto: Response from the API. Person returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_person called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_person.")
            _url_path = "/Persons/{name}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"name": {"value": name, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_person.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_person.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_person")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_person.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Person not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
