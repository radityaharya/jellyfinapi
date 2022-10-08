# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.name_guid_pair import NameGuidPair
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QueryFilters(object):

    """Implementation of the 'QueryFilters' model.

    TODO: type model description here.

    Attributes:
        genres (list of NameGuidPair): TODO: type description here.
        tags (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"genres": "Genres", "tags": "Tags"}

    _optionals = [
        "genres",
        "tags",
    ]

    _nullables = [
        "genres",
        "tags",
    ]

    def __init__(self, genres=APIHelper.SKIP, tags=APIHelper.SKIP):
        """Constructor for the QueryFilters class"""

        # Initialize members of the class
        if genres is not APIHelper.SKIP:
            self.genres = genres
        if tags is not APIHelper.SKIP:
            self.tags = tags

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

        if "Genres" in dictionary.keys():
            genres = (
                [NameGuidPair.from_dictionary(x) for x in dictionary.get("Genres")]
                if dictionary.get("Genres")
                else None
            )
        else:
            genres = APIHelper.SKIP
        tags = dictionary.get("Tags") if "Tags" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(genres, tags)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        genres = XmlUtilities.list_from_xml_element(root, "NameGuidPair", NameGuidPair)
        tags = XmlUtilities.list_from_xml_element(root, "Tags", str)

        return cls(genres, tags)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.genres, "NameGuidPair")
        XmlUtilities.add_list_as_subelement(root, self.tags, "Tags")
