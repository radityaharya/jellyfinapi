# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ImageByNameInfo(object):

    """Implementation of the 'ImageByNameInfo' model.

    TODO: type model description here.

    Attributes:
        name (string): Gets or sets the name.
        theme (string): Gets or sets the theme.
        context (string): Gets or sets the context.
        file_length (long|int): Gets or sets the length of the file.
        format (string): Gets or sets the format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "theme": "Theme",
        "context": "Context",
        "file_length": "FileLength",
        "format": "Format",
    }

    _optionals = [
        "name",
        "theme",
        "context",
        "file_length",
        "format",
    ]

    _nullables = [
        "name",
        "theme",
        "context",
        "format",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        theme=APIHelper.SKIP,
        context=APIHelper.SKIP,
        file_length=APIHelper.SKIP,
        format=APIHelper.SKIP,
    ):
        """Constructor for the ImageByNameInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if theme is not APIHelper.SKIP:
            self.theme = theme
        if context is not APIHelper.SKIP:
            self.context = context
        if file_length is not APIHelper.SKIP:
            self.file_length = file_length
        if format is not APIHelper.SKIP:
            self.format = format

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
        theme = (
            dictionary.get("Theme") if "Theme" in dictionary.keys() else APIHelper.SKIP
        )
        context = (
            dictionary.get("Context")
            if "Context" in dictionary.keys()
            else APIHelper.SKIP
        )
        file_length = (
            dictionary.get("FileLength")
            if dictionary.get("FileLength")
            else APIHelper.SKIP
        )
        format = (
            dictionary.get("Format")
            if "Format" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, theme, context, file_length, format)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        theme = XmlUtilities.value_from_xml_element(root.find("Theme"), str)
        context = XmlUtilities.value_from_xml_element(root.find("Context"), str)
        file_length = XmlUtilities.value_from_xml_element(root.find("FileLength"), int)
        format = XmlUtilities.value_from_xml_element(root.find("Format"), str)

        return cls(name, theme, context, file_length, format)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.theme, "Theme")
        XmlUtilities.add_as_subelement(root, self.context, "Context")
        XmlUtilities.add_as_subelement(root, self.file_length, "FileLength")
        XmlUtilities.add_as_subelement(root, self.format, "Format")
