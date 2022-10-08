# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.trakt_episode_id import TraktEpisodeId
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktEpisode(object):

    """Implementation of the 'TraktEpisode' model.

    TODO: type model description here.

    Attributes:
        season (int): TODO: type description here.
        number (int): TODO: type description here.
        title (string): TODO: type description here.
        ids (TraktEpisodeId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"season": "season", "number": "number", "title": "title", "ids": "ids"}

    _optionals = [
        "season",
        "number",
        "title",
        "ids",
    ]

    _nullables = [
        "title",
        "ids",
    ]

    def __init__(
        self,
        season=APIHelper.SKIP,
        number=APIHelper.SKIP,
        title=APIHelper.SKIP,
        ids=APIHelper.SKIP,
    ):
        """Constructor for the TraktEpisode class"""

        # Initialize members of the class
        if season is not APIHelper.SKIP:
            self.season = season
        if number is not APIHelper.SKIP:
            self.number = number
        if title is not APIHelper.SKIP:
            self.title = title
        if ids is not APIHelper.SKIP:
            self.ids = ids

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

        season = (
            dictionary.get("season") if dictionary.get("season") else APIHelper.SKIP
        )
        number = (
            dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        )
        title = (
            dictionary.get("title") if "title" in dictionary.keys() else APIHelper.SKIP
        )
        if "ids" in dictionary.keys():
            ids = (
                TraktEpisodeId.from_dictionary(dictionary.get("ids"))
                if dictionary.get("ids")
                else None
            )
        else:
            ids = APIHelper.SKIP
        # Return an object of this model
        return cls(season, number, title, ids)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        season = XmlUtilities.value_from_xml_element(root.find("season"), int)
        number = XmlUtilities.value_from_xml_element(root.find("number"), int)
        title = XmlUtilities.value_from_xml_element(root.find("title"), str)
        ids = XmlUtilities.value_from_xml_element(
            root.find("TraktEpisodeId"), TraktEpisodeId
        )

        return cls(season, number, title, ids)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.season, "season")
        XmlUtilities.add_as_subelement(root, self.number, "number")
        XmlUtilities.add_as_subelement(root, self.title, "title")
        XmlUtilities.add_as_subelement(root, self.ids, "TraktEpisodeId")
