# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PingRequestDto(object):

    """Implementation of the 'PingRequestDto' model.

    Class PingRequestDto.

    Attributes:
        ping (long|int): Gets or sets the ping time.

    """

    # Create a mapping from Model property names to API property names
    _names = {"ping": "Ping"}

    _optionals = [
        "ping",
    ]

    def __init__(self, ping=APIHelper.SKIP):
        """Constructor for the PingRequestDto class"""

        # Initialize members of the class
        if ping is not APIHelper.SKIP:
            self.ping = ping

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

        ping = dictionary.get("Ping") if dictionary.get("Ping") else APIHelper.SKIP
        # Return an object of this model
        return cls(ping)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        ping = XmlUtilities.value_from_xml_element(root.find("Ping"), int)

        return cls(ping)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.ping, "Ping")
