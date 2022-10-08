# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ControlResponse(object):

    """Implementation of the 'ControlResponse' model.

    TODO: type model description here.

    Attributes:
        headers (dict): TODO: type description here.
        xml (string): TODO: type description here.
        is_successful (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"headers": "Headers", "xml": "Xml", "is_successful": "IsSuccessful"}

    _optionals = [
        "headers",
        "xml",
        "is_successful",
    ]

    def __init__(
        self, headers=APIHelper.SKIP, xml=APIHelper.SKIP, is_successful=APIHelper.SKIP
    ):
        """Constructor for the ControlResponse class"""

        # Initialize members of the class
        if headers is not APIHelper.SKIP:
            self.headers = headers
        if xml is not APIHelper.SKIP:
            self.xml = xml
        if is_successful is not APIHelper.SKIP:
            self.is_successful = is_successful

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

        headers = (
            dictionary.get("Headers") if dictionary.get("Headers") else APIHelper.SKIP
        )
        xml = dictionary.get("Xml") if dictionary.get("Xml") else APIHelper.SKIP
        is_successful = (
            dictionary.get("IsSuccessful")
            if "IsSuccessful" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(headers, xml, is_successful)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        headers = XmlUtilities.dict_from_xml_element(root.find("Headers"), dict)

        xml = XmlUtilities.value_from_xml_element(root.find("Xml"), str)
        is_successful = XmlUtilities.value_from_xml_element(
            root.find("IsSuccessful"), bool
        )

        return cls(headers, xml, is_successful)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_dict_as_subelement(
            root, self.headers, dictionary_name="Headers"
        )
        XmlUtilities.add_as_subelement(root, self.xml, "Xml")
        XmlUtilities.add_as_subelement(root, self.is_successful, "IsSuccessful")
