# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PluginInfo(object):

    """Implementation of the 'PluginInfo' model.

    This is a serializable stub class that is used by the api to provide
    information about installed plugins.

    Attributes:
        name (string): Gets or sets the name.
        version (string): Gets or sets the version.
        configuration_file_name (string): Gets or sets the name of the
            configuration file.
        description (string): Gets or sets the description.
        id (uuid|string): Gets or sets the unique id.
        can_uninstall (bool): Gets or sets a value indicating whether the
            plugin can be uninstalled.
        has_image (bool): Gets or sets a value indicating whether this plugin
            has a valid image.
        status (PluginStatusEnum): Gets or sets a value indicating the status
            of the plugin.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "version": "Version",
        "configuration_file_name": "ConfigurationFileName",
        "description": "Description",
        "id": "Id",
        "can_uninstall": "CanUninstall",
        "has_image": "HasImage",
        "status": "Status",
    }

    _optionals = [
        "name",
        "version",
        "configuration_file_name",
        "description",
        "id",
        "can_uninstall",
        "has_image",
        "status",
    ]

    _nullables = [
        "configuration_file_name",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        version=APIHelper.SKIP,
        configuration_file_name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        id=APIHelper.SKIP,
        can_uninstall=APIHelper.SKIP,
        has_image=APIHelper.SKIP,
        status=APIHelper.SKIP,
    ):
        """Constructor for the PluginInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if version is not APIHelper.SKIP:
            self.version = version
        if configuration_file_name is not APIHelper.SKIP:
            self.configuration_file_name = configuration_file_name
        if description is not APIHelper.SKIP:
            self.description = description
        if id is not APIHelper.SKIP:
            self.id = id
        if can_uninstall is not APIHelper.SKIP:
            self.can_uninstall = can_uninstall
        if has_image is not APIHelper.SKIP:
            self.has_image = has_image
        if status is not APIHelper.SKIP:
            self.status = status

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        version = (
            dictionary.get("Version") if dictionary.get("Version") else APIHelper.SKIP
        )
        configuration_file_name = (
            dictionary.get("ConfigurationFileName")
            if "ConfigurationFileName" in dictionary.keys()
            else APIHelper.SKIP
        )
        description = (
            dictionary.get("Description")
            if dictionary.get("Description")
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        can_uninstall = (
            dictionary.get("CanUninstall")
            if "CanUninstall" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_image = (
            dictionary.get("HasImage")
            if "HasImage" in dictionary.keys()
            else APIHelper.SKIP
        )
        status = (
            dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            version,
            configuration_file_name,
            description,
            id,
            can_uninstall,
            has_image,
            status,
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
        version = XmlUtilities.value_from_xml_element(root.find("Version"), str)
        configuration_file_name = XmlUtilities.value_from_xml_element(
            root.find("ConfigurationFileName"), str
        )
        description = XmlUtilities.value_from_xml_element(root.find("Description"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        can_uninstall = XmlUtilities.value_from_xml_element(
            root.find("CanUninstall"), bool
        )
        has_image = XmlUtilities.value_from_xml_element(root.find("HasImage"), bool)
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)

        return cls(
            name,
            version,
            configuration_file_name,
            description,
            id,
            can_uninstall,
            has_image,
            status,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.version, "Version")
        XmlUtilities.add_as_subelement(
            root, self.configuration_file_name, "ConfigurationFileName"
        )
        XmlUtilities.add_as_subelement(root, self.description, "Description")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.can_uninstall, "CanUninstall")
        XmlUtilities.add_as_subelement(root, self.has_image, "HasImage")
        XmlUtilities.add_as_subelement(root, self.status, "Status")
