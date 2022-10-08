# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RemoteImageInfo(object):

    """Implementation of the 'RemoteImageInfo' model.

    Class RemoteImageInfo.

    Attributes:
        provider_name (string): Gets or sets the name of the provider.
        url (string): Gets or sets the URL.
        thumbnail_url (string): Gets or sets a url used for previewing a
            smaller version.
        height (int): Gets or sets the height.
        width (int): Gets or sets the width.
        community_rating (float): Gets or sets the community rating.
        vote_count (int): Gets or sets the vote count.
        language (string): Gets or sets the language.
        mtype (ImageTypeEnum): Gets or sets the type.
        rating_type (RatingTypeEnum): Gets or sets the type of the rating.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "provider_name": "ProviderName",
        "url": "Url",
        "thumbnail_url": "ThumbnailUrl",
        "height": "Height",
        "width": "Width",
        "community_rating": "CommunityRating",
        "vote_count": "VoteCount",
        "language": "Language",
        "mtype": "Type",
        "rating_type": "RatingType",
    }

    _optionals = [
        "provider_name",
        "url",
        "thumbnail_url",
        "height",
        "width",
        "community_rating",
        "vote_count",
        "language",
        "mtype",
        "rating_type",
    ]

    _nullables = [
        "provider_name",
        "url",
        "thumbnail_url",
        "height",
        "width",
        "community_rating",
        "vote_count",
        "language",
    ]

    def __init__(
        self,
        provider_name=APIHelper.SKIP,
        url=APIHelper.SKIP,
        thumbnail_url=APIHelper.SKIP,
        height=APIHelper.SKIP,
        width=APIHelper.SKIP,
        community_rating=APIHelper.SKIP,
        vote_count=APIHelper.SKIP,
        language=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        rating_type=APIHelper.SKIP,
    ):
        """Constructor for the RemoteImageInfo class"""

        # Initialize members of the class
        if provider_name is not APIHelper.SKIP:
            self.provider_name = provider_name
        if url is not APIHelper.SKIP:
            self.url = url
        if thumbnail_url is not APIHelper.SKIP:
            self.thumbnail_url = thumbnail_url
        if height is not APIHelper.SKIP:
            self.height = height
        if width is not APIHelper.SKIP:
            self.width = width
        if community_rating is not APIHelper.SKIP:
            self.community_rating = community_rating
        if vote_count is not APIHelper.SKIP:
            self.vote_count = vote_count
        if language is not APIHelper.SKIP:
            self.language = language
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if rating_type is not APIHelper.SKIP:
            self.rating_type = rating_type

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

        provider_name = (
            dictionary.get("ProviderName")
            if "ProviderName" in dictionary.keys()
            else APIHelper.SKIP
        )
        url = dictionary.get("Url") if "Url" in dictionary.keys() else APIHelper.SKIP
        thumbnail_url = (
            dictionary.get("ThumbnailUrl")
            if "ThumbnailUrl" in dictionary.keys()
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
        community_rating = (
            dictionary.get("CommunityRating")
            if "CommunityRating" in dictionary.keys()
            else APIHelper.SKIP
        )
        vote_count = (
            dictionary.get("VoteCount")
            if "VoteCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        language = (
            dictionary.get("Language")
            if "Language" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        rating_type = (
            dictionary.get("RatingType")
            if dictionary.get("RatingType")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            provider_name,
            url,
            thumbnail_url,
            height,
            width,
            community_rating,
            vote_count,
            language,
            mtype,
            rating_type,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        provider_name = XmlUtilities.value_from_xml_element(
            root.find("ProviderName"), str
        )
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)
        thumbnail_url = XmlUtilities.value_from_xml_element(
            root.find("ThumbnailUrl"), str
        )
        height = XmlUtilities.value_from_xml_element(root.find("Height"), int)
        width = XmlUtilities.value_from_xml_element(root.find("Width"), int)
        community_rating = XmlUtilities.value_from_xml_element(
            root.find("CommunityRating"), float
        )
        vote_count = XmlUtilities.value_from_xml_element(root.find("VoteCount"), int)
        language = XmlUtilities.value_from_xml_element(root.find("Language"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        rating_type = XmlUtilities.value_from_xml_element(root.find("RatingType"), str)

        return cls(
            provider_name,
            url,
            thumbnail_url,
            height,
            width,
            community_rating,
            vote_count,
            language,
            mtype,
            rating_type,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.provider_name, "ProviderName")
        XmlUtilities.add_as_subelement(root, self.url, "Url")
        XmlUtilities.add_as_subelement(root, self.thumbnail_url, "ThumbnailUrl")
        XmlUtilities.add_as_subelement(root, self.height, "Height")
        XmlUtilities.add_as_subelement(root, self.width, "Width")
        XmlUtilities.add_as_subelement(root, self.community_rating, "CommunityRating")
        XmlUtilities.add_as_subelement(root, self.vote_count, "VoteCount")
        XmlUtilities.add_as_subelement(root, self.language, "Language")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.rating_type, "RatingType")
