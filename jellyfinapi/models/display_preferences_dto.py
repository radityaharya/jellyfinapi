# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DisplayPreferencesDto(object):

    """Implementation of the 'DisplayPreferencesDto' model.

    Defines the display preferences for any item that supports them (usually
    Folders).

    Attributes:
        id (string): Gets or sets the user id.
        view_type (string): Gets or sets the type of the view.
        sort_by (string): Gets or sets the sort by.
        index_by (string): Gets or sets the index by.
        remember_indexing (bool): Gets or sets a value indicating whether
            [remember indexing].
        primary_image_height (int): Gets or sets the height of the primary
            image.
        primary_image_width (int): Gets or sets the width of the primary
            image.
        custom_prefs (dict): Gets or sets the custom prefs.
        scroll_direction (ScrollDirectionEnum): An enum representing the axis
            that should be scrolled.
        show_backdrop (bool): Gets or sets a value indicating whether to show
            backdrops on this item.
        remember_sorting (bool): Gets or sets a value indicating whether
            [remember sorting].
        sort_order (SortOrderEnum): An enum representing the sorting order.
        show_sidebar (bool): Gets or sets a value indicating whether [show
            sidebar].
        client (string): Gets or sets the client.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "view_type": "ViewType",
        "sort_by": "SortBy",
        "index_by": "IndexBy",
        "remember_indexing": "RememberIndexing",
        "primary_image_height": "PrimaryImageHeight",
        "primary_image_width": "PrimaryImageWidth",
        "custom_prefs": "CustomPrefs",
        "scroll_direction": "ScrollDirection",
        "show_backdrop": "ShowBackdrop",
        "remember_sorting": "RememberSorting",
        "sort_order": "SortOrder",
        "show_sidebar": "ShowSidebar",
        "client": "Client",
    }

    _optionals = [
        "id",
        "view_type",
        "sort_by",
        "index_by",
        "remember_indexing",
        "primary_image_height",
        "primary_image_width",
        "custom_prefs",
        "scroll_direction",
        "show_backdrop",
        "remember_sorting",
        "sort_order",
        "show_sidebar",
        "client",
    ]

    _nullables = [
        "id",
        "view_type",
        "sort_by",
        "index_by",
        "custom_prefs",
        "client",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        view_type=APIHelper.SKIP,
        sort_by=APIHelper.SKIP,
        index_by=APIHelper.SKIP,
        remember_indexing=APIHelper.SKIP,
        primary_image_height=APIHelper.SKIP,
        primary_image_width=APIHelper.SKIP,
        custom_prefs=APIHelper.SKIP,
        scroll_direction=APIHelper.SKIP,
        show_backdrop=APIHelper.SKIP,
        remember_sorting=APIHelper.SKIP,
        sort_order=APIHelper.SKIP,
        show_sidebar=APIHelper.SKIP,
        client=APIHelper.SKIP,
    ):
        """Constructor for the DisplayPreferencesDto class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if view_type is not APIHelper.SKIP:
            self.view_type = view_type
        if sort_by is not APIHelper.SKIP:
            self.sort_by = sort_by
        if index_by is not APIHelper.SKIP:
            self.index_by = index_by
        if remember_indexing is not APIHelper.SKIP:
            self.remember_indexing = remember_indexing
        if primary_image_height is not APIHelper.SKIP:
            self.primary_image_height = primary_image_height
        if primary_image_width is not APIHelper.SKIP:
            self.primary_image_width = primary_image_width
        if custom_prefs is not APIHelper.SKIP:
            self.custom_prefs = custom_prefs
        if scroll_direction is not APIHelper.SKIP:
            self.scroll_direction = scroll_direction
        if show_backdrop is not APIHelper.SKIP:
            self.show_backdrop = show_backdrop
        if remember_sorting is not APIHelper.SKIP:
            self.remember_sorting = remember_sorting
        if sort_order is not APIHelper.SKIP:
            self.sort_order = sort_order
        if show_sidebar is not APIHelper.SKIP:
            self.show_sidebar = show_sidebar
        if client is not APIHelper.SKIP:
            self.client = client

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

        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        view_type = (
            dictionary.get("ViewType")
            if "ViewType" in dictionary.keys()
            else APIHelper.SKIP
        )
        sort_by = (
            dictionary.get("SortBy")
            if "SortBy" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_by = (
            dictionary.get("IndexBy")
            if "IndexBy" in dictionary.keys()
            else APIHelper.SKIP
        )
        remember_indexing = (
            dictionary.get("RememberIndexing")
            if "RememberIndexing" in dictionary.keys()
            else APIHelper.SKIP
        )
        primary_image_height = (
            dictionary.get("PrimaryImageHeight")
            if dictionary.get("PrimaryImageHeight")
            else APIHelper.SKIP
        )
        primary_image_width = (
            dictionary.get("PrimaryImageWidth")
            if dictionary.get("PrimaryImageWidth")
            else APIHelper.SKIP
        )
        custom_prefs = (
            dictionary.get("CustomPrefs")
            if "CustomPrefs" in dictionary.keys()
            else APIHelper.SKIP
        )
        scroll_direction = (
            dictionary.get("ScrollDirection")
            if dictionary.get("ScrollDirection")
            else APIHelper.SKIP
        )
        show_backdrop = (
            dictionary.get("ShowBackdrop")
            if "ShowBackdrop" in dictionary.keys()
            else APIHelper.SKIP
        )
        remember_sorting = (
            dictionary.get("RememberSorting")
            if "RememberSorting" in dictionary.keys()
            else APIHelper.SKIP
        )
        sort_order = (
            dictionary.get("SortOrder")
            if dictionary.get("SortOrder")
            else APIHelper.SKIP
        )
        show_sidebar = (
            dictionary.get("ShowSidebar")
            if "ShowSidebar" in dictionary.keys()
            else APIHelper.SKIP
        )
        client = (
            dictionary.get("Client")
            if "Client" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            view_type,
            sort_by,
            index_by,
            remember_indexing,
            primary_image_height,
            primary_image_width,
            custom_prefs,
            scroll_direction,
            show_backdrop,
            remember_sorting,
            sort_order,
            show_sidebar,
            client,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        view_type = XmlUtilities.value_from_xml_element(root.find("ViewType"), str)
        sort_by = XmlUtilities.value_from_xml_element(root.find("SortBy"), str)
        index_by = XmlUtilities.value_from_xml_element(root.find("IndexBy"), str)
        remember_indexing = XmlUtilities.value_from_xml_element(
            root.find("RememberIndexing"), bool
        )
        primary_image_height = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageHeight"), int
        )
        primary_image_width = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageWidth"), int
        )
        custom_prefs = XmlUtilities.dict_from_xml_element(
            root.find("CustomPrefs"), dict
        )

        scroll_direction = XmlUtilities.value_from_xml_element(
            root.find("ScrollDirection"), str
        )
        show_backdrop = XmlUtilities.value_from_xml_element(
            root.find("ShowBackdrop"), bool
        )
        remember_sorting = XmlUtilities.value_from_xml_element(
            root.find("RememberSorting"), bool
        )
        sort_order = XmlUtilities.value_from_xml_element(root.find("SortOrder"), str)
        show_sidebar = XmlUtilities.value_from_xml_element(
            root.find("ShowSidebar"), bool
        )
        client = XmlUtilities.value_from_xml_element(root.find("Client"), str)

        return cls(
            id,
            view_type,
            sort_by,
            index_by,
            remember_indexing,
            primary_image_height,
            primary_image_width,
            custom_prefs,
            scroll_direction,
            show_backdrop,
            remember_sorting,
            sort_order,
            show_sidebar,
            client,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.view_type, "ViewType")
        XmlUtilities.add_as_subelement(root, self.sort_by, "SortBy")
        XmlUtilities.add_as_subelement(root, self.index_by, "IndexBy")
        XmlUtilities.add_as_subelement(root, self.remember_indexing, "RememberIndexing")
        XmlUtilities.add_as_subelement(
            root, self.primary_image_height, "PrimaryImageHeight"
        )
        XmlUtilities.add_as_subelement(
            root, self.primary_image_width, "PrimaryImageWidth"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.custom_prefs, dictionary_name="CustomPrefs"
        )
        XmlUtilities.add_as_subelement(root, self.scroll_direction, "ScrollDirection")
        XmlUtilities.add_as_subelement(root, self.show_backdrop, "ShowBackdrop")
        XmlUtilities.add_as_subelement(root, self.remember_sorting, "RememberSorting")
        XmlUtilities.add_as_subelement(root, self.sort_order, "SortOrder")
        XmlUtilities.add_as_subelement(root, self.show_sidebar, "ShowSidebar")
        XmlUtilities.add_as_subelement(root, self.client, "Client")
