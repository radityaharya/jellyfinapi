# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.trakt_show_id import TraktShowId
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktShow(object):

    """Implementation of the 'TraktShow' model.

    TODO: type model description here.

    Attributes:
        title (string): TODO: type description here.
        year (int): TODO: type description here.
        ids (TraktShowId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"title": "title", "year": "year", "ids": "ids"}

    _optionals = [
        "title",
        "year",
        "ids",
    ]

    _nullables = [
        "title",
        "year",
        "ids",
    ]

    def __init__(self, title=APIHelper.SKIP, year=APIHelper.SKIP, ids=APIHelper.SKIP):
        """Constructor for the TraktShow class"""

        # Initialize members of the class
        if title is not APIHelper.SKIP:
            self.title = title
        if year is not APIHelper.SKIP:
            self.year = year
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

        title = (
            dictionary.get("title") if "title" in dictionary.keys() else APIHelper.SKIP
        )
        year = dictionary.get("year") if "year" in dictionary.keys() else APIHelper.SKIP
        if "ids" in dictionary.keys():
            ids = (
                TraktShowId.from_dictionary(dictionary.get("ids"))
                if dictionary.get("ids")
                else None
            )
        else:
            ids = APIHelper.SKIP
        # Return an object of this model
        return cls(title, year, ids)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        title = XmlUtilities.value_from_xml_element(root.find("title"), str)
        year = XmlUtilities.value_from_xml_element(root.find("year"), int)
        ids = XmlUtilities.value_from_xml_element(root.find("TraktShowId"), TraktShowId)

        return cls(title, year, ids)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.title, "title")
        XmlUtilities.add_as_subelement(root, self.year, "year")
        XmlUtilities.add_as_subelement(root, self.ids, "TraktShowId")
