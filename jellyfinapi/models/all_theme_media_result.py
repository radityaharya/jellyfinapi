# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.theme_media_result import ThemeMediaResult
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AllThemeMediaResult(object):

    """Implementation of the 'AllThemeMediaResult' model.

    TODO: type model description here.

    Attributes:
        theme_videos_result (ThemeMediaResult): Class ThemeMediaResult.
        theme_songs_result (ThemeMediaResult): Class ThemeMediaResult.
        soundtrack_songs_result (ThemeMediaResult): Class ThemeMediaResult.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "theme_videos_result": "ThemeVideosResult",
        "theme_songs_result": "ThemeSongsResult",
        "soundtrack_songs_result": "SoundtrackSongsResult",
    }

    _optionals = [
        "theme_videos_result",
        "theme_songs_result",
        "soundtrack_songs_result",
    ]

    _nullables = [
        "theme_videos_result",
        "theme_songs_result",
        "soundtrack_songs_result",
    ]

    def __init__(
        self,
        theme_videos_result=APIHelper.SKIP,
        theme_songs_result=APIHelper.SKIP,
        soundtrack_songs_result=APIHelper.SKIP,
    ):
        """Constructor for the AllThemeMediaResult class"""

        # Initialize members of the class
        if theme_videos_result is not APIHelper.SKIP:
            self.theme_videos_result = theme_videos_result
        if theme_songs_result is not APIHelper.SKIP:
            self.theme_songs_result = theme_songs_result
        if soundtrack_songs_result is not APIHelper.SKIP:
            self.soundtrack_songs_result = soundtrack_songs_result

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

        if "ThemeVideosResult" in dictionary.keys():
            theme_videos_result = (
                ThemeMediaResult.from_dictionary(dictionary.get("ThemeVideosResult"))
                if dictionary.get("ThemeVideosResult")
                else None
            )
        else:
            theme_videos_result = APIHelper.SKIP
        if "ThemeSongsResult" in dictionary.keys():
            theme_songs_result = (
                ThemeMediaResult.from_dictionary(dictionary.get("ThemeSongsResult"))
                if dictionary.get("ThemeSongsResult")
                else None
            )
        else:
            theme_songs_result = APIHelper.SKIP
        if "SoundtrackSongsResult" in dictionary.keys():
            soundtrack_songs_result = (
                ThemeMediaResult.from_dictionary(
                    dictionary.get("SoundtrackSongsResult")
                )
                if dictionary.get("SoundtrackSongsResult")
                else None
            )
        else:
            soundtrack_songs_result = APIHelper.SKIP
        # Return an object of this model
        return cls(theme_videos_result, theme_songs_result, soundtrack_songs_result)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        theme_videos_result = XmlUtilities.value_from_xml_element(
            root.find("ThemeMediaResult"), ThemeMediaResult
        )
        theme_songs_result = XmlUtilities.value_from_xml_element(
            root.find("ThemeMediaResult"), ThemeMediaResult
        )
        soundtrack_songs_result = XmlUtilities.value_from_xml_element(
            root.find("ThemeMediaResult"), ThemeMediaResult
        )

        return cls(theme_videos_result, theme_songs_result, soundtrack_songs_result)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.theme_videos_result, "ThemeMediaResult"
        )
        XmlUtilities.add_as_subelement(
            root, self.theme_songs_result, "ThemeMediaResult"
        )
        XmlUtilities.add_as_subelement(
            root, self.soundtrack_songs_result, "ThemeMediaResult"
        )
