# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.search_hint import SearchHint
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SearchHintResult(object):

    """Implementation of the 'SearchHintResult' model.

    Class SearchHintResult.

    Attributes:
        search_hints (list of SearchHint): Gets the search hints.
        total_record_count (int): Gets the total record count.

    """

    # Create a mapping from Model property names to API property names
    _names = {"search_hints": "SearchHints", "total_record_count": "TotalRecordCount"}

    _optionals = [
        "search_hints",
        "total_record_count",
    ]

    def __init__(self, search_hints=APIHelper.SKIP, total_record_count=APIHelper.SKIP):
        """Constructor for the SearchHintResult class"""

        # Initialize members of the class
        if search_hints is not APIHelper.SKIP:
            self.search_hints = search_hints
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

        search_hints = None
        if dictionary.get("SearchHints") is not None:
            search_hints = [
                SearchHint.from_dictionary(x) for x in dictionary.get("SearchHints")
            ]
        else:
            search_hints = APIHelper.SKIP
        total_record_count = (
            dictionary.get("TotalRecordCount")
            if dictionary.get("TotalRecordCount")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(search_hints, total_record_count)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        search_hints = XmlUtilities.list_from_xml_element(
            root, "SearchHint", SearchHint
        )
        total_record_count = XmlUtilities.value_from_xml_element(
            root.find("TotalRecordCount"), int
        )

        return cls(search_hints, total_record_count)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.search_hints, "SearchHint")
        XmlUtilities.add_as_subelement(
            root, self.total_record_count, "TotalRecordCount"
        )
