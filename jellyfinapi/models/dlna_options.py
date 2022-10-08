# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DlnaOptions(object):

    """Implementation of the 'DlnaOptions' model.

    The DlnaOptions class contains the user definable parameters for the dlna
    subsystems.

    Attributes:
        enable_play_to (bool): Gets or sets a value indicating whether gets or
            sets a value to indicate the status of the dlna playTo subsystem.
        enable_server (bool): Gets or sets a value indicating whether gets or
            sets a value to indicate the status of the dlna server subsystem.
        enable_debug_log (bool): Gets or sets a value indicating whether
            detailed dlna server logs are sent to the console/log.  If the
            setting "Emby.Dlna": "Debug" msut be set in logging.default.json
            for this property to work.
        enable_play_to_tracing (bool): Gets or sets a value indicating whether
            whether detailed playTo debug logs are sent to the console/log.
            If the setting "Emby.Dlna.PlayTo": "Debug" msut be set in
            logging.default.json for this property to work.
        client_discovery_interval_seconds (int): Gets or sets the ssdp client
            discovery interval time (in seconds).  This is the time after
            which the server will send a ssdp search request.
        alive_message_interval_seconds (int): Gets or sets the frequency at
            which ssdp alive notifications are transmitted.
        blast_alive_message_interval_seconds (int): Gets or sets the frequency
            at which ssdp alive notifications are transmitted. MIGRATING - TO
            BE REMOVED ONCE WEB HAS BEEN ALTERED.
        default_user_id (string): Gets or sets the default user account that
            the dlna server uses.
        auto_create_play_to_profiles (bool): Gets or sets a value indicating
            whether playTo device profiles should be created.
        blast_alive_messages (bool): Gets or sets a value indicating whether
            to blast alive messages.
        send_only_matched_host (bool): gets or sets a value indicating whether
            to send only matched host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_play_to": "EnablePlayTo",
        "enable_server": "EnableServer",
        "enable_debug_log": "EnableDebugLog",
        "enable_play_to_tracing": "EnablePlayToTracing",
        "client_discovery_interval_seconds": "ClientDiscoveryIntervalSeconds",
        "alive_message_interval_seconds": "AliveMessageIntervalSeconds",
        "blast_alive_message_interval_seconds": "BlastAliveMessageIntervalSeconds",
        "default_user_id": "DefaultUserId",
        "auto_create_play_to_profiles": "AutoCreatePlayToProfiles",
        "blast_alive_messages": "BlastAliveMessages",
        "send_only_matched_host": "SendOnlyMatchedHost",
    }

    _optionals = [
        "enable_play_to",
        "enable_server",
        "enable_debug_log",
        "enable_play_to_tracing",
        "client_discovery_interval_seconds",
        "alive_message_interval_seconds",
        "blast_alive_message_interval_seconds",
        "default_user_id",
        "auto_create_play_to_profiles",
        "blast_alive_messages",
        "send_only_matched_host",
    ]

    _nullables = [
        "default_user_id",
    ]

    def __init__(
        self,
        enable_play_to=APIHelper.SKIP,
        enable_server=APIHelper.SKIP,
        enable_debug_log=APIHelper.SKIP,
        enable_play_to_tracing=APIHelper.SKIP,
        client_discovery_interval_seconds=APIHelper.SKIP,
        alive_message_interval_seconds=APIHelper.SKIP,
        blast_alive_message_interval_seconds=APIHelper.SKIP,
        default_user_id=APIHelper.SKIP,
        auto_create_play_to_profiles=APIHelper.SKIP,
        blast_alive_messages=APIHelper.SKIP,
        send_only_matched_host=APIHelper.SKIP,
    ):
        """Constructor for the DlnaOptions class"""

        # Initialize members of the class
        if enable_play_to is not APIHelper.SKIP:
            self.enable_play_to = enable_play_to
        if enable_server is not APIHelper.SKIP:
            self.enable_server = enable_server
        if enable_debug_log is not APIHelper.SKIP:
            self.enable_debug_log = enable_debug_log
        if enable_play_to_tracing is not APIHelper.SKIP:
            self.enable_play_to_tracing = enable_play_to_tracing
        if client_discovery_interval_seconds is not APIHelper.SKIP:
            self.client_discovery_interval_seconds = client_discovery_interval_seconds
        if alive_message_interval_seconds is not APIHelper.SKIP:
            self.alive_message_interval_seconds = alive_message_interval_seconds
        if blast_alive_message_interval_seconds is not APIHelper.SKIP:
            self.blast_alive_message_interval_seconds = (
                blast_alive_message_interval_seconds
            )
        if default_user_id is not APIHelper.SKIP:
            self.default_user_id = default_user_id
        if auto_create_play_to_profiles is not APIHelper.SKIP:
            self.auto_create_play_to_profiles = auto_create_play_to_profiles
        if blast_alive_messages is not APIHelper.SKIP:
            self.blast_alive_messages = blast_alive_messages
        if send_only_matched_host is not APIHelper.SKIP:
            self.send_only_matched_host = send_only_matched_host

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

        enable_play_to = (
            dictionary.get("EnablePlayTo")
            if "EnablePlayTo" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_server = (
            dictionary.get("EnableServer")
            if "EnableServer" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_debug_log = (
            dictionary.get("EnableDebugLog")
            if "EnableDebugLog" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_play_to_tracing = (
            dictionary.get("EnablePlayToTracing")
            if "EnablePlayToTracing" in dictionary.keys()
            else APIHelper.SKIP
        )
        client_discovery_interval_seconds = (
            dictionary.get("ClientDiscoveryIntervalSeconds")
            if dictionary.get("ClientDiscoveryIntervalSeconds")
            else APIHelper.SKIP
        )
        alive_message_interval_seconds = (
            dictionary.get("AliveMessageIntervalSeconds")
            if dictionary.get("AliveMessageIntervalSeconds")
            else APIHelper.SKIP
        )
        blast_alive_message_interval_seconds = (
            dictionary.get("BlastAliveMessageIntervalSeconds")
            if dictionary.get("BlastAliveMessageIntervalSeconds")
            else APIHelper.SKIP
        )
        default_user_id = (
            dictionary.get("DefaultUserId")
            if "DefaultUserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        auto_create_play_to_profiles = (
            dictionary.get("AutoCreatePlayToProfiles")
            if "AutoCreatePlayToProfiles" in dictionary.keys()
            else APIHelper.SKIP
        )
        blast_alive_messages = (
            dictionary.get("BlastAliveMessages")
            if "BlastAliveMessages" in dictionary.keys()
            else APIHelper.SKIP
        )
        send_only_matched_host = (
            dictionary.get("SendOnlyMatchedHost")
            if "SendOnlyMatchedHost" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            enable_play_to,
            enable_server,
            enable_debug_log,
            enable_play_to_tracing,
            client_discovery_interval_seconds,
            alive_message_interval_seconds,
            blast_alive_message_interval_seconds,
            default_user_id,
            auto_create_play_to_profiles,
            blast_alive_messages,
            send_only_matched_host,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        enable_play_to = XmlUtilities.value_from_xml_element(
            root.find("EnablePlayTo"), bool
        )
        enable_server = XmlUtilities.value_from_xml_element(
            root.find("EnableServer"), bool
        )
        enable_debug_log = XmlUtilities.value_from_xml_element(
            root.find("EnableDebugLog"), bool
        )
        enable_play_to_tracing = XmlUtilities.value_from_xml_element(
            root.find("EnablePlayToTracing"), bool
        )
        client_discovery_interval_seconds = XmlUtilities.value_from_xml_element(
            root.find("ClientDiscoveryIntervalSeconds"), int
        )
        alive_message_interval_seconds = XmlUtilities.value_from_xml_element(
            root.find("AliveMessageIntervalSeconds"), int
        )
        blast_alive_message_interval_seconds = XmlUtilities.value_from_xml_element(
            root.find("BlastAliveMessageIntervalSeconds"), int
        )
        default_user_id = XmlUtilities.value_from_xml_element(
            root.find("DefaultUserId"), str
        )
        auto_create_play_to_profiles = XmlUtilities.value_from_xml_element(
            root.find("AutoCreatePlayToProfiles"), bool
        )
        blast_alive_messages = XmlUtilities.value_from_xml_element(
            root.find("BlastAliveMessages"), bool
        )
        send_only_matched_host = XmlUtilities.value_from_xml_element(
            root.find("SendOnlyMatchedHost"), bool
        )

        return cls(
            enable_play_to,
            enable_server,
            enable_debug_log,
            enable_play_to_tracing,
            client_discovery_interval_seconds,
            alive_message_interval_seconds,
            blast_alive_message_interval_seconds,
            default_user_id,
            auto_create_play_to_profiles,
            blast_alive_messages,
            send_only_matched_host,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.enable_play_to, "EnablePlayTo")
        XmlUtilities.add_as_subelement(root, self.enable_server, "EnableServer")
        XmlUtilities.add_as_subelement(root, self.enable_debug_log, "EnableDebugLog")
        XmlUtilities.add_as_subelement(
            root, self.enable_play_to_tracing, "EnablePlayToTracing"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.client_discovery_interval_seconds,
            "ClientDiscoveryIntervalSeconds",
        )
        XmlUtilities.add_as_subelement(
            root, self.alive_message_interval_seconds, "AliveMessageIntervalSeconds"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.blast_alive_message_interval_seconds,
            "BlastAliveMessageIntervalSeconds",
        )
        XmlUtilities.add_as_subelement(root, self.default_user_id, "DefaultUserId")
        XmlUtilities.add_as_subelement(
            root, self.auto_create_play_to_profiles, "AutoCreatePlayToProfiles"
        )
        XmlUtilities.add_as_subelement(
            root, self.blast_alive_messages, "BlastAliveMessages"
        )
        XmlUtilities.add_as_subelement(
            root, self.send_only_matched_host, "SendOnlyMatchedHost"
        )
