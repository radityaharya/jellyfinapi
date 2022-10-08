# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SendCommand(object):

    """Implementation of the 'SendCommand' model.

    Class SendCommand.

    Attributes:
        group_id (uuid|string): Gets the group identifier.
        playlist_item_id (uuid|string): Gets the playlist identifier of the
            playing item.
        when (datetime): Gets or sets the UTC time when to execute the
            command.
        position_ticks (long|int): Gets the position ticks.
        command (SendCommandTypeEnum): Gets the command.
        emitted_at (datetime): Gets the UTC time when this command has been
            emitted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_id": "GroupId",
        "playlist_item_id": "PlaylistItemId",
        "when": "When",
        "position_ticks": "PositionTicks",
        "command": "Command",
        "emitted_at": "EmittedAt",
    }

    _optionals = [
        "group_id",
        "playlist_item_id",
        "when",
        "position_ticks",
        "command",
        "emitted_at",
    ]

    _nullables = [
        "position_ticks",
    ]

    def __init__(
        self,
        group_id=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
        when=APIHelper.SKIP,
        position_ticks=APIHelper.SKIP,
        command=APIHelper.SKIP,
        emitted_at=APIHelper.SKIP,
    ):
        """Constructor for the SendCommand class"""

        # Initialize members of the class
        if group_id is not APIHelper.SKIP:
            self.group_id = group_id
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id
        if when is not APIHelper.SKIP:
            self.when = APIHelper.RFC3339DateTime(when) if when else None
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks
        if command is not APIHelper.SKIP:
            self.command = command
        if emitted_at is not APIHelper.SKIP:
            self.emitted_at = (
                APIHelper.RFC3339DateTime(emitted_at) if emitted_at else None
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

        group_id = (
            dictionary.get("GroupId") if dictionary.get("GroupId") else APIHelper.SKIP
        )
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if dictionary.get("PlaylistItemId")
            else APIHelper.SKIP
        )
        when = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("When")).datetime
            if dictionary.get("When")
            else APIHelper.SKIP
        )
        position_ticks = (
            dictionary.get("PositionTicks")
            if "PositionTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        command = (
            dictionary.get("Command") if dictionary.get("Command") else APIHelper.SKIP
        )
        emitted_at = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("EmittedAt")).datetime
            if dictionary.get("EmittedAt")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            group_id, playlist_item_id, when, position_ticks, command, emitted_at
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        group_id = XmlUtilities.value_from_xml_element(root.find("GroupId"), str)
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )
        when = XmlUtilities.value_from_xml_element(
            root.find("When"), APIHelper.RFC3339DateTime
        )
        position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PositionTicks"), int
        )
        command = XmlUtilities.value_from_xml_element(root.find("Command"), str)
        emitted_at = XmlUtilities.value_from_xml_element(
            root.find("EmittedAt"), APIHelper.RFC3339DateTime
        )

        return cls(
            group_id, playlist_item_id, when, position_ticks, command, emitted_at
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.group_id, "GroupId")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
        XmlUtilities.add_as_subelement(root, self.when, "When")
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
        XmlUtilities.add_as_subelement(root, self.command, "Command")
        XmlUtilities.add_as_subelement(root, self.emitted_at, "EmittedAt")
