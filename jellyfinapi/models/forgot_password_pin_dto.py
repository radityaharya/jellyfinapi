# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ForgotPasswordPinDto(object):

    """Implementation of the 'ForgotPasswordPinDto' model.

    Forgot Password Pin enter request body DTO.

    Attributes:
        pin (string): Gets or sets the entered pin to have the password
            reset.

    """

    # Create a mapping from Model property names to API property names
    _names = {"pin": "Pin"}

    def __init__(self, pin=None):
        """Constructor for the ForgotPasswordPinDto class"""

        # Initialize members of the class
        self.pin = pin

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

        pin = dictionary.get("Pin") if dictionary.get("Pin") else None
        # Return an object of this model
        return cls(pin)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        pin = XmlUtilities.value_from_xml_element(root.find("Pin"), str)

        return cls(pin)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.pin, "Pin")
