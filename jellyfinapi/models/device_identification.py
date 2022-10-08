# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.http_header_info import HttpHeaderInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceIdentification(object):

    """Implementation of the 'DeviceIdentification' model.

    TODO: type model description here.

    Attributes:
        friendly_name (string): Gets or sets the name of the friendly.
        model_number (string): Gets or sets the model number.
        serial_number (string): Gets or sets the serial number.
        model_name (string): Gets or sets the name of the model.
        model_description (string): Gets or sets the model description.
        model_url (string): Gets or sets the model URL.
        manufacturer (string): Gets or sets the manufacturer.
        manufacturer_url (string): Gets or sets the manufacturer URL.
        headers (list of HttpHeaderInfo): Gets or sets the headers.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "friendly_name": "FriendlyName",
        "model_number": "ModelNumber",
        "serial_number": "SerialNumber",
        "model_name": "ModelName",
        "model_description": "ModelDescription",
        "model_url": "ModelUrl",
        "manufacturer": "Manufacturer",
        "manufacturer_url": "ManufacturerUrl",
        "headers": "Headers",
    }

    _optionals = [
        "friendly_name",
        "model_number",
        "serial_number",
        "model_name",
        "model_description",
        "model_url",
        "manufacturer",
        "manufacturer_url",
        "headers",
    ]

    def __init__(
        self,
        friendly_name=APIHelper.SKIP,
        model_number=APIHelper.SKIP,
        serial_number=APIHelper.SKIP,
        model_name=APIHelper.SKIP,
        model_description=APIHelper.SKIP,
        model_url=APIHelper.SKIP,
        manufacturer=APIHelper.SKIP,
        manufacturer_url=APIHelper.SKIP,
        headers=APIHelper.SKIP,
    ):
        """Constructor for the DeviceIdentification class"""

        # Initialize members of the class
        if friendly_name is not APIHelper.SKIP:
            self.friendly_name = friendly_name
        if model_number is not APIHelper.SKIP:
            self.model_number = model_number
        if serial_number is not APIHelper.SKIP:
            self.serial_number = serial_number
        if model_name is not APIHelper.SKIP:
            self.model_name = model_name
        if model_description is not APIHelper.SKIP:
            self.model_description = model_description
        if model_url is not APIHelper.SKIP:
            self.model_url = model_url
        if manufacturer is not APIHelper.SKIP:
            self.manufacturer = manufacturer
        if manufacturer_url is not APIHelper.SKIP:
            self.manufacturer_url = manufacturer_url
        if headers is not APIHelper.SKIP:
            self.headers = headers

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

        friendly_name = (
            dictionary.get("FriendlyName")
            if dictionary.get("FriendlyName")
            else APIHelper.SKIP
        )
        model_number = (
            dictionary.get("ModelNumber")
            if dictionary.get("ModelNumber")
            else APIHelper.SKIP
        )
        serial_number = (
            dictionary.get("SerialNumber")
            if dictionary.get("SerialNumber")
            else APIHelper.SKIP
        )
        model_name = (
            dictionary.get("ModelName")
            if dictionary.get("ModelName")
            else APIHelper.SKIP
        )
        model_description = (
            dictionary.get("ModelDescription")
            if dictionary.get("ModelDescription")
            else APIHelper.SKIP
        )
        model_url = (
            dictionary.get("ModelUrl") if dictionary.get("ModelUrl") else APIHelper.SKIP
        )
        manufacturer = (
            dictionary.get("Manufacturer")
            if dictionary.get("Manufacturer")
            else APIHelper.SKIP
        )
        manufacturer_url = (
            dictionary.get("ManufacturerUrl")
            if dictionary.get("ManufacturerUrl")
            else APIHelper.SKIP
        )
        headers = None
        if dictionary.get("Headers") is not None:
            headers = [
                HttpHeaderInfo.from_dictionary(x) for x in dictionary.get("Headers")
            ]
        else:
            headers = APIHelper.SKIP
        # Return an object of this model
        return cls(
            friendly_name,
            model_number,
            serial_number,
            model_name,
            model_description,
            model_url,
            manufacturer,
            manufacturer_url,
            headers,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        friendly_name = XmlUtilities.value_from_xml_element(
            root.find("FriendlyName"), str
        )
        model_number = XmlUtilities.value_from_xml_element(
            root.find("ModelNumber"), str
        )
        serial_number = XmlUtilities.value_from_xml_element(
            root.find("SerialNumber"), str
        )
        model_name = XmlUtilities.value_from_xml_element(root.find("ModelName"), str)
        model_description = XmlUtilities.value_from_xml_element(
            root.find("ModelDescription"), str
        )
        model_url = XmlUtilities.value_from_xml_element(root.find("ModelUrl"), str)
        manufacturer = XmlUtilities.value_from_xml_element(
            root.find("Manufacturer"), str
        )
        manufacturer_url = XmlUtilities.value_from_xml_element(
            root.find("ManufacturerUrl"), str
        )
        headers = XmlUtilities.list_from_xml_element(
            root, "HttpHeaderInfo", HttpHeaderInfo
        )

        return cls(
            friendly_name,
            model_number,
            serial_number,
            model_name,
            model_description,
            model_url,
            manufacturer,
            manufacturer_url,
            headers,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.friendly_name, "FriendlyName")
        XmlUtilities.add_as_subelement(root, self.model_number, "ModelNumber")
        XmlUtilities.add_as_subelement(root, self.serial_number, "SerialNumber")
        XmlUtilities.add_as_subelement(root, self.model_name, "ModelName")
        XmlUtilities.add_as_subelement(root, self.model_description, "ModelDescription")
        XmlUtilities.add_as_subelement(root, self.model_url, "ModelUrl")
        XmlUtilities.add_as_subelement(root, self.manufacturer, "Manufacturer")
        XmlUtilities.add_as_subelement(root, self.manufacturer_url, "ManufacturerUrl")
        XmlUtilities.add_list_as_subelement(root, self.headers, "HttpHeaderInfo")
