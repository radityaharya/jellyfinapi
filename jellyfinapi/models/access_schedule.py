# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AccessSchedule(object):

    """Implementation of the 'AccessSchedule' model.

    An entity representing a user's access schedule.

    Attributes:
        id (int): Gets the id of this instance.
        user_id (uuid|string): Gets the id of the associated user.
        day_of_week (DynamicDayOfWeekEnum): Gets or sets the day of week.
        start_hour (float): Gets or sets the start hour.
        end_hour (float): Gets or sets the end hour.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "user_id": "UserId",
        "day_of_week": "DayOfWeek",
        "start_hour": "StartHour",
        "end_hour": "EndHour",
    }

    _optionals = [
        "id",
        "user_id",
        "day_of_week",
        "start_hour",
        "end_hour",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        day_of_week=APIHelper.SKIP,
        start_hour=APIHelper.SKIP,
        end_hour=APIHelper.SKIP,
    ):
        """Constructor for the AccessSchedule class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if day_of_week is not APIHelper.SKIP:
            self.day_of_week = day_of_week
        if start_hour is not APIHelper.SKIP:
            self.start_hour = start_hour
        if end_hour is not APIHelper.SKIP:
            self.end_hour = end_hour

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

        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        day_of_week = (
            dictionary.get("DayOfWeek")
            if dictionary.get("DayOfWeek")
            else APIHelper.SKIP
        )
        start_hour = (
            dictionary.get("StartHour")
            if dictionary.get("StartHour")
            else APIHelper.SKIP
        )
        end_hour = (
            dictionary.get("EndHour") if dictionary.get("EndHour") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(id, user_id, day_of_week, start_hour, end_hour)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), int)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        day_of_week = XmlUtilities.value_from_xml_element(root.find("DayOfWeek"), str)
        start_hour = XmlUtilities.value_from_xml_element(root.find("StartHour"), float)
        end_hour = XmlUtilities.value_from_xml_element(root.find("EndHour"), float)

        return cls(id, user_id, day_of_week, start_hour, end_hour)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.day_of_week, "DayOfWeek")
        XmlUtilities.add_as_subelement(root, self.start_hour, "StartHour")
        XmlUtilities.add_as_subelement(root, self.end_hour, "EndHour")
