# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.name_value_pair import NameValuePair
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ListingsProviderInfo(object):

    """Implementation of the 'ListingsProviderInfo' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        mtype (string): TODO: type description here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        listings_id (string): TODO: type description here.
        zip_code (string): TODO: type description here.
        country (string): TODO: type description here.
        path (string): TODO: type description here.
        enabled_tuners (list of string): TODO: type description here.
        enable_all_tuners (bool): TODO: type description here.
        news_categories (list of string): TODO: type description here.
        sports_categories (list of string): TODO: type description here.
        kids_categories (list of string): TODO: type description here.
        movie_categories (list of string): TODO: type description here.
        channel_mappings (list of NameValuePair): TODO: type description
            here.
        movie_prefix (string): TODO: type description here.
        preferred_language (string): TODO: type description here.
        user_agent (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "mtype": "Type",
        "username": "Username",
        "password": "Password",
        "listings_id": "ListingsId",
        "zip_code": "ZipCode",
        "country": "Country",
        "path": "Path",
        "enabled_tuners": "EnabledTuners",
        "enable_all_tuners": "EnableAllTuners",
        "news_categories": "NewsCategories",
        "sports_categories": "SportsCategories",
        "kids_categories": "KidsCategories",
        "movie_categories": "MovieCategories",
        "channel_mappings": "ChannelMappings",
        "movie_prefix": "MoviePrefix",
        "preferred_language": "PreferredLanguage",
        "user_agent": "UserAgent",
    }

    _optionals = [
        "id",
        "mtype",
        "username",
        "password",
        "listings_id",
        "zip_code",
        "country",
        "path",
        "enabled_tuners",
        "enable_all_tuners",
        "news_categories",
        "sports_categories",
        "kids_categories",
        "movie_categories",
        "channel_mappings",
        "movie_prefix",
        "preferred_language",
        "user_agent",
    ]

    _nullables = [
        "id",
        "mtype",
        "username",
        "password",
        "listings_id",
        "zip_code",
        "country",
        "path",
        "enabled_tuners",
        "news_categories",
        "sports_categories",
        "kids_categories",
        "movie_categories",
        "channel_mappings",
        "movie_prefix",
        "preferred_language",
        "user_agent",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        username=APIHelper.SKIP,
        password=APIHelper.SKIP,
        listings_id=APIHelper.SKIP,
        zip_code=APIHelper.SKIP,
        country=APIHelper.SKIP,
        path=APIHelper.SKIP,
        enabled_tuners=APIHelper.SKIP,
        enable_all_tuners=APIHelper.SKIP,
        news_categories=APIHelper.SKIP,
        sports_categories=APIHelper.SKIP,
        kids_categories=APIHelper.SKIP,
        movie_categories=APIHelper.SKIP,
        channel_mappings=APIHelper.SKIP,
        movie_prefix=APIHelper.SKIP,
        preferred_language=APIHelper.SKIP,
        user_agent=APIHelper.SKIP,
    ):
        """Constructor for the ListingsProviderInfo class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if username is not APIHelper.SKIP:
            self.username = username
        if password is not APIHelper.SKIP:
            self.password = password
        if listings_id is not APIHelper.SKIP:
            self.listings_id = listings_id
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code
        if country is not APIHelper.SKIP:
            self.country = country
        if path is not APIHelper.SKIP:
            self.path = path
        if enabled_tuners is not APIHelper.SKIP:
            self.enabled_tuners = enabled_tuners
        if enable_all_tuners is not APIHelper.SKIP:
            self.enable_all_tuners = enable_all_tuners
        if news_categories is not APIHelper.SKIP:
            self.news_categories = news_categories
        if sports_categories is not APIHelper.SKIP:
            self.sports_categories = sports_categories
        if kids_categories is not APIHelper.SKIP:
            self.kids_categories = kids_categories
        if movie_categories is not APIHelper.SKIP:
            self.movie_categories = movie_categories
        if channel_mappings is not APIHelper.SKIP:
            self.channel_mappings = channel_mappings
        if movie_prefix is not APIHelper.SKIP:
            self.movie_prefix = movie_prefix
        if preferred_language is not APIHelper.SKIP:
            self.preferred_language = preferred_language
        if user_agent is not APIHelper.SKIP:
            self.user_agent = user_agent

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

        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        username = (
            dictionary.get("Username")
            if "Username" in dictionary.keys()
            else APIHelper.SKIP
        )
        password = (
            dictionary.get("Password")
            if "Password" in dictionary.keys()
            else APIHelper.SKIP
        )
        listings_id = (
            dictionary.get("ListingsId")
            if "ListingsId" in dictionary.keys()
            else APIHelper.SKIP
        )
        zip_code = (
            dictionary.get("ZipCode")
            if "ZipCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        country = (
            dictionary.get("Country")
            if "Country" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        enabled_tuners = (
            dictionary.get("EnabledTuners")
            if "EnabledTuners" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_all_tuners = (
            dictionary.get("EnableAllTuners")
            if "EnableAllTuners" in dictionary.keys()
            else APIHelper.SKIP
        )
        news_categories = (
            dictionary.get("NewsCategories")
            if "NewsCategories" in dictionary.keys()
            else APIHelper.SKIP
        )
        sports_categories = (
            dictionary.get("SportsCategories")
            if "SportsCategories" in dictionary.keys()
            else APIHelper.SKIP
        )
        kids_categories = (
            dictionary.get("KidsCategories")
            if "KidsCategories" in dictionary.keys()
            else APIHelper.SKIP
        )
        movie_categories = (
            dictionary.get("MovieCategories")
            if "MovieCategories" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ChannelMappings" in dictionary.keys():
            channel_mappings = (
                [
                    NameValuePair.from_dictionary(x)
                    for x in dictionary.get("ChannelMappings")
                ]
                if dictionary.get("ChannelMappings")
                else None
            )
        else:
            channel_mappings = APIHelper.SKIP
        movie_prefix = (
            dictionary.get("MoviePrefix")
            if "MoviePrefix" in dictionary.keys()
            else APIHelper.SKIP
        )
        preferred_language = (
            dictionary.get("PreferredLanguage")
            if "PreferredLanguage" in dictionary.keys()
            else APIHelper.SKIP
        )
        user_agent = (
            dictionary.get("UserAgent")
            if "UserAgent" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            mtype,
            username,
            password,
            listings_id,
            zip_code,
            country,
            path,
            enabled_tuners,
            enable_all_tuners,
            news_categories,
            sports_categories,
            kids_categories,
            movie_categories,
            channel_mappings,
            movie_prefix,
            preferred_language,
            user_agent,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        username = XmlUtilities.value_from_xml_element(root.find("Username"), str)
        password = XmlUtilities.value_from_xml_element(root.find("Password"), str)
        listings_id = XmlUtilities.value_from_xml_element(root.find("ListingsId"), str)
        zip_code = XmlUtilities.value_from_xml_element(root.find("ZipCode"), str)
        country = XmlUtilities.value_from_xml_element(root.find("Country"), str)
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        enabled_tuners = XmlUtilities.list_from_xml_element(root, "EnabledTuners", str)
        enable_all_tuners = XmlUtilities.value_from_xml_element(
            root.find("EnableAllTuners"), bool
        )
        news_categories = XmlUtilities.list_from_xml_element(
            root, "NewsCategories", str
        )
        sports_categories = XmlUtilities.list_from_xml_element(
            root, "SportsCategories", str
        )
        kids_categories = XmlUtilities.list_from_xml_element(
            root, "KidsCategories", str
        )
        movie_categories = XmlUtilities.list_from_xml_element(
            root, "MovieCategories", str
        )
        channel_mappings = XmlUtilities.list_from_xml_element(
            root, "NameValuePair", NameValuePair
        )
        movie_prefix = XmlUtilities.value_from_xml_element(
            root.find("MoviePrefix"), str
        )
        preferred_language = XmlUtilities.value_from_xml_element(
            root.find("PreferredLanguage"), str
        )
        user_agent = XmlUtilities.value_from_xml_element(root.find("UserAgent"), str)

        return cls(
            id,
            mtype,
            username,
            password,
            listings_id,
            zip_code,
            country,
            path,
            enabled_tuners,
            enable_all_tuners,
            news_categories,
            sports_categories,
            kids_categories,
            movie_categories,
            channel_mappings,
            movie_prefix,
            preferred_language,
            user_agent,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.username, "Username")
        XmlUtilities.add_as_subelement(root, self.password, "Password")
        XmlUtilities.add_as_subelement(root, self.listings_id, "ListingsId")
        XmlUtilities.add_as_subelement(root, self.zip_code, "ZipCode")
        XmlUtilities.add_as_subelement(root, self.country, "Country")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_list_as_subelement(root, self.enabled_tuners, "EnabledTuners")
        XmlUtilities.add_as_subelement(root, self.enable_all_tuners, "EnableAllTuners")
        XmlUtilities.add_list_as_subelement(
            root, self.news_categories, "NewsCategories"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.sports_categories, "SportsCategories"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.kids_categories, "KidsCategories"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.movie_categories, "MovieCategories"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.channel_mappings, "NameValuePair"
        )
        XmlUtilities.add_as_subelement(root, self.movie_prefix, "MoviePrefix")
        XmlUtilities.add_as_subelement(
            root, self.preferred_language, "PreferredLanguage"
        )
        XmlUtilities.add_as_subelement(root, self.user_agent, "UserAgent")
