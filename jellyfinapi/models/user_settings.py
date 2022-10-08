# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.user import User
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UserSettings(object):

    """Implementation of the 'UserSettings' model.

    TODO: type model description here.

    Attributes:
        user (User): TODO: type description here.
        error (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"user": "user", "error": "error"}

    _optionals = [
        "user",
        "error",
    ]

    _nullables = [
        "user",
        "error",
    ]

    def __init__(self, user=APIHelper.SKIP, error=APIHelper.SKIP):
        """Constructor for the UserSettings class"""

        # Initialize members of the class
        if user is not APIHelper.SKIP:
            self.user = user
        if error is not APIHelper.SKIP:
            self.error = error

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

        if "user" in dictionary.keys():
            user = (
                User.from_dictionary(dictionary.get("user"))
                if dictionary.get("user")
                else None
            )
        else:
            user = APIHelper.SKIP
        error = (
            dictionary.get("error") if "error" in dictionary.keys() else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(user, error)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        user = XmlUtilities.value_from_xml_element(root.find("User"), User)
        error = XmlUtilities.value_from_xml_element(root.find("error"), str)

        return cls(user, error)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.user, "User")
        XmlUtilities.add_as_subelement(root, self.error, "error")
