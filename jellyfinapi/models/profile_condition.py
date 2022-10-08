# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ProfileCondition(object):

    """Implementation of the 'ProfileCondition' model.

    TODO: type model description here.

    Attributes:
        condition (ProfileConditionTypeEnum): TODO: type description here.
        property (ProfileConditionValueEnum): TODO: type description here.
        value (string): TODO: type description here.
        is_required (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "condition": "Condition",
        "property": "Property",
        "value": "Value",
        "is_required": "IsRequired",
    }

    _optionals = [
        "condition",
        "property",
        "value",
        "is_required",
    ]

    _nullables = [
        "value",
    ]

    def __init__(
        self,
        condition=APIHelper.SKIP,
        property=APIHelper.SKIP,
        value=APIHelper.SKIP,
        is_required=APIHelper.SKIP,
    ):
        """Constructor for the ProfileCondition class"""

        # Initialize members of the class
        if condition is not APIHelper.SKIP:
            self.condition = condition
        if property is not APIHelper.SKIP:
            self.property = property
        if value is not APIHelper.SKIP:
            self.value = value
        if is_required is not APIHelper.SKIP:
            self.is_required = is_required

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

        condition = (
            dictionary.get("Condition")
            if dictionary.get("Condition")
            else APIHelper.SKIP
        )
        property = (
            dictionary.get("Property") if dictionary.get("Property") else APIHelper.SKIP
        )
        value = (
            dictionary.get("Value") if "Value" in dictionary.keys() else APIHelper.SKIP
        )
        is_required = (
            dictionary.get("IsRequired")
            if "IsRequired" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(condition, property, value, is_required)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        condition = XmlUtilities.value_from_xml_element(root.find("Condition"), str)
        property = XmlUtilities.value_from_xml_element(root.find("Property"), str)
        value = XmlUtilities.value_from_xml_element(root.find("Value"), str)
        is_required = XmlUtilities.value_from_xml_element(root.find("IsRequired"), bool)

        return cls(condition, property, value, is_required)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.condition, "Condition")
        XmlUtilities.add_as_subelement(root, self.property, "Property")
        XmlUtilities.add_as_subelement(root, self.value, "Value")
        XmlUtilities.add_as_subelement(root, self.is_required, "IsRequired")
