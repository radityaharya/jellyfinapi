# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationsSummaryDto(object):

    """Implementation of the 'NotificationsSummaryDto' model.

    The notification summary DTO.

    Attributes:
        unread_count (int): Gets or sets the number of unread notifications.
        max_unread_notification_level (NotificationLevelEnum): Gets or sets
            the maximum unread notification level.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "unread_count": "UnreadCount",
        "max_unread_notification_level": "MaxUnreadNotificationLevel",
    }

    _optionals = [
        "unread_count",
        "max_unread_notification_level",
    ]

    _nullables = [
        "max_unread_notification_level",
    ]

    def __init__(
        self, unread_count=APIHelper.SKIP, max_unread_notification_level=APIHelper.SKIP
    ):
        """Constructor for the NotificationsSummaryDto class"""

        # Initialize members of the class
        if unread_count is not APIHelper.SKIP:
            self.unread_count = unread_count
        if max_unread_notification_level is not APIHelper.SKIP:
            self.max_unread_notification_level = max_unread_notification_level

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

        unread_count = (
            dictionary.get("UnreadCount")
            if dictionary.get("UnreadCount")
            else APIHelper.SKIP
        )
        max_unread_notification_level = (
            dictionary.get("MaxUnreadNotificationLevel")
            if "MaxUnreadNotificationLevel" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(unread_count, max_unread_notification_level)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        unread_count = XmlUtilities.value_from_xml_element(
            root.find("UnreadCount"), int
        )
        max_unread_notification_level = XmlUtilities.value_from_xml_element(
            root.find("MaxUnreadNotificationLevel"), str
        )

        return cls(unread_count, max_unread_notification_level)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.unread_count, "UnreadCount")
        XmlUtilities.add_as_subelement(
            root, self.max_unread_notification_level, "MaxUnreadNotificationLevel"
        )
