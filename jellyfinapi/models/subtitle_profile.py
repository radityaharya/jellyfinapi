# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SubtitleProfile(object):

    """Implementation of the 'SubtitleProfile' model.

    TODO: type model description here.

    Attributes:
        format (string): TODO: type description here.
        method (SubtitleDeliveryMethodEnum): Delivery method to use during
            playback of a specific subtitle format.
        didl_mode (string): TODO: type description here.
        language (string): TODO: type description here.
        container (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "format": "Format",
        "method": "Method",
        "didl_mode": "DidlMode",
        "language": "Language",
        "container": "Container",
    }

    _optionals = [
        "format",
        "method",
        "didl_mode",
        "language",
        "container",
    ]

    _nullables = [
        "format",
        "didl_mode",
        "language",
        "container",
    ]

    def __init__(
        self,
        format=APIHelper.SKIP,
        method=APIHelper.SKIP,
        didl_mode=APIHelper.SKIP,
        language=APIHelper.SKIP,
        container=APIHelper.SKIP,
    ):
        """Constructor for the SubtitleProfile class"""

        # Initialize members of the class
        if format is not APIHelper.SKIP:
            self.format = format
        if method is not APIHelper.SKIP:
            self.method = method
        if didl_mode is not APIHelper.SKIP:
            self.didl_mode = didl_mode
        if language is not APIHelper.SKIP:
            self.language = language
        if container is not APIHelper.SKIP:
            self.container = container

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

        format = (
            dictionary.get("Format")
            if "Format" in dictionary.keys()
            else APIHelper.SKIP
        )
        method = (
            dictionary.get("Method") if dictionary.get("Method") else APIHelper.SKIP
        )
        didl_mode = (
            dictionary.get("DidlMode")
            if "DidlMode" in dictionary.keys()
            else APIHelper.SKIP
        )
        language = (
            dictionary.get("Language")
            if "Language" in dictionary.keys()
            else APIHelper.SKIP
        )
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(format, method, didl_mode, language, container)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        format = XmlUtilities.value_from_xml_element(root.find("Format"), str)
        method = XmlUtilities.value_from_xml_element(root.find("Method"), str)
        didl_mode = XmlUtilities.value_from_xml_element(root.find("DidlMode"), str)
        language = XmlUtilities.value_from_xml_element(root.find("Language"), str)
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)

        return cls(format, method, didl_mode, language, container)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.format, "Format")
        XmlUtilities.add_as_subelement(root, self.method, "Method")
        XmlUtilities.add_as_subelement(root, self.didl_mode, "DidlMode")
        XmlUtilities.add_as_subelement(root, self.language, "Language")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
