# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.image_option import ImageOption
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TypeOptions(object):

    """Implementation of the 'TypeOptions' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        metadata_fetchers (list of string): TODO: type description here.
        metadata_fetcher_order (list of string): TODO: type description here.
        image_fetchers (list of string): TODO: type description here.
        image_fetcher_order (list of string): TODO: type description here.
        image_options (list of ImageOption): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "metadata_fetchers": "MetadataFetchers",
        "metadata_fetcher_order": "MetadataFetcherOrder",
        "image_fetchers": "ImageFetchers",
        "image_fetcher_order": "ImageFetcherOrder",
        "image_options": "ImageOptions",
    }

    _optionals = [
        "mtype",
        "metadata_fetchers",
        "metadata_fetcher_order",
        "image_fetchers",
        "image_fetcher_order",
        "image_options",
    ]

    _nullables = [
        "mtype",
        "metadata_fetchers",
        "metadata_fetcher_order",
        "image_fetchers",
        "image_fetcher_order",
        "image_options",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        metadata_fetchers=APIHelper.SKIP,
        metadata_fetcher_order=APIHelper.SKIP,
        image_fetchers=APIHelper.SKIP,
        image_fetcher_order=APIHelper.SKIP,
        image_options=APIHelper.SKIP,
    ):
        """Constructor for the TypeOptions class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if metadata_fetchers is not APIHelper.SKIP:
            self.metadata_fetchers = metadata_fetchers
        if metadata_fetcher_order is not APIHelper.SKIP:
            self.metadata_fetcher_order = metadata_fetcher_order
        if image_fetchers is not APIHelper.SKIP:
            self.image_fetchers = image_fetchers
        if image_fetcher_order is not APIHelper.SKIP:
            self.image_fetcher_order = image_fetcher_order
        if image_options is not APIHelper.SKIP:
            self.image_options = image_options

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

        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        metadata_fetchers = (
            dictionary.get("MetadataFetchers")
            if "MetadataFetchers" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_fetcher_order = (
            dictionary.get("MetadataFetcherOrder")
            if "MetadataFetcherOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_fetchers = (
            dictionary.get("ImageFetchers")
            if "ImageFetchers" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_fetcher_order = (
            dictionary.get("ImageFetcherOrder")
            if "ImageFetcherOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ImageOptions" in dictionary.keys():
            image_options = (
                [ImageOption.from_dictionary(x) for x in dictionary.get("ImageOptions")]
                if dictionary.get("ImageOptions")
                else None
            )
        else:
            image_options = APIHelper.SKIP
        # Return an object of this model
        return cls(
            mtype,
            metadata_fetchers,
            metadata_fetcher_order,
            image_fetchers,
            image_fetcher_order,
            image_options,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        metadata_fetchers = XmlUtilities.list_from_xml_element(
            root, "MetadataFetchers", str
        )
        metadata_fetcher_order = XmlUtilities.list_from_xml_element(
            root, "MetadataFetcherOrder", str
        )
        image_fetchers = XmlUtilities.list_from_xml_element(root, "ImageFetchers", str)
        image_fetcher_order = XmlUtilities.list_from_xml_element(
            root, "ImageFetcherOrder", str
        )
        image_options = XmlUtilities.list_from_xml_element(
            root, "ImageOption", ImageOption
        )

        return cls(
            mtype,
            metadata_fetchers,
            metadata_fetcher_order,
            image_fetchers,
            image_fetcher_order,
            image_options,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_fetchers, "MetadataFetchers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_fetcher_order, "MetadataFetcherOrder"
        )
        XmlUtilities.add_list_as_subelement(root, self.image_fetchers, "ImageFetchers")
        XmlUtilities.add_list_as_subelement(
            root, self.image_fetcher_order, "ImageFetcherOrder"
        )
        XmlUtilities.add_list_as_subelement(root, self.image_options, "ImageOption")
