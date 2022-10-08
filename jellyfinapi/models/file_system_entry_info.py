# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class FileSystemEntryInfo(object):

    """Implementation of the 'FileSystemEntryInfo' model.

    Class FileSystemEntryInfo.

    Attributes:
        name (string): Gets the name.
        path (string): Gets the path.
        mtype (FileSystemEntryTypeEnum): Gets the type.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "path": "Path", "mtype": "Type"}

    _optionals = [
        "name",
        "path",
        "mtype",
    ]

    def __init__(self, name=APIHelper.SKIP, path=APIHelper.SKIP, mtype=APIHelper.SKIP):
        """Constructor for the FileSystemEntryInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if path is not APIHelper.SKIP:
            self.path = path
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype

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
        path = dictionary.get("Path") if dictionary.get("Path") else APIHelper.SKIP
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name, path, mtype)

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
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)

        return cls(name, path, mtype)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
