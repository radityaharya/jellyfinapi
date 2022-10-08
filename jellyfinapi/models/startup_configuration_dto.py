# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class StartupConfigurationDto(object):

    """Implementation of the 'StartupConfigurationDto' model.

    The startup configuration DTO.

    Attributes:
        ui_culture (string): Gets or sets UI language culture.
        metadata_country_code (string): Gets or sets the metadata country
            code.
        preferred_metadata_language (string): Gets or sets the preferred
            language for the metadata.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ui_culture": "UICulture",
        "metadata_country_code": "MetadataCountryCode",
        "preferred_metadata_language": "PreferredMetadataLanguage",
    }

    _optionals = [
        "ui_culture",
        "metadata_country_code",
        "preferred_metadata_language",
    ]

    _nullables = [
        "ui_culture",
        "metadata_country_code",
        "preferred_metadata_language",
    ]

    def __init__(
        self,
        ui_culture=APIHelper.SKIP,
        metadata_country_code=APIHelper.SKIP,
        preferred_metadata_language=APIHelper.SKIP,
    ):
        """Constructor for the StartupConfigurationDto class"""

        # Initialize members of the class
        if ui_culture is not APIHelper.SKIP:
            self.ui_culture = ui_culture
        if metadata_country_code is not APIHelper.SKIP:
            self.metadata_country_code = metadata_country_code
        if preferred_metadata_language is not APIHelper.SKIP:
            self.preferred_metadata_language = preferred_metadata_language

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

        ui_culture = (
            dictionary.get("UICulture")
            if "UICulture" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_country_code = (
            dictionary.get("MetadataCountryCode")
            if "MetadataCountryCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        preferred_metadata_language = (
            dictionary.get("PreferredMetadataLanguage")
            if "PreferredMetadataLanguage" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(ui_culture, metadata_country_code, preferred_metadata_language)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        ui_culture = XmlUtilities.value_from_xml_element(root.find("UICulture"), str)
        metadata_country_code = XmlUtilities.value_from_xml_element(
            root.find("MetadataCountryCode"), str
        )
        preferred_metadata_language = XmlUtilities.value_from_xml_element(
            root.find("PreferredMetadataLanguage"), str
        )

        return cls(ui_culture, metadata_country_code, preferred_metadata_language)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.ui_culture, "UICulture")
        XmlUtilities.add_as_subelement(
            root, self.metadata_country_code, "MetadataCountryCode"
        )
        XmlUtilities.add_as_subelement(
            root, self.preferred_metadata_language, "PreferredMetadataLanguage"
        )
