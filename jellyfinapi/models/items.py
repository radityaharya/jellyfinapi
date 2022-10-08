# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class Items(object):

    """Implementation of the 'Items' model.

    TODO: type model description here.

    Attributes:
        movies (int): TODO: type description here.
        episodes (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"movies": "movies", "episodes": "episodes"}

    _optionals = [
        "movies",
        "episodes",
    ]

    def __init__(self, movies=APIHelper.SKIP, episodes=APIHelper.SKIP):
        """Constructor for the Items class"""

        # Initialize members of the class
        if movies is not APIHelper.SKIP:
            self.movies = movies
        if episodes is not APIHelper.SKIP:
            self.episodes = episodes

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

        movies = (
            dictionary.get("movies") if dictionary.get("movies") else APIHelper.SKIP
        )
        episodes = (
            dictionary.get("episodes") if dictionary.get("episodes") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(movies, episodes)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        movies = XmlUtilities.value_from_xml_element(root.find("movies"), int)
        episodes = XmlUtilities.value_from_xml_element(root.find("episodes"), int)

        return cls(movies, episodes)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.movies, "movies")
        XmlUtilities.add_as_subelement(root, self.episodes, "episodes")
