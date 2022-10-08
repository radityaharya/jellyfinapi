# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.library_options import LibraryOptions
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class VirtualFolderInfo(object):

    """Implementation of the 'VirtualFolderInfo' model.

    Used to hold information about a user's list of configured virtual
    folders.

    Attributes:
        name (string): Gets or sets the name.
        locations (list of string): Gets or sets the locations.
        collection_type (CollectionTypeOptionsEnum): Gets or sets the type of
            the collection.
        library_options (LibraryOptions): TODO: type description here.
        item_id (string): Gets or sets the item identifier.
        primary_image_item_id (string): Gets or sets the primary image item
            identifier.
        refresh_progress (float): TODO: type description here.
        refresh_status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "locations": "Locations",
        "collection_type": "CollectionType",
        "library_options": "LibraryOptions",
        "item_id": "ItemId",
        "primary_image_item_id": "PrimaryImageItemId",
        "refresh_progress": "RefreshProgress",
        "refresh_status": "RefreshStatus",
    }

    _optionals = [
        "name",
        "locations",
        "collection_type",
        "library_options",
        "item_id",
        "primary_image_item_id",
        "refresh_progress",
        "refresh_status",
    ]

    _nullables = [
        "name",
        "locations",
        "collection_type",
        "library_options",
        "item_id",
        "primary_image_item_id",
        "refresh_progress",
        "refresh_status",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        locations=APIHelper.SKIP,
        collection_type=APIHelper.SKIP,
        library_options=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
        primary_image_item_id=APIHelper.SKIP,
        refresh_progress=APIHelper.SKIP,
        refresh_status=APIHelper.SKIP,
    ):
        """Constructor for the VirtualFolderInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if locations is not APIHelper.SKIP:
            self.locations = locations
        if collection_type is not APIHelper.SKIP:
            self.collection_type = collection_type
        if library_options is not APIHelper.SKIP:
            self.library_options = library_options
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if primary_image_item_id is not APIHelper.SKIP:
            self.primary_image_item_id = primary_image_item_id
        if refresh_progress is not APIHelper.SKIP:
            self.refresh_progress = refresh_progress
        if refresh_status is not APIHelper.SKIP:
            self.refresh_status = refresh_status

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
        locations = (
            dictionary.get("Locations")
            if "Locations" in dictionary.keys()
            else APIHelper.SKIP
        )
        collection_type = (
            dictionary.get("CollectionType")
            if "CollectionType" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "LibraryOptions" in dictionary.keys():
            library_options = (
                LibraryOptions.from_dictionary(dictionary.get("LibraryOptions"))
                if dictionary.get("LibraryOptions")
                else None
            )
        else:
            library_options = APIHelper.SKIP
        item_id = (
            dictionary.get("ItemId")
            if "ItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        primary_image_item_id = (
            dictionary.get("PrimaryImageItemId")
            if "PrimaryImageItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        refresh_progress = (
            dictionary.get("RefreshProgress")
            if "RefreshProgress" in dictionary.keys()
            else APIHelper.SKIP
        )
        refresh_status = (
            dictionary.get("RefreshStatus")
            if "RefreshStatus" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            locations,
            collection_type,
            library_options,
            item_id,
            primary_image_item_id,
            refresh_progress,
            refresh_status,
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
        locations = XmlUtilities.list_from_xml_element(root, "Locations", str)
        collection_type = XmlUtilities.value_from_xml_element(
            root.find("CollectionType"), str
        )
        library_options = XmlUtilities.value_from_xml_element(
            root.find("LibraryOptions"), LibraryOptions
        )
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        primary_image_item_id = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageItemId"), str
        )
        refresh_progress = XmlUtilities.value_from_xml_element(
            root.find("RefreshProgress"), float
        )
        refresh_status = XmlUtilities.value_from_xml_element(
            root.find("RefreshStatus"), str
        )

        return cls(
            name,
            locations,
            collection_type,
            library_options,
            item_id,
            primary_image_item_id,
            refresh_progress,
            refresh_status,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_list_as_subelement(root, self.locations, "Locations")
        XmlUtilities.add_as_subelement(root, self.collection_type, "CollectionType")
        XmlUtilities.add_as_subelement(root, self.library_options, "LibraryOptions")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(
            root, self.primary_image_item_id, "PrimaryImageItemId"
        )
        XmlUtilities.add_as_subelement(root, self.refresh_progress, "RefreshProgress")
        XmlUtilities.add_as_subelement(root, self.refresh_status, "RefreshStatus")
