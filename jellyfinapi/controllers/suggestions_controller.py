# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfinapi.exceptions.api_exception import APIException


class SuggestionsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(SuggestionsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_suggestions(
        self,
        user_id,
        media_type=None,
        mtype=None,
        start_index=None,
        limit=None,
        enable_total_record_count=False,
    ):
        """Does a GET request to /Users/{userId}/Suggestions.

        Gets suggestions.

        Args:
            user_id (uuid|string): The user id.
            media_type (list of string, optional): The media types.
            mtype (list of BaseItemKindEnum, optional): The type.
            start_index (int, optional): Optional. The start index.
            limit (int, optional): Optional. The limit.
            enable_total_record_count (bool, optional): Whether to enable the
                total record count.

        Returns:
            BaseItemDtoQueryResult: Response from the API. Suggestions
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_suggestions called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_suggestions.")
            _url_path = "/Users/{userId}/Suggestions"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"userId": {"value": user_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "mediaType": media_type,
                "type": mtype,
                "startIndex": start_index,
                "limit": limit,
                "enableTotalRecordCount": enable_total_record_count,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_suggestions.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_suggestions.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_suggestions")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_suggestions.")
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
