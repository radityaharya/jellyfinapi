# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ForgotPasswordDto(object):

    """Implementation of the 'ForgotPasswordDto' model.

    Forgot Password request body DTO.

    Attributes:
        entered_username (string): Gets or sets the entered username to have
            its password reset.

    """

    # Create a mapping from Model property names to API property names
    _names = {"entered_username": "EnteredUsername"}

    def __init__(self, entered_username=None):
        """Constructor for the ForgotPasswordDto class"""

        # Initialize members of the class
        self.entered_username = entered_username

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

        entered_username = (
            dictionary.get("EnteredUsername")
            if dictionary.get("EnteredUsername")
            else None
        )
        # Return an object of this model
        return cls(entered_username)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        entered_username = XmlUtilities.value_from_xml_element(
            root.find("EnteredUsername"), str
        )

        return cls(entered_username)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.entered_username, "EnteredUsername")
