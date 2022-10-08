# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.music_video_info import MusicVideoInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MusicVideoInfoRemoteSearchQuery(object):

    """Implementation of the 'MusicVideoInfoRemoteSearchQuery' model.

    TODO: type model description here.

    Attributes:
        search_info (MusicVideoInfo): TODO: type description here.
        item_id (uuid|string): TODO: type description here.
        search_provider_name (string): Gets or sets the provider name to
            search within if set.
        include_disabled_providers (bool): Gets or sets a value indicating
            whether disabled providers should be included.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_info": "SearchInfo",
        "item_id": "ItemId",
        "search_provider_name": "SearchProviderName",
        "include_disabled_providers": "IncludeDisabledProviders",
    }

    _optionals = [
        "search_info",
        "item_id",
        "search_provider_name",
        "include_disabled_providers",
    ]

    _nullables = [
        "search_info",
        "search_provider_name",
    ]

    def __init__(
        self,
        search_info=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        search_provider_name=APIHelper.SKIP,
        include_disabled_providers=APIHelper.SKIP,
    ):
        """Constructor for the MusicVideoInfoRemoteSearchQuery class"""

        # Initialize members of the class
        if search_info is not APIHelper.SKIP:
            self.search_info = search_info
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if search_provider_name is not APIHelper.SKIP:
            self.search_provider_name = search_provider_name
        if include_disabled_providers is not APIHelper.SKIP:
            self.include_disabled_providers = include_disabled_providers

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

        if "SearchInfo" in dictionary.keys():
            search_info = (
                MusicVideoInfo.from_dictionary(dictionary.get("SearchInfo"))
                if dictionary.get("SearchInfo")
                else None
            )
        else:
            search_info = APIHelper.SKIP
        item_id = (
            dictionary.get("ItemId") if dictionary.get("ItemId") else APIHelper.SKIP
        )
        search_provider_name = (
            dictionary.get("SearchProviderName")
            if "SearchProviderName" in dictionary.keys()
            else APIHelper.SKIP
        )
        include_disabled_providers = (
            dictionary.get("IncludeDisabledProviders")
            if "IncludeDisabledProviders" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            search_info, item_id, search_provider_name, include_disabled_providers
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        search_info = XmlUtilities.value_from_xml_element(
            root.find("MusicVideoInfo"), MusicVideoInfo
        )
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        search_provider_name = XmlUtilities.value_from_xml_element(
            root.find("SearchProviderName"), str
        )
        include_disabled_providers = XmlUtilities.value_from_xml_element(
            root.find("IncludeDisabledProviders"), bool
        )

        return cls(
            search_info, item_id, search_provider_name, include_disabled_providers
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.search_info, "MusicVideoInfo")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(
            root, self.search_provider_name, "SearchProviderName"
        )
        XmlUtilities.add_as_subelement(
            root, self.include_disabled_providers, "IncludeDisabledProviders"
        )
