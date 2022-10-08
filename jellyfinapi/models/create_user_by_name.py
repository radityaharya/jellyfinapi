# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CreateUserByName(object):

    """Implementation of the 'CreateUserByName' model.

    The create user by name request body.

    Attributes:
        name (string): Gets or sets the username.
        password (string): Gets or sets the password.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "password": "Password"}

    _optionals = [
        "name",
        "password",
    ]

    _nullables = [
        "name",
        "password",
    ]

    def __init__(self, name=APIHelper.SKIP, password=APIHelper.SKIP):
        """Constructor for the CreateUserByName class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        password = (
            dictionary.get("Password")
            if "Password" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, password)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        password = XmlUtilities.value_from_xml_element(root.find("Password"), str)

        return cls(name, password)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.password, "Password")
