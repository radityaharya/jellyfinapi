# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.device_profile import DeviceProfile
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ClientCapabilitiesDto(object):

    """Implementation of the 'ClientCapabilitiesDto' model.

    Client capabilities dto.

    Attributes:
        playable_media_types (list of string): Gets or sets the list of
            playable media types.
        supported_commands (list of GeneralCommandTypeEnum): Gets or sets the
            list of supported commands.
        supports_media_control (bool): Gets or sets a value indicating whether
            session supports media control.
        supports_content_uploading (bool): Gets or sets a value indicating
            whether session supports content uploading.
        message_callback_url (string): Gets or sets the message callback url.
        supports_persistent_identifier (bool): Gets or sets a value indicating
            whether session supports a persistent identifier.
        supports_sync (bool): Gets or sets a value indicating whether session
            supports sync.
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
        app_store_url (string): Gets or sets the app store url.
        icon_url (string): Gets or sets the icon url.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "playable_media_types": "PlayableMediaTypes",
        "supported_commands": "SupportedCommands",
        "supports_media_control": "SupportsMediaControl",
        "supports_content_uploading": "SupportsContentUploading",
        "message_callback_url": "MessageCallbackUrl",
        "supports_persistent_identifier": "SupportsPersistentIdentifier",
        "supports_sync": "SupportsSync",
        "device_profile": "DeviceProfile",
        "app_store_url": "AppStoreUrl",
        "icon_url": "IconUrl",
    }

    _optionals = [
        "playable_media_types",
        "supported_commands",
        "supports_media_control",
        "supports_content_uploading",
        "message_callback_url",
        "supports_persistent_identifier",
        "supports_sync",
        "device_profile",
        "app_store_url",
        "icon_url",
    ]

    _nullables = [
        "message_callback_url",
        "device_profile",
        "app_store_url",
        "icon_url",
    ]

    def __init__(
        self,
        playable_media_types=APIHelper.SKIP,
        supported_commands=APIHelper.SKIP,
        supports_media_control=APIHelper.SKIP,
        supports_content_uploading=APIHelper.SKIP,
        message_callback_url=APIHelper.SKIP,
        supports_persistent_identifier=APIHelper.SKIP,
        supports_sync=APIHelper.SKIP,
        device_profile=APIHelper.SKIP,
        app_store_url=APIHelper.SKIP,
        icon_url=APIHelper.SKIP,
    ):
        """Constructor for the ClientCapabilitiesDto class"""

        # Initialize members of the class
        if playable_media_types is not APIHelper.SKIP:
            self.playable_media_types = playable_media_types
        if supported_commands is not APIHelper.SKIP:
            self.supported_commands = supported_commands
        if supports_media_control is not APIHelper.SKIP:
            self.supports_media_control = supports_media_control
        if supports_content_uploading is not APIHelper.SKIP:
            self.supports_content_uploading = supports_content_uploading
        if message_callback_url is not APIHelper.SKIP:
            self.message_callback_url = message_callback_url
        if supports_persistent_identifier is not APIHelper.SKIP:
            self.supports_persistent_identifier = supports_persistent_identifier
        if supports_sync is not APIHelper.SKIP:
            self.supports_sync = supports_sync
        if device_profile is not APIHelper.SKIP:
            self.device_profile = device_profile
        if app_store_url is not APIHelper.SKIP:
            self.app_store_url = app_store_url
        if icon_url is not APIHelper.SKIP:
            self.icon_url = icon_url

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

        playable_media_types = (
            dictionary.get("PlayableMediaTypes")
            if dictionary.get("PlayableMediaTypes")
            else APIHelper.SKIP
        )
        supported_commands = (
            dictionary.get("SupportedCommands")
            if dictionary.get("SupportedCommands")
            else APIHelper.SKIP
        )
        supports_media_control = (
            dictionary.get("SupportsMediaControl")
            if "SupportsMediaControl" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_content_uploading = (
            dictionary.get("SupportsContentUploading")
            if "SupportsContentUploading" in dictionary.keys()
            else APIHelper.SKIP
        )
        message_callback_url = (
            dictionary.get("MessageCallbackUrl")
            if "MessageCallbackUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_persistent_identifier = (
            dictionary.get("SupportsPersistentIdentifier")
            if "SupportsPersistentIdentifier" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_sync = (
            dictionary.get("SupportsSync")
            if "SupportsSync" in dictionary.keys()
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
        app_store_url = (
            dictionary.get("AppStoreUrl")
            if "AppStoreUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        icon_url = (
            dictionary.get("IconUrl")
            if "IconUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            playable_media_types,
            supported_commands,
            supports_media_control,
            supports_content_uploading,
            message_callback_url,
            supports_persistent_identifier,
            supports_sync,
            device_profile,
            app_store_url,
            icon_url,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        playable_media_types = XmlUtilities.list_from_xml_element(
            root, "PlayableMediaTypes", str
        )
        supported_commands = XmlUtilities.list_from_xml_element(
            root, "SupportedCommands", str
        )
        supports_media_control = XmlUtilities.value_from_xml_element(
            root.find("SupportsMediaControl"), bool
        )
        supports_content_uploading = XmlUtilities.value_from_xml_element(
            root.find("SupportsContentUploading"), bool
        )
        message_callback_url = XmlUtilities.value_from_xml_element(
            root.find("MessageCallbackUrl"), str
        )
        supports_persistent_identifier = XmlUtilities.value_from_xml_element(
            root.find("SupportsPersistentIdentifier"), bool
        )
        supports_sync = XmlUtilities.value_from_xml_element(
            root.find("SupportsSync"), bool
        )
        device_profile = XmlUtilities.value_from_xml_element(
            root.find("DeviceProfile"), DeviceProfile
        )
        app_store_url = XmlUtilities.value_from_xml_element(
            root.find("AppStoreUrl"), str
        )
        icon_url = XmlUtilities.value_from_xml_element(root.find("IconUrl"), str)

        return cls(
            playable_media_types,
            supported_commands,
            supports_media_control,
            supports_content_uploading,
            message_callback_url,
            supports_persistent_identifier,
            supports_sync,
            device_profile,
            app_store_url,
            icon_url,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.playable_media_types, "PlayableMediaTypes"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.supported_commands, "SupportedCommands"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_media_control, "SupportsMediaControl"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_content_uploading, "SupportsContentUploading"
        )
        XmlUtilities.add_as_subelement(
            root, self.message_callback_url, "MessageCallbackUrl"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_persistent_identifier, "SupportsPersistentIdentifier"
        )
        XmlUtilities.add_as_subelement(root, self.supports_sync, "SupportsSync")
        XmlUtilities.add_as_subelement(root, self.device_profile, "DeviceProfile")
        XmlUtilities.add_as_subelement(root, self.app_store_url, "AppStoreUrl")
        XmlUtilities.add_as_subelement(root, self.icon_url, "IconUrl")
