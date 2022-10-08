# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlayRequest(object):

    """Implementation of the 'PlayRequest' model.

    Class PlayRequest.

    Attributes:
        item_ids (list of uuid|string): Gets or sets the item ids.
        start_position_ticks (long|int): Gets or sets the start position ticks
            that the first item should be played at.
        play_command (PlayCommandEnum): Gets or sets the play command.
        controlling_user_id (uuid|string): Gets or sets the controlling user
            identifier.
        subtitle_stream_index (int): TODO: type description here.
        audio_stream_index (int): TODO: type description here.
        media_source_id (string): TODO: type description here.
        start_index (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item_ids": "ItemIds",
        "start_position_ticks": "StartPositionTicks",
        "play_command": "PlayCommand",
        "controlling_user_id": "ControllingUserId",
        "subtitle_stream_index": "SubtitleStreamIndex",
        "audio_stream_index": "AudioStreamIndex",
        "media_source_id": "MediaSourceId",
        "start_index": "StartIndex",
    }

    _optionals = [
        "item_ids",
        "start_position_ticks",
        "play_command",
        "controlling_user_id",
        "subtitle_stream_index",
        "audio_stream_index",
        "media_source_id",
        "start_index",
    ]

    _nullables = [
        "item_ids",
        "start_position_ticks",
        "subtitle_stream_index",
        "audio_stream_index",
        "media_source_id",
        "start_index",
    ]

    def __init__(
        self,
        item_ids=APIHelper.SKIP,
        start_position_ticks=APIHelper.SKIP,
        play_command=APIHelper.SKIP,
        controlling_user_id=APIHelper.SKIP,
        subtitle_stream_index=APIHelper.SKIP,
        audio_stream_index=APIHelper.SKIP,
        media_source_id=APIHelper.SKIP,
        start_index=APIHelper.SKIP,
    ):
        """Constructor for the PlayRequest class"""

        # Initialize members of the class
        if item_ids is not APIHelper.SKIP:
            self.item_ids = item_ids
        if start_position_ticks is not APIHelper.SKIP:
            self.start_position_ticks = start_position_ticks
        if play_command is not APIHelper.SKIP:
            self.play_command = play_command
        if controlling_user_id is not APIHelper.SKIP:
            self.controlling_user_id = controlling_user_id
        if subtitle_stream_index is not APIHelper.SKIP:
            self.subtitle_stream_index = subtitle_stream_index
        if audio_stream_index is not APIHelper.SKIP:
            self.audio_stream_index = audio_stream_index
        if media_source_id is not APIHelper.SKIP:
            self.media_source_id = media_source_id
        if start_index is not APIHelper.SKIP:
            self.start_index = start_index

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

        item_ids = (
            dictionary.get("ItemIds")
            if "ItemIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        start_position_ticks = (
            dictionary.get("StartPositionTicks")
            if "StartPositionTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_command = (
            dictionary.get("PlayCommand")
            if dictionary.get("PlayCommand")
            else APIHelper.SKIP
        )
        controlling_user_id = (
            dictionary.get("ControllingUserId")
            if dictionary.get("ControllingUserId")
            else APIHelper.SKIP
        )
        subtitle_stream_index = (
            dictionary.get("SubtitleStreamIndex")
            if "SubtitleStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        audio_stream_index = (
            dictionary.get("AudioStreamIndex")
            if "AudioStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_source_id = (
            dictionary.get("MediaSourceId")
            if "MediaSourceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        start_index = (
            dictionary.get("StartIndex")
            if "StartIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            item_ids,
            start_position_ticks,
            play_command,
            controlling_user_id,
            subtitle_stream_index,
            audio_stream_index,
            media_source_id,
            start_index,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        item_ids = XmlUtilities.list_from_xml_element(root, "ItemIds", str)
        start_position_ticks = XmlUtilities.value_from_xml_element(
            root.find("StartPositionTicks"), int
        )
        play_command = XmlUtilities.value_from_xml_element(
            root.find("PlayCommand"), str
        )
        controlling_user_id = XmlUtilities.value_from_xml_element(
            root.find("ControllingUserId"), str
        )
        subtitle_stream_index = XmlUtilities.value_from_xml_element(
            root.find("SubtitleStreamIndex"), int
        )
        audio_stream_index = XmlUtilities.value_from_xml_element(
            root.find("AudioStreamIndex"), int
        )
        media_source_id = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceId"), str
        )
        start_index = XmlUtilities.value_from_xml_element(root.find("StartIndex"), int)

        return cls(
            item_ids,
            start_position_ticks,
            play_command,
            controlling_user_id,
            subtitle_stream_index,
            audio_stream_index,
            media_source_id,
            start_index,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.item_ids, "ItemIds")
        XmlUtilities.add_as_subelement(
            root, self.start_position_ticks, "StartPositionTicks"
        )
        XmlUtilities.add_as_subelement(root, self.play_command, "PlayCommand")
        XmlUtilities.add_as_subelement(
            root, self.controlling_user_id, "ControllingUserId"
        )
        XmlUtilities.add_as_subelement(
            root, self.subtitle_stream_index, "SubtitleStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.audio_stream_index, "AudioStreamIndex"
        )
        XmlUtilities.add_as_subelement(root, self.media_source_id, "MediaSourceId")
        XmlUtilities.add_as_subelement(root, self.start_index, "StartIndex")
