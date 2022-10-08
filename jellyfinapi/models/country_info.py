# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CountryInfo(object):

    """Implementation of the 'CountryInfo' model.

    Class CountryInfo.

    Attributes:
        name (string): Gets or sets the name.
        display_name (string): Gets or sets the display name.
        two_letter_iso_region_name (string): Gets or sets the name of the two
            letter ISO region.
        three_letter_iso_region_name (string): Gets or sets the name of the
            three letter ISO region.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "display_name": "DisplayName",
        "two_letter_iso_region_name": "TwoLetterISORegionName",
        "three_letter_iso_region_name": "ThreeLetterISORegionName",
    }

    _optionals = [
        "name",
        "display_name",
        "two_letter_iso_region_name",
        "three_letter_iso_region_name",
    ]

    _nullables = [
        "name",
        "display_name",
        "two_letter_iso_region_name",
        "three_letter_iso_region_name",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        display_name=APIHelper.SKIP,
        two_letter_iso_region_name=APIHelper.SKIP,
        three_letter_iso_region_name=APIHelper.SKIP,
    ):
        """Constructor for the CountryInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name
        if two_letter_iso_region_name is not APIHelper.SKIP:
            self.two_letter_iso_region_name = two_letter_iso_region_name
        if three_letter_iso_region_name is not APIHelper.SKIP:
            self.three_letter_iso_region_name = three_letter_iso_region_name

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
        display_name = (
            dictionary.get("DisplayName")
            if "DisplayName" in dictionary.keys()
            else APIHelper.SKIP
        )
        two_letter_iso_region_name = (
            dictionary.get("TwoLetterISORegionName")
            if "TwoLetterISORegionName" in dictionary.keys()
            else APIHelper.SKIP
        )
        three_letter_iso_region_name = (
            dictionary.get("ThreeLetterISORegionName")
            if "ThreeLetterISORegionName" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name, display_name, two_letter_iso_region_name, three_letter_iso_region_name
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        display_name = XmlUtilities.value_from_xml_element(
            root.find("DisplayName"), str
        )
        two_letter_iso_region_name = XmlUtilities.value_from_xml_element(
            root.find("TwoLetterISORegionName"), str
        )
        three_letter_iso_region_name = XmlUtilities.value_from_xml_element(
            root.find("ThreeLetterISORegionName"), str
        )

        return cls(
            name, display_name, two_letter_iso_region_name, three_letter_iso_region_name
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.display_name, "DisplayName")
        XmlUtilities.add_as_subelement(
            root, self.two_letter_iso_region_name, "TwoLetterISORegionName"
        )
        XmlUtilities.add_as_subelement(
            root, self.three_letter_iso_region_name, "ThreeLetterISORegionName"
        )
