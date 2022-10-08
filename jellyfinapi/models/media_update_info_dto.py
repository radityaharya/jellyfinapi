# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_update_info_path_dto import MediaUpdateInfoPathDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaUpdateInfoDto(object):

    """Implementation of the 'MediaUpdateInfoDto' model.

    Media Update Info Dto.

    Attributes:
        updates (list of MediaUpdateInfoPathDto): Gets or sets the list of
            updates.

    """

    # Create a mapping from Model property names to API property names
    _names = {"updates": "Updates"}

    _optionals = [
        "updates",
    ]

    def __init__(self, updates=APIHelper.SKIP):
        """Constructor for the MediaUpdateInfoDto class"""

        # Initialize members of the class
        if updates is not APIHelper.SKIP:
            self.updates = updates

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

        updates = None
        if dictionary.get("Updates") is not None:
            updates = [
                MediaUpdateInfoPathDto.from_dictionary(x)
                for x in dictionary.get("Updates")
            ]
        else:
            updates = APIHelper.SKIP
        # Return an object of this model
        return cls(updates)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        updates = XmlUtilities.list_from_xml_element(
            root, "MediaUpdateInfoPathDto", MediaUpdateInfoPathDto
        )

        return cls(updates)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.updates, "MediaUpdateInfoPathDto"
        )
