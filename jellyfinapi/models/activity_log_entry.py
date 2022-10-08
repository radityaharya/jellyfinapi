# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ActivityLogEntry(object):

    """Implementation of the 'ActivityLogEntry' model.

    An activity log entry.

    Attributes:
        id (long|int): Gets or sets the identifier.
        name (string): Gets or sets the name.
        overview (string): Gets or sets the overview.
        short_overview (string): Gets or sets the short overview.
        mtype (string): Gets or sets the type.
        item_id (string): Gets or sets the item identifier.
        date (datetime): Gets or sets the date.
        user_id (uuid|string): Gets or sets the user identifier.
        user_primary_image_tag (string): Gets or sets the user primary image
            tag.
        severity (LogLevelEnum): Gets or sets the log severity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "name": "Name",
        "overview": "Overview",
        "short_overview": "ShortOverview",
        "mtype": "Type",
        "item_id": "ItemId",
        "date": "Date",
        "user_id": "UserId",
        "user_primary_image_tag": "UserPrimaryImageTag",
        "severity": "Severity",
    }

    _optionals = [
        "id",
        "name",
        "overview",
        "short_overview",
        "mtype",
        "item_id",
        "date",
        "user_id",
        "user_primary_image_tag",
        "severity",
    ]

    _nullables = [
        "overview",
        "short_overview",
        "item_id",
        "user_primary_image_tag",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        overview=APIHelper.SKIP,
        short_overview=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        date=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        user_primary_image_tag=APIHelper.SKIP,
        severity=APIHelper.SKIP,
    ):
        """Constructor for the ActivityLogEntry class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if overview is not APIHelper.SKIP:
            self.overview = overview
        if short_overview is not APIHelper.SKIP:
            self.short_overview = short_overview
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if date is not APIHelper.SKIP:
            self.date = APIHelper.RFC3339DateTime(date) if date else None
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if user_primary_image_tag is not APIHelper.SKIP:
            self.user_primary_image_tag = user_primary_image_tag
        if severity is not APIHelper.SKIP:
            self.severity = severity

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
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        overview = (
            dictionary.get("Overview")
            if "Overview" in dictionary.keys()
            else APIHelper.SKIP
        )
        short_overview = (
            dictionary.get("ShortOverview")
            if "ShortOverview" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        item_id = (
            dictionary.get("ItemId")
            if "ItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("Date")).datetime
            if dictionary.get("Date")
            else APIHelper.SKIP
        )
        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        user_primary_image_tag = (
            dictionary.get("UserPrimaryImageTag")
            if "UserPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        severity = (
            dictionary.get("Severity") if dictionary.get("Severity") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            name,
            overview,
            short_overview,
            mtype,
            item_id,
            date,
            user_id,
            user_primary_image_tag,
            severity,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), int)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        overview = XmlUtilities.value_from_xml_element(root.find("Overview"), str)
        short_overview = XmlUtilities.value_from_xml_element(
            root.find("ShortOverview"), str
        )
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        date = XmlUtilities.value_from_xml_element(
            root.find("Date"), APIHelper.RFC3339DateTime
        )
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        user_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("UserPrimaryImageTag"), str
        )
        severity = XmlUtilities.value_from_xml_element(root.find("Severity"), str)

        return cls(
            id,
            name,
            overview,
            short_overview,
            mtype,
            item_id,
            date,
            user_id,
            user_primary_image_tag,
            severity,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.overview, "Overview")
        XmlUtilities.add_as_subelement(root, self.short_overview, "ShortOverview")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(root, self.date, "Date")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(
            root, self.user_primary_image_tag, "UserPrimaryImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.severity, "Severity")
