# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class User(object):

    """Implementation of the 'User' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "name"}

    _optionals = [
        "name",
    ]

    _nullables = [
        "name",
    ]

    def __init__(self, name=APIHelper.SKIP):
        """Constructor for the User class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name

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

        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("name"), str)

        return cls(name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "name")
