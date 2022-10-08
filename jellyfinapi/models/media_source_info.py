# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_attachment import MediaAttachment
from jellyfinapi.models.media_stream import MediaStream
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaSourceInfo(object):

    """Implementation of the 'MediaSourceInfo' model.

    TODO: type model description here.

    Attributes:
        protocol (MediaProtocolEnum): TODO: type description here.
        id (string): TODO: type description here.
        path (string): TODO: type description here.
        encoder_path (string): TODO: type description here.
        encoder_protocol (MediaProtocolEnum): TODO: type description here.
        mtype (MediaSourceTypeEnum): TODO: type description here.
        container (string): TODO: type description here.
        size (long|int): TODO: type description here.
        name (string): TODO: type description here.
        is_remote (bool): Gets or sets a value indicating whether the media is
            remote.  Differentiate internet url vs local network.
        e_tag (string): TODO: type description here.
        run_time_ticks (long|int): TODO: type description here.
        read_at_native_framerate (bool): TODO: type description here.
        ignore_dts (bool): TODO: type description here.
        ignore_index (bool): TODO: type description here.
        gen_pts_input (bool): TODO: type description here.
        supports_transcoding (bool): TODO: type description here.
        supports_direct_stream (bool): TODO: type description here.
        supports_direct_play (bool): TODO: type description here.
        is_infinite_stream (bool): TODO: type description here.
        requires_opening (bool): TODO: type description here.
        open_token (string): TODO: type description here.
        requires_closing (bool): TODO: type description here.
        live_stream_id (string): TODO: type description here.
        buffer_ms (int): TODO: type description here.
        requires_looping (bool): TODO: type description here.
        supports_probing (bool): TODO: type description here.
        video_type (VideoTypeEnum): TODO: type description here.
        iso_type (IsoTypeEnum): TODO: type description here.
        video_3_d_format (Video3DFormatEnum): TODO: type description here.
        media_streams (list of MediaStream): TODO: type description here.
        media_attachments (list of MediaAttachment): TODO: type description
            here.
        formats (list of string): TODO: type description here.
        bitrate (int): TODO: type description here.
        timestamp (TransportStreamTimestampEnum): TODO: type description
            here.
        required_http_headers (dict): TODO: type description here.
        transcoding_url (string): TODO: type description here.
        transcoding_sub_protocol (string): TODO: type description here.
        transcoding_container (string): TODO: type description here.
        analyze_duration_ms (int): TODO: type description here.
        default_audio_stream_index (int): TODO: type description here.
        default_subtitle_stream_index (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protocol": "Protocol",
        "id": "Id",
        "path": "Path",
        "encoder_path": "EncoderPath",
        "encoder_protocol": "EncoderProtocol",
        "mtype": "Type",
        "container": "Container",
        "size": "Size",
        "name": "Name",
        "is_remote": "IsRemote",
        "e_tag": "ETag",
        "run_time_ticks": "RunTimeTicks",
        "read_at_native_framerate": "ReadAtNativeFramerate",
        "ignore_dts": "IgnoreDts",
        "ignore_index": "IgnoreIndex",
        "gen_pts_input": "GenPtsInput",
        "supports_transcoding": "SupportsTranscoding",
        "supports_direct_stream": "SupportsDirectStream",
        "supports_direct_play": "SupportsDirectPlay",
        "is_infinite_stream": "IsInfiniteStream",
        "requires_opening": "RequiresOpening",
        "open_token": "OpenToken",
        "requires_closing": "RequiresClosing",
        "live_stream_id": "LiveStreamId",
        "buffer_ms": "BufferMs",
        "requires_looping": "RequiresLooping",
        "supports_probing": "SupportsProbing",
        "video_type": "VideoType",
        "iso_type": "IsoType",
        "video_3_d_format": "Video3DFormat",
        "media_streams": "MediaStreams",
        "media_attachments": "MediaAttachments",
        "formats": "Formats",
        "bitrate": "Bitrate",
        "timestamp": "Timestamp",
        "required_http_headers": "RequiredHttpHeaders",
        "transcoding_url": "TranscodingUrl",
        "transcoding_sub_protocol": "TranscodingSubProtocol",
        "transcoding_container": "TranscodingContainer",
        "analyze_duration_ms": "AnalyzeDurationMs",
        "default_audio_stream_index": "DefaultAudioStreamIndex",
        "default_subtitle_stream_index": "DefaultSubtitleStreamIndex",
    }

    _optionals = [
        "protocol",
        "id",
        "path",
        "encoder_path",
        "encoder_protocol",
        "mtype",
        "container",
        "size",
        "name",
        "is_remote",
        "e_tag",
        "run_time_ticks",
        "read_at_native_framerate",
        "ignore_dts",
        "ignore_index",
        "gen_pts_input",
        "supports_transcoding",
        "supports_direct_stream",
        "supports_direct_play",
        "is_infinite_stream",
        "requires_opening",
        "open_token",
        "requires_closing",
        "live_stream_id",
        "buffer_ms",
        "requires_looping",
        "supports_probing",
        "video_type",
        "iso_type",
        "video_3_d_format",
        "media_streams",
        "media_attachments",
        "formats",
        "bitrate",
        "timestamp",
        "required_http_headers",
        "transcoding_url",
        "transcoding_sub_protocol",
        "transcoding_container",
        "analyze_duration_ms",
        "default_audio_stream_index",
        "default_subtitle_stream_index",
    ]

    _nullables = [
        "id",
        "path",
        "encoder_path",
        "encoder_protocol",
        "container",
        "size",
        "name",
        "e_tag",
        "run_time_ticks",
        "open_token",
        "live_stream_id",
        "buffer_ms",
        "video_type",
        "iso_type",
        "video_3_d_format",
        "media_streams",
        "media_attachments",
        "formats",
        "bitrate",
        "timestamp",
        "required_http_headers",
        "transcoding_url",
        "transcoding_sub_protocol",
        "transcoding_container",
        "analyze_duration_ms",
        "default_audio_stream_index",
        "default_subtitle_stream_index",
    ]

    def __init__(
        self,
        protocol=APIHelper.SKIP,
        id=APIHelper.SKIP,
        path=APIHelper.SKIP,
        encoder_path=APIHelper.SKIP,
        encoder_protocol=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        container=APIHelper.SKIP,
        size=APIHelper.SKIP,
        name=APIHelper.SKIP,
        is_remote=APIHelper.SKIP,
        e_tag=APIHelper.SKIP,
        run_time_ticks=APIHelper.SKIP,
        read_at_native_framerate=APIHelper.SKIP,
        ignore_dts=APIHelper.SKIP,
        ignore_index=APIHelper.SKIP,
        gen_pts_input=APIHelper.SKIP,
        supports_transcoding=APIHelper.SKIP,
        supports_direct_stream=APIHelper.SKIP,
        supports_direct_play=APIHelper.SKIP,
        is_infinite_stream=APIHelper.SKIP,
        requires_opening=APIHelper.SKIP,
        open_token=APIHelper.SKIP,
        requires_closing=APIHelper.SKIP,
        live_stream_id=APIHelper.SKIP,
        buffer_ms=APIHelper.SKIP,
        requires_looping=APIHelper.SKIP,
        supports_probing=APIHelper.SKIP,
        video_type=APIHelper.SKIP,
        iso_type=APIHelper.SKIP,
        video_3_d_format=APIHelper.SKIP,
        media_streams=APIHelper.SKIP,
        media_attachments=APIHelper.SKIP,
        formats=APIHelper.SKIP,
        bitrate=APIHelper.SKIP,
        timestamp=APIHelper.SKIP,
        required_http_headers=APIHelper.SKIP,
        transcoding_url=APIHelper.SKIP,
        transcoding_sub_protocol=APIHelper.SKIP,
        transcoding_container=APIHelper.SKIP,
        analyze_duration_ms=APIHelper.SKIP,
        default_audio_stream_index=APIHelper.SKIP,
        default_subtitle_stream_index=APIHelper.SKIP,
    ):
        """Constructor for the MediaSourceInfo class"""

        # Initialize members of the class
        if protocol is not APIHelper.SKIP:
            self.protocol = protocol
        if id is not APIHelper.SKIP:
            self.id = id
        if path is not APIHelper.SKIP:
            self.path = path
        if encoder_path is not APIHelper.SKIP:
            self.encoder_path = encoder_path
        if encoder_protocol is not APIHelper.SKIP:
            self.encoder_protocol = encoder_protocol
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if container is not APIHelper.SKIP:
            self.container = container
        if size is not APIHelper.SKIP:
            self.size = size
        if name is not APIHelper.SKIP:
            self.name = name
        if is_remote is not APIHelper.SKIP:
            self.is_remote = is_remote
        if e_tag is not APIHelper.SKIP:
            self.e_tag = e_tag
        if run_time_ticks is not APIHelper.SKIP:
            self.run_time_ticks = run_time_ticks
        if read_at_native_framerate is not APIHelper.SKIP:
            self.read_at_native_framerate = read_at_native_framerate
        if ignore_dts is not APIHelper.SKIP:
            self.ignore_dts = ignore_dts
        if ignore_index is not APIHelper.SKIP:
            self.ignore_index = ignore_index
        if gen_pts_input is not APIHelper.SKIP:
            self.gen_pts_input = gen_pts_input
        if supports_transcoding is not APIHelper.SKIP:
            self.supports_transcoding = supports_transcoding
        if supports_direct_stream is not APIHelper.SKIP:
            self.supports_direct_stream = supports_direct_stream
        if supports_direct_play is not APIHelper.SKIP:
            self.supports_direct_play = supports_direct_play
        if is_infinite_stream is not APIHelper.SKIP:
            self.is_infinite_stream = is_infinite_stream
        if requires_opening is not APIHelper.SKIP:
            self.requires_opening = requires_opening
        if open_token is not APIHelper.SKIP:
            self.open_token = open_token
        if requires_closing is not APIHelper.SKIP:
            self.requires_closing = requires_closing
        if live_stream_id is not APIHelper.SKIP:
            self.live_stream_id = live_stream_id
        if buffer_ms is not APIHelper.SKIP:
            self.buffer_ms = buffer_ms
        if requires_looping is not APIHelper.SKIP:
            self.requires_looping = requires_looping
        if supports_probing is not APIHelper.SKIP:
            self.supports_probing = supports_probing
        if video_type is not APIHelper.SKIP:
            self.video_type = video_type
        if iso_type is not APIHelper.SKIP:
            self.iso_type = iso_type
        if video_3_d_format is not APIHelper.SKIP:
            self.video_3_d_format = video_3_d_format
        if media_streams is not APIHelper.SKIP:
            self.media_streams = media_streams
        if media_attachments is not APIHelper.SKIP:
            self.media_attachments = media_attachments
        if formats is not APIHelper.SKIP:
            self.formats = formats
        if bitrate is not APIHelper.SKIP:
            self.bitrate = bitrate
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp
        if required_http_headers is not APIHelper.SKIP:
            self.required_http_headers = required_http_headers
        if transcoding_url is not APIHelper.SKIP:
            self.transcoding_url = transcoding_url
        if transcoding_sub_protocol is not APIHelper.SKIP:
            self.transcoding_sub_protocol = transcoding_sub_protocol
        if transcoding_container is not APIHelper.SKIP:
            self.transcoding_container = transcoding_container
        if analyze_duration_ms is not APIHelper.SKIP:
            self.analyze_duration_ms = analyze_duration_ms
        if default_audio_stream_index is not APIHelper.SKIP:
            self.default_audio_stream_index = default_audio_stream_index
        if default_subtitle_stream_index is not APIHelper.SKIP:
            self.default_subtitle_stream_index = default_subtitle_stream_index

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

        protocol = (
            dictionary.get("Protocol") if dictionary.get("Protocol") else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        encoder_path = (
            dictionary.get("EncoderPath")
            if "EncoderPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        encoder_protocol = (
            dictionary.get("EncoderProtocol")
            if "EncoderProtocol" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        size = dictionary.get("Size") if "Size" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        is_remote = (
            dictionary.get("IsRemote")
            if "IsRemote" in dictionary.keys()
            else APIHelper.SKIP
        )
        e_tag = (
            dictionary.get("ETag") if "ETag" in dictionary.keys() else APIHelper.SKIP
        )
        run_time_ticks = (
            dictionary.get("RunTimeTicks")
            if "RunTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        read_at_native_framerate = (
            dictionary.get("ReadAtNativeFramerate")
            if "ReadAtNativeFramerate" in dictionary.keys()
            else APIHelper.SKIP
        )
        ignore_dts = (
            dictionary.get("IgnoreDts")
            if "IgnoreDts" in dictionary.keys()
            else APIHelper.SKIP
        )
        ignore_index = (
            dictionary.get("IgnoreIndex")
            if "IgnoreIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        gen_pts_input = (
            dictionary.get("GenPtsInput")
            if "GenPtsInput" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_transcoding = (
            dictionary.get("SupportsTranscoding")
            if "SupportsTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_direct_stream = (
            dictionary.get("SupportsDirectStream")
            if "SupportsDirectStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_direct_play = (
            dictionary.get("SupportsDirectPlay")
            if "SupportsDirectPlay" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_infinite_stream = (
            dictionary.get("IsInfiniteStream")
            if "IsInfiniteStream" in dictionary.keys()
            else APIHelper.SKIP
        )
        requires_opening = (
            dictionary.get("RequiresOpening")
            if "RequiresOpening" in dictionary.keys()
            else APIHelper.SKIP
        )
        open_token = (
            dictionary.get("OpenToken")
            if "OpenToken" in dictionary.keys()
            else APIHelper.SKIP
        )
        requires_closing = (
            dictionary.get("RequiresClosing")
            if "RequiresClosing" in dictionary.keys()
            else APIHelper.SKIP
        )
        live_stream_id = (
            dictionary.get("LiveStreamId")
            if "LiveStreamId" in dictionary.keys()
            else APIHelper.SKIP
        )
        buffer_ms = (
            dictionary.get("BufferMs")
            if "BufferMs" in dictionary.keys()
            else APIHelper.SKIP
        )
        requires_looping = (
            dictionary.get("RequiresLooping")
            if "RequiresLooping" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_probing = (
            dictionary.get("SupportsProbing")
            if "SupportsProbing" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_type = (
            dictionary.get("VideoType")
            if "VideoType" in dictionary.keys()
            else APIHelper.SKIP
        )
        iso_type = (
            dictionary.get("IsoType")
            if "IsoType" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_3_d_format = (
            dictionary.get("Video3DFormat")
            if "Video3DFormat" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "MediaStreams" in dictionary.keys():
            media_streams = (
                [MediaStream.from_dictionary(x) for x in dictionary.get("MediaStreams")]
                if dictionary.get("MediaStreams")
                else None
            )
        else:
            media_streams = APIHelper.SKIP
        if "MediaAttachments" in dictionary.keys():
            media_attachments = (
                [
                    MediaAttachment.from_dictionary(x)
                    for x in dictionary.get("MediaAttachments")
                ]
                if dictionary.get("MediaAttachments")
                else None
            )
        else:
            media_attachments = APIHelper.SKIP
        formats = (
            dictionary.get("Formats")
            if "Formats" in dictionary.keys()
            else APIHelper.SKIP
        )
        bitrate = (
            dictionary.get("Bitrate")
            if "Bitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        timestamp = (
            dictionary.get("Timestamp")
            if "Timestamp" in dictionary.keys()
            else APIHelper.SKIP
        )
        required_http_headers = (
            dictionary.get("RequiredHttpHeaders")
            if "RequiredHttpHeaders" in dictionary.keys()
            else APIHelper.SKIP
        )
        transcoding_url = (
            dictionary.get("TranscodingUrl")
            if "TranscodingUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        transcoding_sub_protocol = (
            dictionary.get("TranscodingSubProtocol")
            if "TranscodingSubProtocol" in dictionary.keys()
            else APIHelper.SKIP
        )
        transcoding_container = (
            dictionary.get("TranscodingContainer")
            if "TranscodingContainer" in dictionary.keys()
            else APIHelper.SKIP
        )
        analyze_duration_ms = (
            dictionary.get("AnalyzeDurationMs")
            if "AnalyzeDurationMs" in dictionary.keys()
            else APIHelper.SKIP
        )
        default_audio_stream_index = (
            dictionary.get("DefaultAudioStreamIndex")
            if "DefaultAudioStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        default_subtitle_stream_index = (
            dictionary.get("DefaultSubtitleStreamIndex")
            if "DefaultSubtitleStreamIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            protocol,
            id,
            path,
            encoder_path,
            encoder_protocol,
            mtype,
            container,
            size,
            name,
            is_remote,
            e_tag,
            run_time_ticks,
            read_at_native_framerate,
            ignore_dts,
            ignore_index,
            gen_pts_input,
            supports_transcoding,
            supports_direct_stream,
            supports_direct_play,
            is_infinite_stream,
            requires_opening,
            open_token,
            requires_closing,
            live_stream_id,
            buffer_ms,
            requires_looping,
            supports_probing,
            video_type,
            iso_type,
            video_3_d_format,
            media_streams,
            media_attachments,
            formats,
            bitrate,
            timestamp,
            required_http_headers,
            transcoding_url,
            transcoding_sub_protocol,
            transcoding_container,
            analyze_duration_ms,
            default_audio_stream_index,
            default_subtitle_stream_index,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        protocol = XmlUtilities.value_from_xml_element(root.find("Protocol"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        encoder_path = XmlUtilities.value_from_xml_element(
            root.find("EncoderPath"), str
        )
        encoder_protocol = XmlUtilities.value_from_xml_element(
            root.find("EncoderProtocol"), str
        )
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        size = XmlUtilities.value_from_xml_element(root.find("Size"), int)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        is_remote = XmlUtilities.value_from_xml_element(root.find("IsRemote"), bool)
        e_tag = XmlUtilities.value_from_xml_element(root.find("ETag"), str)
        run_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("RunTimeTicks"), int
        )
        read_at_native_framerate = XmlUtilities.value_from_xml_element(
            root.find("ReadAtNativeFramerate"), bool
        )
        ignore_dts = XmlUtilities.value_from_xml_element(root.find("IgnoreDts"), bool)
        ignore_index = XmlUtilities.value_from_xml_element(
            root.find("IgnoreIndex"), bool
        )
        gen_pts_input = XmlUtilities.value_from_xml_element(
            root.find("GenPtsInput"), bool
        )
        supports_transcoding = XmlUtilities.value_from_xml_element(
            root.find("SupportsTranscoding"), bool
        )
        supports_direct_stream = XmlUtilities.value_from_xml_element(
            root.find("SupportsDirectStream"), bool
        )
        supports_direct_play = XmlUtilities.value_from_xml_element(
            root.find("SupportsDirectPlay"), bool
        )
        is_infinite_stream = XmlUtilities.value_from_xml_element(
            root.find("IsInfiniteStream"), bool
        )
        requires_opening = XmlUtilities.value_from_xml_element(
            root.find("RequiresOpening"), bool
        )
        open_token = XmlUtilities.value_from_xml_element(root.find("OpenToken"), str)
        requires_closing = XmlUtilities.value_from_xml_element(
            root.find("RequiresClosing"), bool
        )
        live_stream_id = XmlUtilities.value_from_xml_element(
            root.find("LiveStreamId"), str
        )
        buffer_ms = XmlUtilities.value_from_xml_element(root.find("BufferMs"), int)
        requires_looping = XmlUtilities.value_from_xml_element(
            root.find("RequiresLooping"), bool
        )
        supports_probing = XmlUtilities.value_from_xml_element(
            root.find("SupportsProbing"), bool
        )
        video_type = XmlUtilities.value_from_xml_element(root.find("VideoType"), str)
        iso_type = XmlUtilities.value_from_xml_element(root.find("IsoType"), str)
        video_3_d_format = XmlUtilities.value_from_xml_element(
            root.find("Video3DFormat"), str
        )
        media_streams = XmlUtilities.list_from_xml_element(
            root, "MediaStream", MediaStream
        )
        media_attachments = XmlUtilities.list_from_xml_element(
            root, "MediaAttachment", MediaAttachment
        )
        formats = XmlUtilities.list_from_xml_element(root, "Formats", str)
        bitrate = XmlUtilities.value_from_xml_element(root.find("Bitrate"), int)
        timestamp = XmlUtilities.value_from_xml_element(root.find("Timestamp"), str)
        required_http_headers = XmlUtilities.dict_from_xml_element(
            root.find("RequiredHttpHeaders"), dict
        )

        transcoding_url = XmlUtilities.value_from_xml_element(
            root.find("TranscodingUrl"), str
        )
        transcoding_sub_protocol = XmlUtilities.value_from_xml_element(
            root.find("TranscodingSubProtocol"), str
        )
        transcoding_container = XmlUtilities.value_from_xml_element(
            root.find("TranscodingContainer"), str
        )
        analyze_duration_ms = XmlUtilities.value_from_xml_element(
            root.find("AnalyzeDurationMs"), int
        )
        default_audio_stream_index = XmlUtilities.value_from_xml_element(
            root.find("DefaultAudioStreamIndex"), int
        )
        default_subtitle_stream_index = XmlUtilities.value_from_xml_element(
            root.find("DefaultSubtitleStreamIndex"), int
        )

        return cls(
            protocol,
            id,
            path,
            encoder_path,
            encoder_protocol,
            mtype,
            container,
            size,
            name,
            is_remote,
            e_tag,
            run_time_ticks,
            read_at_native_framerate,
            ignore_dts,
            ignore_index,
            gen_pts_input,
            supports_transcoding,
            supports_direct_stream,
            supports_direct_play,
            is_infinite_stream,
            requires_opening,
            open_token,
            requires_closing,
            live_stream_id,
            buffer_ms,
            requires_looping,
            supports_probing,
            video_type,
            iso_type,
            video_3_d_format,
            media_streams,
            media_attachments,
            formats,
            bitrate,
            timestamp,
            required_http_headers,
            transcoding_url,
            transcoding_sub_protocol,
            transcoding_container,
            analyze_duration_ms,
            default_audio_stream_index,
            default_subtitle_stream_index,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.protocol, "Protocol")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.encoder_path, "EncoderPath")
        XmlUtilities.add_as_subelement(root, self.encoder_protocol, "EncoderProtocol")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.size, "Size")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.is_remote, "IsRemote")
        XmlUtilities.add_as_subelement(root, self.e_tag, "ETag")
        XmlUtilities.add_as_subelement(root, self.run_time_ticks, "RunTimeTicks")
        XmlUtilities.add_as_subelement(
            root, self.read_at_native_framerate, "ReadAtNativeFramerate"
        )
        XmlUtilities.add_as_subelement(root, self.ignore_dts, "IgnoreDts")
        XmlUtilities.add_as_subelement(root, self.ignore_index, "IgnoreIndex")
        XmlUtilities.add_as_subelement(root, self.gen_pts_input, "GenPtsInput")
        XmlUtilities.add_as_subelement(
            root, self.supports_transcoding, "SupportsTranscoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_direct_stream, "SupportsDirectStream"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_direct_play, "SupportsDirectPlay"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_infinite_stream, "IsInfiniteStream"
        )
        XmlUtilities.add_as_subelement(root, self.requires_opening, "RequiresOpening")
        XmlUtilities.add_as_subelement(root, self.open_token, "OpenToken")
        XmlUtilities.add_as_subelement(root, self.requires_closing, "RequiresClosing")
        XmlUtilities.add_as_subelement(root, self.live_stream_id, "LiveStreamId")
        XmlUtilities.add_as_subelement(root, self.buffer_ms, "BufferMs")
        XmlUtilities.add_as_subelement(root, self.requires_looping, "RequiresLooping")
        XmlUtilities.add_as_subelement(root, self.supports_probing, "SupportsProbing")
        XmlUtilities.add_as_subelement(root, self.video_type, "VideoType")
        XmlUtilities.add_as_subelement(root, self.iso_type, "IsoType")
        XmlUtilities.add_as_subelement(root, self.video_3_d_format, "Video3DFormat")
        XmlUtilities.add_list_as_subelement(root, self.media_streams, "MediaStream")
        XmlUtilities.add_list_as_subelement(
            root, self.media_attachments, "MediaAttachment"
        )
        XmlUtilities.add_list_as_subelement(root, self.formats, "Formats")
        XmlUtilities.add_as_subelement(root, self.bitrate, "Bitrate")
        XmlUtilities.add_as_subelement(root, self.timestamp, "Timestamp")
        XmlUtilities.add_dict_as_subelement(
            root, self.required_http_headers, dictionary_name="RequiredHttpHeaders"
        )
        XmlUtilities.add_as_subelement(root, self.transcoding_url, "TranscodingUrl")
        XmlUtilities.add_as_subelement(
            root, self.transcoding_sub_protocol, "TranscodingSubProtocol"
        )
        XmlUtilities.add_as_subelement(
            root, self.transcoding_container, "TranscodingContainer"
        )
        XmlUtilities.add_as_subelement(
            root, self.analyze_duration_ms, "AnalyzeDurationMs"
        )
        XmlUtilities.add_as_subelement(
            root, self.default_audio_stream_index, "DefaultAudioStreamIndex"
        )
        XmlUtilities.add_as_subelement(
            root, self.default_subtitle_stream_index, "DefaultSubtitleStreamIndex"
        )
