# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.recommendation_dto import RecommendationDto
from jellyfinapi.exceptions.api_exception import APIException


class MoviesController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(MoviesController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_movie_recommendations(
        self, user_id=None, parent_id=None, fields=None, category_limit=5, item_limit=8
    ):
        """Does a GET request to /Movies/Recommendations.

        Gets movie recommendations.

        Args:
            user_id (uuid|string, optional): Optional. Filter by user id, and
                attach user data.
            parent_id (uuid|string, optional): Specify this to localize the
                search to a specific item or folder. Omit to use the root.
            fields (list of ItemFieldsEnum, optional): Optional. The fields to
                return.
            category_limit (int, optional): The max number of categories to
                return.
            item_limit (int, optional): The max number of items to return per
                category.

        Returns:
            list of RecommendationDto: Response from the API. Movie
                recommendations returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_movie_recommendations called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_movie_recommendations.")
            _url_path = "/Movies/Recommendations"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "userId": user_id,
                "parentId": parent_id,
                "fields": fields,
                "categoryLimit": category_limit,
                "itemLimit": item_limit,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_movie_recommendations.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_movie_recommendations."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_movie_recommendations")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_movie_recommendations.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, RecommendationDto.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
