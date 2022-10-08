# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TaskResult(object):

    """Implementation of the 'TaskResult' model.

    Class TaskExecutionInfo.

    Attributes:
        start_time_utc (datetime): Gets or sets the start time UTC.
        end_time_utc (datetime): Gets or sets the end time UTC.
        status (TaskCompletionStatusEnum): Gets or sets the status.
        name (string): Gets or sets the name.
        key (string): Gets or sets the key.
        id (string): Gets or sets the id.
        error_message (string): Gets or sets the error message.
        long_error_message (string): Gets or sets the long error message.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time_utc": "StartTimeUtc",
        "end_time_utc": "EndTimeUtc",
        "status": "Status",
        "name": "Name",
        "key": "Key",
        "id": "Id",
        "error_message": "ErrorMessage",
        "long_error_message": "LongErrorMessage",
    }

    _optionals = [
        "start_time_utc",
        "end_time_utc",
        "status",
        "name",
        "key",
        "id",
        "error_message",
        "long_error_message",
    ]

    _nullables = [
        "name",
        "key",
        "id",
        "error_message",
        "long_error_message",
    ]

    def __init__(
        self,
        start_time_utc=APIHelper.SKIP,
        end_time_utc=APIHelper.SKIP,
        status=APIHelper.SKIP,
        name=APIHelper.SKIP,
        key=APIHelper.SKIP,
        id=APIHelper.SKIP,
        error_message=APIHelper.SKIP,
        long_error_message=APIHelper.SKIP,
    ):
        """Constructor for the TaskResult class"""

        # Initialize members of the class
        if start_time_utc is not APIHelper.SKIP:
            self.start_time_utc = (
                APIHelper.RFC3339DateTime(start_time_utc) if start_time_utc else None
            )
        if end_time_utc is not APIHelper.SKIP:
            self.end_time_utc = (
                APIHelper.RFC3339DateTime(end_time_utc) if end_time_utc else None
            )
        if status is not APIHelper.SKIP:
            self.status = status
        if name is not APIHelper.SKIP:
            self.name = name
        if key is not APIHelper.SKIP:
            self.key = key
        if id is not APIHelper.SKIP:
            self.id = id
        if error_message is not APIHelper.SKIP:
            self.error_message = error_message
        if long_error_message is not APIHelper.SKIP:
            self.long_error_message = long_error_message

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

        start_time_utc = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("StartTimeUtc")
            ).datetime
            if dictionary.get("StartTimeUtc")
            else APIHelper.SKIP
        )
        end_time_utc = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("EndTimeUtc")).datetime
            if dictionary.get("EndTimeUtc")
            else APIHelper.SKIP
        )
        status = (
            dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        )
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        key = dictionary.get("Key") if "Key" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        error_message = (
            dictionary.get("ErrorMessage")
            if "ErrorMessage" in dictionary.keys()
            else APIHelper.SKIP
        )
        long_error_message = (
            dictionary.get("LongErrorMessage")
            if "LongErrorMessage" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            start_time_utc,
            end_time_utc,
            status,
            name,
            key,
            id,
            error_message,
            long_error_message,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        start_time_utc = XmlUtilities.value_from_xml_element(
            root.find("StartTimeUtc"), APIHelper.RFC3339DateTime
        )
        end_time_utc = XmlUtilities.value_from_xml_element(
            root.find("EndTimeUtc"), APIHelper.RFC3339DateTime
        )
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        key = XmlUtilities.value_from_xml_element(root.find("Key"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        error_message = XmlUtilities.value_from_xml_element(
            root.find("ErrorMessage"), str
        )
        long_error_message = XmlUtilities.value_from_xml_element(
            root.find("LongErrorMessage"), str
        )

        return cls(
            start_time_utc,
            end_time_utc,
            status,
            name,
            key,
            id,
            error_message,
            long_error_message,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.start_time_utc, "StartTimeUtc")
        XmlUtilities.add_as_subelement(root, self.end_time_utc, "EndTimeUtc")
        XmlUtilities.add_as_subelement(root, self.status, "Status")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.key, "Key")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.error_message, "ErrorMessage")
        XmlUtilities.add_as_subelement(
            root, self.long_error_message, "LongErrorMessage"
        )
