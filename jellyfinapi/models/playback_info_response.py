# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_source_info import MediaSourceInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlaybackInfoResponse(object):

    """Implementation of the 'PlaybackInfoResponse' model.

    Class PlaybackInfoResponse.

    Attributes:
        media_sources (list of MediaSourceInfo): Gets or sets the media
            sources.
        play_session_id (string): Gets or sets the play session identifier.
        error_code (PlaybackErrorCodeEnum): Gets or sets the error code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "media_sources": "MediaSources",
        "play_session_id": "PlaySessionId",
        "error_code": "ErrorCode",
    }

    _optionals = [
        "media_sources",
        "play_session_id",
        "error_code",
    ]

    _nullables = [
        "play_session_id",
        "error_code",
    ]

    def __init__(
        self,
        media_sources=APIHelper.SKIP,
        play_session_id=APIHelper.SKIP,
        error_code=APIHelper.SKIP,
    ):
        """Constructor for the PlaybackInfoResponse class"""

        # Initialize members of the class
        if media_sources is not APIHelper.SKIP:
            self.media_sources = media_sources
        if play_session_id is not APIHelper.SKIP:
            self.play_session_id = play_session_id
        if error_code is not APIHelper.SKIP:
            self.error_code = error_code

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        media_sources = None
        if dictionary.get("MediaSources") is not None:
            media_sources = [
                MediaSourceInfo.from_dictionary(x)
                for x in dictionary.get("MediaSources")
            ]
        else:
            media_sources = APIHelper.SKIP
        play_session_id = (
            dictionary.get("PlaySessionId")
            if "PlaySessionId" in dictionary.keys()
            else APIHelper.SKIP
        )
        error_code = (
            dictionary.get("ErrorCode")
            if "ErrorCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(media_sources, play_session_id, error_code)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        media_sources = XmlUtilities.list_from_xml_element(
            root, "MediaSourceInfo", MediaSourceInfo
        )
        play_session_id = XmlUtilities.value_from_xml_element(
            root.find("PlaySessionId"), str
        )
        error_code = XmlUtilities.value_from_xml_element(root.find("ErrorCode"), str)

        return cls(media_sources, play_session_id, error_code)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.media_sources, "MediaSourceInfo")
        XmlUtilities.add_as_subelement(root, self.play_session_id, "PlaySessionId")
        XmlUtilities.add_as_subelement(root, self.error_code, "ErrorCode")
