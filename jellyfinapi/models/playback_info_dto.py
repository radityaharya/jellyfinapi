# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.device_profile import DeviceProfile
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PlaybackInfoDto(object):

    """Implementation of the 'PlaybackInfoDto' model.

    Plabyback info dto.

    Attributes:
        user_id (uuid|string): Gets or sets the playback userId.
        max_streaming_bitrate (int): Gets or sets the max streaming bitrate.
        start_time_ticks (long|int): Gets or sets the start time in ticks.
        audio_stream_index (int): Gets or sets the audio stream index.
        subtitle_stream_index (int): Gets or sets the subtitle stream index.
        max_audio_channels (int): Gets or sets the max audio channels.
        media_source_id (string): Gets or sets the media source id.
        live_stream_id (string): Gets or sets the live stream id.
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
        enable_direct_play (bool): Gets or sets a value indicating whether to
            enable direct play.
        enable_direct_stream (bool): Gets or sets a value indicating whether
            to enable direct stream.
        enable_transcoding (bool): Gets or sets a value indicating whether to
            enable transcoding.
        allow_video_stream_copy (bool): Gets or sets a value indicating
            whether to enable video stream copy.
        allow_audio_stream_copy (bool): Gets or sets a value indicating
            whether to allow audio stream copy.
        auto_open_live_stream (bool): Gets or sets a value indicating whether
            to auto open the live stream.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": "UserId",
        "max_streaming_bitrate": "MaxStreamingBitrate",
        "start_time_ticks": "StartTimeTicks",
        "audio_stream_index": "AudioStreamIndex",
        "subtitle_stream_index": "SubtitleStreamIndex",
        "max_audio_channels": "MaxAudioChannels",
        "media_source_id": "MediaSourceId",
        "live_stream_id": "LiveStreamId",
        "device_profile": "DeviceProfile",
        "enable_direct_play": "EnableDirectPlay",
        "enable_direct_stream": "EnableDirectStream",
        "enable_transcoding": "EnableTranscoding",
        "allow_video_stream_copy": "AllowVideoStreamCopy",
        "allow_audio_stream_copy": "AllowAudioStreamCopy",
        "auto_open_live_stream": "AutoOpenLiveStream",
    }

    _optionals = [
        "user_id",
        "max_streaming_bitrate",
        "start_time_ticks",
        "audio_stream_index",
        "subtitle_stream_index",
        "max_audio_channels",
        "media_source_id",
        "live_stream_id",
        "device_profile",
        "enable_direct_play",
        "enable_direct_stream",
        "enable_transcoding",
        "allow_video_stream_copy",
        "allow_audio_stream_copy",
        "auto_open_live_stream",
    ]

    _nullables = [
        "user_id",
        "max_streaming_bitrate",
        "start_time_ticks",
        "audio_stream_index",
        "subtitle_stream_index",
        "max_audio_channels",
        "media_source_id",
        "live_stream_id",
        "device_profile",
        "enable_direct_play",
        "enable_direct_stream",
        "enable_transcoding",
        "allow_video_stream_copy",
        "allow_audio_stream_copy",
        "auto_open_live_stream",
    ]

    def __init__(
        self,
        user_id=APIHelper.SKIP,
        max_streaming_bitrate=APIHelper.SKIP,
        start_time_ticks=APIHelper.SKIP,
        audio_stream_index=APIHelper.SKIP,
        subtitle_stream_index=APIHelper.SKIP,
        max_audio_channels=APIHelper.SKIP,
        media_source_id=APIHelper.SKIP,
        live_stream_id=APIHelper.SKIP,
        device_profile=APIHelper.SKIP,
        enable_direct_play=APIHelper.SKIP,
        enable_direct_stream=APIHelper.SKIP,
        enable_transcoding=APIHelper.SKIP,
        allow_video_stream_copy=APIHelper.SKIP,
        allow_audio_stream_copy=APIHelper.SKIP,
        auto_open_live_stream=APIHelper.SKIP,
    ):
        """Constructor for the PlaybackInfoDto class"""

        # Initialize members of the class
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
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
        if media_source_id is not APIHelper.SKIP:
            self.media_source_id = media_source_id
        if live_stream_id is not APIHelper.SKIP:
            self.live_stream_id = live_stream_id
        if device_profile is not APIHelper.SKIP:
            self.device_profile = device_profile
        if enable_direct_play is not APIHelper.SKIP:
            self.enable_direct_play = enable_direct_play
        if enable_direct_stream is not APIHelper.SKIP:
            self.enable_direct_stream = enable_direct_stream
        if enable_transcoding is not APIHelper.SKIP:
            self.enable_transcoding = enable_transcoding
        if allow_video_stream_copy is not APIHelper.SKIP:
            self.allow_video_stream_copy = allow_video_stream_copy
        if allow_audio_stream_copy is not APIHelper.SKIP:
            self.allow_audio_stream_copy = allow_audio_stream_copy
        if auto_open_live_stream is not APIHelper.SKIP:
            self.auto_open_live_stream = auto_open_live_stream

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

        user_id = (
            dictionary.get("UserId")
            if "UserId" in dictionary.keys()
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
        media_source_id = (
            dictionary.get("MediaSourceId")
            if "MediaSourceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        live_stream_id = (
            dictionary.get("LiveStreamId")
            if "LiveStreamId" in dictionary.keys()
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
        enable_transcoding = (
            dictionary.get("EnableTranscoding")
            if "EnableTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_video_stream_copy = (
            dictionary.get("AllowVideoStreamCopy")
            if "AllowVideoStreamCopy" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_audio_stream_copy = (
            dictionary.get("AllowAudioStreamCopy")
            if "AllowAudioStreamCopy" in dictionary.keys()
            else APIHelper.SKIP
        )
        auto_open_live_stream = (
            dictionary.get("AutoOpenLiveStream")
            if "AutoOpenLiveStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            user_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            media_source_id,
            live_stream_id,
            device_profile,
            enable_direct_play,
            enable_direct_stream,
            enable_transcoding,
            allow_video_stream_copy,
            allow_audio_stream_copy,
            auto_open_live_stream,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
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
        media_source_id = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceId"), str
        )
        live_stream_id = XmlUtilities.value_from_xml_element(
            root.find("LiveStreamId"), str
        )
        device_profile = XmlUtilities.value_from_xml_element(
            root.find("DeviceProfile"), DeviceProfile
        )
        enable_direct_play = XmlUtilities.value_from_xml_element(
            root.find("EnableDirectPlay"), bool
        )
        enable_direct_stream = XmlUtilities.value_from_xml_element(
            root.find("EnableDirectStream"), bool
        )
        enable_transcoding = XmlUtilities.value_from_xml_element(
            root.find("EnableTranscoding"), bool
        )
        allow_video_stream_copy = XmlUtilities.value_from_xml_element(
            root.find("AllowVideoStreamCopy"), bool
        )
        allow_audio_stream_copy = XmlUtilities.value_from_xml_element(
            root.find("AllowAudioStreamCopy"), bool
        )
        auto_open_live_stream = XmlUtilities.value_from_xml_element(
            root.find("AutoOpenLiveStream"), bool
        )

        return cls(
            user_id,
            max_streaming_bitrate,
            start_time_ticks,
            audio_stream_index,
            subtitle_stream_index,
            max_audio_channels,
            media_source_id,
            live_stream_id,
            device_profile,
            enable_direct_play,
            enable_direct_stream,
            enable_transcoding,
            allow_video_stream_copy,
            allow_audio_stream_copy,
            auto_open_live_stream,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
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
        XmlUtilities.add_as_subelement(root, self.media_source_id, "MediaSourceId")
        XmlUtilities.add_as_subelement(root, self.live_stream_id, "LiveStreamId")
        XmlUtilities.add_as_subelement(root, self.device_profile, "DeviceProfile")
        XmlUtilities.add_as_subelement(
            root, self.enable_direct_play, "EnableDirectPlay"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_direct_stream, "EnableDirectStream"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_transcoding, "EnableTranscoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_video_stream_copy, "AllowVideoStreamCopy"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_audio_stream_copy, "AllowAudioStreamCopy"
        )
        XmlUtilities.add_as_subelement(
            root, self.auto_open_live_stream, "AutoOpenLiveStream"
        )
