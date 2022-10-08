# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SetChannelMappingDto(object):

    """Implementation of the 'SetChannelMappingDto' model.

    Set channel mapping dto.

    Attributes:
        provider_id (string): Gets or sets the provider id.
        tuner_channel_id (string): Gets or sets the tuner channel id.
        provider_channel_id (string): Gets or sets the provider channel id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "provider_id": "ProviderId",
        "tuner_channel_id": "TunerChannelId",
        "provider_channel_id": "ProviderChannelId",
    }

    def __init__(
        self, provider_id=None, tuner_channel_id=None, provider_channel_id=None
    ):
        """Constructor for the SetChannelMappingDto class"""

        # Initialize members of the class
        self.provider_id = provider_id
        self.tuner_channel_id = tuner_channel_id
        self.provider_channel_id = provider_channel_id

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

        provider_id = (
            dictionary.get("ProviderId") if dictionary.get("ProviderId") else None
        )
        tuner_channel_id = (
            dictionary.get("TunerChannelId")
            if dictionary.get("TunerChannelId")
            else None
        )
        provider_channel_id = (
            dictionary.get("ProviderChannelId")
            if dictionary.get("ProviderChannelId")
            else None
        )
        # Return an object of this model
        return cls(provider_id, tuner_channel_id, provider_channel_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        provider_id = XmlUtilities.value_from_xml_element(root.find("ProviderId"), str)
        tuner_channel_id = XmlUtilities.value_from_xml_element(
            root.find("TunerChannelId"), str
        )
        provider_channel_id = XmlUtilities.value_from_xml_element(
            root.find("ProviderChannelId"), str
        )

        return cls(provider_id, tuner_channel_id, provider_channel_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.provider_id, "ProviderId")
        XmlUtilities.add_as_subelement(root, self.tuner_channel_id, "TunerChannelId")
        XmlUtilities.add_as_subelement(
            root, self.provider_channel_id, "ProviderChannelId"
        )
