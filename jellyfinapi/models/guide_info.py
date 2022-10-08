# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class GuideInfo(object):

    """Implementation of the 'GuideInfo' model.

    TODO: type model description here.

    Attributes:
        start_date (datetime): Gets or sets the start date.
        end_date (datetime): Gets or sets the end date.

    """

    # Create a mapping from Model property names to API property names
    _names = {"start_date": "StartDate", "end_date": "EndDate"}

    _optionals = [
        "start_date",
        "end_date",
    ]

    def __init__(self, start_date=APIHelper.SKIP, end_date=APIHelper.SKIP):
        """Constructor for the GuideInfo class"""

        # Initialize members of the class
        if start_date is not APIHelper.SKIP:
            self.start_date = (
                APIHelper.RFC3339DateTime(start_date) if start_date else None
            )
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.RFC3339DateTime(end_date) if end_date else None

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

        start_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("StartDate")).datetime
            if dictionary.get("StartDate")
            else APIHelper.SKIP
        )
        end_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("EndDate")).datetime
            if dictionary.get("EndDate")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(start_date, end_date)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        start_date = XmlUtilities.value_from_xml_element(
            root.find("StartDate"), APIHelper.RFC3339DateTime
        )
        end_date = XmlUtilities.value_from_xml_element(
            root.find("EndDate"), APIHelper.RFC3339DateTime
        )

        return cls(start_date, end_date)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.start_date, "StartDate")
        XmlUtilities.add_as_subelement(root, self.end_date, "EndDate")
