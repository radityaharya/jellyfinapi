# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ImageProviderInfo(object):

    """Implementation of the 'ImageProviderInfo' model.

    Class ImageProviderInfo.

    Attributes:
        name (string): Gets the name.
        supported_images (list of ImageTypeEnum): Gets the supported image
            types.

    """

    # Create a mapping from Model property names to API property names
    _names = {"name": "Name", "supported_images": "SupportedImages"}

    _optionals = [
        "name",
        "supported_images",
    ]

    def __init__(self, name=APIHelper.SKIP, supported_images=APIHelper.SKIP):
        """Constructor for the ImageProviderInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if supported_images is not APIHelper.SKIP:
            self.supported_images = supported_images

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        supported_images = (
            dictionary.get("SupportedImages")
            if dictionary.get("SupportedImages")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, supported_images)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        supported_images = XmlUtilities.list_from_xml_element(
            root, "SupportedImages", str
        )

        return cls(name, supported_images)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_list_as_subelement(
            root, self.supported_images, "SupportedImages"
        )
