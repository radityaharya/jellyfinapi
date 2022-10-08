# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LoginInfoInput(object):

    """Implementation of the 'LoginInfoInput' model.

    TODO: type model description here.

    Attributes:
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        custom_api_key (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username": "Username",
        "password": "Password",
        "custom_api_key": "CustomApiKey",
    }

    _optionals = [
        "custom_api_key",
    ]

    def __init__(self, username=None, password=None, custom_api_key=APIHelper.SKIP):
        """Constructor for the LoginInfoInput class"""

        # Initialize members of the class
        self.username = username
        self.password = password
        if custom_api_key is not APIHelper.SKIP:
            self.custom_api_key = custom_api_key

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

        username = dictionary.get("Username") if dictionary.get("Username") else None
        password = dictionary.get("Password") if dictionary.get("Password") else None
        custom_api_key = (
            dictionary.get("CustomApiKey")
            if dictionary.get("CustomApiKey")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(username, password, custom_api_key)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        username = XmlUtilities.value_from_xml_element(root.find("Username"), str)
        password = XmlUtilities.value_from_xml_element(root.find("Password"), str)
        custom_api_key = XmlUtilities.value_from_xml_element(
            root.find("CustomApiKey"), str
        )

        return cls(username, password, custom_api_key)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.username, "Username")
        XmlUtilities.add_as_subelement(root, self.password, "Password")
        XmlUtilities.add_as_subelement(root, self.custom_api_key, "CustomApiKey")
