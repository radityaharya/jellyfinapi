# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class HttpHeaderInfo(object):

    """Implementation of the 'HttpHeaderInfo' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        value (string): TODO: type description here.
        match (HeaderMatchTypeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "value": "Value", "match": "Match"}

    _optionals = [
        "name",
        "value",
        "match",
    ]

    _nullables = [
        "name",
        "value",
    ]

    def __init__(self, name=APIHelper.SKIP, value=APIHelper.SKIP, match=APIHelper.SKIP):
        """Constructor for the HttpHeaderInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if value is not APIHelper.SKIP:
            self.value = value
        if match is not APIHelper.SKIP:
            self.match = match

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        value = (
            dictionary.get("Value") if "Value" in dictionary.keys() else APIHelper.SKIP
        )
        match = dictionary.get("Match") if dictionary.get("Match") else APIHelper.SKIP
        # Return an object of this model
        return cls(name, value, match)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        value = XmlUtilities.value_from_xml_element(root.find("Value"), str)
        match = XmlUtilities.value_from_xml_element(root.find("Match"), str)

        return cls(name, value, match)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.value, "Value")
        XmlUtilities.add_as_subelement(root, self.match, "Match")
