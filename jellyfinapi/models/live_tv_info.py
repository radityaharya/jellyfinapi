# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.live_tv_service_info import LiveTvServiceInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LiveTvInfo(object):

    """Implementation of the 'LiveTvInfo' model.

    TODO: type model description here.

    Attributes:
        services (list of LiveTvServiceInfo): Gets or sets the services.
        is_enabled (bool): Gets or sets a value indicating whether this
            instance is enabled.
        enabled_users (list of string): Gets or sets the enabled users.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "services": "Services",
        "is_enabled": "IsEnabled",
        "enabled_users": "EnabledUsers",
    }

    _optionals = [
        "services",
        "is_enabled",
        "enabled_users",
    ]

    def __init__(
        self,
        services=APIHelper.SKIP,
        is_enabled=APIHelper.SKIP,
        enabled_users=APIHelper.SKIP,
    ):
        """Constructor for the LiveTvInfo class"""

        # Initialize members of the class
        if services is not APIHelper.SKIP:
            self.services = services
        if is_enabled is not APIHelper.SKIP:
            self.is_enabled = is_enabled
        if enabled_users is not APIHelper.SKIP:
            self.enabled_users = enabled_users

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

        services = None
        if dictionary.get("Services") is not None:
            services = [
                LiveTvServiceInfo.from_dictionary(x) for x in dictionary.get("Services")
            ]
        else:
            services = APIHelper.SKIP
        is_enabled = (
            dictionary.get("IsEnabled")
            if "IsEnabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        enabled_users = (
            dictionary.get("EnabledUsers")
            if dictionary.get("EnabledUsers")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(services, is_enabled, enabled_users)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        services = XmlUtilities.list_from_xml_element(
            root, "LiveTvServiceInfo", LiveTvServiceInfo
        )
        is_enabled = XmlUtilities.value_from_xml_element(root.find("IsEnabled"), bool)
        enabled_users = XmlUtilities.list_from_xml_element(root, "EnabledUsers", str)

        return cls(services, is_enabled, enabled_users)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.services, "LiveTvServiceInfo")
        XmlUtilities.add_as_subelement(root, self.is_enabled, "IsEnabled")
        XmlUtilities.add_list_as_subelement(root, self.enabled_users, "EnabledUsers")
