# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ConfigurationPageInfo(object):

    """Implementation of the 'ConfigurationPageInfo' model.

    The configuration page info.

    Attributes:
        name (string): Gets or sets the name.
        enable_in_main_menu (bool): Gets or sets a value indicating whether
            the configurations page is enabled in the main menu.
        menu_section (string): Gets or sets the menu section.
        menu_icon (string): Gets or sets the menu icon.
        display_name (string): Gets or sets the display name.
        plugin_id (uuid|string): Gets or sets the plugin id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "enable_in_main_menu": "EnableInMainMenu",
        "menu_section": "MenuSection",
        "menu_icon": "MenuIcon",
        "display_name": "DisplayName",
        "plugin_id": "PluginId",
    }

    _optionals = [
        "name",
        "enable_in_main_menu",
        "menu_section",
        "menu_icon",
        "display_name",
        "plugin_id",
    ]

    _nullables = [
        "menu_section",
        "menu_icon",
        "display_name",
        "plugin_id",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        enable_in_main_menu=APIHelper.SKIP,
        menu_section=APIHelper.SKIP,
        menu_icon=APIHelper.SKIP,
        display_name=APIHelper.SKIP,
        plugin_id=APIHelper.SKIP,
    ):
        """Constructor for the ConfigurationPageInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if enable_in_main_menu is not APIHelper.SKIP:
            self.enable_in_main_menu = enable_in_main_menu
        if menu_section is not APIHelper.SKIP:
            self.menu_section = menu_section
        if menu_icon is not APIHelper.SKIP:
            self.menu_icon = menu_icon
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name
        if plugin_id is not APIHelper.SKIP:
            self.plugin_id = plugin_id

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
        enable_in_main_menu = (
            dictionary.get("EnableInMainMenu")
            if "EnableInMainMenu" in dictionary.keys()
            else APIHelper.SKIP
        )
        menu_section = (
            dictionary.get("MenuSection")
            if "MenuSection" in dictionary.keys()
            else APIHelper.SKIP
        )
        menu_icon = (
            dictionary.get("MenuIcon")
            if "MenuIcon" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_name = (
            dictionary.get("DisplayName")
            if "DisplayName" in dictionary.keys()
            else APIHelper.SKIP
        )
        plugin_id = (
            dictionary.get("PluginId")
            if "PluginId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name, enable_in_main_menu, menu_section, menu_icon, display_name, plugin_id
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
        enable_in_main_menu = XmlUtilities.value_from_xml_element(
            root.find("EnableInMainMenu"), bool
        )
        menu_section = XmlUtilities.value_from_xml_element(
            root.find("MenuSection"), str
        )
        menu_icon = XmlUtilities.value_from_xml_element(root.find("MenuIcon"), str)
        display_name = XmlUtilities.value_from_xml_element(
            root.find("DisplayName"), str
        )
        plugin_id = XmlUtilities.value_from_xml_element(root.find("PluginId"), str)

        return cls(
            name, enable_in_main_menu, menu_section, menu_icon, display_name, plugin_id
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(
            root, self.enable_in_main_menu, "EnableInMainMenu"
        )
        XmlUtilities.add_as_subelement(root, self.menu_section, "MenuSection")
        XmlUtilities.add_as_subelement(root, self.menu_icon, "MenuIcon")
        XmlUtilities.add_as_subelement(root, self.display_name, "DisplayName")
        XmlUtilities.add_as_subelement(root, self.plugin_id, "PluginId")
