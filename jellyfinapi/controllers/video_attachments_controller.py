# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class VideoAttachmentsController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(VideoAttachmentsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_attachment(self, video_id, media_source_id, index):
        """Does a GET request to /Videos/{videoId}/{mediaSourceId}/Attachments/{index}.

        Get video attachment.

        Args:
            video_id (uuid|string): Video ID.
            media_source_id (string): Media Source ID.
            index (int): Attachment Index.

        Returns:
            binary: Response from the API. Attachment retrieved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_attachment called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_attachment.")
            _url_path = "/Videos/{videoId}/{mediaSourceId}/Attachments/{index}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "videoId": {"value": video_id, "encode": True},
                    "mediaSourceId": {"value": media_source_id, "encode": True},
                    "index": {"value": index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_attachment.")
            _request = self.config.http_client.get(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, binary=True, name="get_attachment"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_attachment.")
            if _response.status_code == 404:
                raise ProblemDetailsException(
                    "Video or attachment not found.", _response
                )
            self.validate_response(_response)

            decoded = _response.text

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
