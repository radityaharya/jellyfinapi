# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationDto(object):

    """Implementation of the 'NotificationDto' model.

    The notification DTO.

    Attributes:
        id (string): Gets or sets the notification ID. Defaults to an empty
            string.
        user_id (string): Gets or sets the notification's user ID. Defaults to
            an empty string.
        date (datetime): Gets or sets the notification date.
        is_read (bool): Gets or sets a value indicating whether the
            notification has been read. Defaults to false.
        name (string): Gets or sets the notification's name. Defaults to an
            empty string.
        description (string): Gets or sets the notification's description.
            Defaults to an empty string.
        url (string): Gets or sets the notification's URL. Defaults to an
            empty string.
        level (NotificationLevelEnum): Gets or sets the notification level.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "user_id": "UserId",
        "date": "Date",
        "is_read": "IsRead",
        "name": "Name",
        "description": "Description",
        "url": "Url",
        "level": "Level",
    }

    _optionals = [
        "id",
        "user_id",
        "date",
        "is_read",
        "name",
        "description",
        "url",
        "level",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        date=APIHelper.SKIP,
        is_read=APIHelper.SKIP,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        url=APIHelper.SKIP,
        level=APIHelper.SKIP,
    ):
        """Constructor for the NotificationDto class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if date is not APIHelper.SKIP:
            self.date = APIHelper.RFC3339DateTime(date) if date else None
        if is_read is not APIHelper.SKIP:
            self.is_read = is_read
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if url is not APIHelper.SKIP:
            self.url = url
        if level is not APIHelper.SKIP:
            self.level = level

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
        date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("Date")).datetime
            if dictionary.get("Date")
            else APIHelper.SKIP
        )
        is_read = (
            dictionary.get("IsRead")
            if "IsRead" in dictionary.keys()
            else APIHelper.SKIP
        )
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        description = (
            dictionary.get("Description")
            if dictionary.get("Description")
            else APIHelper.SKIP
        )
        url = dictionary.get("Url") if dictionary.get("Url") else APIHelper.SKIP
        level = dictionary.get("Level") if dictionary.get("Level") else APIHelper.SKIP
        # Return an object of this model
        return cls(id, user_id, date, is_read, name, description, url, level)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        date = XmlUtilities.value_from_xml_element(
            root.find("Date"), APIHelper.RFC3339DateTime
        )
        is_read = XmlUtilities.value_from_xml_element(root.find("IsRead"), bool)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        description = XmlUtilities.value_from_xml_element(root.find("Description"), str)
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)
        level = XmlUtilities.value_from_xml_element(root.find("Level"), str)

        return cls(id, user_id, date, is_read, name, description, url, level)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.date, "Date")
        XmlUtilities.add_as_subelement(root, self.is_read, "IsRead")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.description, "Description")
        XmlUtilities.add_as_subelement(root, self.url, "Url")
        XmlUtilities.add_as_subelement(root, self.level, "Level")
