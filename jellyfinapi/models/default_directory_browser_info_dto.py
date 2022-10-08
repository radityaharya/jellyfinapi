# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DefaultDirectoryBrowserInfoDto(object):

    """Implementation of the 'DefaultDirectoryBrowserInfoDto' model.

    Default directory browser info.

    Attributes:
        path (string): Gets or sets the path.

    """

    # Create a mapping from Model property names to API property names
    _names = {"path": "Path"}

    _optionals = [
        "path",
    ]

    _nullables = [
        "path",
    ]

    def __init__(self, path=APIHelper.SKIP):
        """Constructor for the DefaultDirectoryBrowserInfoDto class"""

        # Initialize members of the class
        if path is not APIHelper.SKIP:
            self.path = path

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

        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(path)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)

        return cls(path)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.path, "Path")
