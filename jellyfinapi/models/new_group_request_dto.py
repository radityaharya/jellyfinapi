# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NewGroupRequestDto(object):

    """Implementation of the 'NewGroupRequestDto' model.

    Class NewGroupRequestDto.

    Attributes:
        group_name (string): Gets or sets the group name.

    """

    # Create a mapping from Model property names to API property names
    _names = {"group_name": "GroupName"}

    _optionals = [
        "group_name",
    ]

    def __init__(self, group_name=APIHelper.SKIP):
        """Constructor for the NewGroupRequestDto class"""

        # Initialize members of the class
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name

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

        group_name = (
            dictionary.get("GroupName")
            if dictionary.get("GroupName")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(group_name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        group_name = XmlUtilities.value_from_xml_element(root.find("GroupName"), str)

        return cls(group_name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.group_name, "GroupName")
