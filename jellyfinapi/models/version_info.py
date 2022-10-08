# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class VersionInfo(object):

    """Implementation of the 'VersionInfo' model.

    Defines the MediaBrowser.Model.Updates.VersionInfo class.

    Attributes:
        version (string): Gets or sets the version.
        version_number (string): Gets the version as a System.Version.
        changelog (string): Gets or sets the changelog for this version.
        target_abi (string): Gets or sets the ABI that this version was built
            against.
        source_url (string): Gets or sets the source URL.
        checksum (string): Gets or sets a checksum for the binary.
        timestamp (string): Gets or sets a timestamp of when the binary was
            built.
        repository_name (string): Gets or sets the repository name.
        repository_url (string): Gets or sets the repository url.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": "version",
        "version_number": "VersionNumber",
        "changelog": "changelog",
        "target_abi": "targetAbi",
        "source_url": "sourceUrl",
        "checksum": "checksum",
        "timestamp": "timestamp",
        "repository_name": "repositoryName",
        "repository_url": "repositoryUrl",
    }

    _optionals = [
        "version",
        "version_number",
        "changelog",
        "target_abi",
        "source_url",
        "checksum",
        "timestamp",
        "repository_name",
        "repository_url",
    ]

    _nullables = [
        "changelog",
        "target_abi",
        "source_url",
        "checksum",
        "timestamp",
    ]

    def __init__(
        self,
        version=APIHelper.SKIP,
        version_number=APIHelper.SKIP,
        changelog=APIHelper.SKIP,
        target_abi=APIHelper.SKIP,
        source_url=APIHelper.SKIP,
        checksum=APIHelper.SKIP,
        timestamp=APIHelper.SKIP,
        repository_name=APIHelper.SKIP,
        repository_url=APIHelper.SKIP,
    ):
        """Constructor for the VersionInfo class"""

        # Initialize members of the class
        if version is not APIHelper.SKIP:
            self.version = version
        if version_number is not APIHelper.SKIP:
            self.version_number = version_number
        if changelog is not APIHelper.SKIP:
            self.changelog = changelog
        if target_abi is not APIHelper.SKIP:
            self.target_abi = target_abi
        if source_url is not APIHelper.SKIP:
            self.source_url = source_url
        if checksum is not APIHelper.SKIP:
            self.checksum = checksum
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp
        if repository_name is not APIHelper.SKIP:
            self.repository_name = repository_name
        if repository_url is not APIHelper.SKIP:
            self.repository_url = repository_url

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

        version = (
            dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        )
        version_number = (
            dictionary.get("VersionNumber")
            if dictionary.get("VersionNumber")
            else APIHelper.SKIP
        )
        changelog = (
            dictionary.get("changelog")
            if "changelog" in dictionary.keys()
            else APIHelper.SKIP
        )
        target_abi = (
            dictionary.get("targetAbi")
            if "targetAbi" in dictionary.keys()
            else APIHelper.SKIP
        )
        source_url = (
            dictionary.get("sourceUrl")
            if "sourceUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        checksum = (
            dictionary.get("checksum")
            if "checksum" in dictionary.keys()
            else APIHelper.SKIP
        )
        timestamp = (
            dictionary.get("timestamp")
            if "timestamp" in dictionary.keys()
            else APIHelper.SKIP
        )
        repository_name = (
            dictionary.get("repositoryName")
            if dictionary.get("repositoryName")
            else APIHelper.SKIP
        )
        repository_url = (
            dictionary.get("repositoryUrl")
            if dictionary.get("repositoryUrl")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            version,
            version_number,
            changelog,
            target_abi,
            source_url,
            checksum,
            timestamp,
            repository_name,
            repository_url,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        version = XmlUtilities.value_from_xml_element(root.find("version"), str)
        version_number = XmlUtilities.value_from_xml_element(
            root.find("VersionNumber"), str
        )
        changelog = XmlUtilities.value_from_xml_element(root.find("changelog"), str)
        target_abi = XmlUtilities.value_from_xml_element(root.find("targetAbi"), str)
        source_url = XmlUtilities.value_from_xml_element(root.find("sourceUrl"), str)
        checksum = XmlUtilities.value_from_xml_element(root.find("checksum"), str)
        timestamp = XmlUtilities.value_from_xml_element(root.find("timestamp"), str)
        repository_name = XmlUtilities.value_from_xml_element(
            root.find("repositoryName"), str
        )
        repository_url = XmlUtilities.value_from_xml_element(
            root.find("repositoryUrl"), str
        )

        return cls(
            version,
            version_number,
            changelog,
            target_abi,
            source_url,
            checksum,
            timestamp,
            repository_name,
            repository_url,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.version, "version")
        XmlUtilities.add_as_subelement(root, self.version_number, "VersionNumber")
        XmlUtilities.add_as_subelement(root, self.changelog, "changelog")
        XmlUtilities.add_as_subelement(root, self.target_abi, "targetAbi")
        XmlUtilities.add_as_subelement(root, self.source_url, "sourceUrl")
        XmlUtilities.add_as_subelement(root, self.checksum, "checksum")
        XmlUtilities.add_as_subelement(root, self.timestamp, "timestamp")
        XmlUtilities.add_as_subelement(root, self.repository_name, "repositoryName")
        XmlUtilities.add_as_subelement(root, self.repository_url, "repositoryUrl")
