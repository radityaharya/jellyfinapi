# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.device_info import DeviceInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceInfoQueryResult(object):

    """Implementation of the 'DeviceInfoQueryResult' model.

    TODO: type model description here.

    Attributes:
        items (list of DeviceInfo): Gets or sets the items.
        total_record_count (int): Gets or sets the total number of records
            available.
        start_index (int): Gets or sets the index of the first record in
            Items.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items": "Items",
        "total_record_count": "TotalRecordCount",
        "start_index": "StartIndex",
    }

    _optionals = [
        "items",
        "total_record_count",
        "start_index",
    ]

    _nullables = [
        "items",
    ]

    def __init__(
        self,
        items=APIHelper.SKIP,
        total_record_count=APIHelper.SKIP,
        start_index=APIHelper.SKIP,
    ):
        """Constructor for the DeviceInfoQueryResult class"""

        # Initialize members of the class
        if items is not APIHelper.SKIP:
            self.items = items
        if total_record_count is not APIHelper.SKIP:
            self.total_record_count = total_record_count
        if start_index is not APIHelper.SKIP:
            self.start_index = start_index

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

        if "Items" in dictionary.keys():
            items = (
                [DeviceInfo.from_dictionary(x) for x in dictionary.get("Items")]
                if dictionary.get("Items")
                else None
            )
        else:
            items = APIHelper.SKIP
        total_record_count = (
            dictionary.get("TotalRecordCount")
            if dictionary.get("TotalRecordCount")
            else APIHelper.SKIP
        )
        start_index = (
            dictionary.get("StartIndex")
            if dictionary.get("StartIndex")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(items, total_record_count, start_index)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        items = XmlUtilities.list_from_xml_element(root, "DeviceInfo", DeviceInfo)
        total_record_count = XmlUtilities.value_from_xml_element(
            root.find("TotalRecordCount"), int
        )
        start_index = XmlUtilities.value_from_xml_element(root.find("StartIndex"), int)

        return cls(items, total_record_count, start_index)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.items, "DeviceInfo")
        XmlUtilities.add_as_subelement(
            root, self.total_record_count, "TotalRecordCount"
        )
        XmlUtilities.add_as_subelement(root, self.start_index, "StartIndex")
