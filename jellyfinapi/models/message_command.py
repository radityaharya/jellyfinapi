# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MessageCommand(object):

    """Implementation of the 'MessageCommand' model.

    TODO: type model description here.

    Attributes:
        header (string): TODO: type description here.
        text (string): TODO: type description here.
        timeout_ms (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"text": "Text", "header": "Header", "timeout_ms": "TimeoutMs"}

    _optionals = [
        "header",
        "timeout_ms",
    ]

    _nullables = [
        "header",
        "timeout_ms",
    ]

    def __init__(self, text=None, header=APIHelper.SKIP, timeout_ms=APIHelper.SKIP):
        """Constructor for the MessageCommand class"""

        # Initialize members of the class
        if header is not APIHelper.SKIP:
            self.header = header
        self.text = text
        if timeout_ms is not APIHelper.SKIP:
            self.timeout_ms = timeout_ms

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

        text = dictionary.get("Text") if dictionary.get("Text") else None
        header = (
            dictionary.get("Header")
            if "Header" in dictionary.keys()
            else APIHelper.SKIP
        )
        timeout_ms = (
            dictionary.get("TimeoutMs")
            if "TimeoutMs" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(text, header, timeout_ms)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        text = XmlUtilities.value_from_xml_element(root.find("Text"), str)
        header = XmlUtilities.value_from_xml_element(root.find("Header"), str)
        timeout_ms = XmlUtilities.value_from_xml_element(root.find("TimeoutMs"), int)

        return cls(text, header, timeout_ms)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.text, "Text")
        XmlUtilities.add_as_subelement(root, self.header, "Header")
        XmlUtilities.add_as_subelement(root, self.timeout_ms, "TimeoutMs")
