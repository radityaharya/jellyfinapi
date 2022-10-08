# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.trakt_episode import TraktEpisode
from jellyfinapi.models.trakt_movie import TraktMovie
from jellyfinapi.models.trakt_person import TraktPerson
from jellyfinapi.models.trakt_season import TraktSeason
from jellyfinapi.models.trakt_show import TraktShow
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotFoundObjects(object):

    """Implementation of the 'NotFoundObjects' model.

    TODO: type model description here.

    Attributes:
        movies (list of TraktMovie): TODO: type description here.
        shows (list of TraktShow): TODO: type description here.
        episodes (list of TraktEpisode): TODO: type description here.
        seasons (list of TraktSeason): TODO: type description here.
        people (list of TraktPerson): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "movies": "movies",
        "shows": "shows",
        "episodes": "episodes",
        "seasons": "seasons",
        "people": "people",
    }

    _optionals = [
        "movies",
        "shows",
        "episodes",
        "seasons",
        "people",
    ]

    _nullables = [
        "movies",
        "shows",
        "episodes",
        "seasons",
        "people",
    ]

    def __init__(
        self,
        movies=APIHelper.SKIP,
        shows=APIHelper.SKIP,
        episodes=APIHelper.SKIP,
        seasons=APIHelper.SKIP,
        people=APIHelper.SKIP,
    ):
        """Constructor for the NotFoundObjects class"""

        # Initialize members of the class
        if movies is not APIHelper.SKIP:
            self.movies = movies
        if shows is not APIHelper.SKIP:
            self.shows = shows
        if episodes is not APIHelper.SKIP:
            self.episodes = episodes
        if seasons is not APIHelper.SKIP:
            self.seasons = seasons
        if people is not APIHelper.SKIP:
            self.people = people

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

        if "movies" in dictionary.keys():
            movies = (
                [TraktMovie.from_dictionary(x) for x in dictionary.get("movies")]
                if dictionary.get("movies")
                else None
            )
        else:
            movies = APIHelper.SKIP
        if "shows" in dictionary.keys():
            shows = (
                [TraktShow.from_dictionary(x) for x in dictionary.get("shows")]
                if dictionary.get("shows")
                else None
            )
        else:
            shows = APIHelper.SKIP
        if "episodes" in dictionary.keys():
            episodes = (
                [TraktEpisode.from_dictionary(x) for x in dictionary.get("episodes")]
                if dictionary.get("episodes")
                else None
            )
        else:
            episodes = APIHelper.SKIP
        if "seasons" in dictionary.keys():
            seasons = (
                [TraktSeason.from_dictionary(x) for x in dictionary.get("seasons")]
                if dictionary.get("seasons")
                else None
            )
        else:
            seasons = APIHelper.SKIP
        if "people" in dictionary.keys():
            people = (
                [TraktPerson.from_dictionary(x) for x in dictionary.get("people")]
                if dictionary.get("people")
                else None
            )
        else:
            people = APIHelper.SKIP
        # Return an object of this model
        return cls(movies, shows, episodes, seasons, people)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        movies = XmlUtilities.list_from_xml_element(root, "TraktMovie", TraktMovie)
        shows = XmlUtilities.list_from_xml_element(root, "TraktShow", TraktShow)
        episodes = XmlUtilities.list_from_xml_element(
            root, "TraktEpisode", TraktEpisode
        )
        seasons = XmlUtilities.list_from_xml_element(root, "TraktSeason", TraktSeason)
        people = XmlUtilities.list_from_xml_element(root, "TraktPerson", TraktPerson)

        return cls(movies, shows, episodes, seasons, people)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.movies, "TraktMovie")
        XmlUtilities.add_list_as_subelement(root, self.shows, "TraktShow")
        XmlUtilities.add_list_as_subelement(root, self.episodes, "TraktEpisode")
        XmlUtilities.add_list_as_subelement(root, self.seasons, "TraktSeason")
        XmlUtilities.add_list_as_subelement(root, self.people, "TraktPerson")
