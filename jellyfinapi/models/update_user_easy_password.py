# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UpdateUserEasyPassword(object):

    """Implementation of the 'UpdateUserEasyPassword' model.

    The update user easy password request body.

    Attributes:
        new_password (string): Gets or sets the new sha1-hashed password.
        new_pw (string): Gets or sets the new password.
        reset_password (bool): Gets or sets a value indicating whether to
            reset the password.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "new_password": "NewPassword",
        "new_pw": "NewPw",
        "reset_password": "ResetPassword",
    }

    _optionals = [
        "new_password",
        "new_pw",
        "reset_password",
    ]

    _nullables = [
        "new_password",
        "new_pw",
    ]

    def __init__(
        self,
        new_password=APIHelper.SKIP,
        new_pw=APIHelper.SKIP,
        reset_password=APIHelper.SKIP,
    ):
        """Constructor for the UpdateUserEasyPassword class"""

        # Initialize members of the class
        if new_password is not APIHelper.SKIP:
            self.new_password = new_password
        if new_pw is not APIHelper.SKIP:
            self.new_pw = new_pw
        if reset_password is not APIHelper.SKIP:
            self.reset_password = reset_password

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

        new_password = (
            dictionary.get("NewPassword")
            if "NewPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        new_pw = (
            dictionary.get("NewPw") if "NewPw" in dictionary.keys() else APIHelper.SKIP
        )
        reset_password = (
            dictionary.get("ResetPassword")
            if "ResetPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(new_password, new_pw, reset_password)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        new_password = XmlUtilities.value_from_xml_element(
            root.find("NewPassword"), str
        )
        new_pw = XmlUtilities.value_from_xml_element(root.find("NewPw"), str)
        reset_password = XmlUtilities.value_from_xml_element(
            root.find("ResetPassword"), bool
        )

        return cls(new_password, new_pw, reset_password)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.new_password, "NewPassword")
        XmlUtilities.add_as_subelement(root, self.new_pw, "NewPw")
        XmlUtilities.add_as_subelement(root, self.reset_password, "ResetPassword")
