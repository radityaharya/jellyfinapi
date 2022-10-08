# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ImageInfo(object):

    """Implementation of the 'ImageInfo' model.

    Class ImageInfo.

    Attributes:
        image_type (ImageTypeEnum): Gets or sets the type of the image.
        image_index (int): Gets or sets the index of the image.
        image_tag (string): Gets or sets the image tag.
        path (string): Gets or sets the path.
        blur_hash (string): Gets or sets the blurhash.
        height (int): Gets or sets the height.
        width (int): Gets or sets the width.
        size (long|int): Gets or sets the size.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "image_type": "ImageType",
        "image_index": "ImageIndex",
        "image_tag": "ImageTag",
        "path": "Path",
        "blur_hash": "BlurHash",
        "height": "Height",
        "width": "Width",
        "size": "Size",
    }

    _optionals = [
        "image_type",
        "image_index",
        "image_tag",
        "path",
        "blur_hash",
        "height",
        "width",
        "size",
    ]

    _nullables = [
        "image_index",
        "image_tag",
        "path",
        "blur_hash",
        "height",
        "width",
    ]

    def __init__(
        self,
        image_type=APIHelper.SKIP,
        image_index=APIHelper.SKIP,
        image_tag=APIHelper.SKIP,
        path=APIHelper.SKIP,
        blur_hash=APIHelper.SKIP,
        height=APIHelper.SKIP,
        width=APIHelper.SKIP,
        size=APIHelper.SKIP,
    ):
        """Constructor for the ImageInfo class"""

        # Initialize members of the class
        if image_type is not APIHelper.SKIP:
            self.image_type = image_type
        if image_index is not APIHelper.SKIP:
            self.image_index = image_index
        if image_tag is not APIHelper.SKIP:
            self.image_tag = image_tag
        if path is not APIHelper.SKIP:
            self.path = path
        if blur_hash is not APIHelper.SKIP:
            self.blur_hash = blur_hash
        if height is not APIHelper.SKIP:
            self.height = height
        if width is not APIHelper.SKIP:
            self.width = width
        if size is not APIHelper.SKIP:
            self.size = size

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

        image_type = (
            dictionary.get("ImageType")
            if dictionary.get("ImageType")
            else APIHelper.SKIP
        )
        image_index = (
            dictionary.get("ImageIndex")
            if "ImageIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_tag = (
            dictionary.get("ImageTag")
            if "ImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        blur_hash = (
            dictionary.get("BlurHash")
            if "BlurHash" in dictionary.keys()
            else APIHelper.SKIP
        )
        height = (
            dictionary.get("Height")
            if "Height" in dictionary.keys()
            else APIHelper.SKIP
        )
        width = (
            dictionary.get("Width") if "Width" in dictionary.keys() else APIHelper.SKIP
        )
        size = dictionary.get("Size") if dictionary.get("Size") else APIHelper.SKIP
        # Return an object of this model
        return cls(
            image_type, image_index, image_tag, path, blur_hash, height, width, size
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        image_type = XmlUtilities.value_from_xml_element(root.find("ImageType"), str)
        image_index = XmlUtilities.value_from_xml_element(root.find("ImageIndex"), int)
        image_tag = XmlUtilities.value_from_xml_element(root.find("ImageTag"), str)
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        blur_hash = XmlUtilities.value_from_xml_element(root.find("BlurHash"), str)
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        size = XmlUtilities.value_from_xml_element(root.find("Size"), int)

        return cls(
            image_type, image_index, image_tag, path, blur_hash, height, width, size
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.image_type, "ImageType")
        XmlUtilities.add_as_subelement(root, self.image_index, "ImageIndex")
        XmlUtilities.add_as_subelement(root, self.image_tag, "ImageTag")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.blur_hash, "BlurHash")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(root, self.size, "Size")
