# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.trakt_person_id import TraktPersonId
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktPerson(object):

    """Implementation of the 'TraktPerson' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        ids (TraktPersonId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "name", "ids": "ids"}

    _optionals = [
        "name",
        "ids",
    ]

    _nullables = [
        "name",
        "ids",
    ]

    def __init__(self, name=APIHelper.SKIP, ids=APIHelper.SKIP):
        """Constructor for the TraktPerson class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
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

        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        if "ids" in dictionary.keys():
            ids = (
                TraktPersonId.from_dictionary(dictionary.get("ids"))
                if dictionary.get("ids")
                else None
            )
        else:
            ids = APIHelper.SKIP
        # Return an object of this model
        return cls(name, ids)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("name"), str)
        ids = XmlUtilities.value_from_xml_element(
            root.find("TraktPersonId"), TraktPersonId
        )

        return cls(name, ids)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "name")
        XmlUtilities.add_as_subelement(root, self.ids, "TraktPersonId")
