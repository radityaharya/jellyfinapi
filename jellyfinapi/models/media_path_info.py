# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaPathInfo(object):

    """Implementation of the 'MediaPathInfo' model.

    TODO: type model description here.

    Attributes:
        path (string): TODO: type description here.
        network_path (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"path": "Path", "network_path": "NetworkPath"}

    _optionals = [
        "path",
        "network_path",
    ]

    _nullables = [
        "network_path",
    ]

    def __init__(self, path=APIHelper.SKIP, network_path=APIHelper.SKIP):
        """Constructor for the MediaPathInfo class"""

        # Initialize members of the class
        if path is not APIHelper.SKIP:
            self.path = path
        if network_path is not APIHelper.SKIP:
            self.network_path = network_path

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

        path = dictionary.get("Path") if dictionary.get("Path") else APIHelper.SKIP
        network_path = (
            dictionary.get("NetworkPath")
            if "NetworkPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(path, network_path)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        network_path = XmlUtilities.value_from_xml_element(
            root.find("NetworkPath"), str
        )

        return cls(path, network_path)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.network_path, "NetworkPath")
