# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_path_info import MediaPathInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaPathDto(object):

    """Implementation of the 'MediaPathDto' model.

    Media Path dto.

    Attributes:
        name (string): Gets or sets the name of the library.
        path (string): Gets or sets the path to add.
        path_info (MediaPathInfo): Gets or sets the path info.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "path": "Path", "path_info": "PathInfo"}

    _optionals = [
        "path",
        "path_info",
    ]

    _nullables = [
        "path",
        "path_info",
    ]

    def __init__(self, name=None, path=APIHelper.SKIP, path_info=APIHelper.SKIP):
        """Constructor for the MediaPathDto class"""

        # Initialize members of the class
        self.name = name
        if path is not APIHelper.SKIP:
            self.path = path
        if path_info is not APIHelper.SKIP:
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
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        if "PathInfo" in dictionary.keys():
            path_info = (
                MediaPathInfo.from_dictionary(dictionary.get("PathInfo"))
                if dictionary.get("PathInfo")
                else None
            )
        else:
            path_info = APIHelper.SKIP
        # Return an object of this model
        return cls(name, path, path_info)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        path_info = XmlUtilities.value_from_xml_element(
            root.find("MediaPathInfo"), MediaPathInfo
        )

        return cls(name, path, path_info)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.path_info, "MediaPathInfo")
