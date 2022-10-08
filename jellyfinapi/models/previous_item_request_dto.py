# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PreviousItemRequestDto(object):

    """Implementation of the 'PreviousItemRequestDto' model.

    Class PreviousItemRequestDto.

    Attributes:
        playlist_item_id (uuid|string): Gets or sets the playing item
            identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {"playlist_item_id": "PlaylistItemId"}

    _optionals = [
        "playlist_item_id",
    ]

    def __init__(self, playlist_item_id=APIHelper.SKIP):
        """Constructor for the PreviousItemRequestDto class"""

        # Initialize members of the class
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

        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if dictionary.get("PlaylistItemId")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(playlist_item_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )

        return cls(playlist_item_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
