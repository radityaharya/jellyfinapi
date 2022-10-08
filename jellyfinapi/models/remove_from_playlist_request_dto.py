# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RemoveFromPlaylistRequestDto(object):

    """Implementation of the 'RemoveFromPlaylistRequestDto' model.

    Class RemoveFromPlaylistRequestDto.

    Attributes:
        playlist_item_ids (list of uuid|string): Gets or sets the playlist
            identifiers ot the items. Ignored when clearing the playlist.
        clear_playlist (bool): Gets or sets a value indicating whether the
            entire playlist should be cleared.
        clear_playing_item (bool): Gets or sets a value indicating whether the
            playing item should be removed as well. Used only when clearing
            the playlist.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "playlist_item_ids": "PlaylistItemIds",
        "clear_playlist": "ClearPlaylist",
        "clear_playing_item": "ClearPlayingItem",
    }

    _optionals = [
        "playlist_item_ids",
        "clear_playlist",
        "clear_playing_item",
    ]

    def __init__(
        self,
        playlist_item_ids=APIHelper.SKIP,
        clear_playlist=APIHelper.SKIP,
        clear_playing_item=APIHelper.SKIP,
    ):
        """Constructor for the RemoveFromPlaylistRequestDto class"""

        # Initialize members of the class
        if playlist_item_ids is not APIHelper.SKIP:
            self.playlist_item_ids = playlist_item_ids
        if clear_playlist is not APIHelper.SKIP:
            self.clear_playlist = clear_playlist
        if clear_playing_item is not APIHelper.SKIP:
            self.clear_playing_item = clear_playing_item

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

        playlist_item_ids = (
            dictionary.get("PlaylistItemIds")
            if dictionary.get("PlaylistItemIds")
            else APIHelper.SKIP
        )
        clear_playlist = (
            dictionary.get("ClearPlaylist")
            if "ClearPlaylist" in dictionary.keys()
            else APIHelper.SKIP
        )
        clear_playing_item = (
            dictionary.get("ClearPlayingItem")
            if "ClearPlayingItem" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(playlist_item_ids, clear_playlist, clear_playing_item)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        playlist_item_ids = XmlUtilities.list_from_xml_element(
            root, "PlaylistItemIds", str
        )
        clear_playlist = XmlUtilities.value_from_xml_element(
            root.find("ClearPlaylist"), bool
        )
        clear_playing_item = XmlUtilities.value_from_xml_element(
            root.find("ClearPlayingItem"), bool
        )

        return cls(playlist_item_ids, clear_playlist, clear_playing_item)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.playlist_item_ids, "PlaylistItemIds"
        )
        XmlUtilities.add_as_subelement(root, self.clear_playlist, "ClearPlaylist")
        XmlUtilities.add_as_subelement(
            root, self.clear_playing_item, "ClearPlayingItem"
        )
