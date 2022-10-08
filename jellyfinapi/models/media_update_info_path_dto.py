# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaUpdateInfoPathDto(object):

    """Implementation of the 'MediaUpdateInfoPathDto' model.

    The media update info path.

    Attributes:
        path (string): Gets or sets media path.
        update_type (string): Gets or sets media update type.  Created,
            Modified, Deleted.

    """

    # Create a mapping from Model property names to API property names
    _names = {"path": "Path", "update_type": "UpdateType"}

    _optionals = [
        "path",
        "update_type",
    ]

    _nullables = [
        "path",
        "update_type",
    ]

    def __init__(self, path=APIHelper.SKIP, update_type=APIHelper.SKIP):
        """Constructor for the MediaUpdateInfoPathDto class"""

        # Initialize members of the class
        if path is not APIHelper.SKIP:
            self.path = path
        if update_type is not APIHelper.SKIP:
            self.update_type = update_type

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

        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        update_type = (
            dictionary.get("UpdateType")
            if "UpdateType" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(path, update_type)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        update_type = XmlUtilities.value_from_xml_element(root.find("UpdateType"), str)

        return cls(path, update_type)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.update_type, "UpdateType")
