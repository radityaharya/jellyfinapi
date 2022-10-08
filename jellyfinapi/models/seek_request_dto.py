# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SeekRequestDto(object):

    """Implementation of the 'SeekRequestDto' model.

    Class SeekRequestDto.

    Attributes:
        position_ticks (long|int): Gets or sets the position ticks.

    """

    # Create a mapping from Model property names to API property names
    _names = {"position_ticks": "PositionTicks"}

    _optionals = [
        "position_ticks",
    ]

    def __init__(self, position_ticks=APIHelper.SKIP):
        """Constructor for the SeekRequestDto class"""

        # Initialize members of the class
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks

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

        position_ticks = (
            dictionary.get("PositionTicks")
            if dictionary.get("PositionTicks")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(position_ticks)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PositionTicks"), int
        )

        return cls(position_ticks)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
