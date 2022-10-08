# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.installation_info import InstallationInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SystemInfo(object):

    """Implementation of the 'SystemInfo' model.

    Class SystemInfo.

    Attributes:
        local_address (string): Gets or sets the local address.
        server_name (string): Gets or sets the name of the server.
        version (string): Gets or sets the server version.
        product_name (string): Gets or sets the product name. This is the
            AssemblyProduct name.
        operating_system (string): Gets or sets the operating system.
        id (string): Gets or sets the id.
        startup_wizard_completed (bool): Gets or sets a value indicating
            whether the startup wizard is completed.
        operating_system_display_name (string): Gets or sets the display name
            of the operating system.
        package_name (string): Gets or sets the package name.
        has_pending_restart (bool): Gets or sets a value indicating whether
            this instance has pending restart.
        is_shutting_down (bool): TODO: type description here.
        supports_library_monitor (bool): Gets or sets a value indicating
            whether [supports library monitor].
        web_socket_port_number (int): Gets or sets the web socket port
            number.
        completed_installations (list of InstallationInfo): Gets or sets the
            completed installations.
        can_self_restart (bool): Gets or sets a value indicating whether this
            instance can self restart.
        can_launch_web_browser (bool): TODO: type description here.
        program_data_path (string): Gets or sets the program data path.
        web_path (string): Gets or sets the web UI resources path.
        items_by_name_path (string): Gets or sets the items by name path.
        cache_path (string): Gets or sets the cache path.
        log_path (string): Gets or sets the log path.
        internal_metadata_path (string): Gets or sets the internal metadata
            path.
        transcoding_temp_path (string): Gets or sets the transcode path.
        has_update_available (bool): Gets or sets a value indicating whether
            this instance has update available.
        encoder_location (FFmpegLocationEnum): Enum describing the location of
            the FFmpeg tool.
        system_architecture (ArchitectureEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "local_address": "LocalAddress",
        "server_name": "ServerName",
        "version": "Version",
        "product_name": "ProductName",
        "operating_system": "OperatingSystem",
        "id": "Id",
        "startup_wizard_completed": "StartupWizardCompleted",
        "operating_system_display_name": "OperatingSystemDisplayName",
        "package_name": "PackageName",
        "has_pending_restart": "HasPendingRestart",
        "is_shutting_down": "IsShuttingDown",
        "supports_library_monitor": "SupportsLibraryMonitor",
        "web_socket_port_number": "WebSocketPortNumber",
        "completed_installations": "CompletedInstallations",
        "can_self_restart": "CanSelfRestart",
        "can_launch_web_browser": "CanLaunchWebBrowser",
        "program_data_path": "ProgramDataPath",
        "web_path": "WebPath",
        "items_by_name_path": "ItemsByNamePath",
        "cache_path": "CachePath",
        "log_path": "LogPath",
        "internal_metadata_path": "InternalMetadataPath",
        "transcoding_temp_path": "TranscodingTempPath",
        "has_update_available": "HasUpdateAvailable",
        "encoder_location": "EncoderLocation",
        "system_architecture": "SystemArchitecture",
    }

    _optionals = [
        "local_address",
        "server_name",
        "version",
        "product_name",
        "operating_system",
        "id",
        "startup_wizard_completed",
        "operating_system_display_name",
        "package_name",
        "has_pending_restart",
        "is_shutting_down",
        "supports_library_monitor",
        "web_socket_port_number",
        "completed_installations",
        "can_self_restart",
        "can_launch_web_browser",
        "program_data_path",
        "web_path",
        "items_by_name_path",
        "cache_path",
        "log_path",
        "internal_metadata_path",
        "transcoding_temp_path",
        "has_update_available",
        "encoder_location",
        "system_architecture",
    ]

    _nullables = [
        "local_address",
        "server_name",
        "version",
        "product_name",
        "operating_system",
        "id",
        "startup_wizard_completed",
        "operating_system_display_name",
        "package_name",
        "completed_installations",
        "program_data_path",
        "web_path",
        "items_by_name_path",
        "cache_path",
        "log_path",
        "internal_metadata_path",
        "transcoding_temp_path",
    ]

    def __init__(
        self,
        local_address=APIHelper.SKIP,
        server_name=APIHelper.SKIP,
        version=APIHelper.SKIP,
        product_name=APIHelper.SKIP,
        operating_system=APIHelper.SKIP,
        id=APIHelper.SKIP,
        startup_wizard_completed=APIHelper.SKIP,
        operating_system_display_name=APIHelper.SKIP,
        package_name=APIHelper.SKIP,
        has_pending_restart=APIHelper.SKIP,
        is_shutting_down=APIHelper.SKIP,
        supports_library_monitor=APIHelper.SKIP,
        web_socket_port_number=APIHelper.SKIP,
        completed_installations=APIHelper.SKIP,
        can_self_restart=APIHelper.SKIP,
        can_launch_web_browser=APIHelper.SKIP,
        program_data_path=APIHelper.SKIP,
        web_path=APIHelper.SKIP,
        items_by_name_path=APIHelper.SKIP,
        cache_path=APIHelper.SKIP,
        log_path=APIHelper.SKIP,
        internal_metadata_path=APIHelper.SKIP,
        transcoding_temp_path=APIHelper.SKIP,
        has_update_available=APIHelper.SKIP,
        encoder_location=APIHelper.SKIP,
        system_architecture=APIHelper.SKIP,
    ):
        """Constructor for the SystemInfo class"""

        # Initialize members of the class
        if local_address is not APIHelper.SKIP:
            self.local_address = local_address
        if server_name is not APIHelper.SKIP:
            self.server_name = server_name
        if version is not APIHelper.SKIP:
            self.version = version
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name
        if operating_system is not APIHelper.SKIP:
            self.operating_system = operating_system
        if id is not APIHelper.SKIP:
            self.id = id
        if startup_wizard_completed is not APIHelper.SKIP:
            self.startup_wizard_completed = startup_wizard_completed
        if operating_system_display_name is not APIHelper.SKIP:
            self.operating_system_display_name = operating_system_display_name
        if package_name is not APIHelper.SKIP:
            self.package_name = package_name
        if has_pending_restart is not APIHelper.SKIP:
            self.has_pending_restart = has_pending_restart
        if is_shutting_down is not APIHelper.SKIP:
            self.is_shutting_down = is_shutting_down
        if supports_library_monitor is not APIHelper.SKIP:
            self.supports_library_monitor = supports_library_monitor
        if web_socket_port_number is not APIHelper.SKIP:
            self.web_socket_port_number = web_socket_port_number
        if completed_installations is not APIHelper.SKIP:
            self.completed_installations = completed_installations
        if can_self_restart is not APIHelper.SKIP:
            self.can_self_restart = can_self_restart
        if can_launch_web_browser is not APIHelper.SKIP:
            self.can_launch_web_browser = can_launch_web_browser
        if program_data_path is not APIHelper.SKIP:
            self.program_data_path = program_data_path
        if web_path is not APIHelper.SKIP:
            self.web_path = web_path
        if items_by_name_path is not APIHelper.SKIP:
            self.items_by_name_path = items_by_name_path
        if cache_path is not APIHelper.SKIP:
            self.cache_path = cache_path
        if log_path is not APIHelper.SKIP:
            self.log_path = log_path
        if internal_metadata_path is not APIHelper.SKIP:
            self.internal_metadata_path = internal_metadata_path
        if transcoding_temp_path is not APIHelper.SKIP:
            self.transcoding_temp_path = transcoding_temp_path
        if has_update_available is not APIHelper.SKIP:
            self.has_update_available = has_update_available
        if encoder_location is not APIHelper.SKIP:
            self.encoder_location = encoder_location
        if system_architecture is not APIHelper.SKIP:
            self.system_architecture = system_architecture

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

        local_address = (
            dictionary.get("LocalAddress")
            if "LocalAddress" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_name = (
            dictionary.get("ServerName")
            if "ServerName" in dictionary.keys()
            else APIHelper.SKIP
        )
        version = (
            dictionary.get("Version")
            if "Version" in dictionary.keys()
            else APIHelper.SKIP
        )
        product_name = (
            dictionary.get("ProductName")
            if "ProductName" in dictionary.keys()
            else APIHelper.SKIP
        )
        operating_system = (
            dictionary.get("OperatingSystem")
            if "OperatingSystem" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        startup_wizard_completed = (
            dictionary.get("StartupWizardCompleted")
            if "StartupWizardCompleted" in dictionary.keys()
            else APIHelper.SKIP
        )
        operating_system_display_name = (
            dictionary.get("OperatingSystemDisplayName")
            if "OperatingSystemDisplayName" in dictionary.keys()
            else APIHelper.SKIP
        )
        package_name = (
            dictionary.get("PackageName")
            if "PackageName" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_pending_restart = (
            dictionary.get("HasPendingRestart")
            if "HasPendingRestart" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_shutting_down = (
            dictionary.get("IsShuttingDown")
            if "IsShuttingDown" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_library_monitor = (
            dictionary.get("SupportsLibraryMonitor")
            if "SupportsLibraryMonitor" in dictionary.keys()
            else APIHelper.SKIP
        )
        web_socket_port_number = (
            dictionary.get("WebSocketPortNumber")
            if dictionary.get("WebSocketPortNumber")
            else APIHelper.SKIP
        )
        if "CompletedInstallations" in dictionary.keys():
            completed_installations = (
                [
                    InstallationInfo.from_dictionary(x)
                    for x in dictionary.get("CompletedInstallations")
                ]
                if dictionary.get("CompletedInstallations")
                else None
            )
        else:
            completed_installations = APIHelper.SKIP
        can_self_restart = (
            dictionary.get("CanSelfRestart")
            if "CanSelfRestart" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_launch_web_browser = (
            dictionary.get("CanLaunchWebBrowser")
            if "CanLaunchWebBrowser" in dictionary.keys()
            else APIHelper.SKIP
        )
        program_data_path = (
            dictionary.get("ProgramDataPath")
            if "ProgramDataPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        web_path = (
            dictionary.get("WebPath")
            if "WebPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        items_by_name_path = (
            dictionary.get("ItemsByNamePath")
            if "ItemsByNamePath" in dictionary.keys()
            else APIHelper.SKIP
        )
        cache_path = (
            dictionary.get("CachePath")
            if "CachePath" in dictionary.keys()
            else APIHelper.SKIP
        )
        log_path = (
            dictionary.get("LogPath")
            if "LogPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        internal_metadata_path = (
            dictionary.get("InternalMetadataPath")
            if "InternalMetadataPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        transcoding_temp_path = (
            dictionary.get("TranscodingTempPath")
            if "TranscodingTempPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_update_available = (
            dictionary.get("HasUpdateAvailable")
            if "HasUpdateAvailable" in dictionary.keys()
            else APIHelper.SKIP
        )
        encoder_location = (
            dictionary.get("EncoderLocation")
            if dictionary.get("EncoderLocation")
            else APIHelper.SKIP
        )
        system_architecture = (
            dictionary.get("SystemArchitecture")
            if dictionary.get("SystemArchitecture")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            local_address,
            server_name,
            version,
            product_name,
            operating_system,
            id,
            startup_wizard_completed,
            operating_system_display_name,
            package_name,
            has_pending_restart,
            is_shutting_down,
            supports_library_monitor,
            web_socket_port_number,
            completed_installations,
            can_self_restart,
            can_launch_web_browser,
            program_data_path,
            web_path,
            items_by_name_path,
            cache_path,
            log_path,
            internal_metadata_path,
            transcoding_temp_path,
            has_update_available,
            encoder_location,
            system_architecture,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        local_address = XmlUtilities.value_from_xml_element(
            root.find("LocalAddress"), str
        )
        server_name = XmlUtilities.value_from_xml_element(root.find("ServerName"), str)
        version = XmlUtilities.value_from_xml_element(root.find("Version"), str)
        product_name = XmlUtilities.value_from_xml_element(
            root.find("ProductName"), str
        )
        operating_system = XmlUtilities.value_from_xml_element(
            root.find("OperatingSystem"), str
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        startup_wizard_completed = XmlUtilities.value_from_xml_element(
            root.find("StartupWizardCompleted"), bool
        )
        operating_system_display_name = XmlUtilities.value_from_xml_element(
            root.find("OperatingSystemDisplayName"), str
        )
        package_name = XmlUtilities.value_from_xml_element(
            root.find("PackageName"), str
        )
        has_pending_restart = XmlUtilities.value_from_xml_element(
            root.find("HasPendingRestart"), bool
        )
        is_shutting_down = XmlUtilities.value_from_xml_element(
            root.find("IsShuttingDown"), bool
        )
        supports_library_monitor = XmlUtilities.value_from_xml_element(
            root.find("SupportsLibraryMonitor"), bool
        )
        web_socket_port_number = XmlUtilities.value_from_xml_element(
            root.find("WebSocketPortNumber"), int
        )
        completed_installations = XmlUtilities.list_from_xml_element(
            root, "InstallationInfo", InstallationInfo
        )
        can_self_restart = XmlUtilities.value_from_xml_element(
            root.find("CanSelfRestart"), bool
        )
        can_launch_web_browser = XmlUtilities.value_from_xml_element(
            root.find("CanLaunchWebBrowser"), bool
        )
        program_data_path = XmlUtilities.value_from_xml_element(
            root.find("ProgramDataPath"), str
        )
        web_path = XmlUtilities.value_from_xml_element(root.find("WebPath"), str)
        items_by_name_path = XmlUtilities.value_from_xml_element(
            root.find("ItemsByNamePath"), str
        )
        cache_path = XmlUtilities.value_from_xml_element(root.find("CachePath"), str)
        log_path = XmlUtilities.value_from_xml_element(root.find("LogPath"), str)
        internal_metadata_path = XmlUtilities.value_from_xml_element(
            root.find("InternalMetadataPath"), str
        )
        transcoding_temp_path = XmlUtilities.value_from_xml_element(
            root.find("TranscodingTempPath"), str
        )
        has_update_available = XmlUtilities.value_from_xml_element(
            root.find("HasUpdateAvailable"), bool
        )
        encoder_location = XmlUtilities.value_from_xml_element(
            root.find("EncoderLocation"), str
        )
        system_architecture = XmlUtilities.value_from_xml_element(
            root.find("SystemArchitecture"), str
        )

        return cls(
            local_address,
            server_name,
            version,
            product_name,
            operating_system,
            id,
            startup_wizard_completed,
            operating_system_display_name,
            package_name,
            has_pending_restart,
            is_shutting_down,
            supports_library_monitor,
            web_socket_port_number,
            completed_installations,
            can_self_restart,
            can_launch_web_browser,
            program_data_path,
            web_path,
            items_by_name_path,
            cache_path,
            log_path,
            internal_metadata_path,
            transcoding_temp_path,
            has_update_available,
            encoder_location,
            system_architecture,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.local_address, "LocalAddress")
        XmlUtilities.add_as_subelement(root, self.server_name, "ServerName")
        XmlUtilities.add_as_subelement(root, self.version, "Version")
        XmlUtilities.add_as_subelement(root, self.product_name, "ProductName")
        XmlUtilities.add_as_subelement(root, self.operating_system, "OperatingSystem")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(
            root, self.startup_wizard_completed, "StartupWizardCompleted"
        )
        XmlUtilities.add_as_subelement(
            root, self.operating_system_display_name, "OperatingSystemDisplayName"
        )
        XmlUtilities.add_as_subelement(root, self.package_name, "PackageName")
        XmlUtilities.add_as_subelement(
            root, self.has_pending_restart, "HasPendingRestart"
        )
        XmlUtilities.add_as_subelement(root, self.is_shutting_down, "IsShuttingDown")
        XmlUtilities.add_as_subelement(
            root, self.supports_library_monitor, "SupportsLibraryMonitor"
        )
        XmlUtilities.add_as_subelement(
            root, self.web_socket_port_number, "WebSocketPortNumber"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.completed_installations, "InstallationInfo"
        )
        XmlUtilities.add_as_subelement(root, self.can_self_restart, "CanSelfRestart")
        XmlUtilities.add_as_subelement(
            root, self.can_launch_web_browser, "CanLaunchWebBrowser"
        )
        XmlUtilities.add_as_subelement(root, self.program_data_path, "ProgramDataPath")
        XmlUtilities.add_as_subelement(root, self.web_path, "WebPath")
        XmlUtilities.add_as_subelement(root, self.items_by_name_path, "ItemsByNamePath")
        XmlUtilities.add_as_subelement(root, self.cache_path, "CachePath")
        XmlUtilities.add_as_subelement(root, self.log_path, "LogPath")
        XmlUtilities.add_as_subelement(
            root, self.internal_metadata_path, "InternalMetadataPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.transcoding_temp_path, "TranscodingTempPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.has_update_available, "HasUpdateAvailable"
        )
        XmlUtilities.add_as_subelement(root, self.encoder_location, "EncoderLocation")
        XmlUtilities.add_as_subelement(
            root, self.system_architecture, "SystemArchitecture"
        )
