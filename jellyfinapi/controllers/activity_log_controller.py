# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.activity_log_entry_query_result import (
    ActivityLogEntryQueryResult,
)
from jellyfinapi.exceptions.api_exception import APIException


class ActivityLogController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ActivityLogController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_log_entries(
        self, start_index=None, limit=None, min_date=None, has_user_id=None
    ):
        """Does a GET request to /System/ActivityLog/Entries.

        Gets activity log entries.

        Args:
            start_index (int, optional): Optional. The record index to start
                at. All items with a lower index will be dropped from the
                results.
            limit (int, optional): Optional. The maximum number of records to
                return.
            min_date (datetime, optional): Optional. The minimum date. Format
                = ISO.
            has_user_id (bool, optional): Optional. Filter log entries if it
                has user id, or not.

        Returns:
            ActivityLogEntryQueryResult: Response from the API. Activity log
                returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_log_entries called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_log_entries.")
            _url_path = "/System/ActivityLog/Entries"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "startIndex": start_index,
                "limit": limit,
                "minDate": APIHelper.when_defined(APIHelper.RFC3339DateTime, min_date),
                "hasUserId": has_user_id,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_log_entries.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_log_entries.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_log_entries")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_log_entries.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ActivityLogEntryQueryResult.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
