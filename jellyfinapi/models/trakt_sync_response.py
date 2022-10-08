# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.items import Items
from jellyfinapi.models.not_found_objects import NotFoundObjects
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TraktSyncResponse(object):

    """Implementation of the 'TraktSyncResponse' model.

    TODO: type model description here.

    Attributes:
        added (Items): TODO: type description here.
        deleted (Items): TODO: type description here.
        updated (Items): TODO: type description here.
        not_found (NotFoundObjects): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "added": "added",
        "deleted": "deleted",
        "updated": "updated",
        "not_found": "not_found",
    }

    _optionals = [
        "added",
        "deleted",
        "updated",
        "not_found",
    ]

    _nullables = [
        "added",
        "deleted",
        "updated",
        "not_found",
    ]

    def __init__(
        self,
        added=APIHelper.SKIP,
        deleted=APIHelper.SKIP,
        updated=APIHelper.SKIP,
        not_found=APIHelper.SKIP,
    ):
        """Constructor for the TraktSyncResponse class"""

        # Initialize members of the class
        if added is not APIHelper.SKIP:
            self.added = added
        if deleted is not APIHelper.SKIP:
            self.deleted = deleted
        if updated is not APIHelper.SKIP:
            self.updated = updated
        if not_found is not APIHelper.SKIP:
            self.not_found = not_found

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

        if "added" in dictionary.keys():
            added = (
                Items.from_dictionary(dictionary.get("added"))
                if dictionary.get("added")
                else None
            )
        else:
            added = APIHelper.SKIP
        if "deleted" in dictionary.keys():
            deleted = (
                Items.from_dictionary(dictionary.get("deleted"))
                if dictionary.get("deleted")
                else None
            )
        else:
            deleted = APIHelper.SKIP
        if "updated" in dictionary.keys():
            updated = (
                Items.from_dictionary(dictionary.get("updated"))
                if dictionary.get("updated")
                else None
            )
        else:
            updated = APIHelper.SKIP
        if "not_found" in dictionary.keys():
            not_found = (
                NotFoundObjects.from_dictionary(dictionary.get("not_found"))
                if dictionary.get("not_found")
                else None
            )
        else:
            not_found = APIHelper.SKIP
        # Return an object of this model
        return cls(added, deleted, updated, not_found)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        added = XmlUtilities.value_from_xml_element(root.find("Items"), Items)
        deleted = XmlUtilities.value_from_xml_element(root.find("Items"), Items)
        updated = XmlUtilities.value_from_xml_element(root.find("Items"), Items)
        not_found = XmlUtilities.value_from_xml_element(
            root.find("NotFoundObjects"), NotFoundObjects
        )

        return cls(added, deleted, updated, not_found)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.added, "Items")
        XmlUtilities.add_as_subelement(root, self.deleted, "Items")
        XmlUtilities.add_as_subelement(root, self.updated, "Items")
        XmlUtilities.add_as_subelement(root, self.not_found, "NotFoundObjects")
