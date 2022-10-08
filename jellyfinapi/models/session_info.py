# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item import BaseItem
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.models.client_capabilities import ClientCapabilities
from jellyfinapi.models.player_state_info import PlayerStateInfo
from jellyfinapi.models.queue_item import QueueItem
from jellyfinapi.models.session_user_info import SessionUserInfo
from jellyfinapi.models.transcoding_info import TranscodingInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SessionInfo(object):

    """Implementation of the 'SessionInfo' model.

    Class SessionInfo.

    Attributes:
        play_state (PlayerStateInfo): TODO: type description here.
        additional_users (list of SessionUserInfo): TODO: type description
            here.
        capabilities (ClientCapabilities): TODO: type description here.
        remote_end_point (string): Gets or sets the remote end point.
        playable_media_types (list of string): Gets the playable media types.
        id (string): Gets or sets the id.
        user_id (uuid|string): Gets or sets the user id.
        user_name (string): Gets or sets the username.
        client (string): Gets or sets the type of the client.
        last_activity_date (datetime): Gets or sets the last activity date.
        last_playback_check_in (datetime): Gets or sets the last playback
            check in.
        device_name (string): Gets or sets the name of the device.
        device_type (string): Gets or sets the type of the device.
        now_playing_item (BaseItemDto): This is strictly used as a data
            transfer object from the api layer.  This holds information about
            a BaseItem in a format that is convenient for the client.
        full_now_playing_item (BaseItem): Class BaseItem.
        now_viewing_item (BaseItemDto): This is strictly used as a data
            transfer object from the api layer.  This holds information about
            a BaseItem in a format that is convenient for the client.
        device_id (string): Gets or sets the device id.
        application_version (string): Gets or sets the application version.
        transcoding_info (TranscodingInfo): TODO: type description here.
        is_active (bool): Gets a value indicating whether this instance is
            active.
        supports_media_control (bool): TODO: type description here.
        supports_remote_control (bool): TODO: type description here.
        now_playing_queue (list of QueueItem): TODO: type description here.
        now_playing_queue_full_items (list of BaseItemDto): TODO: type
            description here.
        has_custom_device_name (bool): TODO: type description here.
        playlist_item_id (string): TODO: type description here.
        server_id (string): TODO: type description here.
        user_primary_image_tag (string): TODO: type description here.
        supported_commands (list of GeneralCommandTypeEnum): Gets the
            supported commands.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "play_state": "PlayState",
        "additional_users": "AdditionalUsers",
        "capabilities": "Capabilities",
        "remote_end_point": "RemoteEndPoint",
        "playable_media_types": "PlayableMediaTypes",
        "id": "Id",
        "user_id": "UserId",
        "user_name": "UserName",
        "client": "Client",
        "last_activity_date": "LastActivityDate",
        "last_playback_check_in": "LastPlaybackCheckIn",
        "device_name": "DeviceName",
        "device_type": "DeviceType",
        "now_playing_item": "NowPlayingItem",
        "full_now_playing_item": "FullNowPlayingItem",
        "now_viewing_item": "NowViewingItem",
        "device_id": "DeviceId",
        "application_version": "ApplicationVersion",
        "transcoding_info": "TranscodingInfo",
        "is_active": "IsActive",
        "supports_media_control": "SupportsMediaControl",
        "supports_remote_control": "SupportsRemoteControl",
        "now_playing_queue": "NowPlayingQueue",
        "now_playing_queue_full_items": "NowPlayingQueueFullItems",
        "has_custom_device_name": "HasCustomDeviceName",
        "playlist_item_id": "PlaylistItemId",
        "server_id": "ServerId",
        "user_primary_image_tag": "UserPrimaryImageTag",
        "supported_commands": "SupportedCommands",
    }

    _optionals = [
        "play_state",
        "additional_users",
        "capabilities",
        "remote_end_point",
        "playable_media_types",
        "id",
        "user_id",
        "user_name",
        "client",
        "last_activity_date",
        "last_playback_check_in",
        "device_name",
        "device_type",
        "now_playing_item",
        "full_now_playing_item",
        "now_viewing_item",
        "device_id",
        "application_version",
        "transcoding_info",
        "is_active",
        "supports_media_control",
        "supports_remote_control",
        "now_playing_queue",
        "now_playing_queue_full_items",
        "has_custom_device_name",
        "playlist_item_id",
        "server_id",
        "user_primary_image_tag",
        "supported_commands",
    ]

    _nullables = [
        "play_state",
        "additional_users",
        "capabilities",
        "remote_end_point",
        "playable_media_types",
        "id",
        "user_name",
        "client",
        "device_name",
        "device_type",
        "now_playing_item",
        "full_now_playing_item",
        "now_viewing_item",
        "device_id",
        "application_version",
        "transcoding_info",
        "now_playing_queue",
        "now_playing_queue_full_items",
        "playlist_item_id",
        "server_id",
        "user_primary_image_tag",
        "supported_commands",
    ]

    def __init__(
        self,
        play_state=APIHelper.SKIP,
        additional_users=APIHelper.SKIP,
        capabilities=APIHelper.SKIP,
        remote_end_point=APIHelper.SKIP,
        playable_media_types=APIHelper.SKIP,
        id=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        user_name=APIHelper.SKIP,
        client=APIHelper.SKIP,
        last_activity_date=APIHelper.SKIP,
        last_playback_check_in=APIHelper.SKIP,
        device_name=APIHelper.SKIP,
        device_type=APIHelper.SKIP,
        now_playing_item=APIHelper.SKIP,
        full_now_playing_item=APIHelper.SKIP,
        now_viewing_item=APIHelper.SKIP,
        device_id=APIHelper.SKIP,
        application_version=APIHelper.SKIP,
        transcoding_info=APIHelper.SKIP,
        is_active=APIHelper.SKIP,
        supports_media_control=APIHelper.SKIP,
        supports_remote_control=APIHelper.SKIP,
        now_playing_queue=APIHelper.SKIP,
        now_playing_queue_full_items=APIHelper.SKIP,
        has_custom_device_name=APIHelper.SKIP,
        playlist_item_id=APIHelper.SKIP,
        server_id=APIHelper.SKIP,
        user_primary_image_tag=APIHelper.SKIP,
        supported_commands=APIHelper.SKIP,
    ):
        """Constructor for the SessionInfo class"""

        # Initialize members of the class
        if play_state is not APIHelper.SKIP:
            self.play_state = play_state
        if additional_users is not APIHelper.SKIP:
            self.additional_users = additional_users
        if capabilities is not APIHelper.SKIP:
            self.capabilities = capabilities
        if remote_end_point is not APIHelper.SKIP:
            self.remote_end_point = remote_end_point
        if playable_media_types is not APIHelper.SKIP:
            self.playable_media_types = playable_media_types
        if id is not APIHelper.SKIP:
            self.id = id
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if user_name is not APIHelper.SKIP:
            self.user_name = user_name
        if client is not APIHelper.SKIP:
            self.client = client
        if last_activity_date is not APIHelper.SKIP:
            self.last_activity_date = (
                APIHelper.RFC3339DateTime(last_activity_date)
                if last_activity_date
                else None
            )
        if last_playback_check_in is not APIHelper.SKIP:
            self.last_playback_check_in = (
                APIHelper.RFC3339DateTime(last_playback_check_in)
                if last_playback_check_in
                else None
            )
        if device_name is not APIHelper.SKIP:
            self.device_name = device_name
        if device_type is not APIHelper.SKIP:
            self.device_type = device_type
        if now_playing_item is not APIHelper.SKIP:
            self.now_playing_item = now_playing_item
        if full_now_playing_item is not APIHelper.SKIP:
            self.full_now_playing_item = full_now_playing_item
        if now_viewing_item is not APIHelper.SKIP:
            self.now_viewing_item = now_viewing_item
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id
        if application_version is not APIHelper.SKIP:
            self.application_version = application_version
        if transcoding_info is not APIHelper.SKIP:
            self.transcoding_info = transcoding_info
        if is_active is not APIHelper.SKIP:
            self.is_active = is_active
        if supports_media_control is not APIHelper.SKIP:
            self.supports_media_control = supports_media_control
        if supports_remote_control is not APIHelper.SKIP:
            self.supports_remote_control = supports_remote_control
        if now_playing_queue is not APIHelper.SKIP:
            self.now_playing_queue = now_playing_queue
        if now_playing_queue_full_items is not APIHelper.SKIP:
            self.now_playing_queue_full_items = now_playing_queue_full_items
        if has_custom_device_name is not APIHelper.SKIP:
            self.has_custom_device_name = has_custom_device_name
        if playlist_item_id is not APIHelper.SKIP:
            self.playlist_item_id = playlist_item_id
        if server_id is not APIHelper.SKIP:
            self.server_id = server_id
        if user_primary_image_tag is not APIHelper.SKIP:
            self.user_primary_image_tag = user_primary_image_tag
        if supported_commands is not APIHelper.SKIP:
            self.supported_commands = supported_commands

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

        if "PlayState" in dictionary.keys():
            play_state = (
                PlayerStateInfo.from_dictionary(dictionary.get("PlayState"))
                if dictionary.get("PlayState")
                else None
            )
        else:
            play_state = APIHelper.SKIP
        if "AdditionalUsers" in dictionary.keys():
            additional_users = (
                [
                    SessionUserInfo.from_dictionary(x)
                    for x in dictionary.get("AdditionalUsers")
                ]
                if dictionary.get("AdditionalUsers")
                else None
            )
        else:
            additional_users = APIHelper.SKIP
        if "Capabilities" in dictionary.keys():
            capabilities = (
                ClientCapabilities.from_dictionary(dictionary.get("Capabilities"))
                if dictionary.get("Capabilities")
                else None
            )
        else:
            capabilities = APIHelper.SKIP
        remote_end_point = (
            dictionary.get("RemoteEndPoint")
            if "RemoteEndPoint" in dictionary.keys()
            else APIHelper.SKIP
        )
        playable_media_types = (
            dictionary.get("PlayableMediaTypes")
            if "PlayableMediaTypes" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        user_name = (
            dictionary.get("UserName")
            if "UserName" in dictionary.keys()
            else APIHelper.SKIP
        )
        client = (
            dictionary.get("Client")
            if "Client" in dictionary.keys()
            else APIHelper.SKIP
        )
        last_activity_date = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("LastActivityDate")
            ).datetime
            if dictionary.get("LastActivityDate")
            else APIHelper.SKIP
        )
        last_playback_check_in = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("LastPlaybackCheckIn")
            ).datetime
            if dictionary.get("LastPlaybackCheckIn")
            else APIHelper.SKIP
        )
        device_name = (
            dictionary.get("DeviceName")
            if "DeviceName" in dictionary.keys()
            else APIHelper.SKIP
        )
        device_type = (
            dictionary.get("DeviceType")
            if "DeviceType" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "NowPlayingItem" in dictionary.keys():
            now_playing_item = (
                BaseItemDto.from_dictionary(dictionary.get("NowPlayingItem"))
                if dictionary.get("NowPlayingItem")
                else None
            )
        else:
            now_playing_item = APIHelper.SKIP
        if "FullNowPlayingItem" in dictionary.keys():
            full_now_playing_item = (
                BaseItem.from_dictionary(dictionary.get("FullNowPlayingItem"))
                if dictionary.get("FullNowPlayingItem")
                else None
            )
        else:
            full_now_playing_item = APIHelper.SKIP
        if "NowViewingItem" in dictionary.keys():
            now_viewing_item = (
                BaseItemDto.from_dictionary(dictionary.get("NowViewingItem"))
                if dictionary.get("NowViewingItem")
                else None
            )
        else:
            now_viewing_item = APIHelper.SKIP
        device_id = (
            dictionary.get("DeviceId")
            if "DeviceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        application_version = (
            dictionary.get("ApplicationVersion")
            if "ApplicationVersion" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "TranscodingInfo" in dictionary.keys():
            transcoding_info = (
                TranscodingInfo.from_dictionary(dictionary.get("TranscodingInfo"))
                if dictionary.get("TranscodingInfo")
                else None
            )
        else:
            transcoding_info = APIHelper.SKIP
        is_active = (
            dictionary.get("IsActive")
            if "IsActive" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_media_control = (
            dictionary.get("SupportsMediaControl")
            if "SupportsMediaControl" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_remote_control = (
            dictionary.get("SupportsRemoteControl")
            if "SupportsRemoteControl" in dictionary.keys()
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
        if "NowPlayingQueueFullItems" in dictionary.keys():
            now_playing_queue_full_items = (
                [
                    BaseItemDto.from_dictionary(x)
                    for x in dictionary.get("NowPlayingQueueFullItems")
                ]
                if dictionary.get("NowPlayingQueueFullItems")
                else None
            )
        else:
            now_playing_queue_full_items = APIHelper.SKIP
        has_custom_device_name = (
            dictionary.get("HasCustomDeviceName")
            if "HasCustomDeviceName" in dictionary.keys()
            else APIHelper.SKIP
        )
        playlist_item_id = (
            dictionary.get("PlaylistItemId")
            if "PlaylistItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_id = (
            dictionary.get("ServerId")
            if "ServerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        user_primary_image_tag = (
            dictionary.get("UserPrimaryImageTag")
            if "UserPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        supported_commands = (
            dictionary.get("SupportedCommands")
            if "SupportedCommands" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            play_state,
            additional_users,
            capabilities,
            remote_end_point,
            playable_media_types,
            id,
            user_id,
            user_name,
            client,
            last_activity_date,
            last_playback_check_in,
            device_name,
            device_type,
            now_playing_item,
            full_now_playing_item,
            now_viewing_item,
            device_id,
            application_version,
            transcoding_info,
            is_active,
            supports_media_control,
            supports_remote_control,
            now_playing_queue,
            now_playing_queue_full_items,
            has_custom_device_name,
            playlist_item_id,
            server_id,
            user_primary_image_tag,
            supported_commands,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        play_state = XmlUtilities.value_from_xml_element(
            root.find("PlayerStateInfo"), PlayerStateInfo
        )
        additional_users = XmlUtilities.list_from_xml_element(
            root, "SessionUserInfo", SessionUserInfo
        )
        capabilities = XmlUtilities.value_from_xml_element(
            root.find("ClientCapabilities"), ClientCapabilities
        )
        remote_end_point = XmlUtilities.value_from_xml_element(
            root.find("RemoteEndPoint"), str
        )
        playable_media_types = XmlUtilities.list_from_xml_element(
            root, "PlayableMediaTypes", str
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        user_name = XmlUtilities.value_from_xml_element(root.find("UserName"), str)
        client = XmlUtilities.value_from_xml_element(root.find("Client"), str)
        last_activity_date = XmlUtilities.value_from_xml_element(
            root.find("LastActivityDate"), APIHelper.RFC3339DateTime
        )
        last_playback_check_in = XmlUtilities.value_from_xml_element(
            root.find("LastPlaybackCheckIn"), APIHelper.RFC3339DateTime
        )
        device_name = XmlUtilities.value_from_xml_element(root.find("DeviceName"), str)
        device_type = XmlUtilities.value_from_xml_element(root.find("DeviceType"), str)
        now_playing_item = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
        )
        full_now_playing_item = XmlUtilities.value_from_xml_element(
            root.find("BaseItem"), BaseItem
        )
        now_viewing_item = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
        )
        device_id = XmlUtilities.value_from_xml_element(root.find("DeviceId"), str)
        application_version = XmlUtilities.value_from_xml_element(
            root.find("ApplicationVersion"), str
        )
        transcoding_info = XmlUtilities.value_from_xml_element(
            root.find("TranscodingInfo"), TranscodingInfo
        )
        is_active = XmlUtilities.value_from_xml_element(root.find("IsActive"), bool)
        supports_media_control = XmlUtilities.value_from_xml_element(
            root.find("SupportsMediaControl"), bool
        )
        supports_remote_control = XmlUtilities.value_from_xml_element(
            root.find("SupportsRemoteControl"), bool
        )
        now_playing_queue = XmlUtilities.list_from_xml_element(
            root, "QueueItem", QueueItem
        )
        now_playing_queue_full_items = XmlUtilities.list_from_xml_element(
            root, "BaseItemDto", BaseItemDto
        )
        has_custom_device_name = XmlUtilities.value_from_xml_element(
            root.find("HasCustomDeviceName"), bool
        )
        playlist_item_id = XmlUtilities.value_from_xml_element(
            root.find("PlaylistItemId"), str
        )
        server_id = XmlUtilities.value_from_xml_element(root.find("ServerId"), str)
        user_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("UserPrimaryImageTag"), str
        )
        supported_commands = XmlUtilities.list_from_xml_element(
            root, "SupportedCommands", str
        )

        return cls(
            play_state,
            additional_users,
            capabilities,
            remote_end_point,
            playable_media_types,
            id,
            user_id,
            user_name,
            client,
            last_activity_date,
            last_playback_check_in,
            device_name,
            device_type,
            now_playing_item,
            full_now_playing_item,
            now_viewing_item,
            device_id,
            application_version,
            transcoding_info,
            is_active,
            supports_media_control,
            supports_remote_control,
            now_playing_queue,
            now_playing_queue_full_items,
            has_custom_device_name,
            playlist_item_id,
            server_id,
            user_primary_image_tag,
            supported_commands,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.play_state, "PlayerStateInfo")
        XmlUtilities.add_list_as_subelement(
            root, self.additional_users, "SessionUserInfo"
        )
        XmlUtilities.add_as_subelement(root, self.capabilities, "ClientCapabilities")
        XmlUtilities.add_as_subelement(root, self.remote_end_point, "RemoteEndPoint")
        XmlUtilities.add_list_as_subelement(
            root, self.playable_media_types, "PlayableMediaTypes"
        )
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.user_name, "UserName")
        XmlUtilities.add_as_subelement(root, self.client, "Client")
        XmlUtilities.add_as_subelement(
            root, self.last_activity_date, "LastActivityDate"
        )
        XmlUtilities.add_as_subelement(
            root, self.last_playback_check_in, "LastPlaybackCheckIn"
        )
        XmlUtilities.add_as_subelement(root, self.device_name, "DeviceName")
        XmlUtilities.add_as_subelement(root, self.device_type, "DeviceType")
        XmlUtilities.add_as_subelement(root, self.now_playing_item, "BaseItemDto")
        XmlUtilities.add_as_subelement(root, self.full_now_playing_item, "BaseItem")
        XmlUtilities.add_as_subelement(root, self.now_viewing_item, "BaseItemDto")
        XmlUtilities.add_as_subelement(root, self.device_id, "DeviceId")
        XmlUtilities.add_as_subelement(
            root, self.application_version, "ApplicationVersion"
        )
        XmlUtilities.add_as_subelement(root, self.transcoding_info, "TranscodingInfo")
        XmlUtilities.add_as_subelement(root, self.is_active, "IsActive")
        XmlUtilities.add_as_subelement(
            root, self.supports_media_control, "SupportsMediaControl"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_remote_control, "SupportsRemoteControl"
        )
        XmlUtilities.add_list_as_subelement(root, self.now_playing_queue, "QueueItem")
        XmlUtilities.add_list_as_subelement(
            root, self.now_playing_queue_full_items, "BaseItemDto"
        )
        XmlUtilities.add_as_subelement(
            root, self.has_custom_device_name, "HasCustomDeviceName"
        )
        XmlUtilities.add_as_subelement(root, self.playlist_item_id, "PlaylistItemId")
        XmlUtilities.add_as_subelement(root, self.server_id, "ServerId")
        XmlUtilities.add_as_subelement(
            root, self.user_primary_image_tag, "UserPrimaryImageTag"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.supported_commands, "SupportedCommands"
        )
