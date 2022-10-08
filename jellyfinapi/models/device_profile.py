# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.codec_profile import CodecProfile
from jellyfinapi.models.container_profile import ContainerProfile
from jellyfinapi.models.device_identification import DeviceIdentification
from jellyfinapi.models.direct_play_profile import DirectPlayProfile
from jellyfinapi.models.response_profile import ResponseProfile
from jellyfinapi.models.subtitle_profile import SubtitleProfile
from jellyfinapi.models.transcoding_profile import TranscodingProfile
from jellyfinapi.models.xml_attribute import XmlAttribute
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceProfile(object):

    """Implementation of the 'DeviceProfile' model.

    A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which
    determines which content a certain device is able to play.
    <br />
    Specifically, it defines the supported <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers
    </see> and
    <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see>
    (video and/or audio, including codec profiles and levels)
    the device is able to direct play (without transcoding or remuxing),
    as well as which <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containe
    rs/codecs to transcode to</see> in case it isn't.

    Attributes:
        name (string): Gets or sets the name of this device profile.
        id (string): Gets or sets the Id.
        identification (DeviceIdentification): Gets or sets the
            Identification.
        friendly_name (string): Gets or sets the friendly name of the device
            profile, which can be shown to users.
        manufacturer (string): Gets or sets the manufacturer of the device
            which this profile represents.
        manufacturer_url (string): Gets or sets an url for the manufacturer of
            the device which this profile represents.
        model_name (string): Gets or sets the model name of the device which
            this profile represents.
        model_description (string): Gets or sets the model description of the
            device which this profile represents.
        model_number (string): Gets or sets the model number of the device
            which this profile represents.
        model_url (string): Gets or sets the ModelUrl.
        serial_number (string): Gets or sets the serial number of the device
            which this profile represents.
        enable_album_art_in_didl (bool): Gets or sets a value indicating
            whether EnableAlbumArtInDidl.
        enable_single_album_art_limit (bool): Gets or sets a value indicating
            whether EnableSingleAlbumArtLimit.
        enable_single_subtitle_limit (bool): Gets or sets a value indicating
            whether EnableSingleSubtitleLimit.
        supported_media_types (string): Gets or sets the SupportedMediaTypes.
        user_id (string): Gets or sets the UserId.
        album_art_pn (string): Gets or sets the AlbumArtPn.
        max_album_art_width (int): Gets or sets the MaxAlbumArtWidth.
        max_album_art_height (int): Gets or sets the MaxAlbumArtHeight.
        max_icon_width (int): Gets or sets the maximum allowed width of
            embedded icons.
        max_icon_height (int): Gets or sets the maximum allowed height of
            embedded icons.
        max_streaming_bitrate (int): Gets or sets the maximum allowed bitrate
            for all streamed content.
        max_static_bitrate (int): Gets or sets the maximum allowed bitrate for
            statically streamed content (= direct played files).
        music_streaming_transcoding_bitrate (int): Gets or sets the maximum
            allowed bitrate for transcoded music streams.
        max_static_music_bitrate (int): Gets or sets the maximum allowed
            bitrate for statically streamed (= direct played) music files.
        sony_aggregation_flags (string): Gets or sets the content of the
            aggregationFlags element in the urn:schemas-sonycom:av namespace.
        protocol_info (string): Gets or sets the ProtocolInfo.
        timeline_offset_seconds (int): Gets or sets the
            TimelineOffsetSeconds.
        requires_plain_video_items (bool): Gets or sets a value indicating
            whether RequiresPlainVideoItems.
        requires_plain_folders (bool): Gets or sets a value indicating whether
            RequiresPlainFolders.
        enable_ms_media_receiver_registrar (bool): Gets or sets a value
            indicating whether EnableMSMediaReceiverRegistrar.
        ignore_transcode_byte_range_requests (bool): Gets or sets a value
            indicating whether IgnoreTranscodeByteRangeRequests.
        xml_root_attributes (list of XmlAttribute): Gets or sets the
            XmlRootAttributes.
        direct_play_profiles (list of DirectPlayProfile): Gets or sets the
            direct play profiles.
        transcoding_profiles (list of TranscodingProfile): Gets or sets the
            transcoding profiles.
        container_profiles (list of ContainerProfile): Gets or sets the
            container profiles.
        codec_profiles (list of CodecProfile): Gets or sets the codec
            profiles.
        response_profiles (list of ResponseProfile): Gets or sets the
            ResponseProfiles.
        subtitle_profiles (list of SubtitleProfile): Gets or sets the subtitle
            profiles.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "id": "Id",
        "identification": "Identification",
        "friendly_name": "FriendlyName",
        "manufacturer": "Manufacturer",
        "manufacturer_url": "ManufacturerUrl",
        "model_name": "ModelName",
        "model_description": "ModelDescription",
        "model_number": "ModelNumber",
        "model_url": "ModelUrl",
        "serial_number": "SerialNumber",
        "enable_album_art_in_didl": "EnableAlbumArtInDidl",
        "enable_single_album_art_limit": "EnableSingleAlbumArtLimit",
        "enable_single_subtitle_limit": "EnableSingleSubtitleLimit",
        "supported_media_types": "SupportedMediaTypes",
        "user_id": "UserId",
        "album_art_pn": "AlbumArtPn",
        "max_album_art_width": "MaxAlbumArtWidth",
        "max_album_art_height": "MaxAlbumArtHeight",
        "max_icon_width": "MaxIconWidth",
        "max_icon_height": "MaxIconHeight",
        "max_streaming_bitrate": "MaxStreamingBitrate",
        "max_static_bitrate": "MaxStaticBitrate",
        "music_streaming_transcoding_bitrate": "MusicStreamingTranscodingBitrate",
        "max_static_music_bitrate": "MaxStaticMusicBitrate",
        "sony_aggregation_flags": "SonyAggregationFlags",
        "protocol_info": "ProtocolInfo",
        "timeline_offset_seconds": "TimelineOffsetSeconds",
        "requires_plain_video_items": "RequiresPlainVideoItems",
        "requires_plain_folders": "RequiresPlainFolders",
        "enable_ms_media_receiver_registrar": "EnableMSMediaReceiverRegistrar",
        "ignore_transcode_byte_range_requests": "IgnoreTranscodeByteRangeRequests",
        "xml_root_attributes": "XmlRootAttributes",
        "direct_play_profiles": "DirectPlayProfiles",
        "transcoding_profiles": "TranscodingProfiles",
        "container_profiles": "ContainerProfiles",
        "codec_profiles": "CodecProfiles",
        "response_profiles": "ResponseProfiles",
        "subtitle_profiles": "SubtitleProfiles",
    }

    _optionals = [
        "name",
        "id",
        "identification",
        "friendly_name",
        "manufacturer",
        "manufacturer_url",
        "model_name",
        "model_description",
        "model_number",
        "model_url",
        "serial_number",
        "enable_album_art_in_didl",
        "enable_single_album_art_limit",
        "enable_single_subtitle_limit",
        "supported_media_types",
        "user_id",
        "album_art_pn",
        "max_album_art_width",
        "max_album_art_height",
        "max_icon_width",
        "max_icon_height",
        "max_streaming_bitrate",
        "max_static_bitrate",
        "music_streaming_transcoding_bitrate",
        "max_static_music_bitrate",
        "sony_aggregation_flags",
        "protocol_info",
        "timeline_offset_seconds",
        "requires_plain_video_items",
        "requires_plain_folders",
        "enable_ms_media_receiver_registrar",
        "ignore_transcode_byte_range_requests",
        "xml_root_attributes",
        "direct_play_profiles",
        "transcoding_profiles",
        "container_profiles",
        "codec_profiles",
        "response_profiles",
        "subtitle_profiles",
    ]

    _nullables = [
        "name",
        "id",
        "identification",
        "friendly_name",
        "manufacturer",
        "manufacturer_url",
        "model_name",
        "model_description",
        "model_number",
        "model_url",
        "serial_number",
        "user_id",
        "album_art_pn",
        "max_album_art_width",
        "max_album_art_height",
        "max_icon_width",
        "max_icon_height",
        "max_streaming_bitrate",
        "max_static_bitrate",
        "music_streaming_transcoding_bitrate",
        "max_static_music_bitrate",
        "sony_aggregation_flags",
        "protocol_info",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        id=APIHelper.SKIP,
        identification=APIHelper.SKIP,
        friendly_name=APIHelper.SKIP,
        manufacturer=APIHelper.SKIP,
        manufacturer_url=APIHelper.SKIP,
        model_name=APIHelper.SKIP,
        model_description=APIHelper.SKIP,
        model_number=APIHelper.SKIP,
        model_url=APIHelper.SKIP,
        serial_number=APIHelper.SKIP,
        enable_album_art_in_didl=False,
        enable_single_album_art_limit=False,
        enable_single_subtitle_limit=False,
        supported_media_types=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        album_art_pn=APIHelper.SKIP,
        max_album_art_width=APIHelper.SKIP,
        max_album_art_height=APIHelper.SKIP,
        max_icon_width=APIHelper.SKIP,
        max_icon_height=APIHelper.SKIP,
        max_streaming_bitrate=APIHelper.SKIP,
        max_static_bitrate=APIHelper.SKIP,
        music_streaming_transcoding_bitrate=APIHelper.SKIP,
        max_static_music_bitrate=APIHelper.SKIP,
        sony_aggregation_flags=APIHelper.SKIP,
        protocol_info=APIHelper.SKIP,
        timeline_offset_seconds=0,
        requires_plain_video_items=False,
        requires_plain_folders=False,
        enable_ms_media_receiver_registrar=False,
        ignore_transcode_byte_range_requests=False,
        xml_root_attributes=APIHelper.SKIP,
        direct_play_profiles=APIHelper.SKIP,
        transcoding_profiles=APIHelper.SKIP,
        container_profiles=APIHelper.SKIP,
        codec_profiles=APIHelper.SKIP,
        response_profiles=APIHelper.SKIP,
        subtitle_profiles=APIHelper.SKIP,
    ):
        """Constructor for the DeviceProfile class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if id is not APIHelper.SKIP:
            self.id = id
        if identification is not APIHelper.SKIP:
            self.identification = identification
        if friendly_name is not APIHelper.SKIP:
            self.friendly_name = friendly_name
        if manufacturer is not APIHelper.SKIP:
            self.manufacturer = manufacturer
        if manufacturer_url is not APIHelper.SKIP:
            self.manufacturer_url = manufacturer_url
        if model_name is not APIHelper.SKIP:
            self.model_name = model_name
        if model_description is not APIHelper.SKIP:
            self.model_description = model_description
        if model_number is not APIHelper.SKIP:
            self.model_number = model_number
        if model_url is not APIHelper.SKIP:
            self.model_url = model_url
        if serial_number is not APIHelper.SKIP:
            self.serial_number = serial_number
        self.enable_album_art_in_didl = enable_album_art_in_didl
        self.enable_single_album_art_limit = enable_single_album_art_limit
        self.enable_single_subtitle_limit = enable_single_subtitle_limit
        if supported_media_types is not APIHelper.SKIP:
            self.supported_media_types = supported_media_types
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if album_art_pn is not APIHelper.SKIP:
            self.album_art_pn = album_art_pn
        if max_album_art_width is not APIHelper.SKIP:
            self.max_album_art_width = max_album_art_width
        if max_album_art_height is not APIHelper.SKIP:
            self.max_album_art_height = max_album_art_height
        if max_icon_width is not APIHelper.SKIP:
            self.max_icon_width = max_icon_width
        if max_icon_height is not APIHelper.SKIP:
            self.max_icon_height = max_icon_height
        if max_streaming_bitrate is not APIHelper.SKIP:
            self.max_streaming_bitrate = max_streaming_bitrate
        if max_static_bitrate is not APIHelper.SKIP:
            self.max_static_bitrate = max_static_bitrate
        if music_streaming_transcoding_bitrate is not APIHelper.SKIP:
            self.music_streaming_transcoding_bitrate = (
                music_streaming_transcoding_bitrate
            )
        if max_static_music_bitrate is not APIHelper.SKIP:
            self.max_static_music_bitrate = max_static_music_bitrate
        if sony_aggregation_flags is not APIHelper.SKIP:
            self.sony_aggregation_flags = sony_aggregation_flags
        if protocol_info is not APIHelper.SKIP:
            self.protocol_info = protocol_info
        self.timeline_offset_seconds = timeline_offset_seconds
        self.requires_plain_video_items = requires_plain_video_items
        self.requires_plain_folders = requires_plain_folders
        self.enable_ms_media_receiver_registrar = enable_ms_media_receiver_registrar
        self.ignore_transcode_byte_range_requests = ignore_transcode_byte_range_requests
        if xml_root_attributes is not APIHelper.SKIP:
            self.xml_root_attributes = xml_root_attributes
        if direct_play_profiles is not APIHelper.SKIP:
            self.direct_play_profiles = direct_play_profiles
        if transcoding_profiles is not APIHelper.SKIP:
            self.transcoding_profiles = transcoding_profiles
        if container_profiles is not APIHelper.SKIP:
            self.container_profiles = container_profiles
        if codec_profiles is not APIHelper.SKIP:
            self.codec_profiles = codec_profiles
        if response_profiles is not APIHelper.SKIP:
            self.response_profiles = response_profiles
        if subtitle_profiles is not APIHelper.SKIP:
            self.subtitle_profiles = subtitle_profiles

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        if "Identification" in dictionary.keys():
            identification = (
                DeviceIdentification.from_dictionary(dictionary.get("Identification"))
                if dictionary.get("Identification")
                else None
            )
        else:
            identification = APIHelper.SKIP
        friendly_name = (
            dictionary.get("FriendlyName")
            if "FriendlyName" in dictionary.keys()
            else APIHelper.SKIP
        )
        manufacturer = (
            dictionary.get("Manufacturer")
            if "Manufacturer" in dictionary.keys()
            else APIHelper.SKIP
        )
        manufacturer_url = (
            dictionary.get("ManufacturerUrl")
            if "ManufacturerUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        model_name = (
            dictionary.get("ModelName")
            if "ModelName" in dictionary.keys()
            else APIHelper.SKIP
        )
        model_description = (
            dictionary.get("ModelDescription")
            if "ModelDescription" in dictionary.keys()
            else APIHelper.SKIP
        )
        model_number = (
            dictionary.get("ModelNumber")
            if "ModelNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        model_url = (
            dictionary.get("ModelUrl")
            if "ModelUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        serial_number = (
            dictionary.get("SerialNumber")
            if "SerialNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_album_art_in_didl = (
            dictionary.get("EnableAlbumArtInDidl")
            if dictionary.get("EnableAlbumArtInDidl")
            else False
        )
        enable_single_album_art_limit = (
            dictionary.get("EnableSingleAlbumArtLimit")
            if dictionary.get("EnableSingleAlbumArtLimit")
            else False
        )
        enable_single_subtitle_limit = (
            dictionary.get("EnableSingleSubtitleLimit")
            if dictionary.get("EnableSingleSubtitleLimit")
            else False
        )
        supported_media_types = (
            dictionary.get("SupportedMediaTypes")
            if dictionary.get("SupportedMediaTypes")
            else APIHelper.SKIP
        )
        user_id = (
            dictionary.get("UserId")
            if "UserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_art_pn = (
            dictionary.get("AlbumArtPn")
            if "AlbumArtPn" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_album_art_width = (
            dictionary.get("MaxAlbumArtWidth")
            if "MaxAlbumArtWidth" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_album_art_height = (
            dictionary.get("MaxAlbumArtHeight")
            if "MaxAlbumArtHeight" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_icon_width = (
            dictionary.get("MaxIconWidth")
            if "MaxIconWidth" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_icon_height = (
            dictionary.get("MaxIconHeight")
            if "MaxIconHeight" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_streaming_bitrate = (
            dictionary.get("MaxStreamingBitrate")
            if "MaxStreamingBitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_static_bitrate = (
            dictionary.get("MaxStaticBitrate")
            if "MaxStaticBitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        music_streaming_transcoding_bitrate = (
            dictionary.get("MusicStreamingTranscodingBitrate")
            if "MusicStreamingTranscodingBitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_static_music_bitrate = (
            dictionary.get("MaxStaticMusicBitrate")
            if "MaxStaticMusicBitrate" in dictionary.keys()
            else APIHelper.SKIP
        )
        sony_aggregation_flags = (
            dictionary.get("SonyAggregationFlags")
            if "SonyAggregationFlags" in dictionary.keys()
            else APIHelper.SKIP
        )
        protocol_info = (
            dictionary.get("ProtocolInfo")
            if "ProtocolInfo" in dictionary.keys()
            else APIHelper.SKIP
        )
        timeline_offset_seconds = (
            dictionary.get("TimelineOffsetSeconds")
            if dictionary.get("TimelineOffsetSeconds")
            else 0
        )
        requires_plain_video_items = (
            dictionary.get("RequiresPlainVideoItems")
            if dictionary.get("RequiresPlainVideoItems")
            else False
        )
        requires_plain_folders = (
            dictionary.get("RequiresPlainFolders")
            if dictionary.get("RequiresPlainFolders")
            else False
        )
        enable_ms_media_receiver_registrar = (
            dictionary.get("EnableMSMediaReceiverRegistrar")
            if dictionary.get("EnableMSMediaReceiverRegistrar")
            else False
        )
        ignore_transcode_byte_range_requests = (
            dictionary.get("IgnoreTranscodeByteRangeRequests")
            if dictionary.get("IgnoreTranscodeByteRangeRequests")
            else False
        )
        xml_root_attributes = None
        if dictionary.get("XmlRootAttributes") is not None:
            xml_root_attributes = [
                XmlAttribute.from_dictionary(x)
                for x in dictionary.get("XmlRootAttributes")
            ]
        else:
            xml_root_attributes = APIHelper.SKIP
        direct_play_profiles = None
        if dictionary.get("DirectPlayProfiles") is not None:
            direct_play_profiles = [
                DirectPlayProfile.from_dictionary(x)
                for x in dictionary.get("DirectPlayProfiles")
            ]
        else:
            direct_play_profiles = APIHelper.SKIP
        transcoding_profiles = None
        if dictionary.get("TranscodingProfiles") is not None:
            transcoding_profiles = [
                TranscodingProfile.from_dictionary(x)
                for x in dictionary.get("TranscodingProfiles")
            ]
        else:
            transcoding_profiles = APIHelper.SKIP
        container_profiles = None
        if dictionary.get("ContainerProfiles") is not None:
            container_profiles = [
                ContainerProfile.from_dictionary(x)
                for x in dictionary.get("ContainerProfiles")
            ]
        else:
            container_profiles = APIHelper.SKIP
        codec_profiles = None
        if dictionary.get("CodecProfiles") is not None:
            codec_profiles = [
                CodecProfile.from_dictionary(x) for x in dictionary.get("CodecProfiles")
            ]
        else:
            codec_profiles = APIHelper.SKIP
        response_profiles = None
        if dictionary.get("ResponseProfiles") is not None:
            response_profiles = [
                ResponseProfile.from_dictionary(x)
                for x in dictionary.get("ResponseProfiles")
            ]
        else:
            response_profiles = APIHelper.SKIP
        subtitle_profiles = None
        if dictionary.get("SubtitleProfiles") is not None:
            subtitle_profiles = [
                SubtitleProfile.from_dictionary(x)
                for x in dictionary.get("SubtitleProfiles")
            ]
        else:
            subtitle_profiles = APIHelper.SKIP
        # Return an object of this model
        return cls(
            name,
            id,
            identification,
            friendly_name,
            manufacturer,
            manufacturer_url,
            model_name,
            model_description,
            model_number,
            model_url,
            serial_number,
            enable_album_art_in_didl,
            enable_single_album_art_limit,
            enable_single_subtitle_limit,
            supported_media_types,
            user_id,
            album_art_pn,
            max_album_art_width,
            max_album_art_height,
            max_icon_width,
            max_icon_height,
            max_streaming_bitrate,
            max_static_bitrate,
            music_streaming_transcoding_bitrate,
            max_static_music_bitrate,
            sony_aggregation_flags,
            protocol_info,
            timeline_offset_seconds,
            requires_plain_video_items,
            requires_plain_folders,
            enable_ms_media_receiver_registrar,
            ignore_transcode_byte_range_requests,
            xml_root_attributes,
            direct_play_profiles,
            transcoding_profiles,
            container_profiles,
            codec_profiles,
            response_profiles,
            subtitle_profiles,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        identification = XmlUtilities.value_from_xml_element(
            root.find("DeviceIdentification"), DeviceIdentification
        )
        friendly_name = XmlUtilities.value_from_xml_element(
            root.find("FriendlyName"), str
        )
        manufacturer = XmlUtilities.value_from_xml_element(
            root.find("Manufacturer"), str
        )
        manufacturer_url = XmlUtilities.value_from_xml_element(
            root.find("ManufacturerUrl"), str
        )
        model_name = XmlUtilities.value_from_xml_element(root.find("ModelName"), str)
        model_description = XmlUtilities.value_from_xml_element(
            root.find("ModelDescription"), str
        )
        model_number = XmlUtilities.value_from_xml_element(
            root.find("ModelNumber"), str
        )
        model_url = XmlUtilities.value_from_xml_element(root.find("ModelUrl"), str)
        serial_number = XmlUtilities.value_from_xml_element(
            root.find("SerialNumber"), str
        )
        enable_album_art_in_didl = XmlUtilities.value_from_xml_element(
            root.find("EnableAlbumArtInDidl"), bool
        )
        enable_single_album_art_limit = XmlUtilities.value_from_xml_element(
            root.find("EnableSingleAlbumArtLimit"), bool
        )
        enable_single_subtitle_limit = XmlUtilities.value_from_xml_element(
            root.find("EnableSingleSubtitleLimit"), bool
        )
        supported_media_types = XmlUtilities.value_from_xml_element(
            root.find("SupportedMediaTypes"), str
        )
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        album_art_pn = XmlUtilities.value_from_xml_element(root.find("AlbumArtPn"), str)
        max_album_art_width = XmlUtilities.value_from_xml_element(
            root.find("MaxAlbumArtWidth"), int
        )
        max_album_art_height = XmlUtilities.value_from_xml_element(
            root.find("MaxAlbumArtHeight"), int
        )
        max_icon_width = XmlUtilities.value_from_xml_element(
            root.find("MaxIconWidth"), int
        )
        max_icon_height = XmlUtilities.value_from_xml_element(
            root.find("MaxIconHeight"), int
        )
        max_streaming_bitrate = XmlUtilities.value_from_xml_element(
            root.find("MaxStreamingBitrate"), int
        )
        max_static_bitrate = XmlUtilities.value_from_xml_element(
            root.find("MaxStaticBitrate"), int
        )
        music_streaming_transcoding_bitrate = XmlUtilities.value_from_xml_element(
            root.find("MusicStreamingTranscodingBitrate"), int
        )
        max_static_music_bitrate = XmlUtilities.value_from_xml_element(
            root.find("MaxStaticMusicBitrate"), int
        )
        sony_aggregation_flags = XmlUtilities.value_from_xml_element(
            root.find("SonyAggregationFlags"), str
        )
        protocol_info = XmlUtilities.value_from_xml_element(
            root.find("ProtocolInfo"), str
        )
        timeline_offset_seconds = XmlUtilities.value_from_xml_element(
            root.find("TimelineOffsetSeconds"), int
        )
        requires_plain_video_items = XmlUtilities.value_from_xml_element(
            root.find("RequiresPlainVideoItems"), bool
        )
        requires_plain_folders = XmlUtilities.value_from_xml_element(
            root.find("RequiresPlainFolders"), bool
        )
        enable_ms_media_receiver_registrar = XmlUtilities.value_from_xml_element(
            root.find("EnableMSMediaReceiverRegistrar"), bool
        )
        ignore_transcode_byte_range_requests = XmlUtilities.value_from_xml_element(
            root.find("IgnoreTranscodeByteRangeRequests"), bool
        )
        xml_root_attributes = XmlUtilities.list_from_xml_element(
            root, "XmlAttribute", XmlAttribute
        )
        direct_play_profiles = XmlUtilities.list_from_xml_element(
            root, "DirectPlayProfile", DirectPlayProfile
        )
        transcoding_profiles = XmlUtilities.list_from_xml_element(
            root, "TranscodingProfile", TranscodingProfile
        )
        container_profiles = XmlUtilities.list_from_xml_element(
            root, "ContainerProfile", ContainerProfile
        )
        codec_profiles = XmlUtilities.list_from_xml_element(
            root, "CodecProfile", CodecProfile
        )
        response_profiles = XmlUtilities.list_from_xml_element(
            root, "ResponseProfile", ResponseProfile
        )
        subtitle_profiles = XmlUtilities.list_from_xml_element(
            root, "SubtitleProfile", SubtitleProfile
        )

        return cls(
            name,
            id,
            identification,
            friendly_name,
            manufacturer,
            manufacturer_url,
            model_name,
            model_description,
            model_number,
            model_url,
            serial_number,
            enable_album_art_in_didl,
            enable_single_album_art_limit,
            enable_single_subtitle_limit,
            supported_media_types,
            user_id,
            album_art_pn,
            max_album_art_width,
            max_album_art_height,
            max_icon_width,
            max_icon_height,
            max_streaming_bitrate,
            max_static_bitrate,
            music_streaming_transcoding_bitrate,
            max_static_music_bitrate,
            sony_aggregation_flags,
            protocol_info,
            timeline_offset_seconds,
            requires_plain_video_items,
            requires_plain_folders,
            enable_ms_media_receiver_registrar,
            ignore_transcode_byte_range_requests,
            xml_root_attributes,
            direct_play_profiles,
            transcoding_profiles,
            container_profiles,
            codec_profiles,
            response_profiles,
            subtitle_profiles,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(
            root, self.identification, "DeviceIdentification"
        )
        XmlUtilities.add_as_subelement(root, self.friendly_name, "FriendlyName")
        XmlUtilities.add_as_subelement(root, self.manufacturer, "Manufacturer")
        XmlUtilities.add_as_subelement(root, self.manufacturer_url, "ManufacturerUrl")
        XmlUtilities.add_as_subelement(root, self.model_name, "ModelName")
        XmlUtilities.add_as_subelement(root, self.model_description, "ModelDescription")
        XmlUtilities.add_as_subelement(root, self.model_number, "ModelNumber")
        XmlUtilities.add_as_subelement(root, self.model_url, "ModelUrl")
        XmlUtilities.add_as_subelement(root, self.serial_number, "SerialNumber")
        XmlUtilities.add_as_subelement(
            root, self.enable_album_art_in_didl, "EnableAlbumArtInDidl"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_single_album_art_limit, "EnableSingleAlbumArtLimit"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_single_subtitle_limit, "EnableSingleSubtitleLimit"
        )
        XmlUtilities.add_as_subelement(
            root, self.supported_media_types, "SupportedMediaTypes"
        )
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.album_art_pn, "AlbumArtPn")
        XmlUtilities.add_as_subelement(
            root, self.max_album_art_width, "MaxAlbumArtWidth"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_album_art_height, "MaxAlbumArtHeight"
        )
        XmlUtilities.add_as_subelement(root, self.max_icon_width, "MaxIconWidth")
        XmlUtilities.add_as_subelement(root, self.max_icon_height, "MaxIconHeight")
        XmlUtilities.add_as_subelement(
            root, self.max_streaming_bitrate, "MaxStreamingBitrate"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_static_bitrate, "MaxStaticBitrate"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.music_streaming_transcoding_bitrate,
            "MusicStreamingTranscodingBitrate",
        )
        XmlUtilities.add_as_subelement(
            root, self.max_static_music_bitrate, "MaxStaticMusicBitrate"
        )
        XmlUtilities.add_as_subelement(
            root, self.sony_aggregation_flags, "SonyAggregationFlags"
        )
        XmlUtilities.add_as_subelement(root, self.protocol_info, "ProtocolInfo")
        XmlUtilities.add_as_subelement(
            root, self.timeline_offset_seconds, "TimelineOffsetSeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.requires_plain_video_items, "RequiresPlainVideoItems"
        )
        XmlUtilities.add_as_subelement(
            root, self.requires_plain_folders, "RequiresPlainFolders"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_ms_media_receiver_registrar,
            "EnableMSMediaReceiverRegistrar",
        )
        XmlUtilities.add_as_subelement(
            root,
            self.ignore_transcode_byte_range_requests,
            "IgnoreTranscodeByteRangeRequests",
        )
        XmlUtilities.add_list_as_subelement(
            root, self.xml_root_attributes, "XmlAttribute"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.direct_play_profiles, "DirectPlayProfile"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.transcoding_profiles, "TranscodingProfile"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.container_profiles, "ContainerProfile"
        )
        XmlUtilities.add_list_as_subelement(root, self.codec_profiles, "CodecProfile")
        XmlUtilities.add_list_as_subelement(
            root, self.response_profiles, "ResponseProfile"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.subtitle_profiles, "SubtitleProfile"
        )
