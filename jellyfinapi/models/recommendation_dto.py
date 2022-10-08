# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RecommendationDto(object):

    """Implementation of the 'RecommendationDto' model.

    TODO: type model description here.

    Attributes:
        items (list of BaseItemDto): TODO: type description here.
        recommendation_type (RecommendationTypeEnum): TODO: type description
            here.
        baseline_item_name (string): TODO: type description here.
        category_id (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items": "Items",
        "recommendation_type": "RecommendationType",
        "baseline_item_name": "BaselineItemName",
        "category_id": "CategoryId",
    }

    _optionals = [
        "items",
        "recommendation_type",
        "baseline_item_name",
        "category_id",
    ]

    _nullables = [
        "items",
        "baseline_item_name",
    ]

    def __init__(
        self,
        items=APIHelper.SKIP,
        recommendation_type=APIHelper.SKIP,
        baseline_item_name=APIHelper.SKIP,
        category_id=APIHelper.SKIP,
    ):
        """Constructor for the RecommendationDto class"""

        # Initialize members of the class
        if items is not APIHelper.SKIP:
            self.items = items
        if recommendation_type is not APIHelper.SKIP:
            self.recommendation_type = recommendation_type
        if baseline_item_name is not APIHelper.SKIP:
            self.baseline_item_name = baseline_item_name
        if category_id is not APIHelper.SKIP:
            self.category_id = category_id

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

        if "Items" in dictionary.keys():
            items = (
                [BaseItemDto.from_dictionary(x) for x in dictionary.get("Items")]
                if dictionary.get("Items")
                else None
            )
        else:
            items = APIHelper.SKIP
        recommendation_type = (
            dictionary.get("RecommendationType")
            if dictionary.get("RecommendationType")
            else APIHelper.SKIP
        )
        baseline_item_name = (
            dictionary.get("BaselineItemName")
            if "BaselineItemName" in dictionary.keys()
            else APIHelper.SKIP
        )
        category_id = (
            dictionary.get("CategoryId")
            if dictionary.get("CategoryId")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(items, recommendation_type, baseline_item_name, category_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        items = XmlUtilities.list_from_xml_element(root, "BaseItemDto", BaseItemDto)
        recommendation_type = XmlUtilities.value_from_xml_element(
            root.find("RecommendationType"), str
        )
        baseline_item_name = XmlUtilities.value_from_xml_element(
            root.find("BaselineItemName"), str
        )
        category_id = XmlUtilities.value_from_xml_element(root.find("CategoryId"), str)

        return cls(items, recommendation_type, baseline_item_name, category_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.items, "BaseItemDto")
        XmlUtilities.add_as_subelement(
            root, self.recommendation_type, "RecommendationType"
        )
        XmlUtilities.add_as_subelement(
            root, self.baseline_item_name, "BaselineItemName"
        )
        XmlUtilities.add_as_subelement(root, self.category_id, "CategoryId")
