# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.exceptions.api_exception import APIException
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException


class ItemRefreshController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ItemRefreshController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def refresh_item(
        self,
        item_id,
        metadata_refresh_mode="None",
        image_refresh_mode="None",
        replace_all_metadata=False,
        replace_all_images=False,
    ):
        """Does a POST request to /Items/{itemId}/Refresh.

        Refreshes metadata for an item.

        Args:
            item_id (uuid|string): Item id.
            metadata_refresh_mode (MetadataRefreshModeEnum, optional):
                (Optional) Specifies the metadata refresh mode.
            image_refresh_mode (MetadataRefreshModeEnum, optional): (Optional)
                Specifies the image refresh mode.
            replace_all_metadata (bool, optional): (Optional) Determines if
                metadata should be replaced. Only applicable if mode is
                FullRefresh.
            replace_all_images (bool, optional): (Optional) Determines if
                images should be replaced. Only applicable if mode is
                FullRefresh.

        Returns:
            void: Response from the API. Item metadata refresh queued.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("refresh_item called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for refresh_item.")
            _url_path = "/Items/{itemId}/Refresh"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "metadataRefreshMode": metadata_refresh_mode,
                "imageRefreshMode": image_refresh_mode,
                "replaceAllMetadata": replace_all_metadata,
                "replaceAllImages": replace_all_images,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for refresh_item.")
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="refresh_item")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for refresh_item.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item to refresh not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
