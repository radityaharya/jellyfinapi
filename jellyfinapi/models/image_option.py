# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ImageOption(object):

    """Implementation of the 'ImageOption' model.

    TODO: type model description here.

    Attributes:
        mtype (ImageTypeEnum): Gets or sets the type.
        limit (int): Gets or sets the limit.
        min_width (int): Gets or sets the minimum width.

    """

    # Create a mapping from Model property names to API property names
    _names = {"mtype": "Type", "limit": "Limit", "min_width": "MinWidth"}

    _optionals = [
        "mtype",
        "limit",
        "min_width",
    ]

    def __init__(
        self, mtype=APIHelper.SKIP, limit=APIHelper.SKIP, min_width=APIHelper.SKIP
    ):
        """Constructor for the ImageOption class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if limit is not APIHelper.SKIP:
            self.limit = limit
        if min_width is not APIHelper.SKIP:
            self.min_width = min_width

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

        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        limit = dictionary.get("Limit") if dictionary.get("Limit") else APIHelper.SKIP
        min_width = (
            dictionary.get("MinWidth") if dictionary.get("MinWidth") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(mtype, limit, min_width)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        limit = XmlUtilities.value_from_xml_element(root.find("Limit"), int)
        min_width = XmlUtilities.value_from_xml_element(root.find("MinWidth"), int)

        return cls(mtype, limit, min_width)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.limit, "Limit")
        XmlUtilities.add_as_subelement(root, self.min_width, "MinWidth")
