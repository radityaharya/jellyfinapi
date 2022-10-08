# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.trakt_season_id import TraktSeasonId
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktSeason(object):

    """Implementation of the 'TraktSeason' model.

    TODO: type model description here.

    Attributes:
        number (int): TODO: type description here.
        ids (TraktSeasonId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"number": "number", "ids": "ids"}

    _optionals = [
        "number",
        "ids",
    ]

    _nullables = [
        "number",
        "ids",
    ]

    def __init__(self, number=APIHelper.SKIP, ids=APIHelper.SKIP):
        """Constructor for the TraktSeason class"""

        # Initialize members of the class
        if number is not APIHelper.SKIP:
            self.number = number
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

        number = (
            dictionary.get("number")
            if "number" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ids" in dictionary.keys():
            ids = (
                TraktSeasonId.from_dictionary(dictionary.get("ids"))
                if dictionary.get("ids")
                else None
            )
        else:
            ids = APIHelper.SKIP
        # Return an object of this model
        return cls(number, ids)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        number = XmlUtilities.value_from_xml_element(root.find("number"), int)
        ids = XmlUtilities.value_from_xml_element(
            root.find("TraktSeasonId"), TraktSeasonId
        )

        return cls(number, ids)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.number, "number")
        XmlUtilities.add_as_subelement(root, self.ids, "TraktSeasonId")
