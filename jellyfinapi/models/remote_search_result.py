# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class RemoteSearchResult(object):

    """Implementation of the 'RemoteSearchResult' model.

    TODO: type model description here.

    Attributes:
        name (string): Gets or sets the name.
        provider_ids (dict): Gets or sets the provider ids.
        production_year (int): Gets or sets the year.
        index_number (int): TODO: type description here.
        index_number_end (int): TODO: type description here.
        parent_index_number (int): TODO: type description here.
        premiere_date (datetime): TODO: type description here.
        image_url (string): TODO: type description here.
        search_provider_name (string): TODO: type description here.
        overview (string): TODO: type description here.
        album_artist (RemoteSearchResult): TODO: type description here.
        artists (list of RemoteSearchResult): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "provider_ids": "ProviderIds",
        "production_year": "ProductionYear",
        "index_number": "IndexNumber",
        "index_number_end": "IndexNumberEnd",
        "parent_index_number": "ParentIndexNumber",
        "premiere_date": "PremiereDate",
        "image_url": "ImageUrl",
        "search_provider_name": "SearchProviderName",
        "overview": "Overview",
        "album_artist": "AlbumArtist",
        "artists": "Artists",
    }

    _optionals = [
        "name",
        "provider_ids",
        "production_year",
        "index_number",
        "index_number_end",
        "parent_index_number",
        "premiere_date",
        "image_url",
        "search_provider_name",
        "overview",
        "album_artist",
        "artists",
    ]

    _nullables = [
        "name",
        "provider_ids",
        "production_year",
        "index_number",
        "index_number_end",
        "parent_index_number",
        "premiere_date",
        "image_url",
        "search_provider_name",
        "overview",
        "album_artist",
        "artists",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        provider_ids=APIHelper.SKIP,
        production_year=APIHelper.SKIP,
        index_number=APIHelper.SKIP,
        index_number_end=APIHelper.SKIP,
        parent_index_number=APIHelper.SKIP,
        premiere_date=APIHelper.SKIP,
        image_url=APIHelper.SKIP,
        search_provider_name=APIHelper.SKIP,
        overview=APIHelper.SKIP,
        album_artist=APIHelper.SKIP,
        artists=APIHelper.SKIP,
    ):
        """Constructor for the RemoteSearchResult class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if provider_ids is not APIHelper.SKIP:
            self.provider_ids = provider_ids
        if production_year is not APIHelper.SKIP:
            self.production_year = production_year
        if index_number is not APIHelper.SKIP:
            self.index_number = index_number
        if index_number_end is not APIHelper.SKIP:
            self.index_number_end = index_number_end
        if parent_index_number is not APIHelper.SKIP:
            self.parent_index_number = parent_index_number
        if premiere_date is not APIHelper.SKIP:
            self.premiere_date = (
                APIHelper.RFC3339DateTime(premiere_date) if premiere_date else None
            )
        if image_url is not APIHelper.SKIP:
            self.image_url = image_url
        if search_provider_name is not APIHelper.SKIP:
            self.search_provider_name = search_provider_name
        if overview is not APIHelper.SKIP:
            self.overview = overview
        if album_artist is not APIHelper.SKIP:
            self.album_artist = album_artist
        if artists is not APIHelper.SKIP:
            self.artists = artists

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
        provider_ids = (
            dictionary.get("ProviderIds")
            if "ProviderIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        production_year = (
            dictionary.get("ProductionYear")
            if "ProductionYear" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_number = (
            dictionary.get("IndexNumber")
            if "IndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_number_end = (
            dictionary.get("IndexNumberEnd")
            if "IndexNumberEnd" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_index_number = (
            dictionary.get("ParentIndexNumber")
            if "ParentIndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "PremiereDate" in dictionary.keys():
            premiere_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("PremiereDate")
                ).datetime
                if dictionary.get("PremiereDate")
                else None
            )
        else:
            premiere_date = APIHelper.SKIP
        image_url = (
            dictionary.get("ImageUrl")
            if "ImageUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        search_provider_name = (
            dictionary.get("SearchProviderName")
            if "SearchProviderName" in dictionary.keys()
            else APIHelper.SKIP
        )
        overview = (
            dictionary.get("Overview")
            if "Overview" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "AlbumArtist" in dictionary.keys():
            album_artist = (
                RemoteSearchResult.from_dictionary(dictionary.get("AlbumArtist"))
                if dictionary.get("AlbumArtist")
                else None
            )
        else:
            album_artist = APIHelper.SKIP
        if "Artists" in dictionary.keys():
            artists = (
                [
                    RemoteSearchResult.from_dictionary(x)
                    for x in dictionary.get("Artists")
                ]
                if dictionary.get("Artists")
                else None
            )
        else:
            artists = APIHelper.SKIP
        # Return an object of this model
        return cls(
            name,
            provider_ids,
            production_year,
            index_number,
            index_number_end,
            parent_index_number,
            premiere_date,
            image_url,
            search_provider_name,
            overview,
            album_artist,
            artists,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        provider_ids = XmlUtilities.dict_from_xml_element(
            root.find("ProviderIds"), dict
        )

        production_year = XmlUtilities.value_from_xml_element(
            root.find("ProductionYear"), int
        )
        index_number = XmlUtilities.value_from_xml_element(
            root.find("IndexNumber"), int
        )
        index_number_end = XmlUtilities.value_from_xml_element(
            root.find("IndexNumberEnd"), int
        )
        parent_index_number = XmlUtilities.value_from_xml_element(
            root.find("ParentIndexNumber"), int
        )
        premiere_date = XmlUtilities.value_from_xml_element(
            root.find("PremiereDate"), APIHelper.RFC3339DateTime
        )
        image_url = XmlUtilities.value_from_xml_element(root.find("ImageUrl"), str)
        search_provider_name = XmlUtilities.value_from_xml_element(
            root.find("SearchProviderName"), str
        )
        overview = XmlUtilities.value_from_xml_element(root.find("Overview"), str)
        album_artist = XmlUtilities.value_from_xml_element(
            root.find("RemoteSearchResult"), RemoteSearchResult
        )
        artists = XmlUtilities.list_from_xml_element(
            root, "RemoteSearchResult", RemoteSearchResult
        )

        return cls(
            name,
            provider_ids,
            production_year,
            index_number,
            index_number_end,
            parent_index_number,
            premiere_date,
            image_url,
            search_provider_name,
            overview,
            album_artist,
            artists,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_dict_as_subelement(
            root, self.provider_ids, dictionary_name="ProviderIds"
        )
        XmlUtilities.add_as_subelement(root, self.production_year, "ProductionYear")
        XmlUtilities.add_as_subelement(root, self.index_number, "IndexNumber")
        XmlUtilities.add_as_subelement(root, self.index_number_end, "IndexNumberEnd")
        XmlUtilities.add_as_subelement(
            root, self.parent_index_number, "ParentIndexNumber"
        )
        XmlUtilities.add_as_subelement(root, self.premiere_date, "PremiereDate")
        XmlUtilities.add_as_subelement(root, self.image_url, "ImageUrl")
        XmlUtilities.add_as_subelement(
            root, self.search_provider_name, "SearchProviderName"
        )
        XmlUtilities.add_as_subelement(root, self.overview, "Overview")
        XmlUtilities.add_as_subelement(root, self.album_artist, "RemoteSearchResult")
        XmlUtilities.add_list_as_subelement(root, self.artists, "RemoteSearchResult")
