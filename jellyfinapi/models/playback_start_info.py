# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.queue_item import QueueItem
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlaybackStartInfo(object):

    """Implementation of the 'PlaybackStartInfo' model.

    Class PlaybackStartInfo.

    Attributes:
        can_seek (bool): Gets or sets a value indicating whether this instance
            can seek.
        item (BaseItemDto): Gets or sets the item.
        item_id (uuid|string): Gets or sets the item identifier.
        session_id (string): Gets or sets the session id.
        media_source_id (string): Gets or sets the media version identifier.
        audio_stream_index (int): Gets or sets the index of the audio stream.
        subtitle_stream_index (int): Gets or sets the index of the subtitle
            stream.
        is_paused (bool): Gets or sets a value indicating whether this
            instance is paused.
        is_muted (bool): Gets or sets a value indicating whether this instance
            is muted.
        position_ticks (long|int): Gets or sets the position ticks.
        playback_start_time_ticks (long|int): TODO: type description here.
        volume_level (int): Gets or sets the volume level.
        brightness (int): TODO: type description here.
        aspect_ratio (string): TODO: type description here.
        play_method (PlayMethodEnum): Gets or sets the play method.
        live_stream_id (string): Gets or sets the live stream identifier.
        play_session_id (string): Gets or sets the play session identifier.
        repeat_mode (RepeatModeEnum): Gets or sets the repeat mode.
        now_playing_queue (list of QueueItem): TODO: type description here.
        playlist_item_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "can_seek": "CanSeek",
        "item": "Item",
        "item_id": "ItemId",
        "session_id": "SessionId",
        "media_source_id": "MediaSourceId",
        "audio_stream_index": "AudioStreamIndex",
        "subtitle_stream_index": "SubtitleStreamIndex",
        "is_paused": "IsPaused",
        "is_muted": "IsMuted",
        "position_ticks": "PositionTicks",
        "playback_start_time_ticks": "PlaybackStartTimeTicks",
        "volume_level": "VolumeLevel",
        "brightness": "Brightness",
        "aspect_ratio": "AspectRatio",
        "play_method": "PlayMethod",
        "live_stream_id": "LiveStreamId",
        "play_session_id": "PlaySessionId",
        "repeat_mode": "RepeatMode",
        "now_playing_queue": "NowPlayingQueue",
        "playlist_item_id": "PlaylistItemId",
    }

    _optionals = [
        "can_seek",
        "item",
        "item_id",
        "session_id",
        "media_source_id",
        "audio_stream_index",
        "subtitle_stream_index",
        "is_paused",
        "is_muted",
        "position_ticks",
        "playback_start_time_ticks",
        "volume_level",
        "brightness",
        "aspect_ratio",
        "play_method",
        "live_stream_id",
        "play_session_id",
        "repeat_mode",
        "now_playing_queue",
        "playlist_item_id",
    ]

    _nullables = [
        "item",
        "session_id",
        "media_source_id",
        "audio_stream_index",
        "subtitle_stream_index",
        "position_ticks",
        "playback_start_time_ticks",
        "volume_level",
        "brightness",
        "aspect_ratio",
        "live_stream_id",
        "play_session_id",
        "now_playing_queue",
        "playlist_item_id",
    ]

    def __init__(
        self,
        can_seek=APIHelper.SKIP,
        item=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        session_id=APIHelper.SKIP,
        media_source_id=APIHelper.SKIP,
        audio_stream_index=APIHelper.SKIP,
        subtitle_stream_index=APIHelper.SKIP,
        is_paused=APIHelper.SKIP,
        is_muted=APIHelper.SKIP,
        position_ticks=APIHelper.SKIP,
        playback_start_time_ticks=APIHelper.SKIP,
        volume_level=APIHelper.SKIP,
        brightness=APIHelper.SKIP,
        aspect_ratio=APIHelper.SKIP,
        play_method=APIHelper.SKIP,
        live_stream_id=APIHelper.SKIP,
        play_session_id=APIHelper.SKIP,
        repeat_mode=APIHelper.SKIP,
        now_playing_queue=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
    ):
        """Constructor for the PlaybackStartInfo class"""

        # Initialize members of the class
        if can_seek is not APIHelper.SKIP:
            self.can_seek = can_seek
        if item is not APIHelper.SKIP:
            self.item = item
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if session_id is not APIHelper.SKIP:
            self.session_id = session_id
        if media_source_id is not APIHelper.SKIP:
            self.media_source_id = media_source_id
        if audio_stream_index is not APIHelper.SKIP:
            self.audio_stream_index = audio_stream_index
        if subtitle_stream_index is not APIHelper.SKIP:
            self.subtitle_stream_index = subtitle_stream_index
        if is_paused is not APIHelper.SKIP:
            self.is_paused = is_paused
        if is_muted is not APIHelper.SKIP:
            self.is_muted = is_muted
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks
        if playback_start_time_ticks is not APIHelper.SKIP:
            self.playback_start_time_ticks = playback_start_time_ticks
        if volume_level is not APIHelper.SKIP:
            self.volume_level = volume_level
        if brightness is not APIHelper.SKIP:
            self.brightness = brightness
        if aspect_ratio is not APIHelper.SKIP:
            self.aspect_ratio = aspect_ratio
        if play_method is not APIHelper.SKIP:
            self.play_method = play_method
        if live_stream_id is not APIHelper.SKIP:
            self.live_stream_id = live_stream_id
        if play_session_id is not APIHelper.SKIP:
            self.play_session_id = play_session_id
        if repeat_mode is not APIHelper.SKIP:
            self.repeat_mode = repeat_mode
        if now_playing_queue is not APIHelper.SKIP:
            self.now_playing_queue = now_playing_queue
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id

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

        can_seek = (
            dictionary.get("CanSeek")
            if "CanSeek" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "Item" in dictionary.keys():
            item = (
                BaseItemDto.from_dictionary(dictionary.get("Item"))
                if dictionary.get("Item")
                else None
            )
        else:
            item = APIHelper.SKIP
        item_id = (
            dictionary.get("ItemId") if dictionary.get("ItemId") else APIHelper.SKIP
        )
        session_id = (
            dictionary.get("SessionId")
            if "SessionId" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_source_id = (
            dictionary.get("MediaSourceId")
            if "MediaSourceId" in dictionary.keys()
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
        position_ticks = (
            dictionary.get("PositionTicks")
            if "PositionTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        playback_start_time_ticks = (
            dictionary.get("PlaybackStartTimeTicks")
            if "PlaybackStartTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        volume_level = (
            dictionary.get("VolumeLevel")
            if "VolumeLevel" in dictionary.keys()
            else APIHelper.SKIP
        )
        brightness = (
            dictionary.get("Brightness")
            if "Brightness" in dictionary.keys()
            else APIHelper.SKIP
        )
        aspect_ratio = (
            dictionary.get("AspectRatio")
            if "AspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_method = (
            dictionary.get("PlayMethod")
            if dictionary.get("PlayMethod")
            else APIHelper.SKIP
        )
        live_stream_id = (
            dictionary.get("LiveStreamId")
            if "LiveStreamId" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_session_id = (
            dictionary.get("PlaySessionId")
            if "PlaySessionId" in dictionary.keys()
            else APIHelper.SKIP
        )
        repeat_mode = (
            dictionary.get("RepeatMode")
            if dictionary.get("RepeatMode")
            else APIHelper.SKIP
        )
        if "NowPlayingQueue" in dictionary.keys():
            now_playing_queue = (
                [
                    QueueItem.from_dictionary(x)
                    for x in dictionary.get("NowPlayingQueue")
                ]
                if dictionary.get("NowPlayingQueue")
                else None
            )
        else:
            now_playing_queue = APIHelper.SKIP
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if "PlaylistItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            can_seek,
            item,
            item_id,
            session_id,
            media_source_id,
            audio_stream_index,
            subtitle_stream_index,
            is_paused,
            is_muted,
            position_ticks,
            playback_start_time_ticks,
            volume_level,
            brightness,
            aspect_ratio,
            play_method,
            live_stream_id,
            play_session_id,
            repeat_mode,
            now_playing_queue,
            playlist_item_id,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        can_seek = XmlUtilities.value_from_xml_element(root.find("CanSeek"), bool)
        item = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
        )
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        session_id = XmlUtilities.value_from_xml_element(root.find("SessionId"), str)
        media_source_id = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceId"), str
        )
        audio_stream_index = XmlUtilities.value_from_xml_element(
            root.find("AudioStreamIndex"), int
        )
        subtitle_stream_index = XmlUtilities.value_from_xml_element(
            root.find("SubtitleStreamIndex"), int
        )
        is_paused = XmlUtilities.value_from_xml_element(root.find("IsPaused"), bool)
        is_muted = XmlUtilities.value_from_xml_element(root.find("IsMuted"), bool)
        position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PositionTicks"), int
        )
        playback_start_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("PlaybackStartTimeTicks"), int
        )
        volume_level = XmlUtilities.value_from_xml_element(
            root.find("VolumeLevel"), int
        )
        brightness = XmlUtilities.value_from_xml_element(root.find("Brightness"), int)
        aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("AspectRatio"), str
        )
        play_method = XmlUtilities.value_from_xml_element(root.find("PlayMethod"), str)
        live_stream_id = XmlUtilities.value_from_xml_element(
            root.find("LiveStreamId"), str
        )
        play_session_id = XmlUtilities.value_from_xml_element(
            root.find("PlaySessionId"), str
        )
        repeat_mode = XmlUtilities.value_from_xml_element(root.find("RepeatMode"), str)
        now_playing_queue = XmlUtilities.list_from_xml_element(
            root, "QueueItem", QueueItem
        )
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )

        return cls(
            can_seek,
            item,
            item_id,
            session_id,
            media_source_id,
            audio_stream_index,
            subtitle_stream_index,
            is_paused,
            is_muted,
            position_ticks,
            playback_start_time_ticks,
            volume_level,
            brightness,
            aspect_ratio,
            play_method,
            live_stream_id,
            play_session_id,
            repeat_mode,
            now_playing_queue,
            playlist_item_id,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.can_seek, "CanSeek")
        XmlUtilities.add_as_subelement(root, self.item, "BaseItemDto")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(root, self.session_id, "SessionId")
        XmlUtilities.add_as_subelement(root, self.media_source_id, "MediaSourceId")
        XmlUtilities.add_as_subelement(
            root, self.audio_stream_index, "AudioStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.subtitle_stream_index, "SubtitleStreamIndex"
        )
        XmlUtilities.add_as_subelement(root, self.is_paused, "IsPaused")
        XmlUtilities.add_as_subelement(root, self.is_muted, "IsMuted")
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
        XmlUtilities.add_as_subelement(
            root, self.playback_start_time_ticks, "PlaybackStartTimeTicks"
        )
        XmlUtilities.add_as_subelement(root, self.volume_level, "VolumeLevel")
        XmlUtilities.add_as_subelement(root, self.brightness, "Brightness")
        XmlUtilities.add_as_subelement(root, self.aspect_ratio, "AspectRatio")
        XmlUtilities.add_as_subelement(root, self.play_method, "PlayMethod")
        XmlUtilities.add_as_subelement(root, self.live_stream_id, "LiveStreamId")
        XmlUtilities.add_as_subelement(root, self.play_session_id, "PlaySessionId")
        XmlUtilities.add_as_subelement(root, self.repeat_mode, "RepeatMode")
        XmlUtilities.add_list_as_subelement(root, self.now_playing_queue, "QueueItem")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
