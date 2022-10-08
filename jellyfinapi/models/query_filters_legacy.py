# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QueryFiltersLegacy(object):

    """Implementation of the 'QueryFiltersLegacy' model.

    TODO: type model description here.

    Attributes:
        genres (list of string): TODO: type description here.
        tags (list of string): TODO: type description here.
        official_ratings (list of string): TODO: type description here.
        years (list of int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "genres": "Genres",
        "tags": "Tags",
        "official_ratings": "OfficialRatings",
        "years": "Years",
    }

    _optionals = [
        "genres",
        "tags",
        "official_ratings",
        "years",
    ]

    _nullables = [
        "genres",
        "tags",
        "official_ratings",
        "years",
    ]

    def __init__(
        self,
        genres=APIHelper.SKIP,
        tags=APIHelper.SKIP,
        official_ratings=APIHelper.SKIP,
        years=APIHelper.SKIP,
    ):
        """Constructor for the QueryFiltersLegacy class"""

        # Initialize members of the class
        if genres is not APIHelper.SKIP:
            self.genres = genres
        if tags is not APIHelper.SKIP:
            self.tags = tags
        if official_ratings is not APIHelper.SKIP:
            self.official_ratings = official_ratings
        if years is not APIHelper.SKIP:
            self.years = years

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

        genres = (
            dictionary.get("Genres")
            if "Genres" in dictionary.keys()
            else APIHelper.SKIP
        )
        tags = dictionary.get("Tags") if "Tags" in dictionary.keys() else APIHelper.SKIP
        official_ratings = (
            dictionary.get("OfficialRatings")
            if "OfficialRatings" in dictionary.keys()
            else APIHelper.SKIP
        )
        years = (
            dictionary.get("Years") if "Years" in dictionary.keys() else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(genres, tags, official_ratings, years)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        genres = XmlUtilities.list_from_xml_element(root, "Genres", str)
        tags = XmlUtilities.list_from_xml_element(root, "Tags", str)
        official_ratings = XmlUtilities.list_from_xml_element(
            root, "OfficialRatings", str
        )
        years = XmlUtilities.list_from_xml_element(root, "Years", int)

        return cls(genres, tags, official_ratings, years)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.genres, "Genres")
        XmlUtilities.add_list_as_subelement(root, self.tags, "Tags")
        XmlUtilities.add_list_as_subelement(
            root, self.official_ratings, "OfficialRatings"
        )
        XmlUtilities.add_list_as_subelement(root, self.years, "Years")
