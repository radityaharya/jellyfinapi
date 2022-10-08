# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AdminNotificationDto(object):

    """Implementation of the 'AdminNotificationDto' model.

    The admin notification dto.

    Attributes:
        name (string): Gets or sets the notification name.
        description (string): Gets or sets the notification description.
        notification_level (NotificationLevelEnum): Gets or sets the
            notification level.
        url (string): Gets or sets the notification url.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "description": "Description",
        "notification_level": "NotificationLevel",
        "url": "Url",
    }

    _optionals = [
        "name",
        "description",
        "notification_level",
        "url",
    ]

    _nullables = [
        "name",
        "description",
        "notification_level",
        "url",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        notification_level=APIHelper.SKIP,
        url=APIHelper.SKIP,
    ):
        """Constructor for the AdminNotificationDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if notification_level is not APIHelper.SKIP:
            self.notification_level = notification_level
        if url is not APIHelper.SKIP:
            self.url = url

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
        notification_level = (
            dictionary.get("NotificationLevel")
            if "NotificationLevel" in dictionary.keys()
            else APIHelper.SKIP
        )
        url = dictionary.get("Url") if "Url" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name, description, notification_level, url)

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
        notification_level = XmlUtilities.value_from_xml_element(
            root.find("NotificationLevel"), str
        )
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)

        return cls(name, description, notification_level, url)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.description, "Description")
        XmlUtilities.add_as_subelement(
            root, self.notification_level, "NotificationLevel"
        )
        XmlUtilities.add_as_subelement(root, self.url, "Url")
