# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import logging
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.configuration import Server
from jellyfinapi.utilities.xml_utilities import XmlUtilities
from jellyfinapi.controllers.base_controller import BaseController
from jellyfinapi.models.image_info import ImageInfo
from jellyfinapi.exceptions.problem_details_exception import ProblemDetailsException
from jellyfinapi.exceptions.api_exception import APIException


class ImageController(BaseController):

    """A Controller to access Endpoints in the jellyfinapi API."""

    def __init__(self, config, auth_managers):
        super(ImageController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def get_artist_image(
        self,
        name,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Artists/{name}/Images/{imageType}/{imageIndex}.

        Get artist image by name.

        Args:
            name (string): Artist name.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_artist_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_artist_image.")
            _url_path = "/Artists/{name}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_artist_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_artist_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_artist_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_artist_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_splashscreen(
        self,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        width=None,
        height=None,
        fill_width=None,
        fill_height=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        quality=90,
    ):
        """Does a GET request to /Branding/Splashscreen.

        Generates or gets the splashscreen.

        Args:
            tag (string, optional): Supply the cache tag from the item object
                to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            blur (int, optional): Blur image.
            background_color (string, optional): Apply a background color for
                transparent images.
            foreground_layer (string, optional): Apply a foreground layer on
                top of the image.
            quality (int, optional): Quality setting, from 0-100.

        Returns:
            mixed: Response from the API. Splashscreen returned successfully.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_splashscreen called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_splashscreen.")
            _url_path = "/Branding/Splashscreen"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "width": width,
                "height": height,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "quality": quality,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_splashscreen.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_splashscreen.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_splashscreen")
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def upload_custom_splashscreen(self, body=None):
        """Does a POST request to /Branding/Splashscreen.

        Uploads a custom splashscreen.
        The body is expected to the image contents base64 encoded.

        Args:
            body (object, optional): TODO: type description here.

        Returns:
            void: Response from the API. Successfully uploaded new
                splashscreen.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("upload_custom_splashscreen called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for upload_custom_splashscreen.")
            _url_path = "/Branding/Splashscreen"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for upload_custom_splashscreen.")
            _headers = {"content-type": "application/json; charset=utf-8"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for upload_custom_splashscreen."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="upload_custom_splashscreen"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for upload_custom_splashscreen.")
            if _response.status_code == 400:
                raise ProblemDetailsException(
                    "Error reading MimeType from uploaded image.", _response
                )
            elif _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User does not have permission to upload splashscreen..", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_custom_splashscreen(self):
        """Does a DELETE request to /Branding/Splashscreen.

        Delete a custom splashscreen.

        Returns:
            void: Response from the API. Successfully deleted the custom
                splashscreen.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_custom_splashscreen called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_custom_splashscreen.")
            _url_path = "/Branding/Splashscreen"
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for delete_custom_splashscreen."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="delete_custom_splashscreen"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_custom_splashscreen.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException(
                    "User does not have permission to delete splashscreen..", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_genre_image(
        self,
        name,
        image_type,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /Genres/{name}/Images/{imageType}.

        Get genre image by name.

        Args:
            name (string): Genre name.
            image_type (ImageTypeEnum): Image type.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_genre_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_genre_image.")
            _url_path = "/Genres/{name}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_genre_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_genre_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_genre_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_genre_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_genre_image_by_index(
        self,
        name,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Genres/{name}/Images/{imageType}/{imageIndex}.

        Get genre image by name.

        Args:
            name (string): Genre name.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_genre_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_genre_image_by_index.")
            _url_path = "/Genres/{name}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_genre_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_genre_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_genre_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_genre_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item_image_infos(self, item_id):
        """Does a GET request to /Items/{itemId}/Images.

        Get item image infos.

        Args:
            item_id (uuid|string): Item id.

        Returns:
            list of ImageInfo: Response from the API. Item images returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item_image_infos called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item_image_infos.")
            _url_path = "/Items/{itemId}/Images"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {"itemId": {"value": item_id, "encode": True}}
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item_image_infos.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_item_image_infos."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item_image_infos")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item_image_infos.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

            decoded = APIHelper.json_deserialize(
                _response.text, ImageInfo.from_dictionary
            )

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_item_image(self, item_id, image_type, image_index=None):
        """Does a DELETE request to /Items/{itemId}/Images/{imageType}.

        Delete an item's image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            image_index (int, optional): The image index.

        Returns:
            void: Response from the API. Image deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_item_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_item_image.")
            _url_path = "/Items/{itemId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"imageIndex": image_index}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_item_image.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_item_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_item_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_item_image(self, item_id, image_type, body=None):
        """Does a POST request to /Items/{itemId}/Images/{imageType}.

        Set item image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            body (object, optional): TODO: type description here.

        Returns:
            void: Response from the API. Image saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_item_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_item_image.")
            _url_path = "/Items/{itemId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for set_item_image.")
            _headers = {"content-type": "application/json; charset=utf-8"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for set_item_image.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_item_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_item_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item_image(
        self,
        item_id,
        image_type,
        max_width=None,
        max_height=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        tag=None,
        crop_whitespace=None,
        format=None,
        add_played_indicator=None,
        percent_played=None,
        unplayed_count=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /Items/{itemId}/Images/{imageType}.

        Gets the item's image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            format (ImageFormatEnum, optional): Optional. The
                MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item_image.")
            _url_path = "/Items/{itemId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "maxWidth": max_width,
                "maxHeight": max_height,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "tag": tag,
                "cropWhitespace": crop_whitespace,
                "format": format,
                "addPlayedIndicator": add_played_indicator,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_item_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_item_image_by_index(self, item_id, image_type, image_index):
        """Does a DELETE request to /Items/{itemId}/Images/{imageType}/{imageIndex}.

        Delete an item's image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            image_index (int): The image index.

        Returns:
            void: Response from the API. Image deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_item_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_item_image_by_index.")
            _url_path = "/Items/{itemId}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for delete_item_image_by_index."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="delete_item_image_by_index"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_item_image_by_index.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def set_item_image_by_index(self, item_id, image_type, image_index, body=None):
        """Does a POST request to /Items/{itemId}/Images/{imageType}/{imageIndex}.

        Set item image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            image_index (int): (Unused) Image index.
            body (object, optional): TODO: type description here.

        Returns:
            void: Response from the API. Image saved.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("set_item_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for set_item_image_by_index.")
            _url_path = "/Items/{itemId}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for set_item_image_by_index.")
            _headers = {"content-type": "application/json; charset=utf-8"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for set_item_image_by_index."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="set_item_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for set_item_image_by_index.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item_image_by_index(
        self,
        item_id,
        image_type,
        image_index,
        max_width=None,
        max_height=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        tag=None,
        crop_whitespace=None,
        format=None,
        add_played_indicator=None,
        percent_played=None,
        unplayed_count=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Items/{itemId}/Images/{imageType}/{imageIndex}.

        Gets the item's image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            format (ImageFormatEnum, optional): Optional. The
                MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item_image_by_index.")
            _url_path = "/Items/{itemId}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "maxWidth": max_width,
                "maxHeight": max_height,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "tag": tag,
                "cropWhitespace": crop_whitespace,
                "format": format,
                "addPlayedIndicator": add_played_indicator,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_item_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_item_image_2(
        self,
        item_id,
        image_type,
        max_width,
        max_height,
        tag,
        format,
        percent_played,
        unplayed_count,
        image_index,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}.

        Gets the item's image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            tag (string): Optional. Supply the cache tag from the item object
                to receive strong caching headers.
            format (ImageFormatEnum): Determines the output format of the
                image - original,gif,jpg,png.
            percent_played (float): Optional. Percent to render for the
                percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            image_index (int): Image index.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_item_image_2 called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_item_image_2.")
            _url_path = "/Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "maxWidth": {"value": max_width, "encode": True},
                    "maxHeight": {"value": max_height, "encode": True},
                    "tag": {"value": tag, "encode": True},
                    "format": {"value": format, "encode": True},
                    "percentPlayed": {"value": percent_played, "encode": True},
                    "unplayedCount": {"value": unplayed_count, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_item_image_2.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_item_image_2.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_item_image_2")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_item_image_2.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_item_image_index(self, item_id, image_type, image_index, new_index):
        """Does a POST request to /Items/{itemId}/Images/{imageType}/{imageIndex}/Index.

        Updates the index for an item image.

        Args:
            item_id (uuid|string): Item id.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Old image index.
            new_index (int): New image index.

        Returns:
            void: Response from the API. Image index updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("update_item_image_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for update_item_image_index.")
            _url_path = "/Items/{itemId}/Images/{imageType}/{imageIndex}/Index"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "itemId": {"value": item_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"newIndex": new_index}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for update_item_image_index."
            )
            _request = self.config.http_client.post(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="update_item_image_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for update_item_image_index.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise APIException("Forbidden", _response)
            elif _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_music_genre_image(
        self,
        name,
        image_type,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /MusicGenres/{name}/Images/{imageType}.

        Get music genre image by name.

        Args:
            name (string): Music genre name.
            image_type (ImageTypeEnum): Image type.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_music_genre_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_music_genre_image.")
            _url_path = "/MusicGenres/{name}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_music_genre_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_music_genre_image."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_music_genre_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_music_genre_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_music_genre_image_by_index(
        self,
        name,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /MusicGenres/{name}/Images/{imageType}/{imageIndex}.

        Get music genre image by name.

        Args:
            name (string): Music genre name.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_music_genre_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_music_genre_image_by_index.")
            _url_path = "/MusicGenres/{name}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_music_genre_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_music_genre_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="get_music_genre_image_by_index"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_music_genre_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_person_image(
        self,
        name,
        image_type,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /Persons/{name}/Images/{imageType}.

        Get person image by name.

        Args:
            name (string): Person name.
            image_type (ImageTypeEnum): Image type.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_person_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_person_image.")
            _url_path = "/Persons/{name}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_person_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_person_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_person_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_person_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_person_image_by_index(
        self,
        name,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Persons/{name}/Images/{imageType}/{imageIndex}.

        Get person image by name.

        Args:
            name (string): Person name.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_person_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_person_image_by_index.")
            _url_path = "/Persons/{name}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_person_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_person_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_person_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_person_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_studio_image(
        self,
        name,
        image_type,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /Studios/{name}/Images/{imageType}.

        Get studio image by name.

        Args:
            name (string): Studio name.
            image_type (ImageTypeEnum): Image type.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_studio_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_studio_image.")
            _url_path = "/Studios/{name}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_studio_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_studio_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_studio_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_studio_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_studio_image_by_index(
        self,
        name,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Studios/{name}/Images/{imageType}/{imageIndex}.

        Get studio image by name.

        Args:
            name (string): Studio name.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_studio_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_studio_image_by_index.")
            _url_path = "/Studios/{name}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "name": {"value": name, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_studio_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_studio_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_studio_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_studio_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_user_image(self, user_id, image_type, index=None, body=None):
        """Does a POST request to /Users/{userId}/Images/{imageType}.

        Sets the user image.

        Args:
            user_id (uuid|string): User Id.
            image_type (ImageTypeEnum): (Unused) Image type.
            index (int, optional): (Unused) Image index.
            body (object, optional): TODO: type description here.

        Returns:
            void: Response from the API. Image updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_user_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_user_image.")
            _url_path = "/Users/{userId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"index": index}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for post_user_image.")
            _headers = {"content-type": "application/json; charset=utf-8"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for post_user_image.")
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_user_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_user_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User does not have permission to delete the image.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_user_image(self, user_id, image_type, index=None):
        """Does a DELETE request to /Users/{userId}/Images/{imageType}.

        Delete the user's image.

        Args:
            user_id (uuid|string): User Id.
            image_type (ImageTypeEnum): (Unused) Image type.
            index (int, optional): (Unused) Image index.

        Returns:
            void: Response from the API. Image deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_user_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_user_image.")
            _url_path = "/Users/{userId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {"index": index}
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info("Preparing and executing request for delete_user_image.")
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="delete_user_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_user_image.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User does not have permission to delete the image.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_user_image(
        self,
        user_id,
        image_type,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
        image_index=None,
    ):
        """Does a GET request to /Users/{userId}/Images/{imageType}.

        Get user profile image.

        Args:
            user_id (uuid|string): User id.
            image_type (ImageTypeEnum): Image type.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.
            image_index (int, optional): Image index.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_user_image called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_user_image.")
            _url_path = "/Users/{userId}/Images/{imageType}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
                "imageIndex": image_index,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_user_image.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info("Preparing and executing request for get_user_image.")
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_user_image")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_user_image.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_user_image_by_index(
        self,
        user_id,
        image_type,
        image_index,
        tag=None,
        format=None,
        max_width=None,
        max_height=None,
        percent_played=None,
        unplayed_count=None,
        width=None,
        height=None,
        quality=None,
        fill_width=None,
        fill_height=None,
        crop_whitespace=None,
        add_played_indicator=None,
        blur=None,
        background_color=None,
        foreground_layer=None,
    ):
        """Does a GET request to /Users/{userId}/Images/{imageType}/{imageIndex}.

        Get user profile image.

        Args:
            user_id (uuid|string): User id.
            image_type (ImageTypeEnum): Image type.
            image_index (int): Image index.
            tag (string, optional): Optional. Supply the cache tag from the
                item object to receive strong caching headers.
            format (ImageFormatEnum, optional): Determines the output format
                of the image - original,gif,jpg,png.
            max_width (int, optional): The maximum image width to return.
            max_height (int, optional): The maximum image height to return.
            percent_played (float, optional): Optional. Percent to render for
                the percent played overlay.
            unplayed_count (int, optional): Optional. Unplayed count overlay
                to render.
            width (int, optional): The fixed image width to return.
            height (int, optional): The fixed image height to return.
            quality (int, optional): Optional. Quality setting, from 0-100.
                Defaults to 90 and should suffice in most cases.
            fill_width (int, optional): Width of box to fill.
            fill_height (int, optional): Height of box to fill.
            crop_whitespace (bool, optional): Optional. Specify if whitespace
                should be cropped out of the image. True/False. If
                unspecified, whitespace will be cropped from logos and clear
                art.
            add_played_indicator (bool, optional): Optional. Add a played
                indicator.
            blur (int, optional): Optional. Blur image.
            background_color (string, optional): Optional. Apply a background
                color for transparent images.
            foreground_layer (string, optional): Optional. Apply a foreground
                layer on top of the image.

        Returns:
            mixed: Response from the API. Image stream returned.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("get_user_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for get_user_image_by_index.")
            _url_path = "/Users/{userId}/Images/{imageType}/{imageIndex}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "imageIndex": {"value": image_index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                "tag": tag,
                "format": format,
                "maxWidth": max_width,
                "maxHeight": max_height,
                "percentPlayed": percent_played,
                "unplayedCount": unplayed_count,
                "width": width,
                "height": height,
                "quality": quality,
                "fillWidth": fill_width,
                "fillHeight": fill_height,
                "cropWhitespace": crop_whitespace,
                "addPlayedIndicator": add_played_indicator,
                "blur": blur,
                "backgroundColor": background_color,
                "foregroundLayer": foreground_layer,
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for get_user_image_by_index.")
            _headers = {"accept": "application/json"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for get_user_image_by_index."
            )
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="get_user_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for get_user_image_by_index.")
            if _response.status_code == 404:
                raise ProblemDetailsException("Item not found.", _response)
            self.validate_response(_response)
            if (_response.text is not None) or (not str(_response.text)):
                decoded = APIHelper.json_deserialize(_response.text)

            return decoded

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def post_user_image_by_index(self, user_id, image_type, index, body=None):
        """Does a POST request to /Users/{userId}/Images/{imageType}/{index}.

        Sets the user image.

        Args:
            user_id (uuid|string): User Id.
            image_type (ImageTypeEnum): (Unused) Image type.
            index (int): (Unused) Image index.
            body (object, optional): TODO: type description here.

        Returns:
            void: Response from the API. Image updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("post_user_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for post_user_image_by_index.")
            _url_path = "/Users/{userId}/Images/{imageType}/{index}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "index": {"value": index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info("Preparing headers for post_user_image_by_index.")
            _headers = {"content-type": "application/json; charset=utf-8"}

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for post_user_image_by_index."
            )
            _request = self.config.http_client.post(
                _query_url, headers=_headers, parameters=APIHelper.json_serialize(body)
            )
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(_request, name="post_user_image_by_index")

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for post_user_image_by_index.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User does not have permission to delete the image.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_user_image_by_index(self, user_id, image_type, index):
        """Does a DELETE request to /Users/{userId}/Images/{imageType}/{index}.

        Delete the user's image.

        Args:
            user_id (uuid|string): User Id.
            image_type (ImageTypeEnum): (Unused) Image type.
            index (int): (Unused) Image index.

        Returns:
            void: Response from the API. Image deleted.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info("delete_user_image_by_index called.")

            # Prepare query URL
            self.logger.info("Preparing query URL for delete_user_image_by_index.")
            _url_path = "/Users/{userId}/Images/{imageType}/{index}"
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path,
                {
                    "userId": {"value": user_id, "encode": True},
                    "imageType": {"value": image_type, "encode": True},
                    "index": {"value": index, "encode": True},
                },
            )
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                "Preparing and executing request for delete_user_image_by_index."
            )
            _request = self.config.http_client.delete(_query_url)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, "global")

            _response = self.execute_request(
                _request, name="delete_user_image_by_index"
            )

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info("Validating response for delete_user_image_by_index.")
            if _response.status_code == 401:
                raise APIException("Unauthorized", _response)
            elif _response.status_code == 403:
                raise ProblemDetailsException(
                    "User does not have permission to delete the image.", _response
                )
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
