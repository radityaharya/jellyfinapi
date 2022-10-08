# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MetadataOptions(object):

    """Implementation of the 'MetadataOptions' model.

    Class MetadataOptions.

    Attributes:
        item_type (string): TODO: type description here.
        disabled_metadata_savers (list of string): TODO: type description
            here.
        local_metadata_reader_order (list of string): TODO: type description
            here.
        disabled_metadata_fetchers (list of string): TODO: type description
            here.
        metadata_fetcher_order (list of string): TODO: type description here.
        disabled_image_fetchers (list of string): TODO: type description
            here.
        image_fetcher_order (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item_type": "ItemType",
        "disabled_metadata_savers": "DisabledMetadataSavers",
        "local_metadata_reader_order": "LocalMetadataReaderOrder",
        "disabled_metadata_fetchers": "DisabledMetadataFetchers",
        "metadata_fetcher_order": "MetadataFetcherOrder",
        "disabled_image_fetchers": "DisabledImageFetchers",
        "image_fetcher_order": "ImageFetcherOrder",
    }

    _optionals = [
        "item_type",
        "disabled_metadata_savers",
        "local_metadata_reader_order",
        "disabled_metadata_fetchers",
        "metadata_fetcher_order",
        "disabled_image_fetchers",
        "image_fetcher_order",
    ]

    _nullables = [
        "item_type",
        "disabled_metadata_savers",
        "local_metadata_reader_order",
        "disabled_metadata_fetchers",
        "metadata_fetcher_order",
        "disabled_image_fetchers",
        "image_fetcher_order",
    ]

    def __init__(
        self,
        item_type=APIHelper.SKIP,
        disabled_metadata_savers=APIHelper.SKIP,
        local_metadata_reader_order=APIHelper.SKIP,
        disabled_metadata_fetchers=APIHelper.SKIP,
        metadata_fetcher_order=APIHelper.SKIP,
        disabled_image_fetchers=APIHelper.SKIP,
        image_fetcher_order=APIHelper.SKIP,
    ):
        """Constructor for the MetadataOptions class"""

        # Initialize members of the class
        if item_type is not APIHelper.SKIP:
            self.item_type = item_type
        if disabled_metadata_savers is not APIHelper.SKIP:
            self.disabled_metadata_savers = disabled_metadata_savers
        if local_metadata_reader_order is not APIHelper.SKIP:
            self.local_metadata_reader_order = local_metadata_reader_order
        if disabled_metadata_fetchers is not APIHelper.SKIP:
            self.disabled_metadata_fetchers = disabled_metadata_fetchers
        if metadata_fetcher_order is not APIHelper.SKIP:
            self.metadata_fetcher_order = metadata_fetcher_order
        if disabled_image_fetchers is not APIHelper.SKIP:
            self.disabled_image_fetchers = disabled_image_fetchers
        if image_fetcher_order is not APIHelper.SKIP:
            self.image_fetcher_order = image_fetcher_order

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

        item_type = (
            dictionary.get("ItemType")
            if "ItemType" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_metadata_savers = (
            dictionary.get("DisabledMetadataSavers")
            if "DisabledMetadataSavers" in dictionary.keys()
            else APIHelper.SKIP
        )
        local_metadata_reader_order = (
            dictionary.get("LocalMetadataReaderOrder")
            if "LocalMetadataReaderOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_metadata_fetchers = (
            dictionary.get("DisabledMetadataFetchers")
            if "DisabledMetadataFetchers" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_fetcher_order = (
            dictionary.get("MetadataFetcherOrder")
            if "MetadataFetcherOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_image_fetchers = (
            dictionary.get("DisabledImageFetchers")
            if "DisabledImageFetchers" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_fetcher_order = (
            dictionary.get("ImageFetcherOrder")
            if "ImageFetcherOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            item_type,
            disabled_metadata_savers,
            local_metadata_reader_order,
            disabled_metadata_fetchers,
            metadata_fetcher_order,
            disabled_image_fetchers,
            image_fetcher_order,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        item_type = XmlUtilities.value_from_xml_element(root.find("ItemType"), str)
        disabled_metadata_savers = XmlUtilities.list_from_xml_element(
            root, "DisabledMetadataSavers", str
        )
        local_metadata_reader_order = XmlUtilities.list_from_xml_element(
            root, "LocalMetadataReaderOrder", str
        )
        disabled_metadata_fetchers = XmlUtilities.list_from_xml_element(
            root, "DisabledMetadataFetchers", str
        )
        metadata_fetcher_order = XmlUtilities.list_from_xml_element(
            root, "MetadataFetcherOrder", str
        )
        disabled_image_fetchers = XmlUtilities.list_from_xml_element(
            root, "DisabledImageFetchers", str
        )
        image_fetcher_order = XmlUtilities.list_from_xml_element(
            root, "ImageFetcherOrder", str
        )

        return cls(
            item_type,
            disabled_metadata_savers,
            local_metadata_reader_order,
            disabled_metadata_fetchers,
            metadata_fetcher_order,
            disabled_image_fetchers,
            image_fetcher_order,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.item_type, "ItemType")
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_metadata_savers, "DisabledMetadataSavers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.local_metadata_reader_order, "LocalMetadataReaderOrder"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_metadata_fetchers, "DisabledMetadataFetchers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_fetcher_order, "MetadataFetcherOrder"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_image_fetchers, "DisabledImageFetchers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.image_fetcher_order, "ImageFetcherOrder"
        )
