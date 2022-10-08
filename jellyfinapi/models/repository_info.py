# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RepositoryInfo(object):

    """Implementation of the 'RepositoryInfo' model.

    Class RepositoryInfo.

    Attributes:
        name (string): Gets or sets the name.
        url (string): Gets or sets the URL.
        enabled (bool): Gets or sets a value indicating whether the repository
            is enabled.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "url": "Url", "enabled": "Enabled"}

    _optionals = [
        "name",
        "url",
        "enabled",
    ]

    _nullables = [
        "name",
        "url",
    ]

    def __init__(self, name=APIHelper.SKIP, url=APIHelper.SKIP, enabled=APIHelper.SKIP):
        """Constructor for the RepositoryInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if url is not APIHelper.SKIP:
            self.url = url
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled

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
        url = dictionary.get("Url") if "Url" in dictionary.keys() else APIHelper.SKIP
        enabled = (
            dictionary.get("Enabled")
            if "Enabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, url, enabled)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)
        enabled = XmlUtilities.value_from_xml_element(root.find("Enabled"), bool)

        return cls(name, url, enabled)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.url, "Url")
        XmlUtilities.add_as_subelement(root, self.enabled, "Enabled")
