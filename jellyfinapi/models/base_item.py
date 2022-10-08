# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_url import MediaUrl
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class BaseItem(object):

    """Implementation of the 'BaseItem' model.

    Class BaseItem.

    Attributes:
        size (long|int): TODO: type description here.
        container (string): TODO: type description here.
        is_hd (bool): TODO: type description here.
        is_shortcut (bool): TODO: type description here.
        shortcut_path (string): TODO: type description here.
        width (int): TODO: type description here.
        height (int): TODO: type description here.
        extra_ids (list of uuid|string): TODO: type description here.
        date_last_saved (datetime): TODO: type description here.
        remote_trailers (list of MediaUrl): Gets or sets the remote trailers.
        supports_external_transfer (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "size": "Size",
        "container": "Container",
        "is_hd": "IsHD",
        "is_shortcut": "IsShortcut",
        "shortcut_path": "ShortcutPath",
        "width": "Width",
        "height": "Height",
        "extra_ids": "ExtraIds",
        "date_last_saved": "DateLastSaved",
        "remote_trailers": "RemoteTrailers",
        "supports_external_transfer": "SupportsExternalTransfer",
    }

    _optionals = [
        "size",
        "container",
        "is_hd",
        "is_shortcut",
        "shortcut_path",
        "width",
        "height",
        "extra_ids",
        "date_last_saved",
        "remote_trailers",
        "supports_external_transfer",
    ]

    _nullables = [
        "size",
        "container",
        "shortcut_path",
        "extra_ids",
        "remote_trailers",
    ]

    def __init__(
        self,
        size=APIHelper.SKIP,
        container=APIHelper.SKIP,
        is_hd=APIHelper.SKIP,
        is_shortcut=APIHelper.SKIP,
        shortcut_path=APIHelper.SKIP,
        width=APIHelper.SKIP,
        height=APIHelper.SKIP,
        extra_ids=APIHelper.SKIP,
        date_last_saved=APIHelper.SKIP,
        remote_trailers=APIHelper.SKIP,
        supports_external_transfer=APIHelper.SKIP,
    ):
        """Constructor for the BaseItem class"""

        # Initialize members of the class
        if size is not APIHelper.SKIP:
            self.size = size
        if container is not APIHelper.SKIP:
            self.container = container
        if is_hd is not APIHelper.SKIP:
            self.is_hd = is_hd
        if is_shortcut is not APIHelper.SKIP:
            self.is_shortcut = is_shortcut
        if shortcut_path is not APIHelper.SKIP:
            self.shortcut_path = shortcut_path
        if width is not APIHelper.SKIP:
            self.width = width
        if height is not APIHelper.SKIP:
            self.height = height
        if extra_ids is not APIHelper.SKIP:
            self.extra_ids = extra_ids
        if date_last_saved is not APIHelper.SKIP:
            self.date_last_saved = (
                APIHelper.RFC3339DateTime(date_last_saved) if date_last_saved else None
            )
        if remote_trailers is not APIHelper.SKIP:
            self.remote_trailers = remote_trailers
        if supports_external_transfer is not APIHelper.SKIP:
            self.supports_external_transfer = supports_external_transfer

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

        size = dictionary.get("Size") if "Size" in dictionary.keys() else APIHelper.SKIP
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_hd = (
            dictionary.get("IsHD") if "IsHD" in dictionary.keys() else APIHelper.SKIP
        )
        is_shortcut = (
            dictionary.get("IsShortcut")
            if "IsShortcut" in dictionary.keys()
            else APIHelper.SKIP
        )
        shortcut_path = (
            dictionary.get("ShortcutPath")
            if "ShortcutPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        width = dictionary.get("Width") if dictionary.get("Width") else APIHelper.SKIP
        height = (
            dictionary.get("Height") if dictionary.get("Height") else APIHelper.SKIP
        )
        extra_ids = (
            dictionary.get("ExtraIds")
            if "ExtraIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        date_last_saved = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("DateLastSaved")
            ).datetime
            if dictionary.get("DateLastSaved")
            else APIHelper.SKIP
        )
        if "RemoteTrailers" in dictionary.keys():
            remote_trailers = (
                [MediaUrl.from_dictionary(x) for x in dictionary.get("RemoteTrailers")]
                if dictionary.get("RemoteTrailers")
                else None
            )
        else:
            remote_trailers = APIHelper.SKIP
        supports_external_transfer = (
            dictionary.get("SupportsExternalTransfer")
            if "SupportsExternalTransfer" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            size,
            container,
            is_hd,
            is_shortcut,
            shortcut_path,
            width,
            height,
            extra_ids,
            date_last_saved,
            remote_trailers,
            supports_external_transfer,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        size = XmlUtilities.value_from_xml_element(root.find("Size"), int)
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        is_hd = XmlUtilities.value_from_xml_element(root.find("IsHD"), bool)
        is_shortcut = XmlUtilities.value_from_xml_element(root.find("IsShortcut"), bool)
        shortcut_path = XmlUtilities.value_from_xml_element(
            root.find("ShortcutPath"), str
        )
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        extra_ids = XmlUtilities.list_from_xml_element(root, "ExtraIds", str)
        date_last_saved = XmlUtilities.value_from_xml_element(
            root.find("DateLastSaved"), APIHelper.RFC3339DateTime
        )
        remote_trailers = XmlUtilities.list_from_xml_element(root, "MediaUrl", MediaUrl)
        supports_external_transfer = XmlUtilities.value_from_xml_element(
            root.find("SupportsExternalTransfer"), bool
        )

        return cls(
            size,
            container,
            is_hd,
            is_shortcut,
            shortcut_path,
            width,
            height,
            extra_ids,
            date_last_saved,
            remote_trailers,
            supports_external_transfer,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.size, "Size")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.is_hd, "IsHD")
        XmlUtilities.add_as_subelement(root, self.is_shortcut, "IsShortcut")
        XmlUtilities.add_as_subelement(root, self.shortcut_path, "ShortcutPath")
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_list_as_subelement(root, self.extra_ids, "ExtraIds")
        XmlUtilities.add_as_subelement(root, self.date_last_saved, "DateLastSaved")
        XmlUtilities.add_list_as_subelement(root, self.remote_trailers, "MediaUrl")
        XmlUtilities.add_as_subelement(
            root, self.supports_external_transfer, "SupportsExternalTransfer"
        )
