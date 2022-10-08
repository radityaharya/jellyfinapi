# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceOptionsDto(object):

    """Implementation of the 'DeviceOptionsDto' model.

    A dto representing custom options for a device.

    Attributes:
        id (int): Gets or sets the id.
        device_id (string): Gets or sets the device id.
        custom_name (string): Gets or sets the custom name.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "device_id": "DeviceId", "custom_name": "CustomName"}

    _optionals = [
        "id",
        "device_id",
        "custom_name",
    ]

    _nullables = [
        "device_id",
        "custom_name",
    ]

    def __init__(
        self, id=APIHelper.SKIP, device_id=APIHelper.SKIP, custom_name=APIHelper.SKIP
    ):
        """Constructor for the DeviceOptionsDto class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id
        if custom_name is not APIHelper.SKIP:
            self.custom_name = custom_name

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

        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        device_id = (
            dictionary.get("DeviceId")
            if "DeviceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        custom_name = (
            dictionary.get("CustomName")
            if "CustomName" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(id, device_id, custom_name)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), int)
        device_id = XmlUtilities.value_from_xml_element(root.find("DeviceId"), str)
        custom_name = XmlUtilities.value_from_xml_element(root.find("CustomName"), str)

        return cls(id, device_id, custom_name)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.device_id, "DeviceId")
        XmlUtilities.add_as_subelement(root, self.custom_name, "CustomName")
