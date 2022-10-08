# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.version_info import VersionInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PackageInfo(object):

    """Implementation of the 'PackageInfo' model.

    Class PackageInfo.

    Attributes:
        name (string): Gets or sets the name.
        description (string): Gets or sets a long description of the plugin
            containing features or helpful explanations.
        overview (string): Gets or sets a short overview of what the plugin
            does.
        owner (string): Gets or sets the owner.
        category (string): Gets or sets the category.
        guid (uuid|string): Gets or sets the guid of the assembly associated
            with this plugin.  This is used to identify the proper item for
            automatic updates.
        versions (list of VersionInfo): Gets or sets the versions.
        image_url (string): Gets or sets the image url for the package.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "description": "description",
        "overview": "overview",
        "owner": "owner",
        "category": "category",
        "guid": "guid",
        "versions": "versions",
        "image_url": "imageUrl",
    }

    _optionals = [
        "name",
        "description",
        "overview",
        "owner",
        "category",
        "guid",
        "versions",
        "image_url",
    ]

    _nullables = [
        "image_url",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        overview=APIHelper.SKIP,
        owner=APIHelper.SKIP,
        category=APIHelper.SKIP,
        guid=APIHelper.SKIP,
        versions=APIHelper.SKIP,
        image_url=APIHelper.SKIP,
    ):
        """Constructor for the PackageInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        if overview is not APIHelper.SKIP:
            self.overview = overview
        if owner is not APIHelper.SKIP:
            self.owner = owner
        if category is not APIHelper.SKIP:
            self.category = category
        if guid is not APIHelper.SKIP:
            self.guid = guid
        if versions is not APIHelper.SKIP:
            self.versions = versions
        if image_url is not APIHelper.SKIP:
            self.image_url = image_url

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        description = (
            dictionary.get("description")
            if dictionary.get("description")
            else APIHelper.SKIP
        )
        overview = (
            dictionary.get("overview") if dictionary.get("overview") else APIHelper.SKIP
        )
        owner = dictionary.get("owner") if dictionary.get("owner") else APIHelper.SKIP
        category = (
            dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        )
        guid = dictionary.get("guid") if dictionary.get("guid") else APIHelper.SKIP
        versions = None
        if dictionary.get("versions") is not None:
            versions = [
                VersionInfo.from_dictionary(x) for x in dictionary.get("versions")
            ]
        else:
            versions = APIHelper.SKIP
        image_url = (
            dictionary.get("imageUrl")
            if "imageUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name, description, overview, owner, category, guid, versions, image_url
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("name"), str)
        description = XmlUtilities.value_from_xml_element(root.find("description"), str)
        overview = XmlUtilities.value_from_xml_element(root.find("overview"), str)
        owner = XmlUtilities.value_from_xml_element(root.find("owner"), str)
        category = XmlUtilities.value_from_xml_element(root.find("category"), str)
        guid = XmlUtilities.value_from_xml_element(root.find("guid"), str)
        versions = XmlUtilities.list_from_xml_element(root, "VersionInfo", VersionInfo)
        image_url = XmlUtilities.value_from_xml_element(root.find("imageUrl"), str)

        return cls(
            name, description, overview, owner, category, guid, versions, image_url
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "name")
        XmlUtilities.add_as_subelement(root, self.description, "description")
        XmlUtilities.add_as_subelement(root, self.overview, "overview")
        XmlUtilities.add_as_subelement(root, self.owner, "owner")
        XmlUtilities.add_as_subelement(root, self.category, "category")
        XmlUtilities.add_as_subelement(root, self.guid, "guid")
        XmlUtilities.add_list_as_subelement(root, self.versions, "VersionInfo")
        XmlUtilities.add_as_subelement(root, self.image_url, "imageUrl")
