# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.device_profile import DeviceProfile
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class OpenLiveStreamDto(object):

    """Implementation of the 'OpenLiveStreamDto' model.

    Open live stream dto.

    Attributes:
        open_token (string): Gets or sets the open token.
        user_id (uuid|string): Gets or sets the user id.
        play_session_id (string): Gets or sets the play session id.
        max_streaming_bitrate (int): Gets or sets the max streaming bitrate.
        start_time_ticks (long|int): Gets or sets the start time in ticks.
        audio_stream_index (int): Gets or sets the audio stream index.
        subtitle_stream_index (int): Gets or sets the subtitle stream index.
        max_audio_channels (int): Gets or sets the max audio channels.
        item_id (uuid|string): Gets or sets the item id.
        enable_direct_play (bool): Gets or sets a value indicating whether to
            enable direct play.
        enable_direct_stream (bool): Gets or sets a value indicating whether
            to enale direct stream.
        device_profile (DeviceProfile): A
            MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata
            which determines which content a certain device is able to play.
            <br />  Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">co
            ntainers</see> and  <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs
            </see> (video and/or audio, including codec profiles and levels)
            the device is able to direct play (without transcoding or
            remuxing),  as well as which <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">
            containers/codecs to transcode to</see> in case it isn't.
        direct_play_protocols (list of MediaProtocolEnum): Gets or sets the
            device play protocols.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "open_token": "OpenToken",
        "user_id": "UserId",
        "play_session_id": "PlaySessionId",
        "max_streaming_bitrate": "MaxStreamingBitrate",
        "start_time_ticks": "StartTimeTicks",
        "audio_stream_index": "AudioStreamIndex",
        "subtitle_stream_index": "SubtitleStreamIndex",
        "max_audio_channels": "MaxAudioChannels",
        "item_id": "ItemId",
        "enable_direct_play": "EnableDirectPlay",
        "enable_direct_stream": "EnableDirectStream",
        "device_profile": "DeviceProfile",
        "direct_play_protocols": "DirectPlayProtocols",
    }

    _optionals = [
        "open_token",
        "user_id",
        "play_session_id",
        "max_streaming_bitrate",
        "start_time_ticks",
        "audio_stream_index",
        "subtitle_stream_index",
        "max_audio_channels",
        "item_id",
        "enable_direct_play",
        "enable_direct_stream",
        "device_profile",
        "direct_play_protocols",
    ]

    _nullables = [
        "open_token",
        "user_id",
        "play_session_id",
        "max_streaming_bitrate",
        "start_time_ticks",
        "audio_stream_index",
        "subtitle_stream_index",
        "max_audio_channels",
        "item_id",
        "enable_direct_play",
        "enable_direct_stream",
        "device_profile",
    ]

    def __init__(
        self,
        open_token=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        play_session_id=APIHelper.SKIP,
        max_streaming_bitrate=APIHelper.SKIP,
        start_time_ticks=APIHelper.SKIP,
        audio_stream_index=APIHelper.SKIP,
        subtitle_stream_index=APIHelper.SKIP,
        max_audio_channels=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        enable_direct_play=APIHelper.SKIP,
        enable_direct_stream=APIHelper.SKIP,
        device_profile=APIHelper.SKIP,
        direct_play_protocols=APIHelper.SKIP,
    ):
        """Constructor for the OpenLiveStreamDto class"""

        # Initialize members of the class
        if open_token is not APIHelper.SKIP:
            self.open_token = open_token
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if play_session_id is not APIHelper.SKIP:
            self.play_session_id = play_session_id
        if max_streaming_bitrate is not APIHelper.SKIP:
            self.max_streaming_bitrate = max_streaming_bitrate
        if start_time_ticks is not APIHelper.SKIP:
            self.start_time_ticks = start_time_ticks
        if audio_stream_index is not APIHelper.SKIP:
            self.audio_stream_index = audio_stream_index
        if subtitle_stream_index is not APIHelper.SKIP:
            self.subtitle_stream_index = subtitle_stream_index
        if max_audio_channels is not APIHelper.SKIP:
            self.max_audio_channels = max_audio_channels
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if enable_direct_play is not APIHelper.SKIP:
            self.enable_direct_play = enable_direct_play
        if enable_direct_stream is not APIHelper.SKIP:
            self.enable_direct_stream = enable_direct_stream
        if device_profile is not APIHelper.SKIP:
            self.device_profile = device_profile
        if direct_play_protocols is not APIHelper.SKIP:
            self.direct_play_protocols = direct_play_protocols

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

        open_token = (
            dictionary.get("OpenToken")
            if "OpenToken" in dictionary.keys()
            else APIHelper.SKIP
        )
        user_id = (
            dictionary.get("UserId")
            if "UserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_session_id = (
            dictionary.get("PlaySessionId")
            if "PlaySessionId" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_streaming_bitrate = (
            dictionary.get("MaxStreamingBitrate")
            if "MaxStreamingBitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        start_time_ticks = (
            dictionary.get("StartTimeTicks")
            if "StartTimeTicks" in dictionary.keys()
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
        max_audio_channels = (
            dictionary.get("MaxAudioChannels")
            if "MaxAudioChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        item_id = (
            dictionary.get("ItemId")
            if "ItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_direct_play = (
            dictionary.get("EnableDirectPlay")
            if "EnableDirectPlay" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_direct_stream = (
            dictionary.get("EnableDirectStream")
            if "EnableDirectStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "DeviceProfile" in dictionary.keys():
            device_profile = (
                DeviceProfile.from_dictionary(dictionary.get("DeviceProfile"))
                if dictionary.get("DeviceProfile")
                else None
            )
        else:
            device_profile = APIHelper.SKIP
        direct_play_protocols = (
            dictionary.get("DirectPlayProtocols")
            if dictionary.get("DirectPlayProtocols")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            open_token,
            user_id,
            play_session_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            item_id,
            enable_direct_play,
            enable_direct_stream,
            device_profile,
            direct_play_protocols,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        open_token = XmlUtilities.value_from_xml_element(root.find("OpenToken"), str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        play_session_id = XmlUtilities.value_from_xml_element(
            root.find("PlaySessionId"), str
        )
        max_streaming_bitrate = XmlUtilities.value_from_xml_element(
            root.find("MaxStreamingBitrate"), int
        )
        start_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("StartTimeTicks"), int
        )
        audio_stream_index = XmlUtilities.value_from_xml_element(
            root.find("AudioStreamIndex"), int
        )
        subtitle_stream_index = XmlUtilities.value_from_xml_element(
            root.find("SubtitleStreamIndex"), int
        )
        max_audio_channels = XmlUtilities.value_from_xml_element(
            root.find("MaxAudioChannels"), int
        )
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        enable_direct_play = XmlUtilities.value_from_xml_element(
            root.find("EnableDirectPlay"), bool
        )
        enable_direct_stream = XmlUtilities.value_from_xml_element(
            root.find("EnableDirectStream"), bool
        )
        device_profile = XmlUtilities.value_from_xml_element(
            root.find("DeviceProfile"), DeviceProfile
        )
        direct_play_protocols = XmlUtilities.list_from_xml_element(
            root, "DirectPlayProtocols", str
        )

        return cls(
            open_token,
            user_id,
            play_session_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            item_id,
            enable_direct_play,
            enable_direct_stream,
            device_profile,
            direct_play_protocols,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.open_token, "OpenToken")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.play_session_id, "PlaySessionId")
        XmlUtilities.add_as_subelement(
            root, self.max_streaming_bitrate, "MaxStreamingBitrate"
        )
        XmlUtilities.add_as_subelement(root, self.start_time_ticks, "StartTimeTicks")
        XmlUtilities.add_as_subelement(
            root, self.audio_stream_index, "AudioStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.subtitle_stream_index, "SubtitleStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_audio_channels, "MaxAudioChannels"
        )
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(
            root, self.enable_direct_play, "EnableDirectPlay"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_direct_stream, "EnableDirectStream"
        )
        XmlUtilities.add_as_subelement(root, self.device_profile, "DeviceProfile")
        XmlUtilities.add_list_as_subelement(
            root, self.direct_play_protocols, "DirectPlayProtocols"
        )
