# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlayerStateInfo(object):

    """Implementation of the 'PlayerStateInfo' model.

    TODO: type model description here.

    Attributes:
        position_ticks (long|int): Gets or sets the now playing position
            ticks.
        can_seek (bool): Gets or sets a value indicating whether this instance
            can seek.
        is_paused (bool): Gets or sets a value indicating whether this
            instance is paused.
        is_muted (bool): Gets or sets a value indicating whether this instance
            is muted.
        volume_level (int): Gets or sets the volume level.
        audio_stream_index (int): Gets or sets the index of the now playing
            audio stream.
        subtitle_stream_index (int): Gets or sets the index of the now playing
            subtitle stream.
        media_source_id (string): Gets or sets the now playing media version
            identifier.
        play_method (PlayMethodEnum): Gets or sets the play method.
        repeat_mode (RepeatModeEnum): Gets or sets the repeat mode.
        live_stream_id (string): Gets or sets the now playing live stream
            identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "position_ticks": "PositionTicks",
        "can_seek": "CanSeek",
        "is_paused": "IsPaused",
        "is_muted": "IsMuted",
        "volume_level": "VolumeLevel",
        "audio_stream_index": "AudioStreamIndex",
        "subtitle_stream_index": "SubtitleStreamIndex",
        "media_source_id": "MediaSourceId",
        "play_method": "PlayMethod",
        "repeat_mode": "RepeatMode",
        "live_stream_id": "LiveStreamId",
    }

    _optionals = [
        "position_ticks",
        "can_seek",
        "is_paused",
        "is_muted",
        "volume_level",
        "audio_stream_index",
        "subtitle_stream_index",
        "media_source_id",
        "play_method",
        "repeat_mode",
        "live_stream_id",
    ]

    _nullables = [
        "position_ticks",
        "volume_level",
        "audio_stream_index",
        "subtitle_stream_index",
        "media_source_id",
        "play_method",
        "live_stream_id",
    ]

    def __init__(
        self,
        position_ticks=APIHelper.SKIP,
        can_seek=APIHelper.SKIP,
        is_paused=APIHelper.SKIP,
        is_muted=APIHelper.SKIP,
        volume_level=APIHelper.SKIP,
        audio_stream_index=APIHelper.SKIP,
        subtitle_stream_index=APIHelper.SKIP,
        media_source_id=APIHelper.SKIP,
        play_method=APIHelper.SKIP,
        repeat_mode=APIHelper.SKIP,
        live_stream_id=APIHelper.SKIP,
    ):
        """Constructor for the PlayerStateInfo class"""

        # Initialize members of the class
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks
        if can_seek is not APIHelper.SKIP:
            self.can_seek = can_seek
        if is_paused is not APIHelper.SKIP:
            self.is_paused = is_paused
        if is_muted is not APIHelper.SKIP:
            self.is_muted = is_muted
        if volume_level is not APIHelper.SKIP:
            self.volume_level = volume_level
        if audio_stream_index is not APIHelper.SKIP:
            self.audio_stream_index = audio_stream_index
        if subtitle_stream_index is not APIHelper.SKIP:
            self.subtitle_stream_index = subtitle_stream_index
        if media_source_id is not APIHelper.SKIP:
            self.media_source_id = media_source_id
        if play_method is not APIHelper.SKIP:
            self.play_method = play_method
        if repeat_mode is not APIHelper.SKIP:
            self.repeat_mode = repeat_mode
        if live_stream_id is not APIHelper.SKIP:
            self.live_stream_id = live_stream_id

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
            if "PositionTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_seek = (
            dictionary.get("CanSeek")
            if "CanSeek" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_paused = (
            dictionary.get("IsPaused")
            if "IsPaused" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_muted = (
            dictionary.get("IsMuted")
            if "IsMuted" in dictionary.keys()
            else APIHelper.SKIP
        )
        volume_level = (
            dictionary.get("VolumeLevel")
            if "VolumeLevel" in dictionary.keys()
            else APIHelper.SKIP
        )
        audio_stream_index = (
            dictionary.get("AudioStreamIndex")
            if "AudioStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        subtitle_stream_index = (
            dictionary.get("SubtitleStreamIndex")
            if "SubtitleStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_source_id = (
            dictionary.get("MediaSourceId")
            if "MediaSourceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_method = (
            dictionary.get("PlayMethod")
            if "PlayMethod" in dictionary.keys()
            else APIHelper.SKIP
        )
        repeat_mode = (
            dictionary.get("RepeatMode")
            if dictionary.get("RepeatMode")
            else APIHelper.SKIP
        )
        live_stream_id = (
            dictionary.get("LiveStreamId")
            if "LiveStreamId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            position_ticks,
            can_seek,
            is_paused,
            is_muted,
            volume_level,
            audio_stream_index,
            subtitle_stream_index,
            media_source_id,
            play_method,
            repeat_mode,
            live_stream_id,
        )

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
        can_seek = XmlUtilities.value_from_xml_element(root.find("CanSeek"), bool)
        is_paused = XmlUtilities.value_from_xml_element(root.find("IsPaused"), bool)
        is_muted = XmlUtilities.value_from_xml_element(root.find("IsMuted"), bool)
        volume_level = XmlUtilities.value_from_xml_element(
            root.find("VolumeLevel"), int
        )
        audio_stream_index = XmlUtilities.value_from_xml_element(
            root.find("AudioStreamIndex"), int
        )
        subtitle_stream_index = XmlUtilities.value_from_xml_element(
            root.find("SubtitleStreamIndex"), int
        )
        media_source_id = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceId"), str
        )
        play_method = XmlUtilities.value_from_xml_element(root.find("PlayMethod"), str)
        repeat_mode = XmlUtilities.value_from_xml_element(root.find("RepeatMode"), str)
        live_stream_id = XmlUtilities.value_from_xml_element(
            root.find("LiveStreamId"), str
        )

        return cls(
            position_ticks,
            can_seek,
            is_paused,
            is_muted,
            volume_level,
            audio_stream_index,
            subtitle_stream_index,
            media_source_id,
            play_method,
            repeat_mode,
            live_stream_id,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
        XmlUtilities.add_as_subelement(root, self.can_seek, "CanSeek")
        XmlUtilities.add_as_subelement(root, self.is_paused, "IsPaused")
        XmlUtilities.add_as_subelement(root, self.is_muted, "IsMuted")
        XmlUtilities.add_as_subelement(root, self.volume_level, "VolumeLevel")
        XmlUtilities.add_as_subelement(
            root, self.audio_stream_index, "AudioStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.subtitle_stream_index, "SubtitleStreamIndex"
        )
        XmlUtilities.add_as_subelement(root, self.media_source_id, "MediaSourceId")
        XmlUtilities.add_as_subelement(root, self.play_method, "PlayMethod")
        XmlUtilities.add_as_subelement(root, self.repeat_mode, "RepeatMode")
        XmlUtilities.add_as_subelement(root, self.live_stream_id, "LiveStreamId")
