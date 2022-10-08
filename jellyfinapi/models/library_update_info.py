# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LibraryUpdateInfo(object):

    """Implementation of the 'LibraryUpdateInfo' model.

    Class LibraryUpdateInfo.

    Attributes:
        folders_added_to (list of string): Gets or sets the folders added to.
        folders_removed_from (list of string): Gets or sets the folders
            removed from.
        items_added (list of string): Gets or sets the items added.
        items_removed (list of string): Gets or sets the items removed.
        items_updated (list of string): Gets or sets the items updated.
        collection_folders (list of string): TODO: type description here.
        is_empty (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "folders_added_to": "FoldersAddedTo",
        "folders_removed_from": "FoldersRemovedFrom",
        "items_added": "ItemsAdded",
        "items_removed": "ItemsRemoved",
        "items_updated": "ItemsUpdated",
        "collection_folders": "CollectionFolders",
        "is_empty": "IsEmpty",
    }

    _optionals = [
        "folders_added_to",
        "folders_removed_from",
        "items_added",
        "items_removed",
        "items_updated",
        "collection_folders",
        "is_empty",
    ]

    def __init__(
        self,
        folders_added_to=APIHelper.SKIP,
        folders_removed_from=APIHelper.SKIP,
        items_added=APIHelper.SKIP,
        items_removed=APIHelper.SKIP,
        items_updated=APIHelper.SKIP,
        collection_folders=APIHelper.SKIP,
        is_empty=APIHelper.SKIP,
    ):
        """Constructor for the LibraryUpdateInfo class"""

        # Initialize members of the class
        if folders_added_to is not APIHelper.SKIP:
            self.folders_added_to = folders_added_to
        if folders_removed_from is not APIHelper.SKIP:
            self.folders_removed_from = folders_removed_from
        if items_added is not APIHelper.SKIP:
            self.items_added = items_added
        if items_removed is not APIHelper.SKIP:
            self.items_removed = items_removed
        if items_updated is not APIHelper.SKIP:
            self.items_updated = items_updated
        if collection_folders is not APIHelper.SKIP:
            self.collection_folders = collection_folders
        if is_empty is not APIHelper.SKIP:
            self.is_empty = is_empty

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

        folders_added_to = (
            dictionary.get("FoldersAddedTo")
            if dictionary.get("FoldersAddedTo")
            else APIHelper.SKIP
        )
        folders_removed_from = (
            dictionary.get("FoldersRemovedFrom")
            if dictionary.get("FoldersRemovedFrom")
            else APIHelper.SKIP
        )
        items_added = (
            dictionary.get("ItemsAdded")
            if dictionary.get("ItemsAdded")
            else APIHelper.SKIP
        )
        items_removed = (
            dictionary.get("ItemsRemoved")
            if dictionary.get("ItemsRemoved")
            else APIHelper.SKIP
        )
        items_updated = (
            dictionary.get("ItemsUpdated")
            if dictionary.get("ItemsUpdated")
            else APIHelper.SKIP
        )
        collection_folders = (
            dictionary.get("CollectionFolders")
            if dictionary.get("CollectionFolders")
            else APIHelper.SKIP
        )
        is_empty = (
            dictionary.get("IsEmpty")
            if "IsEmpty" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            folders_added_to,
            folders_removed_from,
            items_added,
            items_removed,
            items_updated,
            collection_folders,
            is_empty,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        folders_added_to = XmlUtilities.list_from_xml_element(
            root, "FoldersAddedTo", str
        )
        folders_removed_from = XmlUtilities.list_from_xml_element(
            root, "FoldersRemovedFrom", str
        )
        items_added = XmlUtilities.list_from_xml_element(root, "ItemsAdded", str)
        items_removed = XmlUtilities.list_from_xml_element(root, "ItemsRemoved", str)
        items_updated = XmlUtilities.list_from_xml_element(root, "ItemsUpdated", str)
        collection_folders = XmlUtilities.list_from_xml_element(
            root, "CollectionFolders", str
        )
        is_empty = XmlUtilities.value_from_xml_element(root.find("IsEmpty"), bool)

        return cls(
            folders_added_to,
            folders_removed_from,
            items_added,
            items_removed,
            items_updated,
            collection_folders,
            is_empty,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.folders_added_to, "FoldersAddedTo"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.folders_removed_from, "FoldersRemovedFrom"
        )
        XmlUtilities.add_list_as_subelement(root, self.items_added, "ItemsAdded")
        XmlUtilities.add_list_as_subelement(root, self.items_removed, "ItemsRemoved")
        XmlUtilities.add_list_as_subelement(root, self.items_updated, "ItemsUpdated")
        XmlUtilities.add_list_as_subelement(
            root, self.collection_folders, "CollectionFolders"
        )
        XmlUtilities.add_as_subelement(root, self.is_empty, "IsEmpty")
