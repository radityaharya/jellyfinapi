# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PinRedeemResult(object):

    """Implementation of the 'PinRedeemResult' model.

    TODO: type model description here.

    Attributes:
        success (bool): Gets or sets a value indicating whether this
            MediaBrowser.Model.Users.PinRedeemResult is success.
        users_reset (list of string): Gets or sets the users reset.

    """

    # Create a mapping from Model property names to API property names
    _names = {"success": "Success", "users_reset": "UsersReset"}

    _optionals = [
        "success",
        "users_reset",
    ]

    def __init__(self, success=APIHelper.SKIP, users_reset=APIHelper.SKIP):
        """Constructor for the PinRedeemResult class"""

        # Initialize members of the class
        if success is not APIHelper.SKIP:
            self.success = success
        if users_reset is not APIHelper.SKIP:
            self.users_reset = users_reset

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

        success = (
            dictionary.get("Success")
            if "Success" in dictionary.keys()
            else APIHelper.SKIP
        )
        users_reset = (
            dictionary.get("UsersReset")
            if dictionary.get("UsersReset")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(success, users_reset)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        success = XmlUtilities.value_from_xml_element(root.find("Success"), bool)
        users_reset = XmlUtilities.list_from_xml_element(root, "UsersReset", str)

        return cls(success, users_reset)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.success, "Success")
        XmlUtilities.add_list_as_subelement(root, self.users_reset, "UsersReset")
