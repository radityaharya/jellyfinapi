# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class IPlugin(object):

    """Implementation of the 'IPlugin' model.

    Defines the MediaBrowser.Common.Plugins.IPlugin.

    Attributes:
        name (string): Gets the name of the plugin.
        description (string): Gets the Description.
        id (uuid|string): Gets the unique id.
        version (string): Gets the plugin version.
        assembly_file_path (string): Gets the path to the assembly file.
        can_uninstall (bool): Gets a value indicating whether the plugin can
            be uninstalled.
        data_folder_path (string): Gets the full path to the data folder,
            where the plugin can store any miscellaneous files needed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "description": "Description",
        "id": "Id",
        "version": "Version",
        "assembly_file_path": "AssemblyFilePath",
        "can_uninstall": "CanUninstall",
        "data_folder_path": "DataFolderPath",
    }

    _optionals = [
        "name",
        "description",
        "id",
        "version",
        "assembly_file_path",
        "can_uninstall",
        "data_folder_path",
    ]

    _nullables = [
        "name",
        "description",
        "version",
        "assembly_file_path",
        "data_folder_path",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        id=APIHelper.SKIP,
        version=APIHelper.SKIP,
        assembly_file_path=APIHelper.SKIP,
        can_uninstall=APIHelper.SKIP,
        data_folder_path=APIHelper.SKIP,
    ):
        """Constructor for the IPlugin class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if id is not APIHelper.SKIP:
            self.id = id
        if version is not APIHelper.SKIP:
            self.version = version
        if assembly_file_path is not APIHelper.SKIP:
            self.assembly_file_path = assembly_file_path
        if can_uninstall is not APIHelper.SKIP:
            self.can_uninstall = can_uninstall
        if data_folder_path is not APIHelper.SKIP:
            self.data_folder_path = data_folder_path

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
        description = (
            dictionary.get("Description")
            if "Description" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        version = (
            dictionary.get("Version")
            if "Version" in dictionary.keys()
            else APIHelper.SKIP
        )
        assembly_file_path = (
            dictionary.get("AssemblyFilePath")
            if "AssemblyFilePath" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_uninstall = (
            dictionary.get("CanUninstall")
            if "CanUninstall" in dictionary.keys()
            else APIHelper.SKIP
        )
        data_folder_path = (
            dictionary.get("DataFolderPath")
            if "DataFolderPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            description,
            id,
            version,
            assembly_file_path,
            can_uninstall,
            data_folder_path,
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
        description = XmlUtilities.value_from_xml_element(root.find("Description"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        version = XmlUtilities.value_from_xml_element(root.find("Version"), str)
        assembly_file_path = XmlUtilities.value_from_xml_element(
            root.find("AssemblyFilePath"), str
        )
        can_uninstall = XmlUtilities.value_from_xml_element(
            root.find("CanUninstall"), bool
        )
        data_folder_path = XmlUtilities.value_from_xml_element(
            root.find("DataFolderPath"), str
        )

        return cls(
            name,
            description,
            id,
            version,
            assembly_file_path,
            can_uninstall,
            data_folder_path,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.description, "Description")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.version, "Version")
        XmlUtilities.add_as_subelement(
            root, self.assembly_file_path, "AssemblyFilePath"
        )
        XmlUtilities.add_as_subelement(root, self.can_uninstall, "CanUninstall")
        XmlUtilities.add_as_subelement(root, self.data_folder_path, "DataFolderPath")
