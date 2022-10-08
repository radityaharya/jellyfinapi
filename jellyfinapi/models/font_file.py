# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class FontFile(object):

    """Implementation of the 'FontFile' model.

    Class FontFile.

    Attributes:
        name (string): Gets or sets the name.
        size (long|int): Gets or sets the size.
        date_created (datetime): Gets or sets the date created.
        date_modified (datetime): Gets or sets the date modified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "size": "Size",
        "date_created": "DateCreated",
        "date_modified": "DateModified",
    }

    _optionals = [
        "name",
        "size",
        "date_created",
        "date_modified",
    ]

    _nullables = [
        "name",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        size=APIHelper.SKIP,
        date_created=APIHelper.SKIP,
        date_modified=APIHelper.SKIP,
    ):
        """Constructor for the FontFile class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if size is not APIHelper.SKIP:
            self.size = size
        if date_created is not APIHelper.SKIP:
            self.date_created = (
                APIHelper.RFC3339DateTime(date_created) if date_created else None
            )
        if date_modified is not APIHelper.SKIP:
            self.date_modified = (
                APIHelper.RFC3339DateTime(date_modified) if date_modified else None
            )

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
        size = dictionary.get("Size") if dictionary.get("Size") else APIHelper.SKIP
        date_created = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("DateCreated")).datetime
            if dictionary.get("DateCreated")
            else APIHelper.SKIP
        )
        date_modified = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("DateModified")
            ).datetime
            if dictionary.get("DateModified")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, size, date_created, date_modified)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        size = XmlUtilities.value_from_xml_element(root.find("Size"), int)
        date_created = XmlUtilities.value_from_xml_element(
            root.find("DateCreated"), APIHelper.RFC3339DateTime
        )
        date_modified = XmlUtilities.value_from_xml_element(
            root.find("DateModified"), APIHelper.RFC3339DateTime
        )

        return cls(name, size, date_created, date_modified)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.size, "Size")
        XmlUtilities.add_as_subelement(root, self.date_created, "DateCreated")
        XmlUtilities.add_as_subelement(root, self.date_modified, "DateModified")
