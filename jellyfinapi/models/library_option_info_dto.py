# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LibraryOptionInfoDto(object):

    """Implementation of the 'LibraryOptionInfoDto' model.

    Library option info dto.

    Attributes:
        name (string): Gets or sets name.
        default_enabled (bool): Gets or sets a value indicating whether
            default enabled.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "default_enabled": "DefaultEnabled"}

    _optionals = [
        "name",
        "default_enabled",
    ]

    _nullables = [
        "name",
    ]

    def __init__(self, name=APIHelper.SKIP, default_enabled=APIHelper.SKIP):
        """Constructor for the LibraryOptionInfoDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if default_enabled is not APIHelper.SKIP:
            self.default_enabled = default_enabled

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
        default_enabled = (
            dictionary.get("DefaultEnabled")
            if "DefaultEnabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, default_enabled)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        default_enabled = XmlUtilities.value_from_xml_element(
            root.find("DefaultEnabled"), bool
        )

        return cls(name, default_enabled)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.default_enabled, "DefaultEnabled")
