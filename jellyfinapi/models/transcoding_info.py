# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TranscodingInfo(object):

    """Implementation of the 'TranscodingInfo' model.

    TODO: type model description here.

    Attributes:
        audio_codec (string): TODO: type description here.
        video_codec (string): TODO: type description here.
        container (string): TODO: type description here.
        is_video_direct (bool): TODO: type description here.
        is_audio_direct (bool): TODO: type description here.
        bitrate (int): TODO: type description here.
        framerate (float): TODO: type description here.
        completion_percentage (float): TODO: type description here.
        width (int): TODO: type description here.
        height (int): TODO: type description here.
        audio_channels (int): TODO: type description here.
        hardware_acceleration_type (HardwareEncodingTypeEnum): TODO: type
            description here.
        transcode_reasons (TranscodeReasonsEnum): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audio_codec": "AudioCodec",
        "video_codec": "VideoCodec",
        "container": "Container",
        "is_video_direct": "IsVideoDirect",
        "is_audio_direct": "IsAudioDirect",
        "bitrate": "Bitrate",
        "framerate": "Framerate",
        "completion_percentage": "CompletionPercentage",
        "width": "Width",
        "height": "Height",
        "audio_channels": "AudioChannels",
        "hardware_acceleration_type": "HardwareAccelerationType",
        "transcode_reasons": "TranscodeReasons",
    }

    _optionals = [
        "audio_codec",
        "video_codec",
        "container",
        "is_video_direct",
        "is_audio_direct",
        "bitrate",
        "framerate",
        "completion_percentage",
        "width",
        "height",
        "audio_channels",
        "hardware_acceleration_type",
        "transcode_reasons",
    ]

    _nullables = [
        "audio_codec",
        "video_codec",
        "container",
        "bitrate",
        "framerate",
        "completion_percentage",
        "width",
        "height",
        "audio_channels",
        "hardware_acceleration_type",
    ]

    def __init__(
        self,
        audio_codec=APIHelper.SKIP,
        video_codec=APIHelper.SKIP,
        container=APIHelper.SKIP,
        is_video_direct=APIHelper.SKIP,
        is_audio_direct=APIHelper.SKIP,
        bitrate=APIHelper.SKIP,
        framerate=APIHelper.SKIP,
        completion_percentage=APIHelper.SKIP,
        width=APIHelper.SKIP,
        height=APIHelper.SKIP,
        audio_channels=APIHelper.SKIP,
        hardware_acceleration_type=APIHelper.SKIP,
        transcode_reasons=APIHelper.SKIP,
    ):
        """Constructor for the TranscodingInfo class"""

        # Initialize members of the class
        if audio_codec is not APIHelper.SKIP:
            self.audio_codec = audio_codec
        if video_codec is not APIHelper.SKIP:
            self.video_codec = video_codec
        if container is not APIHelper.SKIP:
            self.container = container
        if is_video_direct is not APIHelper.SKIP:
            self.is_video_direct = is_video_direct
        if is_audio_direct is not APIHelper.SKIP:
            self.is_audio_direct = is_audio_direct
        if bitrate is not APIHelper.SKIP:
            self.bitrate = bitrate
        if framerate is not APIHelper.SKIP:
            self.framerate = framerate
        if completion_percentage is not APIHelper.SKIP:
            self.completion_percentage = completion_percentage
        if width is not APIHelper.SKIP:
            self.width = width
        if height is not APIHelper.SKIP:
            self.height = height
        if audio_channels is not APIHelper.SKIP:
            self.audio_channels = audio_channels
        if hardware_acceleration_type is not APIHelper.SKIP:
            self.hardware_acceleration_type = hardware_acceleration_type
        if transcode_reasons is not APIHelper.SKIP:
            self.transcode_reasons = transcode_reasons

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

        audio_codec = (
            dictionary.get("AudioCodec")
            if "AudioCodec" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_codec = (
            dictionary.get("VideoCodec")
            if "VideoCodec" in dictionary.keys()
            else APIHelper.SKIP
        )
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_video_direct = (
            dictionary.get("IsVideoDirect")
            if "IsVideoDirect" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_audio_direct = (
            dictionary.get("IsAudioDirect")
            if "IsAudioDirect" in dictionary.keys()
            else APIHelper.SKIP
        )
        bitrate = (
            dictionary.get("Bitrate")
            if "Bitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        framerate = (
            dictionary.get("Framerate")
            if "Framerate" in dictionary.keys()
            else APIHelper.SKIP
        )
        completion_percentage = (
            dictionary.get("CompletionPercentage")
            if "CompletionPercentage" in dictionary.keys()
            else APIHelper.SKIP
        )
        width = (
            dictionary.get("Width") if "Width" in dictionary.keys() else APIHelper.SKIP
        )
        height = (
            dictionary.get("Height")
            if "Height" in dictionary.keys()
            else APIHelper.SKIP
        )
        audio_channels = (
            dictionary.get("AudioChannels")
            if "AudioChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        hardware_acceleration_type = (
            dictionary.get("HardwareAccelerationType")
            if "HardwareAccelerationType" in dictionary.keys()
            else APIHelper.SKIP
        )
        transcode_reasons = (
            dictionary.get("TranscodeReasons")
            if dictionary.get("TranscodeReasons")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            audio_codec,
            video_codec,
            container,
            is_video_direct,
            is_audio_direct,
            bitrate,
            framerate,
            completion_percentage,
            width,
            height,
            audio_channels,
            hardware_acceleration_type,
            transcode_reasons,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        audio_codec = XmlUtilities.value_from_xml_element(root.find("AudioCodec"), str)
        video_codec = XmlUtilities.value_from_xml_element(root.find("VideoCodec"), str)
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        is_video_direct = XmlUtilities.value_from_xml_element(
            root.find("IsVideoDirect"), bool
        )
        is_audio_direct = XmlUtilities.value_from_xml_element(
            root.find("IsAudioDirect"), bool
        )
        bitrate = XmlUtilities.value_from_xml_element(root.find("Bitrate"), int)
        framerate = XmlUtilities.value_from_xml_element(root.find("Framerate"), float)
        completion_percentage = XmlUtilities.value_from_xml_element(
            root.find("CompletionPercentage"), float
        )
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        audio_channels = XmlUtilities.value_from_xml_element(
            root.find("AudioChannels"), int
        )
        hardware_acceleration_type = XmlUtilities.value_from_xml_element(
            root.find("HardwareAccelerationType"), str
        )
        transcode_reasons = XmlUtilities.value_from_xml_element(
            root.find("TranscodeReasons"), str
        )

        return cls(
            audio_codec,
            video_codec,
            container,
            is_video_direct,
            is_audio_direct,
            bitrate,
            framerate,
            completion_percentage,
            width,
            height,
            audio_channels,
            hardware_acceleration_type,
            transcode_reasons,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.audio_codec, "AudioCodec")
        XmlUtilities.add_as_subelement(root, self.video_codec, "VideoCodec")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.is_video_direct, "IsVideoDirect")
        XmlUtilities.add_as_subelement(root, self.is_audio_direct, "IsAudioDirect")
        XmlUtilities.add_as_subelement(root, self.bitrate, "Bitrate")
        XmlUtilities.add_as_subelement(root, self.framerate, "Framerate")
        XmlUtilities.add_as_subelement(
            root, self.completion_percentage, "CompletionPercentage"
        )
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_as_subelement(root, self.audio_channels, "AudioChannels")
        XmlUtilities.add_as_subelement(
            root, self.hardware_acceleration_type, "HardwareAccelerationType"
        )
        XmlUtilities.add_as_subelement(root, self.transcode_reasons, "TranscodeReasons")
