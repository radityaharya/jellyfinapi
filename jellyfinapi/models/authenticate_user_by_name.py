# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AuthenticateUserByName(object):

    """Implementation of the 'AuthenticateUserByName' model.

    The authenticate user by name request body.

    Attributes:
        username (string): Gets or sets the username.
        pw (string): Gets or sets the plain text password.
        password (string): Gets or sets the sha1-hashed password.

    """

    # Create a mapping from Model property names to API property names
    _names = {"username": "Username", "pw": "Pw", "password": "Password"}

    _optionals = [
        "username",
        "pw",
        "password",
    ]

    _nullables = [
        "username",
        "pw",
        "password",
    ]

    def __init__(
        self, username=APIHelper.SKIP, pw=APIHelper.SKIP, password=APIHelper.SKIP
    ):
        """Constructor for the AuthenticateUserByName class"""

        # Initialize members of the class
        if username is not APIHelper.SKIP:
            self.username = username
        if pw is not APIHelper.SKIP:
            self.pw = pw
        if password is not APIHelper.SKIP:
            self.password = password

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

        username = (
            dictionary.get("Username")
            if "Username" in dictionary.keys()
            else APIHelper.SKIP
        )
        pw = dictionary.get("Pw") if "Pw" in dictionary.keys() else APIHelper.SKIP
        password = (
            dictionary.get("Password")
            if "Password" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(username, pw, password)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        username = XmlUtilities.value_from_xml_element(root.find("Username"), str)
        pw = XmlUtilities.value_from_xml_element(root.find("Pw"), str)
        password = XmlUtilities.value_from_xml_element(root.find("Password"), str)

        return cls(username, pw, password)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.username, "Username")
        XmlUtilities.add_as_subelement(root, self.pw, "Pw")
        XmlUtilities.add_as_subelement(root, self.password, "Password")
