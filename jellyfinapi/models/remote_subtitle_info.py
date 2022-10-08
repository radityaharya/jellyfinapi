# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RemoteSubtitleInfo(object):

    """Implementation of the 'RemoteSubtitleInfo' model.

    TODO: type model description here.

    Attributes:
        three_letter_iso_language_name (string): TODO: type description here.
        id (string): TODO: type description here.
        provider_name (string): TODO: type description here.
        name (string): TODO: type description here.
        format (string): TODO: type description here.
        author (string): TODO: type description here.
        comment (string): TODO: type description here.
        date_created (datetime): TODO: type description here.
        community_rating (float): TODO: type description here.
        download_count (int): TODO: type description here.
        is_hash_match (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "three_letter_iso_language_name": "ThreeLetterISOLanguageName",
        "id": "Id",
        "provider_name": "ProviderName",
        "name": "Name",
        "format": "Format",
        "author": "Author",
        "comment": "Comment",
        "date_created": "DateCreated",
        "community_rating": "CommunityRating",
        "download_count": "DownloadCount",
        "is_hash_match": "IsHashMatch",
    }

    _optionals = [
        "three_letter_iso_language_name",
        "id",
        "provider_name",
        "name",
        "format",
        "author",
        "comment",
        "date_created",
        "community_rating",
        "download_count",
        "is_hash_match",
    ]

    _nullables = [
        "three_letter_iso_language_name",
        "id",
        "provider_name",
        "name",
        "format",
        "author",
        "comment",
        "date_created",
        "community_rating",
        "download_count",
        "is_hash_match",
    ]

    def __init__(
        self,
        three_letter_iso_language_name=APIHelper.SKIP,
        id=APIHelper.SKIP,
        provider_name=APIHelper.SKIP,
        name=APIHelper.SKIP,
        format=APIHelper.SKIP,
        author=APIHelper.SKIP,
        comment=APIHelper.SKIP,
        date_created=APIHelper.SKIP,
        community_rating=APIHelper.SKIP,
        download_count=APIHelper.SKIP,
        is_hash_match=APIHelper.SKIP,
    ):
        """Constructor for the RemoteSubtitleInfo class"""

        # Initialize members of the class
        if three_letter_iso_language_name is not APIHelper.SKIP:
            self.three_letter_iso_language_name = three_letter_iso_language_name
        if id is not APIHelper.SKIP:
            self.id = id
        if provider_name is not APIHelper.SKIP:
            self.provider_name = provider_name
        if name is not APIHelper.SKIP:
            self.name = name
        if format is not APIHelper.SKIP:
            self.format = format
        if author is not APIHelper.SKIP:
            self.author = author
        if comment is not APIHelper.SKIP:
            self.comment = comment
        if date_created is not APIHelper.SKIP:
            self.date_created = (
                APIHelper.RFC3339DateTime(date_created) if date_created else None
            )
        if community_rating is not APIHelper.SKIP:
            self.community_rating = community_rating
        if download_count is not APIHelper.SKIP:
            self.download_count = download_count
        if is_hash_match is not APIHelper.SKIP:
            self.is_hash_match = is_hash_match

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

        three_letter_iso_language_name = (
            dictionary.get("ThreeLetterISOLanguageName")
            if "ThreeLetterISOLanguageName" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        provider_name = (
            dictionary.get("ProviderName")
            if "ProviderName" in dictionary.keys()
            else APIHelper.SKIP
        )
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        format = (
            dictionary.get("Format")
            if "Format" in dictionary.keys()
            else APIHelper.SKIP
        )
        author = (
            dictionary.get("Author")
            if "Author" in dictionary.keys()
            else APIHelper.SKIP
        )
        comment = (
            dictionary.get("Comment")
            if "Comment" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "DateCreated" in dictionary.keys():
            date_created = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("DateCreated")
                ).datetime
                if dictionary.get("DateCreated")
                else None
            )
        else:
            date_created = APIHelper.SKIP
        community_rating = (
            dictionary.get("CommunityRating")
            if "CommunityRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        download_count = (
            dictionary.get("DownloadCount")
            if "DownloadCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_hash_match = (
            dictionary.get("IsHashMatch")
            if "IsHashMatch" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            three_letter_iso_language_name,
            id,
            provider_name,
            name,
            format,
            author,
            comment,
            date_created,
            community_rating,
            download_count,
            is_hash_match,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        three_letter_iso_language_name = XmlUtilities.value_from_xml_element(
            root.find("ThreeLetterISOLanguageName"), str
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        provider_name = XmlUtilities.value_from_xml_element(
            root.find("ProviderName"), str
        )
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        format = XmlUtilities.value_from_xml_element(root.find("Format"), str)
        author = XmlUtilities.value_from_xml_element(root.find("Author"), str)
        comment = XmlUtilities.value_from_xml_element(root.find("Comment"), str)
        date_created = XmlUtilities.value_from_xml_element(
            root.find("DateCreated"), APIHelper.RFC3339DateTime
        )
        community_rating = XmlUtilities.value_from_xml_element(
            root.find("CommunityRating"), float
        )
        download_count = XmlUtilities.value_from_xml_element(
            root.find("DownloadCount"), int
        )
        is_hash_match = XmlUtilities.value_from_xml_element(
            root.find("IsHashMatch"), bool
        )

        return cls(
            three_letter_iso_language_name,
            id,
            provider_name,
            name,
            format,
            author,
            comment,
            date_created,
            community_rating,
            download_count,
            is_hash_match,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.three_letter_iso_language_name, "ThreeLetterISOLanguageName"
        )
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.provider_name, "ProviderName")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.format, "Format")
        XmlUtilities.add_as_subelement(root, self.author, "Author")
        XmlUtilities.add_as_subelement(root, self.comment, "Comment")
        XmlUtilities.add_as_subelement(root, self.date_created, "DateCreated")
        XmlUtilities.add_as_subelement(root, self.community_rating, "CommunityRating")
        XmlUtilities.add_as_subelement(root, self.download_count, "DownloadCount")
        XmlUtilities.add_as_subelement(root, self.is_hash_match, "IsHashMatch")
