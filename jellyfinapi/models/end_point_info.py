# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class EndPointInfo(object):

    """Implementation of the 'EndPointInfo' model.

    TODO: type model description here.

    Attributes:
        is_local (bool): TODO: type description here.
        is_in_network (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"is_local": "IsLocal", "is_in_network": "IsInNetwork"}

    _optionals = [
        "is_local",
        "is_in_network",
    ]

    def __init__(self, is_local=APIHelper.SKIP, is_in_network=APIHelper.SKIP):
        """Constructor for the EndPointInfo class"""

        # Initialize members of the class
        if is_local is not APIHelper.SKIP:
            self.is_local = is_local
        if is_in_network is not APIHelper.SKIP:
            self.is_in_network = is_in_network

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

        is_local = (
            dictionary.get("IsLocal")
            if "IsLocal" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_in_network = (
            dictionary.get("IsInNetwork")
            if "IsInNetwork" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(is_local, is_in_network)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        is_local = XmlUtilities.value_from_xml_element(root.find("IsLocal"), bool)
        is_in_network = XmlUtilities.value_from_xml_element(
            root.find("IsInNetwork"), bool
        )

        return cls(is_local, is_in_network)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.is_local, "IsLocal")
        XmlUtilities.add_as_subelement(root, self.is_in_network, "IsInNetwork")
