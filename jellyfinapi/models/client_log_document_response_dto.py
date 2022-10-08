# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ClientLogDocumentResponseDto(object):

    """Implementation of the 'ClientLogDocumentResponseDto' model.

    Client log document response dto.

    Attributes:
        file_name (string): Gets the resulting filename.

    """

    # Create a mapping from Model property names to API property names
    _names = {"file_name": "FileName"}

    _optionals = [
        "file_name",
    ]

    def __init__(self, file_name=APIHelper.SKIP):
        """Constructor for the ClientLogDocumentResponseDto class"""

        # Initialize members of the class
        if file_name is not APIHelper.SKIP:
            self.file_name = file_name

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

        file_name = (
            dictionary.get("FileName") if dictionary.get("FileName") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(file_name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        file_name = XmlUtilities.value_from_xml_element(root.find("FileName"), str)

        return cls(file_name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.file_name, "FileName")
