# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.remote_image_info import RemoteImageInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RemoteImageResult(object):

    """Implementation of the 'RemoteImageResult' model.

    Class RemoteImageResult.

    Attributes:
        images (list of RemoteImageInfo): Gets or sets the images.
        total_record_count (int): Gets or sets the total record count.
        providers (list of string): Gets or sets the providers.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "images": "Images",
        "total_record_count": "TotalRecordCount",
        "providers": "Providers",
    }

    _optionals = [
        "images",
        "total_record_count",
        "providers",
    ]

    _nullables = [
        "images",
        "providers",
    ]

    def __init__(
        self,
        images=APIHelper.SKIP,
        total_record_count=APIHelper.SKIP,
        providers=APIHelper.SKIP,
    ):
        """Constructor for the RemoteImageResult class"""

        # Initialize members of the class
        if images is not APIHelper.SKIP:
            self.images = images
        if total_record_count is not APIHelper.SKIP:
            self.total_record_count = total_record_count
        if providers is not APIHelper.SKIP:
            self.providers = providers

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

        if "Images" in dictionary.keys():
            images = (
                [RemoteImageInfo.from_dictionary(x) for x in dictionary.get("Images")]
                if dictionary.get("Images")
                else None
            )
        else:
            images = APIHelper.SKIP
        total_record_count = (
            dictionary.get("TotalRecordCount")
            if dictionary.get("TotalRecordCount")
            else APIHelper.SKIP
        )
        providers = (
            dictionary.get("Providers")
            if "Providers" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(images, total_record_count, providers)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        images = XmlUtilities.list_from_xml_element(
            root, "RemoteImageInfo", RemoteImageInfo
        )
        total_record_count = XmlUtilities.value_from_xml_element(
            root.find("TotalRecordCount"), int
        )
        providers = XmlUtilities.list_from_xml_element(root, "Providers", str)

        return cls(images, total_record_count, providers)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.images, "RemoteImageInfo")
        XmlUtilities.add_as_subelement(
            root, self.total_record_count, "TotalRecordCount"
        )
        XmlUtilities.add_list_as_subelement(root, self.providers, "Providers")
