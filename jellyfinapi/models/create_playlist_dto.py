# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CreatePlaylistDto(object):

    """Implementation of the 'CreatePlaylistDto' model.

    Create new playlist dto.

    Attributes:
        name (string): Gets or sets the name of the new playlist.
        ids (list of uuid|string): Gets or sets item ids to add to the
            playlist.
        user_id (uuid|string): Gets or sets the user id.
        media_type (string): Gets or sets the media type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "ids": "Ids",
        "user_id": "UserId",
        "media_type": "MediaType",
    }

    _optionals = [
        "name",
        "ids",
        "user_id",
        "media_type",
    ]

    _nullables = [
        "name",
        "user_id",
        "media_type",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        ids=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        media_type=APIHelper.SKIP,
    ):
        """Constructor for the CreatePlaylistDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if ids is not APIHelper.SKIP:
            self.ids = ids
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if media_type is not APIHelper.SKIP:
            self.media_type = media_type

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        ids = dictionary.get("Ids") if dictionary.get("Ids") else APIHelper.SKIP
        user_id = (
            dictionary.get("UserId")
            if "UserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_type = (
            dictionary.get("MediaType")
            if "MediaType" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, ids, user_id, media_type)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        ids = XmlUtilities.list_from_xml_element(root, "Ids", str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        media_type = XmlUtilities.value_from_xml_element(root.find("MediaType"), str)

        return cls(name, ids, user_id, media_type)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_list_as_subelement(root, self.ids, "Ids")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.media_type, "MediaType")
