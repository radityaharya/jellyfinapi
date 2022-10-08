# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class IgnoreWaitRequestDto(object):

    """Implementation of the 'IgnoreWaitRequestDto' model.

    Class IgnoreWaitRequestDto.

    Attributes:
        ignore_wait (bool): Gets or sets a value indicating whether the client
            should be ignored.

    """

    # Create a mapping from Model property names to API property names
    _names = {"ignore_wait": "IgnoreWait"}

    _optionals = [
        "ignore_wait",
    ]

    def __init__(self, ignore_wait=APIHelper.SKIP):
        """Constructor for the IgnoreWaitRequestDto class"""

        # Initialize members of the class
        if ignore_wait is not APIHelper.SKIP:
            self.ignore_wait = ignore_wait

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

        ignore_wait = (
            dictionary.get("IgnoreWait")
            if "IgnoreWait" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(ignore_wait)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        ignore_wait = XmlUtilities.value_from_xml_element(root.find("IgnoreWait"), bool)

        return cls(ignore_wait)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.ignore_wait, "IgnoreWait")
