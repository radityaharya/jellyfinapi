# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ChannelFeatures(object):

    """Implementation of the 'ChannelFeatures' model.

    TODO: type model description here.

    Attributes:
        name (string): Gets or sets the name.
        id (uuid|string): Gets or sets the identifier.
        can_search (bool): Gets or sets a value indicating whether this
            instance can search.
        media_types (list of ChannelMediaTypeEnum): Gets or sets the media
            types.
        content_types (list of ChannelMediaContentTypeEnum): Gets or sets the
            content types.
        max_page_size (int): Gets or sets the maximum number of records the
            channel allows retrieving at a time.
        auto_refresh_levels (int): Gets or sets the automatic refresh levels.
        default_sort_fields (list of ChannelItemSortFieldEnum): Gets or sets
            the default sort orders.
        supports_sort_order_toggle (bool): Gets or sets a value indicating
            whether a sort ascending/descending toggle is supported.
        supports_latest_media (bool): Gets or sets a value indicating whether
            [supports latest media].
        can_filter (bool): Gets or sets a value indicating whether this
            instance can filter.
        supports_content_downloading (bool): Gets or sets a value indicating
            whether [supports content downloading].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "id": "Id",
        "can_search": "CanSearch",
        "media_types": "MediaTypes",
        "content_types": "ContentTypes",
        "max_page_size": "MaxPageSize",
        "auto_refresh_levels": "AutoRefreshLevels",
        "default_sort_fields": "DefaultSortFields",
        "supports_sort_order_toggle": "SupportsSortOrderToggle",
        "supports_latest_media": "SupportsLatestMedia",
        "can_filter": "CanFilter",
        "supports_content_downloading": "SupportsContentDownloading",
    }

    _optionals = [
        "name",
        "id",
        "can_search",
        "media_types",
        "content_types",
        "max_page_size",
        "auto_refresh_levels",
        "default_sort_fields",
        "supports_sort_order_toggle",
        "supports_latest_media",
        "can_filter",
        "supports_content_downloading",
    ]

    _nullables = [
        "max_page_size",
        "auto_refresh_levels",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        id=APIHelper.SKIP,
        can_search=APIHelper.SKIP,
        media_types=APIHelper.SKIP,
        content_types=APIHelper.SKIP,
        max_page_size=APIHelper.SKIP,
        auto_refresh_levels=APIHelper.SKIP,
        default_sort_fields=APIHelper.SKIP,
        supports_sort_order_toggle=APIHelper.SKIP,
        supports_latest_media=APIHelper.SKIP,
        can_filter=APIHelper.SKIP,
        supports_content_downloading=APIHelper.SKIP,
    ):
        """Constructor for the ChannelFeatures class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if id is not APIHelper.SKIP:
            self.id = id
        if can_search is not APIHelper.SKIP:
            self.can_search = can_search
        if media_types is not APIHelper.SKIP:
            self.media_types = media_types
        if content_types is not APIHelper.SKIP:
            self.content_types = content_types
        if max_page_size is not APIHelper.SKIP:
            self.max_page_size = max_page_size
        if auto_refresh_levels is not APIHelper.SKIP:
            self.auto_refresh_levels = auto_refresh_levels
        if default_sort_fields is not APIHelper.SKIP:
            self.default_sort_fields = default_sort_fields
        if supports_sort_order_toggle is not APIHelper.SKIP:
            self.supports_sort_order_toggle = supports_sort_order_toggle
        if supports_latest_media is not APIHelper.SKIP:
            self.supports_latest_media = supports_latest_media
        if can_filter is not APIHelper.SKIP:
            self.can_filter = can_filter
        if supports_content_downloading is not APIHelper.SKIP:
            self.supports_content_downloading = supports_content_downloading

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        can_search = (
            dictionary.get("CanSearch")
            if "CanSearch" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_types = (
            dictionary.get("MediaTypes")
            if dictionary.get("MediaTypes")
            else APIHelper.SKIP
        )
        content_types = (
            dictionary.get("ContentTypes")
            if dictionary.get("ContentTypes")
            else APIHelper.SKIP
        )
        max_page_size = (
            dictionary.get("MaxPageSize")
            if "MaxPageSize" in dictionary.keys()
            else APIHelper.SKIP
        )
        auto_refresh_levels = (
            dictionary.get("AutoRefreshLevels")
            if "AutoRefreshLevels" in dictionary.keys()
            else APIHelper.SKIP
        )
        default_sort_fields = (
            dictionary.get("DefaultSortFields")
            if dictionary.get("DefaultSortFields")
            else APIHelper.SKIP
        )
        supports_sort_order_toggle = (
            dictionary.get("SupportsSortOrderToggle")
            if "SupportsSortOrderToggle" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_latest_media = (
            dictionary.get("SupportsLatestMedia")
            if "SupportsLatestMedia" in dictionary.keys()
            else APIHelper.SKIP
        )
        can_filter = (
            dictionary.get("CanFilter")
            if "CanFilter" in dictionary.keys()
            else APIHelper.SKIP
        )
        supports_content_downloading = (
            dictionary.get("SupportsContentDownloading")
            if "SupportsContentDownloading" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            id,
            can_search,
            media_types,
            content_types,
            max_page_size,
            auto_refresh_levels,
            default_sort_fields,
            supports_sort_order_toggle,
            supports_latest_media,
            can_filter,
            supports_content_downloading,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        can_search = XmlUtilities.value_from_xml_element(root.find("CanSearch"), bool)
        media_types = XmlUtilities.list_from_xml_element(root, "MediaTypes", str)
        content_types = XmlUtilities.list_from_xml_element(root, "ContentTypes", str)
        max_page_size = XmlUtilities.value_from_xml_element(
            root.find("MaxPageSize"), int
        )
        auto_refresh_levels = XmlUtilities.value_from_xml_element(
            root.find("AutoRefreshLevels"), int
        )
        default_sort_fields = XmlUtilities.list_from_xml_element(
            root, "DefaultSortFields", str
        )
        supports_sort_order_toggle = XmlUtilities.value_from_xml_element(
            root.find("SupportsSortOrderToggle"), bool
        )
        supports_latest_media = XmlUtilities.value_from_xml_element(
            root.find("SupportsLatestMedia"), bool
        )
        can_filter = XmlUtilities.value_from_xml_element(root.find("CanFilter"), bool)
        supports_content_downloading = XmlUtilities.value_from_xml_element(
            root.find("SupportsContentDownloading"), bool
        )

        return cls(
            name,
            id,
            can_search,
            media_types,
            content_types,
            max_page_size,
            auto_refresh_levels,
            default_sort_fields,
            supports_sort_order_toggle,
            supports_latest_media,
            can_filter,
            supports_content_downloading,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.can_search, "CanSearch")
        XmlUtilities.add_list_as_subelement(root, self.media_types, "MediaTypes")
        XmlUtilities.add_list_as_subelement(root, self.content_types, "ContentTypes")
        XmlUtilities.add_as_subelement(root, self.max_page_size, "MaxPageSize")
        XmlUtilities.add_as_subelement(
            root, self.auto_refresh_levels, "AutoRefreshLevels"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.default_sort_fields, "DefaultSortFields"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_sort_order_toggle, "SupportsSortOrderToggle"
        )
        XmlUtilities.add_as_subelement(
            root, self.supports_latest_media, "SupportsLatestMedia"
        )
        XmlUtilities.add_as_subelement(root, self.can_filter, "CanFilter")
        XmlUtilities.add_as_subelement(
            root, self.supports_content_downloading, "SupportsContentDownloading"
        )
