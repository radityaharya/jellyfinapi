# -*- coding: utf-8 -*-


from jellyfinapi.models.media_path_info import MediaPathInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UpdateMediaPathRequestDto(object):

    """Implementation of the 'UpdateMediaPathRequestDto' model.

    Update library options dto.

    Attributes:
        name (string): Gets or sets the library name.
        path_info (MediaPathInfo): Gets or sets library folder path
            information.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "path_info": "PathInfo"}

    def __init__(self, name=None, path_info=None):
        """Constructor for the UpdateMediaPathRequestDto class"""

        # Initialize members of the class
        self.name = name
        self.path_info = path_info

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

        name = dictionary.get("Name") if dictionary.get("Name") else None
        path_info = (
            MediaPathInfo.from_dictionary(dictionary.get("PathInfo"))
            if dictionary.get("PathInfo")
            else None
        )
        # Return an object of this model
        return cls(name, path_info)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        path_info = XmlUtilities.value_from_xml_element(
            root.find("MediaPathInfo"), MediaPathInfo
        )

        return cls(name, path_info)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.path_info, "MediaPathInfo")
