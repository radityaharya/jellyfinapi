# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ServerDiscoveryInfo(object):

    """Implementation of the 'ServerDiscoveryInfo' model.

    The server discovery info model.

    Attributes:
        address (string): Gets the address.
        id (string): Gets the server identifier.
        name (string): Gets the name.
        endpoint_address (string): Gets the endpoint address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": "Address",
        "id": "Id",
        "name": "Name",
        "endpoint_address": "EndpointAddress",
    }

    _optionals = [
        "address",
        "id",
        "name",
        "endpoint_address",
    ]

    _nullables = [
        "endpoint_address",
    ]

    def __init__(
        self,
        address=APIHelper.SKIP,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        endpoint_address=APIHelper.SKIP,
    ):
        """Constructor for the ServerDiscoveryInfo class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if endpoint_address is not APIHelper.SKIP:
            self.endpoint_address = endpoint_address

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

        address = (
            dictionary.get("Address") if dictionary.get("Address") else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        endpoint_address = (
            dictionary.get("EndpointAddress")
            if "EndpointAddress" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(address, id, name, endpoint_address)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        address = XmlUtilities.value_from_xml_element(root.find("Address"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        endpoint_address = XmlUtilities.value_from_xml_element(
            root.find("EndpointAddress"), str
        )

        return cls(address, id, name, endpoint_address)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.address, "Address")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.endpoint_address, "EndpointAddress")
