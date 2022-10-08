# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.notification_dto import NotificationDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationResultDto(object):

    """Implementation of the 'NotificationResultDto' model.

    A list of notifications with the total record count for pagination.

    Attributes:
        notifications (list of NotificationDto): Gets or sets the current page
            of notifications.
        total_record_count (int): Gets or sets the total number of
            notifications.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "notifications": "Notifications",
        "total_record_count": "TotalRecordCount",
    }

    _optionals = [
        "notifications",
        "total_record_count",
    ]

    def __init__(self, notifications=APIHelper.SKIP, total_record_count=APIHelper.SKIP):
        """Constructor for the NotificationResultDto class"""

        # Initialize members of the class
        if notifications is not APIHelper.SKIP:
            self.notifications = notifications
        if total_record_count is not APIHelper.SKIP:
            self.total_record_count = total_record_count

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

        notifications = None
        if dictionary.get("Notifications") is not None:
            notifications = [
                NotificationDto.from_dictionary(x)
                for x in dictionary.get("Notifications")
            ]
        else:
            notifications = APIHelper.SKIP
        total_record_count = (
            dictionary.get("TotalRecordCount")
            if dictionary.get("TotalRecordCount")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(notifications, total_record_count)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        notifications = XmlUtilities.list_from_xml_element(
            root, "NotificationDto", NotificationDto
        )
        total_record_count = XmlUtilities.value_from_xml_element(
            root.find("TotalRecordCount"), int
        )

        return cls(notifications, total_record_count)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.notifications, "NotificationDto")
        XmlUtilities.add_as_subelement(
            root, self.total_record_count, "TotalRecordCount"
        )
