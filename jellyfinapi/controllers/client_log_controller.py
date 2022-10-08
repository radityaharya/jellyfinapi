# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.file_wrapper import FileWrapper
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.client_log_document_response_dto import (
    ClientLogDocumentResponseDto,
)
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ClientLogController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ClientLogController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def log_file(self, body=None):
        """Does a POST request to /ClientLog/Document.

        Upload a document.

        Args:
            body (typing.BinaryIO, optional): TODO: type description here.

        Returns:
            ClientLogDocumentResponseDto: Response from the API. Document
                saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("log_file called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for log_file.")
            _url_path = "/ClientLog/Document"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            if isinstance(body, FileWrapper):
                body_wrapper = body.file_stream
                body_content_type = body.content_type
            else:
                body_wrapper = body
                body_content_type = "application/octet-stream"

            # Prepare files
            self.logger.info("Preparing files for log_file.")
            _files = {"body": (body_wrapper.name, body_wrapper, body_content_type)}

            # Prepare headers
            self.logger.info("Preparing headers for log_file.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for log_file.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, files=_files
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="log_file")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for log_file.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException("Event logging disabled.", _response)
            elif _response.status_code == 413:
                raise ProblemDetailsException("Upload size too large.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ClientLogDocumentResponseDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
