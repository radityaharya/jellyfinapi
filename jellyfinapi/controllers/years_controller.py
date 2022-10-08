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


class YearsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(YearsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_years(
        self,
        start_index=None,
        limit=None,
        sort_order=None,
        parent_id=None,
        fields=None,
        exclude_item_types=None,
        include_item_types=None,
        media_types=None,
        sort_by=None,
        enable_user_data=None,
        image_type_limit=None,
        enable_image_types=None,
        user_id=None,
        recursive=True,
        enable_images=True,
    ):
        """Does a GET request to /Years.

        Get years.

        Args:
            start_index (int, optional): Skips over a given number of items
                within the results. Use for paging.
            limit (int, optional): Optional. The maximum number of records to
                return.
            sort_order (list of SortOrderEnum, optional): Sort Order -
                Ascending,Descending.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. Specify
                additional fields of information to return in the output.
            exclude_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be excluded based on item type.
                This allows multiple, comma delimited.
            include_item_types (list of BaseItemKindEnum, optional): Optional.
                If specified, results will be included based on item type.
                This allows multiple, comma delimited.
            media_types (list of string, optional): Optional. Filter by
                MediaType. Allows multiple, comma delimited.
            sort_by (list of string, optional): Optional. Specify one or more
                sort orders, comma delimited. Options: Album, AlbumArtist,
                Artist, Budget, CommunityRating, CriticRating, DateCreated,
                DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName,
                Random, Revenue, Runtime.
            enable_user_data (bool, optional): Optional. Include user data.
            image_type_limit (int, optional): Optional. The max number of
                images to return, per image type.
            enable_image_types (list of ImageTypeEnum, optional): Optional.
                The image types to include in the output.
            user_id (uuid|string, optional): User Id.
            recursive (bool, optional): Search recursively.
            enable_images (bool, optional): Optional. Include image
                information in output.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Year query
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_years called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_years.")
            _url_path = "/Years"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "startIndex": start_index,
                "limit": limit,
                "sortOrder": sort_order,
                "parentId": parent_id,
                "fields": fields,
                "excludeItemTypes": exclude_item_types,
                "includeItemTypes": include_item_types,
                "mediaTypes": media_types,
                "sortBy": sort_by,
                "enableUserData": enable_user_data,
                "imageTypeLimit": image_type_limit,
                "enableImageTypes": enable_image_types,
                "userId": user_id,
                "recursive": recursive,
                "enableImages": enable_images,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_years.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_years.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_years")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_years.")
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

    def get_year(self, year, user_id=None):
        """Does a GET request to /Years/{year}.

        Gets a year.

        Args:
            year (int): The year.
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.

        Returns:
            BaseItemDto: Response from the API. Year returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_year called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_year.")
            _url_path = "/Years/{year}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"year": {"value": year, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"userId": user_id}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_year.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_year.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_year")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_year.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Year not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, BaseItemDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
