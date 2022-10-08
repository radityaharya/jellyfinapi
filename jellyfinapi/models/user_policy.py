# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.access_schedule import AccessSchedule
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UserPolicy(object):

    """Implementation of the 'UserPolicy' model.

    TODO: type model description here.

    Attributes:
        is_administrator (bool): Gets or sets a value indicating whether this
            instance is administrator.
        is_hidden (bool): Gets or sets a value indicating whether this
            instance is hidden.
        is_disabled (bool): Gets or sets a value indicating whether this
            instance is disabled.
        max_parental_rating (int): Gets or sets the max parental rating.
        blocked_tags (list of string): TODO: type description here.
        enable_user_preference_access (bool): TODO: type description here.
        access_schedules (list of AccessSchedule): TODO: type description
            here.
        block_unrated_items (list of UnratedItemEnum): TODO: type description
            here.
        enable_remote_control_of_other_users (bool): TODO: type description
            here.
        enable_shared_device_control (bool): TODO: type description here.
        enable_remote_access (bool): TODO: type description here.
        enable_live_tv_management (bool): TODO: type description here.
        enable_live_tv_access (bool): TODO: type description here.
        enable_media_playback (bool): TODO: type description here.
        enable_audio_playback_transcoding (bool): TODO: type description
            here.
        enable_video_playback_transcoding (bool): TODO: type description
            here.
        enable_playback_remuxing (bool): TODO: type description here.
        force_remote_source_transcoding (bool): TODO: type description here.
        enable_content_deletion (bool): TODO: type description here.
        enable_content_deletion_from_folders (list of string): TODO: type
            description here.
        enable_content_downloading (bool): TODO: type description here.
        enable_sync_transcoding (bool): Gets or sets a value indicating
            whether [enable synchronize].
        enable_media_conversion (bool): TODO: type description here.
        enabled_devices (list of string): TODO: type description here.
        enable_all_devices (bool): TODO: type description here.
        enabled_channels (list of uuid|string): TODO: type description here.
        enable_all_channels (bool): TODO: type description here.
        enabled_folders (list of uuid|string): TODO: type description here.
        enable_all_folders (bool): TODO: type description here.
        invalid_login_attempt_count (int): TODO: type description here.
        login_attempts_before_lockout (int): TODO: type description here.
        max_active_sessions (int): TODO: type description here.
        enable_public_sharing (bool): TODO: type description here.
        blocked_media_folders (list of uuid|string): TODO: type description
            here.
        blocked_channels (list of uuid|string): TODO: type description here.
        remote_client_bitrate_limit (int): TODO: type description here.
        authentication_provider_id (string): TODO: type description here.
        password_reset_provider_id (string): TODO: type description here.
        sync_play_access (SyncPlayUserAccessTypeEnum): Enum
            SyncPlayUserAccessType.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_administrator": "IsAdministrator",
        "is_hidden": "IsHidden",
        "is_disabled": "IsDisabled",
        "max_parental_rating": "MaxParentalRating",
        "blocked_tags": "BlockedTags",
        "enable_user_preference_access": "EnableUserPreferenceAccess",
        "access_schedules": "AccessSchedules",
        "block_unrated_items": "BlockUnratedItems",
        "enable_remote_control_of_other_users": "EnableRemoteControlOfOtherUsers",
        "enable_shared_device_control": "EnableSharedDeviceControl",
        "enable_remote_access": "EnableRemoteAccess",
        "enable_live_tv_management": "EnableLiveTvManagement",
        "enable_live_tv_access": "EnableLiveTvAccess",
        "enable_media_playback": "EnableMediaPlayback",
        "enable_audio_playback_transcoding": "EnableAudioPlaybackTranscoding",
        "enable_video_playback_transcoding": "EnableVideoPlaybackTranscoding",
        "enable_playback_remuxing": "EnablePlaybackRemuxing",
        "force_remote_source_transcoding": "ForceRemoteSourceTranscoding",
        "enable_content_deletion": "EnableContentDeletion",
        "enable_content_deletion_from_folders": "EnableContentDeletionFromFolders",
        "enable_content_downloading": "EnableContentDownloading",
        "enable_sync_transcoding": "EnableSyncTranscoding",
        "enable_media_conversion": "EnableMediaConversion",
        "enabled_devices": "EnabledDevices",
        "enable_all_devices": "EnableAllDevices",
        "enabled_channels": "EnabledChannels",
        "enable_all_channels": "EnableAllChannels",
        "enabled_folders": "EnabledFolders",
        "enable_all_folders": "EnableAllFolders",
        "invalid_login_attempt_count": "InvalidLoginAttemptCount",
        "login_attempts_before_lockout": "LoginAttemptsBeforeLockout",
        "max_active_sessions": "MaxActiveSessions",
        "enable_public_sharing": "EnablePublicSharing",
        "blocked_media_folders": "BlockedMediaFolders",
        "blocked_channels": "BlockedChannels",
        "remote_client_bitrate_limit": "RemoteClientBitrateLimit",
        "authentication_provider_id": "AuthenticationProviderId",
        "password_reset_provider_id": "PasswordResetProviderId",
        "sync_play_access": "SyncPlayAccess",
    }

    _optionals = [
        "is_administrator",
        "is_hidden",
        "is_disabled",
        "max_parental_rating",
        "blocked_tags",
        "enable_user_preference_access",
        "access_schedules",
        "block_unrated_items",
        "enable_remote_control_of_other_users",
        "enable_shared_device_control",
        "enable_remote_access",
        "enable_live_tv_management",
        "enable_live_tv_access",
        "enable_media_playback",
        "enable_audio_playback_transcoding",
        "enable_video_playback_transcoding",
        "enable_playback_remuxing",
        "force_remote_source_transcoding",
        "enable_content_deletion",
        "enable_content_deletion_from_folders",
        "enable_content_downloading",
        "enable_sync_transcoding",
        "enable_media_conversion",
        "enabled_devices",
        "enable_all_devices",
        "enabled_channels",
        "enable_all_channels",
        "enabled_folders",
        "enable_all_folders",
        "invalid_login_attempt_count",
        "login_attempts_before_lockout",
        "max_active_sessions",
        "enable_public_sharing",
        "blocked_media_folders",
        "blocked_channels",
        "remote_client_bitrate_limit",
        "authentication_provider_id",
        "password_reset_provider_id",
        "sync_play_access",
    ]

    _nullables = [
        "max_parental_rating",
        "blocked_tags",
        "access_schedules",
        "block_unrated_items",
        "enable_content_deletion_from_folders",
        "enabled_devices",
        "enabled_channels",
        "enabled_folders",
        "blocked_media_folders",
        "blocked_channels",
        "authentication_provider_id",
        "password_reset_provider_id",
    ]

    def __init__(
        self,
        is_administrator=APIHelper.SKIP,
        is_hidden=APIHelper.SKIP,
        is_disabled=APIHelper.SKIP,
        max_parental_rating=APIHelper.SKIP,
        blocked_tags=APIHelper.SKIP,
        enable_user_preference_access=APIHelper.SKIP,
        access_schedules=APIHelper.SKIP,
        block_unrated_items=APIHelper.SKIP,
        enable_remote_control_of_other_users=APIHelper.SKIP,
        enable_shared_device_control=APIHelper.SKIP,
        enable_remote_access=APIHelper.SKIP,
        enable_live_tv_management=APIHelper.SKIP,
        enable_live_tv_access=APIHelper.SKIP,
        enable_media_playback=APIHelper.SKIP,
        enable_audio_playback_transcoding=APIHelper.SKIP,
        enable_video_playback_transcoding=APIHelper.SKIP,
        enable_playback_remuxing=APIHelper.SKIP,
        force_remote_source_transcoding=APIHelper.SKIP,
        enable_content_deletion=APIHelper.SKIP,
        enable_content_deletion_from_folders=APIHelper.SKIP,
        enable_content_downloading=APIHelper.SKIP,
        enable_sync_transcoding=APIHelper.SKIP,
        enable_media_conversion=APIHelper.SKIP,
        enabled_devices=APIHelper.SKIP,
        enable_all_devices=APIHelper.SKIP,
        enabled_channels=APIHelper.SKIP,
        enable_all_channels=APIHelper.SKIP,
        enabled_folders=APIHelper.SKIP,
        enable_all_folders=APIHelper.SKIP,
        invalid_login_attempt_count=APIHelper.SKIP,
        login_attempts_before_lockout=APIHelper.SKIP,
        max_active_sessions=APIHelper.SKIP,
        enable_public_sharing=APIHelper.SKIP,
        blocked_media_folders=APIHelper.SKIP,
        blocked_channels=APIHelper.SKIP,
        remote_client_bitrate_limit=APIHelper.SKIP,
        authentication_provider_id=APIHelper.SKIP,
        password_reset_provider_id=APIHelper.SKIP,
        sync_play_access=APIHelper.SKIP,
    ):
        """Constructor for the UserPolicy class"""

        # Initialize members of the class
        if is_administrator is not APIHelper.SKIP:
            self.is_administrator = is_administrator
        if is_hidden is not APIHelper.SKIP:
            self.is_hidden = is_hidden
        if is_disabled is not APIHelper.SKIP:
            self.is_disabled = is_disabled
        if max_parental_rating is not APIHelper.SKIP:
            self.max_parental_rating = max_parental_rating
        if blocked_tags is not APIHelper.SKIP:
            self.blocked_tags = blocked_tags
        if enable_user_preference_access is not APIHelper.SKIP:
            self.enable_user_preference_access = enable_user_preference_access
        if access_schedules is not APIHelper.SKIP:
            self.access_schedules = access_schedules
        if block_unrated_items is not APIHelper.SKIP:
            self.block_unrated_items = block_unrated_items
        if enable_remote_control_of_other_users is not APIHelper.SKIP:
            self.enable_remote_control_of_other_users = (
                enable_remote_control_of_other_users
            )
        if enable_shared_device_control is not APIHelper.SKIP:
            self.enable_shared_device_control = enable_shared_device_control
        if enable_remote_access is not APIHelper.SKIP:
            self.enable_remote_access = enable_remote_access
        if enable_live_tv_management is not APIHelper.SKIP:
            self.enable_live_tv_management = enable_live_tv_management
        if enable_live_tv_access is not APIHelper.SKIP:
            self.enable_live_tv_access = enable_live_tv_access
        if enable_media_playback is not APIHelper.SKIP:
            self.enable_media_playback = enable_media_playback
        if enable_audio_playback_transcoding is not APIHelper.SKIP:
            self.enable_audio_playback_transcoding = enable_audio_playback_transcoding
        if enable_video_playback_transcoding is not APIHelper.SKIP:
            self.enable_video_playback_transcoding = enable_video_playback_transcoding
        if enable_playback_remuxing is not APIHelper.SKIP:
            self.enable_playback_remuxing = enable_playback_remuxing
        if force_remote_source_transcoding is not APIHelper.SKIP:
            self.force_remote_source_transcoding = force_remote_source_transcoding
        if enable_content_deletion is not APIHelper.SKIP:
            self.enable_content_deletion = enable_content_deletion
        if enable_content_deletion_from_folders is not APIHelper.SKIP:
            self.enable_content_deletion_from_folders = (
                enable_content_deletion_from_folders
            )
        if enable_content_downloading is not APIHelper.SKIP:
            self.enable_content_downloading = enable_content_downloading
        if enable_sync_transcoding is not APIHelper.SKIP:
            self.enable_sync_transcoding = enable_sync_transcoding
        if enable_media_conversion is not APIHelper.SKIP:
            self.enable_media_conversion = enable_media_conversion
        if enabled_devices is not APIHelper.SKIP:
            self.enabled_devices = enabled_devices
        if enable_all_devices is not APIHelper.SKIP:
            self.enable_all_devices = enable_all_devices
        if enabled_channels is not APIHelper.SKIP:
            self.enabled_channels = enabled_channels
        if enable_all_channels is not APIHelper.SKIP:
            self.enable_all_channels = enable_all_channels
        if enabled_folders is not APIHelper.SKIP:
            self.enabled_folders = enabled_folders
        if enable_all_folders is not APIHelper.SKIP:
            self.enable_all_folders = enable_all_folders
        if invalid_login_attempt_count is not APIHelper.SKIP:
            self.invalid_login_attempt_count = invalid_login_attempt_count
        if login_attempts_before_lockout is not APIHelper.SKIP:
            self.login_attempts_before_lockout = login_attempts_before_lockout
        if max_active_sessions is not APIHelper.SKIP:
            self.max_active_sessions = max_active_sessions
        if enable_public_sharing is not APIHelper.SKIP:
            self.enable_public_sharing = enable_public_sharing
        if blocked_media_folders is not APIHelper.SKIP:
            self.blocked_media_folders = blocked_media_folders
        if blocked_channels is not APIHelper.SKIP:
            self.blocked_channels = blocked_channels
        if remote_client_bitrate_limit is not APIHelper.SKIP:
            self.remote_client_bitrate_limit = remote_client_bitrate_limit
        if authentication_provider_id is not APIHelper.SKIP:
            self.authentication_provider_id = authentication_provider_id
        if password_reset_provider_id is not APIHelper.SKIP:
            self.password_reset_provider_id = password_reset_provider_id
        if sync_play_access is not APIHelper.SKIP:
            self.sync_play_access = sync_play_access

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

        is_administrator = (
            dictionary.get("IsAdministrator")
            if "IsAdministrator" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_hidden = (
            dictionary.get("IsHidden")
            if "IsHidden" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_disabled = (
            dictionary.get("IsDisabled")
            if "IsDisabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_parental_rating = (
            dictionary.get("MaxParentalRating")
            if "MaxParentalRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        blocked_tags = (
            dictionary.get("BlockedTags")
            if "BlockedTags" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_user_preference_access = (
            dictionary.get("EnableUserPreferenceAccess")
            if "EnableUserPreferenceAccess" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "AccessSchedules" in dictionary.keys():
            access_schedules = (
                [
                    AccessSchedule.from_dictionary(x)
                    for x in dictionary.get("AccessSchedules")
                ]
                if dictionary.get("AccessSchedules")
                else None
            )
        else:
            access_schedules = APIHelper.SKIP
        block_unrated_items = (
            dictionary.get("BlockUnratedItems")
            if "BlockUnratedItems" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_remote_control_of_other_users = (
            dictionary.get("EnableRemoteControlOfOtherUsers")
            if "EnableRemoteControlOfOtherUsers" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_shared_device_control = (
            dictionary.get("EnableSharedDeviceControl")
            if "EnableSharedDeviceControl" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_remote_access = (
            dictionary.get("EnableRemoteAccess")
            if "EnableRemoteAccess" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_live_tv_management = (
            dictionary.get("EnableLiveTvManagement")
            if "EnableLiveTvManagement" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_live_tv_access = (
            dictionary.get("EnableLiveTvAccess")
            if "EnableLiveTvAccess" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_media_playback = (
            dictionary.get("EnableMediaPlayback")
            if "EnableMediaPlayback" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_audio_playback_transcoding = (
            dictionary.get("EnableAudioPlaybackTranscoding")
            if "EnableAudioPlaybackTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_video_playback_transcoding = (
            dictionary.get("EnableVideoPlaybackTranscoding")
            if "EnableVideoPlaybackTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_playback_remuxing = (
            dictionary.get("EnablePlaybackRemuxing")
            if "EnablePlaybackRemuxing" in dictionary.keys()
            else APIHelper.SKIP
        )
        force_remote_source_transcoding = (
            dictionary.get("ForceRemoteSourceTranscoding")
            if "ForceRemoteSourceTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_content_deletion = (
            dictionary.get("EnableContentDeletion")
            if "EnableContentDeletion" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_content_deletion_from_folders = (
            dictionary.get("EnableContentDeletionFromFolders")
            if "EnableContentDeletionFromFolders" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_content_downloading = (
            dictionary.get("EnableContentDownloading")
            if "EnableContentDownloading" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_sync_transcoding = (
            dictionary.get("EnableSyncTranscoding")
            if "EnableSyncTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_media_conversion = (
            dictionary.get("EnableMediaConversion")
            if "EnableMediaConversion" in dictionary.keys()
            else APIHelper.SKIP
        )
        enabled_devices = (
            dictionary.get("EnabledDevices")
            if "EnabledDevices" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_all_devices = (
            dictionary.get("EnableAllDevices")
            if "EnableAllDevices" in dictionary.keys()
            else APIHelper.SKIP
        )
        enabled_channels = (
            dictionary.get("EnabledChannels")
            if "EnabledChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_all_channels = (
            dictionary.get("EnableAllChannels")
            if "EnableAllChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        enabled_folders = (
            dictionary.get("EnabledFolders")
            if "EnabledFolders" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_all_folders = (
            dictionary.get("EnableAllFolders")
            if "EnableAllFolders" in dictionary.keys()
            else APIHelper.SKIP
        )
        invalid_login_attempt_count = (
            dictionary.get("InvalidLoginAttemptCount")
            if dictionary.get("InvalidLoginAttemptCount")
            else APIHelper.SKIP
        )
        login_attempts_before_lockout = (
            dictionary.get("LoginAttemptsBeforeLockout")
            if dictionary.get("LoginAttemptsBeforeLockout")
            else APIHelper.SKIP
        )
        max_active_sessions = (
            dictionary.get("MaxActiveSessions")
            if dictionary.get("MaxActiveSessions")
            else APIHelper.SKIP
        )
        enable_public_sharing = (
            dictionary.get("EnablePublicSharing")
            if "EnablePublicSharing" in dictionary.keys()
            else APIHelper.SKIP
        )
        blocked_media_folders = (
            dictionary.get("BlockedMediaFolders")
            if "BlockedMediaFolders" in dictionary.keys()
            else APIHelper.SKIP
        )
        blocked_channels = (
            dictionary.get("BlockedChannels")
            if "BlockedChannels" in dictionary.keys()
            else APIHelper.SKIP
        )
        remote_client_bitrate_limit = (
            dictionary.get("RemoteClientBitrateLimit")
            if dictionary.get("RemoteClientBitrateLimit")
            else APIHelper.SKIP
        )
        authentication_provider_id = (
            dictionary.get("AuthenticationProviderId")
            if "AuthenticationProviderId" in dictionary.keys()
            else APIHelper.SKIP
        )
        password_reset_provider_id = (
            dictionary.get("PasswordResetProviderId")
            if "PasswordResetProviderId" in dictionary.keys()
            else APIHelper.SKIP
        )
        sync_play_access = (
            dictionary.get("SyncPlayAccess")
            if dictionary.get("SyncPlayAccess")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            is_administrator,
            is_hidden,
            is_disabled,
            max_parental_rating,
            blocked_tags,
            enable_user_preference_access,
            access_schedules,
            block_unrated_items,
            enable_remote_control_of_other_users,
            enable_shared_device_control,
            enable_remote_access,
            enable_live_tv_management,
            enable_live_tv_access,
            enable_media_playback,
            enable_audio_playback_transcoding,
            enable_video_playback_transcoding,
            enable_playback_remuxing,
            force_remote_source_transcoding,
            enable_content_deletion,
            enable_content_deletion_from_folders,
            enable_content_downloading,
            enable_sync_transcoding,
            enable_media_conversion,
            enabled_devices,
            enable_all_devices,
            enabled_channels,
            enable_all_channels,
            enabled_folders,
            enable_all_folders,
            invalid_login_attempt_count,
            login_attempts_before_lockout,
            max_active_sessions,
            enable_public_sharing,
            blocked_media_folders,
            blocked_channels,
            remote_client_bitrate_limit,
            authentication_provider_id,
            password_reset_provider_id,
            sync_play_access,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        is_administrator = XmlUtilities.value_from_xml_element(
            root.find("IsAdministrator"), bool
        )
        is_hidden = XmlUtilities.value_from_xml_element(root.find("IsHidden"), bool)
        is_disabled = XmlUtilities.value_from_xml_element(root.find("IsDisabled"), bool)
        max_parental_rating = XmlUtilities.value_from_xml_element(
            root.find("MaxParentalRating"), int
        )
        blocked_tags = XmlUtilities.list_from_xml_element(root, "BlockedTags", str)
        enable_user_preference_access = XmlUtilities.value_from_xml_element(
            root.find("EnableUserPreferenceAccess"), bool
        )
        access_schedules = XmlUtilities.list_from_xml_element(
            root, "AccessSchedule", AccessSchedule
        )
        block_unrated_items = XmlUtilities.list_from_xml_element(
            root, "BlockUnratedItems", str
        )
        enable_remote_control_of_other_users = XmlUtilities.value_from_xml_element(
            root.find("EnableRemoteControlOfOtherUsers"), bool
        )
        enable_shared_device_control = XmlUtilities.value_from_xml_element(
            root.find("EnableSharedDeviceControl"), bool
        )
        enable_remote_access = XmlUtilities.value_from_xml_element(
            root.find("EnableRemoteAccess"), bool
        )
        enable_live_tv_management = XmlUtilities.value_from_xml_element(
            root.find("EnableLiveTvManagement"), bool
        )
        enable_live_tv_access = XmlUtilities.value_from_xml_element(
            root.find("EnableLiveTvAccess"), bool
        )
        enable_media_playback = XmlUtilities.value_from_xml_element(
            root.find("EnableMediaPlayback"), bool
        )
        enable_audio_playback_transcoding = XmlUtilities.value_from_xml_element(
            root.find("EnableAudioPlaybackTranscoding"), bool
        )
        enable_video_playback_transcoding = XmlUtilities.value_from_xml_element(
            root.find("EnableVideoPlaybackTranscoding"), bool
        )
        enable_playback_remuxing = XmlUtilities.value_from_xml_element(
            root.find("EnablePlaybackRemuxing"), bool
        )
        force_remote_source_transcoding = XmlUtilities.value_from_xml_element(
            root.find("ForceRemoteSourceTranscoding"), bool
        )
        enable_content_deletion = XmlUtilities.value_from_xml_element(
            root.find("EnableContentDeletion"), bool
        )
        enable_content_deletion_from_folders = XmlUtilities.list_from_xml_element(
            root, "EnableContentDeletionFromFolders", str
        )
        enable_content_downloading = XmlUtilities.value_from_xml_element(
            root.find("EnableContentDownloading"), bool
        )
        enable_sync_transcoding = XmlUtilities.value_from_xml_element(
            root.find("EnableSyncTranscoding"), bool
        )
        enable_media_conversion = XmlUtilities.value_from_xml_element(
            root.find("EnableMediaConversion"), bool
        )
        enabled_devices = XmlUtilities.list_from_xml_element(
            root, "EnabledDevices", str
        )
        enable_all_devices = XmlUtilities.value_from_xml_element(
            root.find("EnableAllDevices"), bool
        )
        enabled_channels = XmlUtilities.list_from_xml_element(
            root, "EnabledChannels", str
        )
        enable_all_channels = XmlUtilities.value_from_xml_element(
            root.find("EnableAllChannels"), bool
        )
        enabled_folders = XmlUtilities.list_from_xml_element(
            root, "EnabledFolders", str
        )
        enable_all_folders = XmlUtilities.value_from_xml_element(
            root.find("EnableAllFolders"), bool
        )
        invalid_login_attempt_count = XmlUtilities.value_from_xml_element(
            root.find("InvalidLoginAttemptCount"), int
        )
        login_attempts_before_lockout = XmlUtilities.value_from_xml_element(
            root.find("LoginAttemptsBeforeLockout"), int
        )
        max_active_sessions = XmlUtilities.value_from_xml_element(
            root.find("MaxActiveSessions"), int
        )
        enable_public_sharing = XmlUtilities.value_from_xml_element(
            root.find("EnablePublicSharing"), bool
        )
        blocked_media_folders = XmlUtilities.list_from_xml_element(
            root, "BlockedMediaFolders", str
        )
        blocked_channels = XmlUtilities.list_from_xml_element(
            root, "BlockedChannels", str
        )
        remote_client_bitrate_limit = XmlUtilities.value_from_xml_element(
            root.find("RemoteClientBitrateLimit"), int
        )
        authentication_provider_id = XmlUtilities.value_from_xml_element(
            root.find("AuthenticationProviderId"), str
        )
        password_reset_provider_id = XmlUtilities.value_from_xml_element(
            root.find("PasswordResetProviderId"), str
        )
        sync_play_access = XmlUtilities.value_from_xml_element(
            root.find("SyncPlayAccess"), str
        )

        return cls(
            is_administrator,
            is_hidden,
            is_disabled,
            max_parental_rating,
            blocked_tags,
            enable_user_preference_access,
            access_schedules,
            block_unrated_items,
            enable_remote_control_of_other_users,
            enable_shared_device_control,
            enable_remote_access,
            enable_live_tv_management,
            enable_live_tv_access,
            enable_media_playback,
            enable_audio_playback_transcoding,
            enable_video_playback_transcoding,
            enable_playback_remuxing,
            force_remote_source_transcoding,
            enable_content_deletion,
            enable_content_deletion_from_folders,
            enable_content_downloading,
            enable_sync_transcoding,
            enable_media_conversion,
            enabled_devices,
            enable_all_devices,
            enabled_channels,
            enable_all_channels,
            enabled_folders,
            enable_all_folders,
            invalid_login_attempt_count,
            login_attempts_before_lockout,
            max_active_sessions,
            enable_public_sharing,
            blocked_media_folders,
            blocked_channels,
            remote_client_bitrate_limit,
            authentication_provider_id,
            password_reset_provider_id,
            sync_play_access,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.is_administrator, "IsAdministrator")
        XmlUtilities.add_as_subelement(root, self.is_hidden, "IsHidden")
        XmlUtilities.add_as_subelement(root, self.is_disabled, "IsDisabled")
        XmlUtilities.add_as_subelement(
            root, self.max_parental_rating, "MaxParentalRating"
        )
        XmlUtilities.add_list_as_subelement(root, self.blocked_tags, "BlockedTags")
        XmlUtilities.add_as_subelement(
            root, self.enable_user_preference_access, "EnableUserPreferenceAccess"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.access_schedules, "AccessSchedule"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.block_unrated_items, "BlockUnratedItems"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_remote_control_of_other_users,
            "EnableRemoteControlOfOtherUsers",
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_shared_device_control, "EnableSharedDeviceControl"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_remote_access, "EnableRemoteAccess"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_live_tv_management, "EnableLiveTvManagement"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_live_tv_access, "EnableLiveTvAccess"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_media_playback, "EnableMediaPlayback"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_audio_playback_transcoding,
            "EnableAudioPlaybackTranscoding",
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_video_playback_transcoding,
            "EnableVideoPlaybackTranscoding",
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_playback_remuxing, "EnablePlaybackRemuxing"
        )
        XmlUtilities.add_as_subelement(
            root, self.force_remote_source_transcoding, "ForceRemoteSourceTranscoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_content_deletion, "EnableContentDeletion"
        )
        XmlUtilities.add_list_as_subelement(
            root,
            self.enable_content_deletion_from_folders,
            "EnableContentDeletionFromFolders",
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_content_downloading, "EnableContentDownloading"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_sync_transcoding, "EnableSyncTranscoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_media_conversion, "EnableMediaConversion"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.enabled_devices, "EnabledDevices"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_all_devices, "EnableAllDevices"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.enabled_channels, "EnabledChannels"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_all_channels, "EnableAllChannels"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.enabled_folders, "EnabledFolders"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_all_folders, "EnableAllFolders"
        )
        XmlUtilities.add_as_subelement(
            root, self.invalid_login_attempt_count, "InvalidLoginAttemptCount"
        )
        XmlUtilities.add_as_subelement(
            root, self.login_attempts_before_lockout, "LoginAttemptsBeforeLockout"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_active_sessions, "MaxActiveSessions"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_public_sharing, "EnablePublicSharing"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.blocked_media_folders, "BlockedMediaFolders"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.blocked_channels, "BlockedChannels"
        )
        XmlUtilities.add_as_subelement(
            root, self.remote_client_bitrate_limit, "RemoteClientBitrateLimit"
        )
        XmlUtilities.add_as_subelement(
            root, self.authentication_provider_id, "AuthenticationProviderId"
        )
        XmlUtilities.add_as_subelement(
            root, self.password_reset_provider_id, "PasswordResetProviderId"
        )
        XmlUtilities.add_as_subelement(root, self.sync_play_access, "SyncPlayAccess")
