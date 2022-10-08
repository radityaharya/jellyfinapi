# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaStream(object):

    """Implementation of the 'MediaStream' model.

    Class MediaStream.

    Attributes:
        codec (string): Gets or sets the codec.
        codec_tag (string): Gets or sets the codec tag.
        language (string): Gets or sets the language.
        color_range (string): Gets or sets the color range.
        color_space (string): Gets or sets the color space.
        color_transfer (string): Gets or sets the color transfer.
        color_primaries (string): Gets or sets the color primaries.
        dv_version_major (int): Gets or sets the Dolby Vision version major.
        dv_version_minor (int): Gets or sets the Dolby Vision version minor.
        dv_profile (int): Gets or sets the Dolby Vision profile.
        dv_level (int): Gets or sets the Dolby Vision level.
        rpu_present_flag (int): Gets or sets the Dolby Vision rpu present
            flag.
        el_present_flag (int): Gets or sets the Dolby Vision el present flag.
        bl_present_flag (int): Gets or sets the Dolby Vision bl present flag.
        dv_bl_signal_compatibility_id (int): Gets or sets the Dolby Vision bl
            signal compatibility id.
        comment (string): Gets or sets the comment.
        time_base (string): Gets or sets the time base.
        codec_time_base (string): Gets or sets the codec time base.
        title (string): Gets or sets the title.
        video_range (string): Gets the video range.
        video_range_type (string): Gets the video range type.
        video_do_vi_title (string): Gets the video dovi title.
        localized_undefined (string): TODO: type description here.
        localized_default (string): TODO: type description here.
        localized_forced (string): TODO: type description here.
        localized_external (string): TODO: type description here.
        display_title (string): TODO: type description here.
        nal_length_size (string): TODO: type description here.
        is_interlaced (bool): Gets or sets a value indicating whether this
            instance is interlaced.
        is_avc (bool): TODO: type description here.
        channel_layout (string): Gets or sets the channel layout.
        bit_rate (int): Gets or sets the bit rate.
        bit_depth (int): Gets or sets the bit depth.
        ref_frames (int): Gets or sets the reference frames.
        packet_length (int): Gets or sets the length of the packet.
        channels (int): Gets or sets the channels.
        sample_rate (int): Gets or sets the sample rate.
        is_default (bool): Gets or sets a value indicating whether this
            instance is default.
        is_forced (bool): Gets or sets a value indicating whether this
            instance is forced.
        height (int): Gets or sets the height.
        width (int): Gets or sets the width.
        average_frame_rate (float): Gets or sets the average frame rate.
        real_frame_rate (float): Gets or sets the real frame rate.
        profile (string): Gets or sets the profile.
        mtype (MediaStreamTypeEnum): Gets or sets the type.
        aspect_ratio (string): Gets or sets the aspect ratio.
        index (int): Gets or sets the index.
        score (int): Gets or sets the score.
        is_external (bool): Gets or sets a value indicating whether this
            instance is external.
        delivery_method (SubtitleDeliveryMethodEnum): Gets or sets the
            method.
        delivery_url (string): Gets or sets the delivery URL.
        is_external_url (bool): Gets or sets a value indicating whether this
            instance is external URL.
        is_text_subtitle_stream (bool): TODO: type description here.
        supports_external_stream (bool): Gets or sets a value indicating
            whether [supports external stream].
        path (string): Gets or sets the filename.
        pixel_format (string): Gets or sets the pixel format.
        level (float): Gets or sets the level.
        is_anamorphic (bool): Gets or sets whether this instance is
            anamorphic.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "codec": "Codec",
        "codec_tag": "CodecTag",
        "language": "Language",
        "color_range": "ColorRange",
        "color_space": "ColorSpace",
        "color_transfer": "ColorTransfer",
        "color_primaries": "ColorPrimaries",
        "dv_version_major": "DvVersionMajor",
        "dv_version_minor": "DvVersionMinor",
        "dv_profile": "DvProfile",
        "dv_level": "DvLevel",
        "rpu_present_flag": "RpuPresentFlag",
        "el_present_flag": "ElPresentFlag",
        "bl_present_flag": "BlPresentFlag",
        "dv_bl_signal_compatibility_id": "DvBlSignalCompatibilityId",
        "comment": "Comment",
        "time_base": "TimeBase",
        "codec_time_base": "CodecTimeBase",
        "title": "Title",
        "video_range": "VideoRange",
        "video_range_type": "VideoRangeType",
        "video_do_vi_title": "VideoDoViTitle",
        "localized_undefined": "LocalizedUndefined",
        "localized_default": "LocalizedDefault",
        "localized_forced": "LocalizedForced",
        "localized_external": "LocalizedExternal",
        "display_title": "DisplayTitle",
        "nal_length_size": "NalLengthSize",
        "is_interlaced": "IsInterlaced",
        "is_avc": "IsAVC",
        "channel_layout": "ChannelLayout",
        "bit_rate": "BitRate",
        "bit_depth": "BitDepth",
        "ref_frames": "RefFrames",
        "packet_length": "PacketLength",
        "channels": "Channels",
        "sample_rate": "SampleRate",
        "is_default": "IsDefault",
        "is_forced": "IsForced",
        "height": "Height",
        "width": "Width",
        "average_frame_rate": "AverageFrameRate",
        "real_frame_rate": "RealFrameRate",
        "profile": "Profile",
        "mtype": "Type",
        "aspect_ratio": "AspectRatio",
        "index": "Index",
        "score": "Score",
        "is_external": "IsExternal",
        "delivery_method": "DeliveryMethod",
        "delivery_url": "DeliveryUrl",
        "is_external_url": "IsExternalUrl",
        "is_text_subtitle_stream": "IsTextSubtitleStream",
        "supports_external_stream": "SupportsExternalStream",
        "path": "Path",
        "pixel_format": "PixelFormat",
        "level": "Level",
        "is_anamorphic": "IsAnamorphic",
    }

    _optionals = [
        "codec",
        "codec_tag",
        "language",
        "color_range",
        "color_space",
        "color_transfer",
        "color_primaries",
        "dv_version_major",
        "dv_version_minor",
        "dv_profile",
        "dv_level",
        "rpu_present_flag",
        "el_present_flag",
        "bl_present_flag",
        "dv_bl_signal_compatibility_id",
        "comment",
        "time_base",
        "codec_time_base",
        "title",
        "video_range",
        "video_range_type",
        "video_do_vi_title",
        "localized_undefined",
        "localized_default",
        "localized_forced",
        "localized_external",
        "display_title",
        "nal_length_size",
        "is_interlaced",
        "is_avc",
        "channel_layout",
        "bit_rate",
        "bit_depth",
        "ref_frames",
        "packet_length",
        "channels",
        "sample_rate",
        "is_default",
        "is_forced",
        "height",
        "width",
        "average_frame_rate",
        "real_frame_rate",
        "profile",
        "mtype",
        "aspect_ratio",
        "index",
        "score",
        "is_external",
        "delivery_method",
        "delivery_url",
        "is_external_url",
        "is_text_subtitle_stream",
        "supports_external_stream",
        "path",
        "pixel_format",
        "level",
        "is_anamorphic",
    ]

    _nullables = [
        "codec",
        "codec_tag",
        "language",
        "color_range",
        "color_space",
        "color_transfer",
        "color_primaries",
        "dv_version_major",
        "dv_version_minor",
        "dv_profile",
        "dv_level",
        "rpu_present_flag",
        "el_present_flag",
        "bl_present_flag",
        "dv_bl_signal_compatibility_id",
        "comment",
        "time_base",
        "codec_time_base",
        "title",
        "video_range",
        "video_range_type",
        "video_do_vi_title",
        "localized_undefined",
        "localized_default",
        "localized_forced",
        "localized_external",
        "display_title",
        "nal_length_size",
        "is_avc",
        "channel_layout",
        "bit_rate",
        "bit_depth",
        "ref_frames",
        "packet_length",
        "channels",
        "sample_rate",
        "height",
        "width",
        "average_frame_rate",
        "real_frame_rate",
        "profile",
        "aspect_ratio",
        "score",
        "delivery_method",
        "delivery_url",
        "is_external_url",
        "path",
        "pixel_format",
        "level",
        "is_anamorphic",
    ]

    def __init__(
        self,
        codec=APIHelper.SKIP,
        codec_tag=APIHelper.SKIP,
        language=APIHelper.SKIP,
        color_range=APIHelper.SKIP,
        color_space=APIHelper.SKIP,
        color_transfer=APIHelper.SKIP,
        color_primaries=APIHelper.SKIP,
        dv_version_major=APIHelper.SKIP,
        dv_version_minor=APIHelper.SKIP,
        dv_profile=APIHelper.SKIP,
        dv_level=APIHelper.SKIP,
        rpu_present_flag=APIHelper.SKIP,
        el_present_flag=APIHelper.SKIP,
        bl_present_flag=APIHelper.SKIP,
        dv_bl_signal_compatibility_id=APIHelper.SKIP,
        comment=APIHelper.SKIP,
        time_base=APIHelper.SKIP,
        codec_time_base=APIHelper.SKIP,
        title=APIHelper.SKIP,
        video_range=APIHelper.SKIP,
        video_range_type=APIHelper.SKIP,
        video_do_vi_title=APIHelper.SKIP,
        localized_undefined=APIHelper.SKIP,
        localized_default=APIHelper.SKIP,
        localized_forced=APIHelper.SKIP,
        localized_external=APIHelper.SKIP,
        display_title=APIHelper.SKIP,
        nal_length_size=APIHelper.SKIP,
        is_interlaced=APIHelper.SKIP,
        is_avc=APIHelper.SKIP,
        channel_layout=APIHelper.SKIP,
        bit_rate=APIHelper.SKIP,
        bit_depth=APIHelper.SKIP,
        ref_frames=APIHelper.SKIP,
        packet_length=APIHelper.SKIP,
        channels=APIHelper.SKIP,
        sample_rate=APIHelper.SKIP,
        is_default=APIHelper.SKIP,
        is_forced=APIHelper.SKIP,
        height=APIHelper.SKIP,
        width=APIHelper.SKIP,
        average_frame_rate=APIHelper.SKIP,
        real_frame_rate=APIHelper.SKIP,
        profile=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        aspect_ratio=APIHelper.SKIP,
        index=APIHelper.SKIP,
        score=APIHelper.SKIP,
        is_external=APIHelper.SKIP,
        delivery_method=APIHelper.SKIP,
        delivery_url=APIHelper.SKIP,
        is_external_url=APIHelper.SKIP,
        is_text_subtitle_stream=APIHelper.SKIP,
        supports_external_stream=APIHelper.SKIP,
        path=APIHelper.SKIP,
        pixel_format=APIHelper.SKIP,
        level=APIHelper.SKIP,
        is_anamorphic=APIHelper.SKIP,
    ):
        """Constructor for the MediaStream class"""

        # Initialize members of the class
        if codec is not APIHelper.SKIP:
            self.codec = codec
        if codec_tag is not APIHelper.SKIP:
            self.codec_tag = codec_tag
        if language is not APIHelper.SKIP:
            self.language = language
        if color_range is not APIHelper.SKIP:
            self.color_range = color_range
        if color_space is not APIHelper.SKIP:
            self.color_space = color_space
        if color_transfer is not APIHelper.SKIP:
            self.color_transfer = color_transfer
        if color_primaries is not APIHelper.SKIP:
            self.color_primaries = color_primaries
        if dv_version_major is not APIHelper.SKIP:
            self.dv_version_major = dv_version_major
        if dv_version_minor is not APIHelper.SKIP:
            self.dv_version_minor = dv_version_minor
        if dv_profile is not APIHelper.SKIP:
            self.dv_profile = dv_profile
        if dv_level is not APIHelper.SKIP:
            self.dv_level = dv_level
        if rpu_present_flag is not APIHelper.SKIP:
            self.rpu_present_flag = rpu_present_flag
        if el_present_flag is not APIHelper.SKIP:
            self.el_present_flag = el_present_flag
        if bl_present_flag is not APIHelper.SKIP:
            self.bl_present_flag = bl_present_flag
        if dv_bl_signal_compatibility_id is not APIHelper.SKIP:
            self.dv_bl_signal_compatibility_id = dv_bl_signal_compatibility_id
        if comment is not APIHelper.SKIP:
            self.comment = comment
        if time_base is not APIHelper.SKIP:
            self.time_base = time_base
        if codec_time_base is not APIHelper.SKIP:
            self.codec_time_base = codec_time_base
        if title is not APIHelper.SKIP:
            self.title = title
        if video_range is not APIHelper.SKIP:
            self.video_range = video_range
        if video_range_type is not APIHelper.SKIP:
            self.video_range_type = video_range_type
        if video_do_vi_title is not APIHelper.SKIP:
            self.video_do_vi_title = video_do_vi_title
        if localized_undefined is not APIHelper.SKIP:
            self.localized_undefined = localized_undefined
        if localized_default is not APIHelper.SKIP:
            self.localized_default = localized_default
        if localized_forced is not APIHelper.SKIP:
            self.localized_forced = localized_forced
        if localized_external is not APIHelper.SKIP:
            self.localized_external = localized_external
        if display_title is not APIHelper.SKIP:
            self.display_title = display_title
        if nal_length_size is not APIHelper.SKIP:
            self.nal_length_size = nal_length_size
        if is_interlaced is not APIHelper.SKIP:
            self.is_interlaced = is_interlaced
        if is_avc is not APIHelper.SKIP:
            self.is_avc = is_avc
        if channel_layout is not APIHelper.SKIP:
            self.channel_layout = channel_layout
        if bit_rate is not APIHelper.SKIP:
            self.bit_rate = bit_rate
        if bit_depth is not APIHelper.SKIP:
            self.bit_depth = bit_depth
        if ref_frames is not APIHelper.SKIP:
            self.ref_frames = ref_frames
        if packet_length is not APIHelper.SKIP:
            self.packet_length = packet_length
        if channels is not APIHelper.SKIP:
            self.channels = channels
        if sample_rate is not APIHelper.SKIP:
            self.sample_rate = sample_rate
        if is_default is not APIHelper.SKIP:
            self.is_default = is_default
        if is_forced is not APIHelper.SKIP:
            self.is_forced = is_forced
        if height is not APIHelper.SKIP:
            self.height = height
        if width is not APIHelper.SKIP:
            self.width = width
        if average_frame_rate is not APIHelper.SKIP:
            self.average_frame_rate = average_frame_rate
        if real_frame_rate is not APIHelper.SKIP:
            self.real_frame_rate = real_frame_rate
        if profile is not APIHelper.SKIP:
            self.profile = profile
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if aspect_ratio is not APIHelper.SKIP:
            self.aspect_ratio = aspect_ratio
        if index is not APIHelper.SKIP:
            self.index = index
        if score is not APIHelper.SKIP:
            self.score = score
        if is_external is not APIHelper.SKIP:
            self.is_external = is_external
        if delivery_method is not APIHelper.SKIP:
            self.delivery_method = delivery_method
        if delivery_url is not APIHelper.SKIP:
            self.delivery_url = delivery_url
        if is_external_url is not APIHelper.SKIP:
            self.is_external_url = is_external_url
        if is_text_subtitle_stream is not APIHelper.SKIP:
            self.is_text_subtitle_stream = is_text_subtitle_stream
        if supports_external_stream is not APIHelper.SKIP:
            self.supports_external_stream = supports_external_stream
        if path is not APIHelper.SKIP:
            self.path = path
        if pixel_format is not APIHelper.SKIP:
            self.pixel_format = pixel_format
        if level is not APIHelper.SKIP:
            self.level = level
        if is_anamorphic is not APIHelper.SKIP:
            self.is_anamorphic = is_anamorphic

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

        codec = (
            dictionary.get("Codec") if "Codec" in dictionary.keys() else APIHelper.SKIP
        )
        codec_tag = (
            dictionary.get("CodecTag")
            if "CodecTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        language = (
            dictionary.get("Language")
            if "Language" in dictionary.keys()
            else APIHelper.SKIP
        )
        color_range = (
            dictionary.get("ColorRange")
            if "ColorRange" in dictionary.keys()
            else APIHelper.SKIP
        )
        color_space = (
            dictionary.get("ColorSpace")
            if "ColorSpace" in dictionary.keys()
            else APIHelper.SKIP
        )
        color_transfer = (
            dictionary.get("ColorTransfer")
            if "ColorTransfer" in dictionary.keys()
            else APIHelper.SKIP
        )
        color_primaries = (
            dictionary.get("ColorPrimaries")
            if "ColorPrimaries" in dictionary.keys()
            else APIHelper.SKIP
        )
        dv_version_major = (
            dictionary.get("DvVersionMajor")
            if "DvVersionMajor" in dictionary.keys()
            else APIHelper.SKIP
        )
        dv_version_minor = (
            dictionary.get("DvVersionMinor")
            if "DvVersionMinor" in dictionary.keys()
            else APIHelper.SKIP
        )
        dv_profile = (
            dictionary.get("DvProfile")
            if "DvProfile" in dictionary.keys()
            else APIHelper.SKIP
        )
        dv_level = (
            dictionary.get("DvLevel")
            if "DvLevel" in dictionary.keys()
            else APIHelper.SKIP
        )
        rpu_present_flag = (
            dictionary.get("RpuPresentFlag")
            if "RpuPresentFlag" in dictionary.keys()
            else APIHelper.SKIP
        )
        el_present_flag = (
            dictionary.get("ElPresentFlag")
            if "ElPresentFlag" in dictionary.keys()
            else APIHelper.SKIP
        )
        bl_present_flag = (
            dictionary.get("BlPresentFlag")
            if "BlPresentFlag" in dictionary.keys()
            else APIHelper.SKIP
        )
        dv_bl_signal_compatibility_id = (
            dictionary.get("DvBlSignalCompatibilityId")
            if "DvBlSignalCompatibilityId" in dictionary.keys()
            else APIHelper.SKIP
        )
        comment = (
            dictionary.get("Comment")
            if "Comment" in dictionary.keys()
            else APIHelper.SKIP
        )
        time_base = (
            dictionary.get("TimeBase")
            if "TimeBase" in dictionary.keys()
            else APIHelper.SKIP
        )
        codec_time_base = (
            dictionary.get("CodecTimeBase")
            if "CodecTimeBase" in dictionary.keys()
            else APIHelper.SKIP
        )
        title = (
            dictionary.get("Title") if "Title" in dictionary.keys() else APIHelper.SKIP
        )
        video_range = (
            dictionary.get("VideoRange")
            if "VideoRange" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_range_type = (
            dictionary.get("VideoRangeType")
            if "VideoRangeType" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_do_vi_title = (
            dictionary.get("VideoDoViTitle")
            if "VideoDoViTitle" in dictionary.keys()
            else APIHelper.SKIP
        )
        localized_undefined = (
            dictionary.get("LocalizedUndefined")
            if "LocalizedUndefined" in dictionary.keys()
            else APIHelper.SKIP
        )
        localized_default = (
            dictionary.get("LocalizedDefault")
            if "LocalizedDefault" in dictionary.keys()
            else APIHelper.SKIP
        )
        localized_forced = (
            dictionary.get("LocalizedForced")
            if "LocalizedForced" in dictionary.keys()
            else APIHelper.SKIP
        )
        localized_external = (
            dictionary.get("LocalizedExternal")
            if "LocalizedExternal" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_title = (
            dictionary.get("DisplayTitle")
            if "DisplayTitle" in dictionary.keys()
            else APIHelper.SKIP
        )
        nal_length_size = (
            dictionary.get("NalLengthSize")
            if "NalLengthSize" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_interlaced = (
            dictionary.get("IsInterlaced")
            if "IsInterlaced" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_avc = (
            dictionary.get("IsAVC") if "IsAVC" in dictionary.keys() else APIHelper.SKIP
        )
        channel_layout = (
            dictionary.get("ChannelLayout")
            if "ChannelLayout" in dictionary.keys()
            else APIHelper.SKIP
        )
        bit_rate = (
            dictionary.get("BitRate")
            if "BitRate" in dictionary.keys()
            else APIHelper.SKIP
        )
        bit_depth = (
            dictionary.get("BitDepth")
            if "BitDepth" in dictionary.keys()
            else APIHelper.SKIP
        )
        ref_frames = (
            dictionary.get("RefFrames")
            if "RefFrames" in dictionary.keys()
            else APIHelper.SKIP
        )
        packet_length = (
            dictionary.get("PacketLength")
            if "PacketLength" in dictionary.keys()
            else APIHelper.SKIP
        )
        channels = (
            dictionary.get("Channels")
            if "Channels" in dictionary.keys()
            else APIHelper.SKIP
        )
        sample_rate = (
            dictionary.get("SampleRate")
            if "SampleRate" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_default = (
            dictionary.get("IsDefault")
            if "IsDefault" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_forced = (
            dictionary.get("IsForced")
            if "IsForced" in dictionary.keys()
            else APIHelper.SKIP
        )
        height = (
            dictionary.get("Height")
            if "Height" in dictionary.keys()
            else APIHelper.SKIP
        )
        width = (
            dictionary.get("Width") if "Width" in dictionary.keys() else APIHelper.SKIP
        )
        average_frame_rate = (
            dictionary.get("AverageFrameRate")
            if "AverageFrameRate" in dictionary.keys()
            else APIHelper.SKIP
        )
        real_frame_rate = (
            dictionary.get("RealFrameRate")
            if "RealFrameRate" in dictionary.keys()
            else APIHelper.SKIP
        )
        profile = (
            dictionary.get("Profile")
            if "Profile" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        aspect_ratio = (
            dictionary.get("AspectRatio")
            if "AspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        index = dictionary.get("Index") if dictionary.get("Index") else APIHelper.SKIP
        score = (
            dictionary.get("Score") if "Score" in dictionary.keys() else APIHelper.SKIP
        )
        is_external = (
            dictionary.get("IsExternal")
            if "IsExternal" in dictionary.keys()
            else APIHelper.SKIP
        )
        delivery_method = (
            dictionary.get("DeliveryMethod")
            if "DeliveryMethod" in dictionary.keys()
            else APIHelper.SKIP
        )
        delivery_url = (
            dictionary.get("DeliveryUrl")
            if "DeliveryUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_external_url = (
            dictionary.get("IsExternalUrl")
            if "IsExternalUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_text_subtitle_stream = (
            dictionary.get("IsTextSubtitleStream")
            if "IsTextSubtitleStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_external_stream = (
            dictionary.get("SupportsExternalStream")
            if "SupportsExternalStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        pixel_format = (
            dictionary.get("PixelFormat")
            if "PixelFormat" in dictionary.keys()
            else APIHelper.SKIP
        )
        level = (
            dictionary.get("Level") if "Level" in dictionary.keys() else APIHelper.SKIP
        )
        is_anamorphic = (
            dictionary.get("IsAnamorphic")
            if "IsAnamorphic" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            codec,
            codec_tag,
            language,
            color_range,
            color_space,
            color_transfer,
            color_primaries,
            dv_version_major,
            dv_version_minor,
            dv_profile,
            dv_level,
            rpu_present_flag,
            el_present_flag,
            bl_present_flag,
            dv_bl_signal_compatibility_id,
            comment,
            time_base,
            codec_time_base,
            title,
            video_range,
            video_range_type,
            video_do_vi_title,
            localized_undefined,
            localized_default,
            localized_forced,
            localized_external,
            display_title,
            nal_length_size,
            is_interlaced,
            is_avc,
            channel_layout,
            bit_rate,
            bit_depth,
            ref_frames,
            packet_length,
            channels,
            sample_rate,
            is_default,
            is_forced,
            height,
            width,
            average_frame_rate,
            real_frame_rate,
            profile,
            mtype,
            aspect_ratio,
            index,
            score,
            is_external,
            delivery_method,
            delivery_url,
            is_external_url,
            is_text_subtitle_stream,
            supports_external_stream,
            path,
            pixel_format,
            level,
            is_anamorphic,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        codec = XmlUtilities.value_from_xml_element(root.find("Codec"), str)
        codec_tag = XmlUtilities.value_from_xml_element(root.find("CodecTag"), str)
        language = XmlUtilities.value_from_xml_element(root.find("Language"), str)
        color_range = XmlUtilities.value_from_xml_element(root.find("ColorRange"), str)
        color_space = XmlUtilities.value_from_xml_element(root.find("ColorSpace"), str)
        color_transfer = XmlUtilities.value_from_xml_element(
            root.find("ColorTransfer"), str
        )
        color_primaries = XmlUtilities.value_from_xml_element(
            root.find("ColorPrimaries"), str
        )
        dv_version_major = XmlUtilities.value_from_xml_element(
            root.find("DvVersionMajor"), int
        )
        dv_version_minor = XmlUtilities.value_from_xml_element(
            root.find("DvVersionMinor"), int
        )
        dv_profile = XmlUtilities.value_from_xml_element(root.find("DvProfile"), int)
        dv_level = XmlUtilities.value_from_xml_element(root.find("DvLevel"), int)
        rpu_present_flag = XmlUtilities.value_from_xml_element(
            root.find("RpuPresentFlag"), int
        )
        el_present_flag = XmlUtilities.value_from_xml_element(
            root.find("ElPresentFlag"), int
        )
        bl_present_flag = XmlUtilities.value_from_xml_element(
            root.find("BlPresentFlag"), int
        )
        dv_bl_signal_compatibility_id = XmlUtilities.value_from_xml_element(
            root.find("DvBlSignalCompatibilityId"), int
        )
        comment = XmlUtilities.value_from_xml_element(root.find("Comment"), str)
        time_base = XmlUtilities.value_from_xml_element(root.find("TimeBase"), str)
        codec_time_base = XmlUtilities.value_from_xml_element(
            root.find("CodecTimeBase"), str
        )
        title = XmlUtilities.value_from_xml_element(root.find("Title"), str)
        video_range = XmlUtilities.value_from_xml_element(root.find("VideoRange"), str)
        video_range_type = XmlUtilities.value_from_xml_element(
            root.find("VideoRangeType"), str
        )
        video_do_vi_title = XmlUtilities.value_from_xml_element(
            root.find("VideoDoViTitle"), str
        )
        localized_undefined = XmlUtilities.value_from_xml_element(
            root.find("LocalizedUndefined"), str
        )
        localized_default = XmlUtilities.value_from_xml_element(
            root.find("LocalizedDefault"), str
        )
        localized_forced = XmlUtilities.value_from_xml_element(
            root.find("LocalizedForced"), str
        )
        localized_external = XmlUtilities.value_from_xml_element(
            root.find("LocalizedExternal"), str
        )
        display_title = XmlUtilities.value_from_xml_element(
            root.find("DisplayTitle"), str
        )
        nal_length_size = XmlUtilities.value_from_xml_element(
            root.find("NalLengthSize"), str
        )
        is_interlaced = XmlUtilities.value_from_xml_element(
            root.find("IsInterlaced"), bool
        )
        is_avc = XmlUtilities.value_from_xml_element(root.find("IsAVC"), bool)
        channel_layout = XmlUtilities.value_from_xml_element(
            root.find("ChannelLayout"), str
        )
        bit_rate = XmlUtilities.value_from_xml_element(root.find("BitRate"), int)
        bit_depth = XmlUtilities.value_from_xml_element(root.find("BitDepth"), int)
        ref_frames = XmlUtilities.value_from_xml_element(root.find("RefFrames"), int)
        packet_length = XmlUtilities.value_from_xml_element(
            root.find("PacketLength"), int
        )
        channels = XmlUtilities.value_from_xml_element(root.find("Channels"), int)
        sample_rate = XmlUtilities.value_from_xml_element(root.find("SampleRate"), int)
        is_default = XmlUtilities.value_from_xml_element(root.find("IsDefault"), bool)
        is_forced = XmlUtilities.value_from_xml_element(root.find("IsForced"), bool)
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        average_frame_rate = XmlUtilities.value_from_xml_element(
            root.find("AverageFrameRate"), float
        )
        real_frame_rate = XmlUtilities.value_from_xml_element(
            root.find("RealFrameRate"), float
        )
        profile = XmlUtilities.value_from_xml_element(root.find("Profile"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("AspectRatio"), str
        )
        index = XmlUtilities.value_from_xml_element(root.find("Index"), int)
        score = XmlUtilities.value_from_xml_element(root.find("Score"), int)
        is_external = XmlUtilities.value_from_xml_element(root.find("IsExternal"), bool)
        delivery_method = XmlUtilities.value_from_xml_element(
            root.find("DeliveryMethod"), str
        )
        delivery_url = XmlUtilities.value_from_xml_element(
            root.find("DeliveryUrl"), str
        )
        is_external_url = XmlUtilities.value_from_xml_element(
            root.find("IsExternalUrl"), bool
        )
        is_text_subtitle_stream = XmlUtilities.value_from_xml_element(
            root.find("IsTextSubtitleStream"), bool
        )
        supports_external_stream = XmlUtilities.value_from_xml_element(
            root.find("SupportsExternalStream"), bool
        )
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        pixel_format = XmlUtilities.value_from_xml_element(
            root.find("PixelFormat"), str
        )
        level = XmlUtilities.value_from_xml_element(root.find("Level"), float)
        is_anamorphic = XmlUtilities.value_from_xml_element(
            root.find("IsAnamorphic"), bool
        )

        return cls(
            codec,
            codec_tag,
            language,
            color_range,
            color_space,
            color_transfer,
            color_primaries,
            dv_version_major,
            dv_version_minor,
            dv_profile,
            dv_level,
            rpu_present_flag,
            el_present_flag,
            bl_present_flag,
            dv_bl_signal_compatibility_id,
            comment,
            time_base,
            codec_time_base,
            title,
            video_range,
            video_range_type,
            video_do_vi_title,
            localized_undefined,
            localized_default,
            localized_forced,
            localized_external,
            display_title,
            nal_length_size,
            is_interlaced,
            is_avc,
            channel_layout,
            bit_rate,
            bit_depth,
            ref_frames,
            packet_length,
            channels,
            sample_rate,
            is_default,
            is_forced,
            height,
            width,
            average_frame_rate,
            real_frame_rate,
            profile,
            mtype,
            aspect_ratio,
            index,
            score,
            is_external,
            delivery_method,
            delivery_url,
            is_external_url,
            is_text_subtitle_stream,
            supports_external_stream,
            path,
            pixel_format,
            level,
            is_anamorphic,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.codec, "Codec")
        XmlUtilities.add_as_subelement(root, self.codec_tag, "CodecTag")
        XmlUtilities.add_as_subelement(root, self.language, "Language")
        XmlUtilities.add_as_subelement(root, self.color_range, "ColorRange")
        XmlUtilities.add_as_subelement(root, self.color_space, "ColorSpace")
        XmlUtilities.add_as_subelement(root, self.color_transfer, "ColorTransfer")
        XmlUtilities.add_as_subelement(root, self.color_primaries, "ColorPrimaries")
        XmlUtilities.add_as_subelement(root, self.dv_version_major, "DvVersionMajor")
        XmlUtilities.add_as_subelement(root, self.dv_version_minor, "DvVersionMinor")
        XmlUtilities.add_as_subelement(root, self.dv_profile, "DvProfile")
        XmlUtilities.add_as_subelement(root, self.dv_level, "DvLevel")
        XmlUtilities.add_as_subelement(root, self.rpu_present_flag, "RpuPresentFlag")
        XmlUtilities.add_as_subelement(root, self.el_present_flag, "ElPresentFlag")
        XmlUtilities.add_as_subelement(root, self.bl_present_flag, "BlPresentFlag")
        XmlUtilities.add_as_subelement(
            root, self.dv_bl_signal_compatibility_id, "DvBlSignalCompatibilityId"
        )
        XmlUtilities.add_as_subelement(root, self.comment, "Comment")
        XmlUtilities.add_as_subelement(root, self.time_base, "TimeBase")
        XmlUtilities.add_as_subelement(root, self.codec_time_base, "CodecTimeBase")
        XmlUtilities.add_as_subelement(root, self.title, "Title")
        XmlUtilities.add_as_subelement(root, self.video_range, "VideoRange")
        XmlUtilities.add_as_subelement(root, self.video_range_type, "VideoRangeType")
        XmlUtilities.add_as_subelement(root, self.video_do_vi_title, "VideoDoViTitle")
        XmlUtilities.add_as_subelement(
            root, self.localized_undefined, "LocalizedUndefined"
        )
        XmlUtilities.add_as_subelement(root, self.localized_default, "LocalizedDefault")
        XmlUtilities.add_as_subelement(root, self.localized_forced, "LocalizedForced")
        XmlUtilities.add_as_subelement(
            root, self.localized_external, "LocalizedExternal"
        )
        XmlUtilities.add_as_subelement(root, self.display_title, "DisplayTitle")
        XmlUtilities.add_as_subelement(root, self.nal_length_size, "NalLengthSize")
        XmlUtilities.add_as_subelement(root, self.is_interlaced, "IsInterlaced")
        XmlUtilities.add_as_subelement(root, self.is_avc, "IsAVC")
        XmlUtilities.add_as_subelement(root, self.channel_layout, "ChannelLayout")
        XmlUtilities.add_as_subelement(root, self.bit_rate, "BitRate")
        XmlUtilities.add_as_subelement(root, self.bit_depth, "BitDepth")
        XmlUtilities.add_as_subelement(root, self.ref_frames, "RefFrames")
        XmlUtilities.add_as_subelement(root, self.packet_length, "PacketLength")
        XmlUtilities.add_as_subelement(root, self.channels, "Channels")
        XmlUtilities.add_as_subelement(root, self.sample_rate, "SampleRate")
        XmlUtilities.add_as_subelement(root, self.is_default, "IsDefault")
        XmlUtilities.add_as_subelement(root, self.is_forced, "IsForced")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(
            root, self.average_frame_rate, "AverageFrameRate"
        )
        XmlUtilities.add_as_subelement(root, self.real_frame_rate, "RealFrameRate")
        XmlUtilities.add_as_subelement(root, self.profile, "Profile")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.aspect_ratio, "AspectRatio")
        XmlUtilities.add_as_subelement(root, self.index, "Index")
        XmlUtilities.add_as_subelement(root, self.score, "Score")
        XmlUtilities.add_as_subelement(root, self.is_external, "IsExternal")
        XmlUtilities.add_as_subelement(root, self.delivery_method, "DeliveryMethod")
        XmlUtilities.add_as_subelement(root, self.delivery_url, "DeliveryUrl")
        XmlUtilities.add_as_subelement(root, self.is_external_url, "IsExternalUrl")
        XmlUtilities.add_as_subelement(
            root, self.is_text_subtitle_stream, "IsTextSubtitleStream"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_external_stream, "SupportsExternalStream"
        )
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.pixel_format, "PixelFormat")
        XmlUtilities.add_as_subelement(root, self.level, "Level")
        XmlUtilities.add_as_subelement(root, self.is_anamorphic, "IsAnamorphic")
