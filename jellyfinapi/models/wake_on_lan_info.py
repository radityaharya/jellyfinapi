# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class WakeOnLanInfo(object):

    """Implementation of the 'WakeOnLanInfo' model.

    Provides the MAC address and port for wake-on-LAN functionality.

    Attributes:
        mac_address (string): Gets the MAC address of the device.
        port (int): Gets or sets the wake-on-LAN port.

    """

    # Create a mapping from Model property names to API property names
    _names = {"mac_address": "MacAddress", "port": "Port"}

    _optionals = [
        "mac_address",
        "port",
    ]

    _nullables = [
        "mac_address",
    ]

    def __init__(self, mac_address=APIHelper.SKIP, port=APIHelper.SKIP):
        """Constructor for the WakeOnLanInfo class"""

        # Initialize members of the class
        if mac_address is not APIHelper.SKIP:
            self.mac_address = mac_address
        if port is not APIHelper.SKIP:
            self.port = port

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

        mac_address = (
            dictionary.get("MacAddress")
            if "MacAddress" in dictionary.keys()
            else APIHelper.SKIP
        )
        port = dictionary.get("Port") if dictionary.get("Port") else APIHelper.SKIP
        # Return an object of this model
        return cls(mac_address, port)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mac_address = XmlUtilities.value_from_xml_element(root.find("MacAddress"), str)
        port = XmlUtilities.value_from_xml_element(root.find("Port"), int)

        return cls(mac_address, port)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mac_address, "MacAddress")
        XmlUtilities.add_as_subelement(root, self.port, "Port")
