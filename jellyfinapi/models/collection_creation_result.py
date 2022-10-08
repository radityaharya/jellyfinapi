# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CollectionCreationResult(object):

    """Implementation of the 'CollectionCreationResult' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id"}

    _optionals = [
        "id",
    ]

    def __init__(self, id=APIHelper.SKIP):
        """Constructor for the CollectionCreationResult class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id

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

        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)

        return cls(id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
