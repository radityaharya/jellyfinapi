# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.special_view_option_dto import SpecialViewOptionDto
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class UserViewsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(UserViewsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_grouping_options(self, user_id):
        """Does a GET request to /Users/{userId}/GroupingOptions.

        Get user view grouping options.

        Args:
            user_id (uuid|string): User id.

        Returns:
            list of SpecialViewOptionDto: Response from the API. User view
                grouping options returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_grouping_options called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_grouping_options.")
            _url_path = "/Users/{userId}/GroupingOptions"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_grouping_options.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_grouping_options."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_grouping_options")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_grouping_options.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("User not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, SpecialViewOptionDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_user_views(
        self,
        user_id,
        include_external_content=None,
        preset_views=None,
        include_hidden=False,
    ):
        """Does a GET request to /Users/{userId}/Views.

        Get user views.

        Args:
            user_id (uuid|string): User id.
            include_external_content (bool, optional): Whether or not to
                include external views such as channels or live tv.
            preset_views (list of string, optional): Preset views.
            include_hidden (bool, optional): Whether or not to include hidden
                content.

        Returns:
            BaseItemDtoQueryResult: Response from the API. User views
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_user_views called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_user_views.")
            _url_path = "/Users/{userId}/Views"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "includeExternalContent": include_external_content,
                "presetViews": preset_views,
                "includeHidden": include_hidden,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_user_views.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_user_views.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_user_views")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_user_views.")
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
