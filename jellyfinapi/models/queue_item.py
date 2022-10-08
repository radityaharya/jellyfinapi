# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QueueItem(object):

    """Implementation of the 'QueueItem' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        playlist_item_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "playlist_item_id": "PlaylistItemId"}

    _optionals = [
        "id",
        "playlist_item_id",
    ]

    _nullables = [
        "playlist_item_id",
    ]

    def __init__(self, id=APIHelper.SKIP, playlist_item_id=APIHelper.SKIP):
        """Constructor for the QueueItem class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
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

        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if "PlaylistItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(id, playlist_item_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )

        return cls(id, playlist_item_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
