# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.library_options import LibraryOptions
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AddVirtualFolderDto(object):

    """Implementation of the 'AddVirtualFolderDto' model.

    Add virtual folder dto.

    Attributes:
        library_options (LibraryOptions): Gets or sets library options.

    """

    # Create a mapping from Model property names to API property names
    _names = {"library_options": "LibraryOptions"}

    _optionals = [
        "library_options",
    ]

    _nullables = [
        "library_options",
    ]

    def __init__(self, library_options=APIHelper.SKIP):
        """Constructor for the AddVirtualFolderDto class"""

        # Initialize members of the class
        if library_options is not APIHelper.SKIP:
            self.library_options = library_options

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

        if "LibraryOptions" in dictionary.keys():
            library_options = (
                LibraryOptions.from_dictionary(dictionary.get("LibraryOptions"))
                if dictionary.get("LibraryOptions")
                else None
            )
        else:
            library_options = APIHelper.SKIP
        # Return an object of this model
        return cls(library_options)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        library_options = XmlUtilities.value_from_xml_element(
            root.find("LibraryOptions"), LibraryOptions
        )

        return cls(library_options)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.library_options, "LibraryOptions")
