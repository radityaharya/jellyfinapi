# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.notification_option import NotificationOption
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationOptions(object):

    """Implementation of the 'NotificationOptions' model.

    TODO: type model description here.

    Attributes:
        options (list of NotificationOption): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"options": "Options"}

    _optionals = [
        "options",
    ]

    _nullables = [
        "options",
    ]

    def __init__(self, options=APIHelper.SKIP):
        """Constructor for the NotificationOptions class"""

        # Initialize members of the class
        if options is not APIHelper.SKIP:
            self.options = options

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

        if "Options" in dictionary.keys():
            options = (
                [
                    NotificationOption.from_dictionary(x)
                    for x in dictionary.get("Options")
                ]
                if dictionary.get("Options")
                else None
            )
        else:
            options = APIHelper.SKIP
        # Return an object of this model
        return cls(options)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        options = XmlUtilities.list_from_xml_element(
            root, "NotificationOption", NotificationOption
        )

        return cls(options)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.options, "NotificationOption")
