# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.name_id_pair import NameIdPair
from jellyfinapi.models.name_value_pair import NameValuePair
from jellyfinapi.models.tuner_channel_mapping import TunerChannelMapping
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ChannelMappingOptionsDto(object):

    """Implementation of the 'ChannelMappingOptionsDto' model.

    Channel mapping options dto.

    Attributes:
        tuner_channels (list of TunerChannelMapping): Gets or sets list of
            tuner channels.
        provider_channels (list of NameIdPair): Gets or sets list of provider
            channels.
        mappings (list of NameValuePair): Gets or sets list of mappings.
        provider_name (string): Gets or sets provider name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tuner_channels": "TunerChannels",
        "provider_channels": "ProviderChannels",
        "mappings": "Mappings",
        "provider_name": "ProviderName",
    }

    _optionals = [
        "tuner_channels",
        "provider_channels",
        "mappings",
        "provider_name",
    ]

    _nullables = [
        "provider_name",
    ]

    def __init__(
        self,
        tuner_channels=APIHelper.SKIP,
        provider_channels=APIHelper.SKIP,
        mappings=APIHelper.SKIP,
        provider_name=APIHelper.SKIP,
    ):
        """Constructor for the ChannelMappingOptionsDto class"""

        # Initialize members of the class
        if tuner_channels is not APIHelper.SKIP:
            self.tuner_channels = tuner_channels
        if provider_channels is not APIHelper.SKIP:
            self.provider_channels = provider_channels
        if mappings is not APIHelper.SKIP:
            self.mappings = mappings
        if provider_name is not APIHelper.SKIP:
            self.provider_name = provider_name

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

        tuner_channels = None
        if dictionary.get("TunerChannels") is not None:
            tuner_channels = [
                TunerChannelMapping.from_dictionary(x)
                for x in dictionary.get("TunerChannels")
            ]
        else:
            tuner_channels = APIHelper.SKIP
        provider_channels = None
        if dictionary.get("ProviderChannels") is not None:
            provider_channels = [
                NameIdPair.from_dictionary(x)
                for x in dictionary.get("ProviderChannels")
            ]
        else:
            provider_channels = APIHelper.SKIP
        mappings = None
        if dictionary.get("Mappings") is not None:
            mappings = [
                NameValuePair.from_dictionary(x) for x in dictionary.get("Mappings")
            ]
        else:
            mappings = APIHelper.SKIP
        provider_name = (
            dictionary.get("ProviderName")
            if "ProviderName" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(tuner_channels, provider_channels, mappings, provider_name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        tuner_channels = XmlUtilities.list_from_xml_element(
            root, "TunerChannelMapping", TunerChannelMapping
        )
        provider_channels = XmlUtilities.list_from_xml_element(
            root, "NameIdPair", NameIdPair
        )
        mappings = XmlUtilities.list_from_xml_element(
            root, "NameValuePair", NameValuePair
        )
        provider_name = XmlUtilities.value_from_xml_element(
            root.find("ProviderName"), str
        )

        return cls(tuner_channels, provider_channels, mappings, provider_name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.tuner_channels, "TunerChannelMapping"
        )
        XmlUtilities.add_list_as_subelement(root, self.provider_channels, "NameIdPair")
        XmlUtilities.add_list_as_subelement(root, self.mappings, "NameValuePair")
        XmlUtilities.add_as_subelement(root, self.provider_name, "ProviderName")
