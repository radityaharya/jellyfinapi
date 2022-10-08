# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CodeStatusResponse(object):

    """Implementation of the 'CodeStatusResponse' model.

    TODO: type model description here.

    Attributes:
        result (string): TODO: type description here.
        message (string): TODO: type description here.
        access_token (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"result": "result", "message": "message", "access_token": "access_token"}

    _optionals = [
        "result",
        "message",
        "access_token",
    ]

    _nullables = [
        "result",
        "message",
        "access_token",
    ]

    def __init__(
        self, result=APIHelper.SKIP, message=APIHelper.SKIP, access_token=APIHelper.SKIP
    ):
        """Constructor for the CodeStatusResponse class"""

        # Initialize members of the class
        if result is not APIHelper.SKIP:
            self.result = result
        if message is not APIHelper.SKIP:
            self.message = message
        if access_token is not APIHelper.SKIP:
            self.access_token = access_token

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

        result = (
            dictionary.get("result")
            if "result" in dictionary.keys()
            else APIHelper.SKIP
        )
        message = (
            dictionary.get("message")
            if "message" in dictionary.keys()
            else APIHelper.SKIP
        )
        access_token = (
            dictionary.get("access_token")
            if "access_token" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(result, message, access_token)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        result = XmlUtilities.value_from_xml_element(root.find("result"), str)
        message = XmlUtilities.value_from_xml_element(root.find("message"), str)
        access_token = XmlUtilities.value_from_xml_element(
            root.find("access_token"), str
        )

        return cls(result, message, access_token)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.result, "result")
        XmlUtilities.add_as_subelement(root, self.message, "message")
        XmlUtilities.add_as_subelement(root, self.access_token, "access_token")
