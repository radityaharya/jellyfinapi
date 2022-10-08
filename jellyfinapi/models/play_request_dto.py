# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlayRequestDto(object):

    """Implementation of the 'PlayRequestDto' model.

    Class PlayRequestDto.

    Attributes:
        playing_queue (list of uuid|string): Gets or sets the playing queue.
        playing_item_position (int): Gets or sets the position of the playing
            item in the queue.
        start_position_ticks (long|int): Gets or sets the start position
            ticks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "playing_queue": "PlayingQueue",
        "playing_item_position": "PlayingItemPosition",
        "start_position_ticks": "StartPositionTicks",
    }

    _optionals = [
        "playing_queue",
        "playing_item_position",
        "start_position_ticks",
    ]

    def __init__(
        self,
        playing_queue=APIHelper.SKIP,
        playing_item_position=APIHelper.SKIP,
        start_position_ticks=APIHelper.SKIP,
    ):
        """Constructor for the PlayRequestDto class"""

        # Initialize members of the class
        if playing_queue is not APIHelper.SKIP:
            self.playing_queue = playing_queue
        if playing_item_position is not APIHelper.SKIP:
            self.playing_item_position = playing_item_position
        if start_position_ticks is not APIHelper.SKIP:
            self.start_position_ticks = start_position_ticks

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

        playing_queue = (
            dictionary.get("PlayingQueue")
            if dictionary.get("PlayingQueue")
            else APIHelper.SKIP
        )
        playing_item_position = (
            dictionary.get("PlayingItemPosition")
            if dictionary.get("PlayingItemPosition")
            else APIHelper.SKIP
        )
        start_position_ticks = (
            dictionary.get("StartPositionTicks")
            if dictionary.get("StartPositionTicks")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(playing_queue, playing_item_position, start_position_ticks)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        playing_queue = XmlUtilities.list_from_xml_element(root, "PlayingQueue", str)
        playing_item_position = XmlUtilities.value_from_xml_element(
            root.find("PlayingItemPosition"), int
        )
        start_position_ticks = XmlUtilities.value_from_xml_element(
            root.find("StartPositionTicks"), int
        )

        return cls(playing_queue, playing_item_position, start_position_ticks)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.playing_queue, "PlayingQueue")
        XmlUtilities.add_as_subelement(
            root, self.playing_item_position, "PlayingItemPosition"
        )
        XmlUtilities.add_as_subelement(
            root, self.start_position_ticks, "StartPositionTicks"
        )
