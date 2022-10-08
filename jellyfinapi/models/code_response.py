# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CodeResponse(object):

    """Implementation of the 'CodeResponse' model.

    TODO: type model description here.

    Attributes:
        result (string): TODO: type description here.
        device_code (string): TODO: type description here.
        user_code (string): TODO: type description here.
        verification_url (string): TODO: type description here.
        expires_in (int): TODO: type description here.
        interval (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "result": "Result",
        "device_code": "device_code",
        "user_code": "user_code",
        "verification_url": "verification_url",
        "expires_in": "expires_in",
        "interval": "Interval",
    }

    _optionals = [
        "result",
        "device_code",
        "user_code",
        "verification_url",
        "expires_in",
        "interval",
    ]

    _nullables = [
        "result",
        "device_code",
        "user_code",
        "verification_url",
        "expires_in",
        "interval",
    ]

    def __init__(
        self,
        result=APIHelper.SKIP,
        device_code=APIHelper.SKIP,
        user_code=APIHelper.SKIP,
        verification_url=APIHelper.SKIP,
        expires_in=APIHelper.SKIP,
        interval=APIHelper.SKIP,
    ):
        """Constructor for the CodeResponse class"""

        # Initialize members of the class
        if result is not APIHelper.SKIP:
            self.result = result
        if device_code is not APIHelper.SKIP:
            self.device_code = device_code
        if user_code is not APIHelper.SKIP:
            self.user_code = user_code
        if verification_url is not APIHelper.SKIP:
            self.verification_url = verification_url
        if expires_in is not APIHelper.SKIP:
            self.expires_in = expires_in
        if interval is not APIHelper.SKIP:
            self.interval = interval

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

        result = (
            dictionary.get("Result")
            if "Result" in dictionary.keys()
            else APIHelper.SKIP
        )
        device_code = (
            dictionary.get("device_code")
            if "device_code" in dictionary.keys()
            else APIHelper.SKIP
        )
        user_code = (
            dictionary.get("user_code")
            if "user_code" in dictionary.keys()
            else APIHelper.SKIP
        )
        verification_url = (
            dictionary.get("verification_url")
            if "verification_url" in dictionary.keys()
            else APIHelper.SKIP
        )
        expires_in = (
            dictionary.get("expires_in")
            if "expires_in" in dictionary.keys()
            else APIHelper.SKIP
        )
        interval = (
            dictionary.get("Interval")
            if "Interval" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            result, device_code, user_code, verification_url, expires_in, interval
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        result = XmlUtilities.value_from_xml_element(root.find("Result"), str)
        device_code = XmlUtilities.value_from_xml_element(root.find("device_code"), str)
        user_code = XmlUtilities.value_from_xml_element(root.find("user_code"), str)
        verification_url = XmlUtilities.value_from_xml_element(
            root.find("verification_url"), str
        )
        expires_in = XmlUtilities.value_from_xml_element(root.find("expires_in"), int)
        interval = XmlUtilities.value_from_xml_element(root.find("Interval"), int)

        return cls(
            result, device_code, user_code, verification_url, expires_in, interval
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.result, "Result")
        XmlUtilities.add_as_subelement(root, self.device_code, "device_code")
        XmlUtilities.add_as_subelement(root, self.user_code, "user_code")
        XmlUtilities.add_as_subelement(root, self.verification_url, "verification_url")
        XmlUtilities.add_as_subelement(root, self.expires_in, "expires_in")
        XmlUtilities.add_as_subelement(root, self.interval, "Interval")
