# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.image_blur_hashes import ImageBlurHashes
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class BaseItemPerson(object):

    """Implementation of the 'BaseItemPerson' model.

    This is used by the api to get information about a Person within a
    BaseItem.

    Attributes:
        name (string): Gets or sets the name.
        id (uuid|string): Gets or sets the identifier.
        role (string): Gets or sets the role.
        mtype (string): Gets or sets the type.
        primary_image_tag (string): Gets or sets the primary image tag.
        image_blur_hashes (ImageBlurHashes): Gets or sets the primary image
            blurhash.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "id": "Id",
        "role": "Role",
        "mtype": "Type",
        "primary_image_tag": "PrimaryImageTag",
        "image_blur_hashes": "ImageBlurHashes",
    }

    _optionals = [
        "name",
        "id",
        "role",
        "mtype",
        "primary_image_tag",
        "image_blur_hashes",
    ]

    _nullables = [
        "name",
        "role",
        "mtype",
        "primary_image_tag",
        "image_blur_hashes",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        id=APIHelper.SKIP,
        role=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        primary_image_tag=APIHelper.SKIP,
        image_blur_hashes=APIHelper.SKIP,
    ):
        """Constructor for the BaseItemPerson class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if id is not APIHelper.SKIP:
            self.id = id
        if role is not APIHelper.SKIP:
            self.role = role
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if primary_image_tag is not APIHelper.SKIP:
            self.primary_image_tag = primary_image_tag
        if image_blur_hashes is not APIHelper.SKIP:
            self.image_blur_hashes = image_blur_hashes

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        role = dictionary.get("Role") if "Role" in dictionary.keys() else APIHelper.SKIP
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        primary_image_tag = (
            dictionary.get("PrimaryImageTag")
            if "PrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ImageBlurHashes" in dictionary.keys():
            image_blur_hashes = (
                ImageBlurHashes.from_dictionary(dictionary.get("ImageBlurHashes"))
                if dictionary.get("ImageBlurHashes")
                else None
            )
        else:
            image_blur_hashes = APIHelper.SKIP
        # Return an object of this model
        return cls(name, id, role, mtype, primary_image_tag, image_blur_hashes)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        role = XmlUtilities.value_from_xml_element(root.find("Role"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageTag"), str
        )
        image_blur_hashes = XmlUtilities.value_from_xml_element(
            root.find("ImageBlurHashes"), ImageBlurHashes
        )

        return cls(name, id, role, mtype, primary_image_tag, image_blur_hashes)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.role, "Role")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.primary_image_tag, "PrimaryImageTag")
        XmlUtilities.add_as_subelement(root, self.image_blur_hashes, "ImageBlurHashes")
