# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SpecialViewOptionDto(object):

    """Implementation of the 'SpecialViewOptionDto' model.

    Special view option dto.

    Attributes:
        name (string): Gets or sets view option name.
        id (string): Gets or sets view option id.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "id": "Id"}

    _optionals = [
        "name",
        "id",
    ]

    _nullables = [
        "name",
        "id",
    ]

    def __init__(self, name=APIHelper.SKIP, id=APIHelper.SKIP):
        """Constructor for the SpecialViewOptionDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if id is not APIHelper.SKIP:
            self.id = id

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
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name, id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)

        return cls(name, id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
