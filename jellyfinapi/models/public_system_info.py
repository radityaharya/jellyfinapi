# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PublicSystemInfo(object):

    """Implementation of the 'PublicSystemInfo' model.

    TODO: type model description here.

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
    }

    _optionals = [
        "local_address",
        "server_name",
        "version",
        "product_name",
        "operating_system",
        "id",
        "startup_wizard_completed",
    ]

    _nullables = [
        "local_address",
        "server_name",
        "version",
        "product_name",
        "operating_system",
        "id",
        "startup_wizard_completed",
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
    ):
        """Constructor for the PublicSystemInfo class"""

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
        # Return an object of this model
        return cls(
            local_address,
            server_name,
            version,
            product_name,
            operating_system,
            id,
            startup_wizard_completed,
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

        return cls(
            local_address,
            server_name,
            version,
            product_name,
            operating_system,
            id,
            startup_wizard_completed,
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
