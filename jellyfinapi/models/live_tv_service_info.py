# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LiveTvServiceInfo(object):

    """Implementation of the 'LiveTvServiceInfo' model.

    Class ServiceInfo.

    Attributes:
        name (string): Gets or sets the name.
        home_page_url (string): Gets or sets the home page URL.
        status (LiveTvServiceStatusEnum): Gets or sets the status.
        status_message (string): Gets or sets the status message.
        version (string): Gets or sets the version.
        has_update_available (bool): Gets or sets a value indicating whether
            this instance has update available.
        is_visible (bool): Gets or sets a value indicating whether this
            instance is visible.
        tuners (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "home_page_url": "HomePageUrl",
        "status": "Status",
        "status_message": "StatusMessage",
        "version": "Version",
        "has_update_available": "HasUpdateAvailable",
        "is_visible": "IsVisible",
        "tuners": "Tuners",
    }

    _optionals = [
        "name",
        "home_page_url",
        "status",
        "status_message",
        "version",
        "has_update_available",
        "is_visible",
        "tuners",
    ]

    _nullables = [
        "name",
        "home_page_url",
        "status_message",
        "version",
        "tuners",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        home_page_url=APIHelper.SKIP,
        status=APIHelper.SKIP,
        status_message=APIHelper.SKIP,
        version=APIHelper.SKIP,
        has_update_available=APIHelper.SKIP,
        is_visible=APIHelper.SKIP,
        tuners=APIHelper.SKIP,
    ):
        """Constructor for the LiveTvServiceInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if home_page_url is not APIHelper.SKIP:
            self.home_page_url = home_page_url
        if status is not APIHelper.SKIP:
            self.status = status
        if status_message is not APIHelper.SKIP:
            self.status_message = status_message
        if version is not APIHelper.SKIP:
            self.version = version
        if has_update_available is not APIHelper.SKIP:
            self.has_update_available = has_update_available
        if is_visible is not APIHelper.SKIP:
            self.is_visible = is_visible
        if tuners is not APIHelper.SKIP:
            self.tuners = tuners

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
        home_page_url = (
            dictionary.get("HomePageUrl")
            if "HomePageUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        status = (
            dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        )
        status_message = (
            dictionary.get("StatusMessage")
            if "StatusMessage" in dictionary.keys()
            else APIHelper.SKIP
        )
        version = (
            dictionary.get("Version")
            if "Version" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_update_available = (
            dictionary.get("HasUpdateAvailable")
            if "HasUpdateAvailable" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_visible = (
            dictionary.get("IsVisible")
            if "IsVisible" in dictionary.keys()
            else APIHelper.SKIP
        )
        tuners = (
            dictionary.get("Tuners")
            if "Tuners" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            home_page_url,
            status,
            status_message,
            version,
            has_update_available,
            is_visible,
            tuners,
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
        home_page_url = XmlUtilities.value_from_xml_element(
            root.find("HomePageUrl"), str
        )
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)
        status_message = XmlUtilities.value_from_xml_element(
            root.find("StatusMessage"), str
        )
        version = XmlUtilities.value_from_xml_element(root.find("Version"), str)
        has_update_available = XmlUtilities.value_from_xml_element(
            root.find("HasUpdateAvailable"), bool
        )
        is_visible = XmlUtilities.value_from_xml_element(root.find("IsVisible"), bool)
        tuners = XmlUtilities.list_from_xml_element(root, "Tuners", str)

        return cls(
            name,
            home_page_url,
            status,
            status_message,
            version,
            has_update_available,
            is_visible,
            tuners,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.home_page_url, "HomePageUrl")
        XmlUtilities.add_as_subelement(root, self.status, "Status")
        XmlUtilities.add_as_subelement(root, self.status_message, "StatusMessage")
        XmlUtilities.add_as_subelement(root, self.version, "Version")
        XmlUtilities.add_as_subelement(
            root, self.has_update_available, "HasUpdateAvailable"
        )
        XmlUtilities.add_as_subelement(root, self.is_visible, "IsVisible")
        XmlUtilities.add_list_as_subelement(root, self.tuners, "Tuners")
