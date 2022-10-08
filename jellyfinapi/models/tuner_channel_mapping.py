# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TunerChannelMapping(object):

    """Implementation of the 'TunerChannelMapping' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        provider_channel_name (string): TODO: type description here.
        provider_channel_id (string): TODO: type description here.
        id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "provider_channel_name": "ProviderChannelName",
        "provider_channel_id": "ProviderChannelId",
        "id": "Id",
    }

    _optionals = [
        "name",
        "provider_channel_name",
        "provider_channel_id",
        "id",
    ]

    _nullables = [
        "name",
        "provider_channel_name",
        "provider_channel_id",
        "id",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        provider_channel_name=APIHelper.SKIP,
        provider_channel_id=APIHelper.SKIP,
        id=APIHelper.SKIP,
    ):
        """Constructor for the TunerChannelMapping class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if provider_channel_name is not APIHelper.SKIP:
            self.provider_channel_name = provider_channel_name
        if provider_channel_id is not APIHelper.SKIP:
            self.provider_channel_id = provider_channel_id
        if id is not APIHelper.SKIP:
            self.id = id

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
        provider_channel_name = (
            dictionary.get("ProviderChannelName")
            if "ProviderChannelName" in dictionary.keys()
            else APIHelper.SKIP
        )
        provider_channel_id = (
            dictionary.get("ProviderChannelId")
            if "ProviderChannelId" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name, provider_channel_name, provider_channel_id, id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        provider_channel_name = XmlUtilities.value_from_xml_element(
            root.find("ProviderChannelName"), str
        )
        provider_channel_id = XmlUtilities.value_from_xml_element(
            root.find("ProviderChannelId"), str
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)

        return cls(name, provider_channel_name, provider_channel_id, id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(
            root, self.provider_channel_name, "ProviderChannelName"
        )
        XmlUtilities.add_as_subelement(
            root, self.provider_channel_id, "ProviderChannelId"
        )
        XmlUtilities.add_as_subelement(root, self.id, "Id")
