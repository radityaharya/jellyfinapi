# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CultureDto(object):

    """Implementation of the 'CultureDto' model.

    Class CultureDto.

    Attributes:
        name (string): Gets the name.
        display_name (string): Gets the display name.
        two_letter_iso_language_name (string): Gets the name of the two letter
            ISO language.
        three_letter_iso_language_name (string): Gets the name of the three
            letter ISO language.
        three_letter_iso_language_names (list of string): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "display_name": "DisplayName",
        "two_letter_iso_language_name": "TwoLetterISOLanguageName",
        "three_letter_iso_language_name": "ThreeLetterISOLanguageName",
        "three_letter_iso_language_names": "ThreeLetterISOLanguageNames",
    }

    _optionals = [
        "name",
        "display_name",
        "two_letter_iso_language_name",
        "three_letter_iso_language_name",
        "three_letter_iso_language_names",
    ]

    _nullables = [
        "three_letter_iso_language_name",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        display_name=APIHelper.SKIP,
        two_letter_iso_language_name=APIHelper.SKIP,
        three_letter_iso_language_name=APIHelper.SKIP,
        three_letter_iso_language_names=APIHelper.SKIP,
    ):
        """Constructor for the CultureDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name
        if two_letter_iso_language_name is not APIHelper.SKIP:
            self.two_letter_iso_language_name = two_letter_iso_language_name
        if three_letter_iso_language_name is not APIHelper.SKIP:
            self.three_letter_iso_language_name = three_letter_iso_language_name
        if three_letter_iso_language_names is not APIHelper.SKIP:
            self.three_letter_iso_language_names = three_letter_iso_language_names

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        display_name = (
            dictionary.get("DisplayName")
            if dictionary.get("DisplayName")
            else APIHelper.SKIP
        )
        two_letter_iso_language_name = (
            dictionary.get("TwoLetterISOLanguageName")
            if dictionary.get("TwoLetterISOLanguageName")
            else APIHelper.SKIP
        )
        three_letter_iso_language_name = (
            dictionary.get("ThreeLetterISOLanguageName")
            if "ThreeLetterISOLanguageName" in dictionary.keys()
            else APIHelper.SKIP
        )
        three_letter_iso_language_names = (
            dictionary.get("ThreeLetterISOLanguageNames")
            if dictionary.get("ThreeLetterISOLanguageNames")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            display_name,
            two_letter_iso_language_name,
            three_letter_iso_language_name,
            three_letter_iso_language_names,
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
        two_letter_iso_language_name = XmlUtilities.value_from_xml_element(
            root.find("TwoLetterISOLanguageName"), str
        )
        three_letter_iso_language_name = XmlUtilities.value_from_xml_element(
            root.find("ThreeLetterISOLanguageName"), str
        )
        three_letter_iso_language_names = XmlUtilities.list_from_xml_element(
            root, "ThreeLetterISOLanguageNames", str
        )

        return cls(
            name,
            display_name,
            two_letter_iso_language_name,
            three_letter_iso_language_name,
            three_letter_iso_language_names,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.display_name, "DisplayName")
        XmlUtilities.add_as_subelement(
            root, self.two_letter_iso_language_name, "TwoLetterISOLanguageName"
        )
        XmlUtilities.add_as_subelement(
            root, self.three_letter_iso_language_name, "ThreeLetterISOLanguageName"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.three_letter_iso_language_names, "ThreeLetterISOLanguageNames"
        )
