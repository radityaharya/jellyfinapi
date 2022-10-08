# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UploadSubtitleDto(object):

    """Implementation of the 'UploadSubtitleDto' model.

    Upload subtitles dto.

    Attributes:
        language (string): Gets or sets the subtitle language.
        format (string): Gets or sets the subtitle format.
        is_forced (bool): Gets or sets a value indicating whether the subtitle
            is forced.
        data (string): Gets or sets the subtitle data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language": "Language",
        "format": "Format",
        "is_forced": "IsForced",
        "data": "Data",
    }

    def __init__(self, language=None, format=None, is_forced=None, data=None):
        """Constructor for the UploadSubtitleDto class"""

        # Initialize members of the class
        self.language = language
        self.format = format
        self.is_forced = is_forced
        self.data = data

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

        language = dictionary.get("Language") if dictionary.get("Language") else None
        format = dictionary.get("Format") if dictionary.get("Format") else None
        is_forced = (
            dictionary.get("IsForced") if "IsForced" in dictionary.keys() else None
        )
        data = dictionary.get("Data") if dictionary.get("Data") else None
        # Return an object of this model
        return cls(language, format, is_forced, data)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        language = XmlUtilities.value_from_xml_element(root.find("Language"), str)
        format = XmlUtilities.value_from_xml_element(root.find("Format"), str)
        is_forced = XmlUtilities.value_from_xml_element(root.find("IsForced"), bool)
        data = XmlUtilities.value_from_xml_element(root.find("Data"), str)

        return cls(language, format, is_forced, data)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.language, "Language")
        XmlUtilities.add_as_subelement(root, self.format, "Format")
        XmlUtilities.add_as_subelement(root, self.is_forced, "IsForced")
        XmlUtilities.add_as_subelement(root, self.data, "Data")
