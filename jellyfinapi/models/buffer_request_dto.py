# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class BufferRequestDto(object):

    """Implementation of the 'BufferRequestDto' model.

    Class BufferRequestDto.

    Attributes:
        when (datetime): Gets or sets when the request has been made by the
            client.
        position_ticks (long|int): Gets or sets the position ticks.
        is_playing (bool): Gets or sets a value indicating whether the client
            playback is unpaused.
        playlist_item_id (uuid|string): Gets or sets the playlist item
            identifier of the playing item.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "when": "When",
        "position_ticks": "PositionTicks",
        "is_playing": "IsPlaying",
        "playlist_item_id": "PlaylistItemId",
    }

    _optionals = [
        "when",
        "position_ticks",
        "is_playing",
        "playlist_item_id",
    ]

    def __init__(
        self,
        when=APIHelper.SKIP,
        position_ticks=APIHelper.SKIP,
        is_playing=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
    ):
        """Constructor for the BufferRequestDto class"""

        # Initialize members of the class
        if when is not APIHelper.SKIP:
            self.when = APIHelper.RFC3339DateTime(when) if when else None
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks
        if is_playing is not APIHelper.SKIP:
            self.is_playing = is_playing
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id

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

        when = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("When")).datetime
            if dictionary.get("When")
            else APIHelper.SKIP
        )
        position_ticks = (
            dictionary.get("PositionTicks")
            if dictionary.get("PositionTicks")
            else APIHelper.SKIP
        )
        is_playing = (
            dictionary.get("IsPlaying")
            if "IsPlaying" in dictionary.keys()
            else APIHelper.SKIP
        )
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if dictionary.get("PlaylistItemId")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(when, position_ticks, is_playing, playlist_item_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        when = XmlUtilities.value_from_xml_element(
            root.find("When"), APIHelper.RFC3339DateTime
        )
        position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PositionTicks"), int
        )
        is_playing = XmlUtilities.value_from_xml_element(root.find("IsPlaying"), bool)
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )

        return cls(when, position_ticks, is_playing, playlist_item_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.when, "When")
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
        XmlUtilities.add_as_subelement(root, self.is_playing, "IsPlaying")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
