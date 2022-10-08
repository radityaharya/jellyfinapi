# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SessionUserInfo(object):

    """Implementation of the 'SessionUserInfo' model.

    Class SessionUserInfo.

    Attributes:
        user_id (uuid|string): Gets or sets the user identifier.
        user_name (string): Gets or sets the name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {"user_id": "UserId", "user_name": "UserName"}

    _optionals = [
        "user_id",
        "user_name",
    ]

    _nullables = [
        "user_name",
    ]

    def __init__(self, user_id=APIHelper.SKIP, user_name=APIHelper.SKIP):
        """Constructor for the SessionUserInfo class"""

        # Initialize members of the class
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if user_name is not APIHelper.SKIP:
            self.user_name = user_name

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

        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        user_name = (
            dictionary.get("UserName")
            if "UserName" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(user_id, user_name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        user_name = XmlUtilities.value_from_xml_element(root.find("UserName"), str)

        return cls(user_id, user_name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.user_name, "UserName")
