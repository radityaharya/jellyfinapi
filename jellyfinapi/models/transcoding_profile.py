# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.profile_condition import ProfileCondition
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TranscodingProfile(object):

    """Implementation of the 'TranscodingProfile' model.

    TODO: type model description here.

    Attributes:
        container (string): TODO: type description here.
        mtype (DlnaProfileTypeEnum): TODO: type description here.
        video_codec (string): TODO: type description here.
        audio_codec (string): TODO: type description here.
        protocol (string): TODO: type description here.
        estimate_content_length (bool): TODO: type description here.
        enable_mpegts_m_2_ts_mode (bool): TODO: type description here.
        transcode_seek_info (TranscodeSeekInfoEnum): TODO: type description
            here.
        copy_timestamps (bool): TODO: type description here.
        context (EncodingContextEnum): TODO: type description here.
        enable_subtitles_in_manifest (bool): TODO: type description here.
        max_audio_channels (string): TODO: type description here.
        min_segments (int): TODO: type description here.
        segment_length (int): TODO: type description here.
        break_on_non_key_frames (bool): TODO: type description here.
        conditions (list of ProfileCondition): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "container": "Container",
        "mtype": "Type",
        "video_codec": "VideoCodec",
        "audio_codec": "AudioCodec",
        "protocol": "Protocol",
        "estimate_content_length": "EstimateContentLength",
        "enable_mpegts_m_2_ts_mode": "EnableMpegtsM2TsMode",
        "transcode_seek_info": "TranscodeSeekInfo",
        "copy_timestamps": "CopyTimestamps",
        "context": "Context",
        "enable_subtitles_in_manifest": "EnableSubtitlesInManifest",
        "max_audio_channels": "MaxAudioChannels",
        "min_segments": "MinSegments",
        "segment_length": "SegmentLength",
        "break_on_non_key_frames": "BreakOnNonKeyFrames",
        "conditions": "Conditions",
    }

    _optionals = [
        "container",
        "mtype",
        "video_codec",
        "audio_codec",
        "protocol",
        "estimate_content_length",
        "enable_mpegts_m_2_ts_mode",
        "transcode_seek_info",
        "copy_timestamps",
        "context",
        "enable_subtitles_in_manifest",
        "max_audio_channels",
        "min_segments",
        "segment_length",
        "break_on_non_key_frames",
        "conditions",
    ]

    _nullables = [
        "max_audio_channels",
    ]

    def __init__(
        self,
        container=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        video_codec=APIHelper.SKIP,
        audio_codec=APIHelper.SKIP,
        protocol=APIHelper.SKIP,
        estimate_content_length=False,
        enable_mpegts_m_2_ts_mode=False,
        transcode_seek_info="Auto",
        copy_timestamps=False,
        context="Streaming",
        enable_subtitles_in_manifest=False,
        max_audio_channels=APIHelper.SKIP,
        min_segments=0,
        segment_length=0,
        break_on_non_key_frames=False,
        conditions=APIHelper.SKIP,
    ):
        """Constructor for the TranscodingProfile class"""

        # Initialize members of the class
        if container is not APIHelper.SKIP:
            self.container = container
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if video_codec is not APIHelper.SKIP:
            self.video_codec = video_codec
        if audio_codec is not APIHelper.SKIP:
            self.audio_codec = audio_codec
        if protocol is not APIHelper.SKIP:
            self.protocol = protocol
        self.estimate_content_length = estimate_content_length
        self.enable_mpegts_m_2_ts_mode = enable_mpegts_m_2_ts_mode
        self.transcode_seek_info = transcode_seek_info
        self.copy_timestamps = copy_timestamps
        self.context = context
        self.enable_subtitles_in_manifest = enable_subtitles_in_manifest
        if max_audio_channels is not APIHelper.SKIP:
            self.max_audio_channels = max_audio_channels
        self.min_segments = min_segments
        self.segment_length = segment_length
        self.break_on_non_key_frames = break_on_non_key_frames
        if conditions is not APIHelper.SKIP:
            self.conditions = conditions

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

        container = (
            dictionary.get("Container")
            if dictionary.get("Container")
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        video_codec = (
            dictionary.get("VideoCodec")
            if dictionary.get("VideoCodec")
            else APIHelper.SKIP
        )
        audio_codec = (
            dictionary.get("AudioCodec")
            if dictionary.get("AudioCodec")
            else APIHelper.SKIP
        )
        protocol = (
            dictionary.get("Protocol") if dictionary.get("Protocol") else APIHelper.SKIP
        )
        estimate_content_length = (
            dictionary.get("EstimateContentLength")
            if dictionary.get("EstimateContentLength")
            else False
        )
        enable_mpegts_m_2_ts_mode = (
            dictionary.get("EnableMpegtsM2TsMode")
            if dictionary.get("EnableMpegtsM2TsMode")
            else False
        )
        transcode_seek_info = (
            dictionary.get("TranscodeSeekInfo")
            if dictionary.get("TranscodeSeekInfo")
            else "Auto"
        )
        copy_timestamps = (
            dictionary.get("CopyTimestamps")
            if dictionary.get("CopyTimestamps")
            else False
        )
        context = (
            dictionary.get("Context") if dictionary.get("Context") else "Streaming"
        )
        enable_subtitles_in_manifest = (
            dictionary.get("EnableSubtitlesInManifest")
            if dictionary.get("EnableSubtitlesInManifest")
            else False
        )
        max_audio_channels = (
            dictionary.get("MaxAudioChannels")
            if "MaxAudioChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        min_segments = (
            dictionary.get("MinSegments") if dictionary.get("MinSegments") else 0
        )
        segment_length = (
            dictionary.get("SegmentLength") if dictionary.get("SegmentLength") else 0
        )
        break_on_non_key_frames = (
            dictionary.get("BreakOnNonKeyFrames")
            if dictionary.get("BreakOnNonKeyFrames")
            else False
        )
        conditions = None
        if dictionary.get("Conditions") is not None:
            conditions = [
                ProfileCondition.from_dictionary(x)
                for x in dictionary.get("Conditions")
            ]
        else:
            conditions = APIHelper.SKIP
        # Return an object of this model
        return cls(
            container,
            mtype,
            video_codec,
            audio_codec,
            protocol,
            estimate_content_length,
            enable_mpegts_m_2_ts_mode,
            transcode_seek_info,
            copy_timestamps,
            context,
            enable_subtitles_in_manifest,
            max_audio_channels,
            min_segments,
            segment_length,
            break_on_non_key_frames,
            conditions,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        video_codec = XmlUtilities.value_from_xml_element(root.find("VideoCodec"), str)
        audio_codec = XmlUtilities.value_from_xml_element(root.find("AudioCodec"), str)
        protocol = XmlUtilities.value_from_xml_element(root.find("Protocol"), str)
        estimate_content_length = XmlUtilities.value_from_xml_element(
            root.find("EstimateContentLength"), bool
        )
        enable_mpegts_m_2_ts_mode = XmlUtilities.value_from_xml_element(
            root.find("EnableMpegtsM2TsMode"), bool
        )
        transcode_seek_info = XmlUtilities.value_from_xml_element(
            root.find("TranscodeSeekInfo"), str
        )
        copy_timestamps = XmlUtilities.value_from_xml_element(
            root.find("CopyTimestamps"), bool
        )
        context = XmlUtilities.value_from_xml_element(root.find("Context"), str)
        enable_subtitles_in_manifest = XmlUtilities.value_from_xml_element(
            root.find("EnableSubtitlesInManifest"), bool
        )
        max_audio_channels = XmlUtilities.value_from_xml_element(
            root.find("MaxAudioChannels"), str
        )
        min_segments = XmlUtilities.value_from_xml_element(
            root.find("MinSegments"), int
        )
        segment_length = XmlUtilities.value_from_xml_element(
            root.find("SegmentLength"), int
        )
        break_on_non_key_frames = XmlUtilities.value_from_xml_element(
            root.find("BreakOnNonKeyFrames"), bool
        )
        conditions = XmlUtilities.list_from_xml_element(
            root, "ProfileCondition", ProfileCondition
        )

        return cls(
            container,
            mtype,
            video_codec,
            audio_codec,
            protocol,
            estimate_content_length,
            enable_mpegts_m_2_ts_mode,
            transcode_seek_info,
            copy_timestamps,
            context,
            enable_subtitles_in_manifest,
            max_audio_channels,
            min_segments,
            segment_length,
            break_on_non_key_frames,
            conditions,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.video_codec, "VideoCodec")
        XmlUtilities.add_as_subelement(root, self.audio_codec, "AudioCodec")
        XmlUtilities.add_as_subelement(root, self.protocol, "Protocol")
        XmlUtilities.add_as_subelement(
            root, self.estimate_content_length, "EstimateContentLength"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_mpegts_m_2_ts_mode, "EnableMpegtsM2TsMode"
        )
        XmlUtilities.add_as_subelement(
            root, self.transcode_seek_info, "TranscodeSeekInfo"
        )
        XmlUtilities.add_as_subelement(root, self.copy_timestamps, "CopyTimestamps")
        XmlUtilities.add_as_subelement(root, self.context, "Context")
        XmlUtilities.add_as_subelement(
            root, self.enable_subtitles_in_manifest, "EnableSubtitlesInManifest"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_audio_channels, "MaxAudioChannels"
        )
        XmlUtilities.add_as_subelement(root, self.min_segments, "MinSegments")
        XmlUtilities.add_as_subelement(root, self.segment_length, "SegmentLength")
        XmlUtilities.add_as_subelement(
            root, self.break_on_non_key_frames, "BreakOnNonKeyFrames"
        )
        XmlUtilities.add_list_as_subelement(root, self.conditions, "ProfileCondition")
