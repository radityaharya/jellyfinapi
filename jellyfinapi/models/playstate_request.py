# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlaystateRequest(object):

    """Implementation of the 'PlaystateRequest' model.

    TODO: type model description here.

    Attributes:
        command (PlaystateCommandEnum): Enum PlaystateCommand.
        seek_position_ticks (long|int): TODO: type description here.
        controlling_user_id (string): Gets or sets the controlling user
            identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "command": "Command",
        "seek_position_ticks": "SeekPositionTicks",
        "controlling_user_id": "ControllingUserId",
    }

    _optionals = [
        "command",
        "seek_position_ticks",
        "controlling_user_id",
    ]

    _nullables = [
        "seek_position_ticks",
        "controlling_user_id",
    ]

    def __init__(
        self,
        command=APIHelper.SKIP,
        seek_position_ticks=APIHelper.SKIP,
        controlling_user_id=APIHelper.SKIP,
    ):
        """Constructor for the PlaystateRequest class"""

        # Initialize members of the class
        if command is not APIHelper.SKIP:
            self.command = command
        if seek_position_ticks is not APIHelper.SKIP:
            self.seek_position_ticks = seek_position_ticks
        if controlling_user_id is not APIHelper.SKIP:
            self.controlling_user_id = controlling_user_id

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

        command = (
            dictionary.get("Command") if dictionary.get("Command") else APIHelper.SKIP
        )
        seek_position_ticks = (
            dictionary.get("SeekPositionTicks")
            if "SeekPositionTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        controlling_user_id = (
            dictionary.get("ControllingUserId")
            if "ControllingUserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(command, seek_position_ticks, controlling_user_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        command = XmlUtilities.value_from_xml_element(root.find("Command"), str)
        seek_position_ticks = XmlUtilities.value_from_xml_element(
            root.find("SeekPositionTicks"), int
        )
        controlling_user_id = XmlUtilities.value_from_xml_element(
            root.find("ControllingUserId"), str
        )

        return cls(command, seek_position_ticks, controlling_user_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.command, "Command")
        XmlUtilities.add_as_subelement(
            root, self.seek_position_ticks, "SeekPositionTicks"
        )
        XmlUtilities.add_as_subelement(
            root, self.controlling_user_id, "ControllingUserId"
        )
