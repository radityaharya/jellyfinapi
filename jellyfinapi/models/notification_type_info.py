# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationTypeInfo(object):

    """Implementation of the 'NotificationTypeInfo' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        name (string): TODO: type description here.
        enabled (bool): TODO: type description here.
        category (string): TODO: type description here.
        is_based_on_user_event (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "name": "Name",
        "enabled": "Enabled",
        "category": "Category",
        "is_based_on_user_event": "IsBasedOnUserEvent",
    }

    _optionals = [
        "mtype",
        "name",
        "enabled",
        "category",
        "is_based_on_user_event",
    ]

    _nullables = [
        "mtype",
        "name",
        "category",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        name=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        category=APIHelper.SKIP,
        is_based_on_user_event=APIHelper.SKIP,
    ):
        """Constructor for the NotificationTypeInfo class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if name is not APIHelper.SKIP:
            self.name = name
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if category is not APIHelper.SKIP:
            self.category = category
        if is_based_on_user_event is not APIHelper.SKIP:
            self.is_based_on_user_event = is_based_on_user_event

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
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        enabled = (
            dictionary.get("Enabled")
            if "Enabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        category = (
            dictionary.get("Category")
            if "Category" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_based_on_user_event = (
            dictionary.get("IsBasedOnUserEvent")
            if "IsBasedOnUserEvent" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(mtype, name, enabled, category, is_based_on_user_event)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        enabled = XmlUtilities.value_from_xml_element(root.find("Enabled"), bool)
        category = XmlUtilities.value_from_xml_element(root.find("Category"), str)
        is_based_on_user_event = XmlUtilities.value_from_xml_element(
            root.find("IsBasedOnUserEvent"), bool
        )

        return cls(mtype, name, enabled, category, is_based_on_user_event)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.enabled, "Enabled")
        XmlUtilities.add_as_subelement(root, self.category, "Category")
        XmlUtilities.add_as_subelement(
            root, self.is_based_on_user_event, "IsBasedOnUserEvent"
        )
