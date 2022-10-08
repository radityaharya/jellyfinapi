# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ForgotPasswordResult(object):

    """Implementation of the 'ForgotPasswordResult' model.

    TODO: type model description here.

    Attributes:
        action (ForgotPasswordActionEnum): Gets or sets the action.
        pin_file (string): Gets or sets the pin file.
        pin_expiration_date (datetime): Gets or sets the pin expiration date.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action": "Action",
        "pin_file": "PinFile",
        "pin_expiration_date": "PinExpirationDate",
    }

    _optionals = [
        "action",
        "pin_file",
        "pin_expiration_date",
    ]

    _nullables = [
        "pin_file",
        "pin_expiration_date",
    ]

    def __init__(
        self,
        action=APIHelper.SKIP,
        pin_file=APIHelper.SKIP,
        pin_expiration_date=APIHelper.SKIP,
    ):
        """Constructor for the ForgotPasswordResult class"""

        # Initialize members of the class
        if action is not APIHelper.SKIP:
            self.action = action
        if pin_file is not APIHelper.SKIP:
            self.pin_file = pin_file
        if pin_expiration_date is not APIHelper.SKIP:
            self.pin_expiration_date = (
                APIHelper.RFC3339DateTime(pin_expiration_date)
                if pin_expiration_date
                else None
            )

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

        action = (
            dictionary.get("Action") if dictionary.get("Action") else APIHelper.SKIP
        )
        pin_file = (
            dictionary.get("PinFile")
            if "PinFile" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "PinExpirationDate" in dictionary.keys():
            pin_expiration_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("PinExpirationDate")
                ).datetime
                if dictionary.get("PinExpirationDate")
                else None
            )
        else:
            pin_expiration_date = APIHelper.SKIP
        # Return an object of this model
        return cls(action, pin_file, pin_expiration_date)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        action = XmlUtilities.value_from_xml_element(root.find("Action"), str)
        pin_file = XmlUtilities.value_from_xml_element(root.find("PinFile"), str)
        pin_expiration_date = XmlUtilities.value_from_xml_element(
            root.find("PinExpirationDate"), APIHelper.RFC3339DateTime
        )

        return cls(action, pin_file, pin_expiration_date)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.action, "Action")
        XmlUtilities.add_as_subelement(root, self.pin_file, "PinFile")
        XmlUtilities.add_as_subelement(
            root, self.pin_expiration_date, "PinExpirationDate"
        )
