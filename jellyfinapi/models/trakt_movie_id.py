# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktMovieId(object):

    """Implementation of the 'TraktMovieId' model.

    TODO: type model description here.

    Attributes:
        trakt (int): TODO: type description here.
        slug (string): TODO: type description here.
        imdb (string): TODO: type description here.
        tmdb (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"trakt": "trakt", "slug": "slug", "imdb": "imdb", "tmdb": "tmdb"}

    _optionals = [
        "trakt",
        "slug",
        "imdb",
        "tmdb",
    ]

    _nullables = [
        "trakt",
        "slug",
        "imdb",
        "tmdb",
    ]

    def __init__(
        self,
        trakt=APIHelper.SKIP,
        slug=APIHelper.SKIP,
        imdb=APIHelper.SKIP,
        tmdb=APIHelper.SKIP,
    ):
        """Constructor for the TraktMovieId class"""

        # Initialize members of the class
        if trakt is not APIHelper.SKIP:
            self.trakt = trakt
        if slug is not APIHelper.SKIP:
            self.slug = slug
        if imdb is not APIHelper.SKIP:
            self.imdb = imdb
        if tmdb is not APIHelper.SKIP:
            self.tmdb = tmdb

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

        trakt = (
            dictionary.get("trakt") if "trakt" in dictionary.keys() else APIHelper.SKIP
        )
        slug = dictionary.get("slug") if "slug" in dictionary.keys() else APIHelper.SKIP
        imdb = dictionary.get("imdb") if "imdb" in dictionary.keys() else APIHelper.SKIP
        tmdb = dictionary.get("tmdb") if "tmdb" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(trakt, slug, imdb, tmdb)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        trakt = XmlUtilities.value_from_xml_element(root.find("trakt"), int)
        slug = XmlUtilities.value_from_xml_element(root.find("slug"), str)
        imdb = XmlUtilities.value_from_xml_element(root.find("imdb"), str)
        tmdb = XmlUtilities.value_from_xml_element(root.find("tmdb"), int)

        return cls(trakt, slug, imdb, tmdb)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.trakt, "trakt")
        XmlUtilities.add_as_subelement(root, self.slug, "slug")
        XmlUtilities.add_as_subelement(root, self.imdb, "imdb")
        XmlUtilities.add_as_subelement(root, self.tmdb, "tmdb")
