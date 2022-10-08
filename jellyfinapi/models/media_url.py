# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaUrl(object):

    """Implementation of the 'MediaUrl' model.

    TODO: type model description here.

    Attributes:
        url (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"url": "Url", "name": "Name"}

    _optionals = [
        "url",
        "name",
    ]

    _nullables = [
        "url",
        "name",
    ]

    def __init__(self, url=APIHelper.SKIP, name=APIHelper.SKIP):
        """Constructor for the MediaUrl class"""

        # Initialize members of the class
        if url is not APIHelper.SKIP:
            self.url = url
        if name is not APIHelper.SKIP:
            self.name = name

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

        url = dictionary.get("Url") if "Url" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(url, name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)

        return cls(url, name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.url, "Url")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
