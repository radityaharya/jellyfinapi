# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.package_info import PackageInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class InstallationInfo(object):

    """Implementation of the 'InstallationInfo' model.

    Class InstallationInfo.

    Attributes:
        guid (uuid|string): Gets or sets the Id.
        name (string): Gets or sets the name.
        version (string): Gets or sets the version.
        changelog (string): Gets or sets the changelog for this version.
        source_url (string): Gets or sets the source URL.
        checksum (string): Gets or sets a checksum for the binary.
        package_info (PackageInfo): Gets or sets package information for the
            installation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "guid": "Guid",
        "name": "Name",
        "version": "Version",
        "changelog": "Changelog",
        "source_url": "SourceUrl",
        "checksum": "Checksum",
        "package_info": "PackageInfo",
    }

    _optionals = [
        "guid",
        "name",
        "version",
        "changelog",
        "source_url",
        "checksum",
        "package_info",
    ]

    _nullables = [
        "name",
        "version",
        "changelog",
        "source_url",
        "checksum",
        "package_info",
    ]

    def __init__(
        self,
        guid=APIHelper.SKIP,
        name=APIHelper.SKIP,
        version=APIHelper.SKIP,
        changelog=APIHelper.SKIP,
        source_url=APIHelper.SKIP,
        checksum=APIHelper.SKIP,
        package_info=APIHelper.SKIP,
    ):
        """Constructor for the InstallationInfo class"""

        # Initialize members of the class
        if guid is not APIHelper.SKIP:
            self.guid = guid
        if name is not APIHelper.SKIP:
            self.name = name
        if version is not APIHelper.SKIP:
            self.version = version
        if changelog is not APIHelper.SKIP:
            self.changelog = changelog
        if source_url is not APIHelper.SKIP:
            self.source_url = source_url
        if checksum is not APIHelper.SKIP:
            self.checksum = checksum
        if package_info is not APIHelper.SKIP:
            self.package_info = package_info

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

        guid = dictionary.get("Guid") if dictionary.get("Guid") else APIHelper.SKIP
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        version = (
            dictionary.get("Version")
            if "Version" in dictionary.keys()
            else APIHelper.SKIP
        )
        changelog = (
            dictionary.get("Changelog")
            if "Changelog" in dictionary.keys()
            else APIHelper.SKIP
        )
        source_url = (
            dictionary.get("SourceUrl")
            if "SourceUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        checksum = (
            dictionary.get("Checksum")
            if "Checksum" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "PackageInfo" in dictionary.keys():
            package_info = (
                PackageInfo.from_dictionary(dictionary.get("PackageInfo"))
                if dictionary.get("PackageInfo")
                else None
            )
        else:
            package_info = APIHelper.SKIP
        # Return an object of this model
        return cls(guid, name, version, changelog, source_url, checksum, package_info)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        guid = XmlUtilities.value_from_xml_element(root.find("Guid"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        version = XmlUtilities.value_from_xml_element(root.find("Version"), str)
        changelog = XmlUtilities.value_from_xml_element(root.find("Changelog"), str)
        source_url = XmlUtilities.value_from_xml_element(root.find("SourceUrl"), str)
        checksum = XmlUtilities.value_from_xml_element(root.find("Checksum"), str)
        package_info = XmlUtilities.value_from_xml_element(
            root.find("PackageInfo"), PackageInfo
        )

        return cls(guid, name, version, changelog, source_url, checksum, package_info)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.guid, "Guid")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.version, "Version")
        XmlUtilities.add_as_subelement(root, self.changelog, "Changelog")
        XmlUtilities.add_as_subelement(root, self.source_url, "SourceUrl")
        XmlUtilities.add_as_subelement(root, self.checksum, "Checksum")
        XmlUtilities.add_as_subelement(root, self.package_info, "PackageInfo")
