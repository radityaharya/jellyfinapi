# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.queue_item import QueueItem
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlaybackStopInfo(object):

    """Implementation of the 'PlaybackStopInfo' model.

    Class PlaybackStopInfo.

    Attributes:
        item (BaseItemDto): Gets or sets the item.
        item_id (uuid|string): Gets or sets the item identifier.
        session_id (string): Gets or sets the session id.
        media_source_id (string): Gets or sets the media version identifier.
        position_ticks (long|int): Gets or sets the position ticks.
        live_stream_id (string): Gets or sets the live stream identifier.
        play_session_id (string): Gets or sets the play session identifier.
        failed (bool): Gets or sets a value indicating whether this
            MediaBrowser.Model.Session.PlaybackStopInfo is failed.
        next_media_type (string): TODO: type description here.
        playlist_item_id (string): TODO: type description here.
        now_playing_queue (list of QueueItem): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item": "Item",
        "item_id": "ItemId",
        "session_id": "SessionId",
        "media_source_id": "MediaSourceId",
        "position_ticks": "PositionTicks",
        "live_stream_id": "LiveStreamId",
        "play_session_id": "PlaySessionId",
        "failed": "Failed",
        "next_media_type": "NextMediaType",
        "playlist_item_id": "PlaylistItemId",
        "now_playing_queue": "NowPlayingQueue",
    }

    _optionals = [
        "item",
        "item_id",
        "session_id",
        "media_source_id",
        "position_ticks",
        "live_stream_id",
        "play_session_id",
        "failed",
        "next_media_type",
        "playlist_item_id",
        "now_playing_queue",
    ]

    _nullables = [
        "item",
        "session_id",
        "media_source_id",
        "position_ticks",
        "live_stream_id",
        "play_session_id",
        "next_media_type",
        "playlist_item_id",
        "now_playing_queue",
    ]

    def __init__(
        self,
        item=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        session_id=APIHelper.SKIP,
        media_source_id=APIHelper.SKIP,
        position_ticks=APIHelper.SKIP,
        live_stream_id=APIHelper.SKIP,
        play_session_id=APIHelper.SKIP,
        failed=APIHelper.SKIP,
        next_media_type=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
        now_playing_queue=APIHelper.SKIP,
    ):
        """Constructor for the PlaybackStopInfo class"""

        # Initialize members of the class
        if item is not APIHelper.SKIP:
            self.item = item
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if session_id is not APIHelper.SKIP:
            self.session_id = session_id
        if media_source_id is not APIHelper.SKIP:
            self.media_source_id = media_source_id
        if position_ticks is not APIHelper.SKIP:
            self.position_ticks = position_ticks
        if live_stream_id is not APIHelper.SKIP:
            self.live_stream_id = live_stream_id
        if play_session_id is not APIHelper.SKIP:
            self.play_session_id = play_session_id
        if failed is not APIHelper.SKIP:
            self.failed = failed
        if next_media_type is not APIHelper.SKIP:
            self.next_media_type = next_media_type
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id
        if now_playing_queue is not APIHelper.SKIP:
            self.now_playing_queue = now_playing_queue

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
        position_ticks = (
            dictionary.get("PositionTicks")
            if "PositionTicks" in dictionary.keys()
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
        failed = (
            dictionary.get("Failed")
            if "Failed" in dictionary.keys()
            else APIHelper.SKIP
        )
        next_media_type = (
            dictionary.get("NextMediaType")
            if "NextMediaType" in dictionary.keys()
            else APIHelper.SKIP
        )
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if "PlaylistItemId" in dictionary.keys()
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
        # Return an object of this model
        return cls(
            item,
            item_id,
            session_id,
            media_source_id,
            position_ticks,
            live_stream_id,
            play_session_id,
            failed,
            next_media_type,
            playlist_item_id,
            now_playing_queue,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        item = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
        )
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        session_id = XmlUtilities.value_from_xml_element(root.find("SessionId"), str)
        media_source_id = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceId"), str
        )
        position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PositionTicks"), int
        )
        live_stream_id = XmlUtilities.value_from_xml_element(
            root.find("LiveStreamId"), str
        )
        play_session_id = XmlUtilities.value_from_xml_element(
            root.find("PlaySessionId"), str
        )
        failed = XmlUtilities.value_from_xml_element(root.find("Failed"), bool)
        next_media_type = XmlUtilities.value_from_xml_element(
            root.find("NextMediaType"), str
        )
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )
        now_playing_queue = XmlUtilities.list_from_xml_element(
            root, "QueueItem", QueueItem
        )

        return cls(
            item,
            item_id,
            session_id,
            media_source_id,
            position_ticks,
            live_stream_id,
            play_session_id,
            failed,
            next_media_type,
            playlist_item_id,
            now_playing_queue,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.item, "BaseItemDto")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(root, self.session_id, "SessionId")
        XmlUtilities.add_as_subelement(root, self.media_source_id, "MediaSourceId")
        XmlUtilities.add_as_subelement(root, self.position_ticks, "PositionTicks")
        XmlUtilities.add_as_subelement(root, self.live_stream_id, "LiveStreamId")
        XmlUtilities.add_as_subelement(root, self.play_session_id, "PlaySessionId")
        XmlUtilities.add_as_subelement(root, self.failed, "Failed")
        XmlUtilities.add_as_subelement(root, self.next_media_type, "NextMediaType")
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
        XmlUtilities.add_list_as_subelement(root, self.now_playing_queue, "QueueItem")
