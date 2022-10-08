# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ValidatePathDto(object):

    """Implementation of the 'ValidatePathDto' model.

    Validate path object.

    Attributes:
        validate_writable (bool): Gets or sets a value indicating whether
            validate if path is writable.
        path (string): Gets or sets the path.
        is_file (bool): Gets or sets is path file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "validate_writable": "ValidateWritable",
        "path": "Path",
        "is_file": "IsFile",
    }

    _optionals = [
        "validate_writable",
        "path",
        "is_file",
    ]

    _nullables = [
        "path",
        "is_file",
    ]

    def __init__(
        self,
        validate_writable=APIHelper.SKIP,
        path=APIHelper.SKIP,
        is_file=APIHelper.SKIP,
    ):
        """Constructor for the ValidatePathDto class"""

        # Initialize members of the class
        if validate_writable is not APIHelper.SKIP:
            self.validate_writable = validate_writable
        if path is not APIHelper.SKIP:
            self.path = path
        if is_file is not APIHelper.SKIP:
            self.is_file = is_file

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

        validate_writable = (
            dictionary.get("ValidateWritable")
            if "ValidateWritable" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        is_file = (
            dictionary.get("IsFile")
            if "IsFile" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(validate_writable, path, is_file)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        validate_writable = XmlUtilities.value_from_xml_element(
            root.find("ValidateWritable"), bool
        )
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        is_file = XmlUtilities.value_from_xml_element(root.find("IsFile"), bool)

        return cls(validate_writable, path, is_file)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.validate_writable, "ValidateWritable")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.is_file, "IsFile")
