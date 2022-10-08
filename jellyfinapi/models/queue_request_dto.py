# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QueueRequestDto(object):

    """Implementation of the 'QueueRequestDto' model.

    Class QueueRequestDto.

    Attributes:
        item_ids (list of uuid|string): Gets or sets the items to enqueue.
        mode (GroupQueueModeEnum): Enum GroupQueueMode.

    """

    # Create a mapping from Model property names to API property names
    _names = {"item_ids": "ItemIds", "mode": "Mode"}

    _optionals = [
        "item_ids",
        "mode",
    ]

    def __init__(self, item_ids=APIHelper.SKIP, mode=APIHelper.SKIP):
        """Constructor for the QueueRequestDto class"""

        # Initialize members of the class
        if item_ids is not APIHelper.SKIP:
            self.item_ids = item_ids
        if mode is not APIHelper.SKIP:
            self.mode = mode

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

        item_ids = (
            dictionary.get("ItemIds") if dictionary.get("ItemIds") else APIHelper.SKIP
        )
        mode = dictionary.get("Mode") if dictionary.get("Mode") else APIHelper.SKIP
        # Return an object of this model
        return cls(item_ids, mode)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        item_ids = XmlUtilities.list_from_xml_element(root, "ItemIds", str)
        mode = XmlUtilities.value_from_xml_element(root.find("Mode"), str)

        return cls(item_ids, mode)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.item_ids, "ItemIds")
        XmlUtilities.add_as_subelement(root, self.mode, "Mode")
