# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SetRepeatModeRequestDto(object):

    """Implementation of the 'SetRepeatModeRequestDto' model.

    Class SetRepeatModeRequestDto.

    Attributes:
        mode (GroupRepeatModeEnum): Enum GroupRepeatMode.

    """

    # Create a mapping from Model property names to API property names
    _names = {"mode": "Mode"}

    _optionals = [
        "mode",
    ]

    def __init__(self, mode=APIHelper.SKIP):
        """Constructor for the SetRepeatModeRequestDto class"""

        # Initialize members of the class
        if mode is not APIHelper.SKIP:
            self.mode = mode

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

        mode = dictionary.get("Mode") if dictionary.get("Mode") else APIHelper.SKIP
        # Return an object of this model
        return cls(mode)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mode = XmlUtilities.value_from_xml_element(root.find("Mode"), str)

        return cls(mode)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mode, "Mode")
