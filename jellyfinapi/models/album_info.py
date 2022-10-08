# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.song_info import SongInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AlbumInfo(object):

    """Implementation of the 'AlbumInfo' model.

    TODO: type model description here.

    Attributes:
        name (string): Gets or sets the name.
        original_title (string): Gets or sets the original title.
        path (string): Gets or sets the path.
        metadata_language (string): Gets or sets the metadata language.
        metadata_country_code (string): Gets or sets the metadata country
            code.
        provider_ids (dict): Gets or sets the provider ids.
        year (int): Gets or sets the year.
        index_number (int): TODO: type description here.
        parent_index_number (int): TODO: type description here.
        premiere_date (datetime): TODO: type description here.
        is_automated (bool): TODO: type description here.
        album_artists (list of string): Gets or sets the album artist.
        artist_provider_ids (dict): Gets or sets the artist provider ids.
        song_infos (list of SongInfo): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "original_title": "OriginalTitle",
        "path": "Path",
        "metadata_language": "MetadataLanguage",
        "metadata_country_code": "MetadataCountryCode",
        "provider_ids": "ProviderIds",
        "year": "Year",
        "index_number": "IndexNumber",
        "parent_index_number": "ParentIndexNumber",
        "premiere_date": "PremiereDate",
        "is_automated": "IsAutomated",
        "album_artists": "AlbumArtists",
        "artist_provider_ids": "ArtistProviderIds",
        "song_infos": "SongInfos",
    }

    _optionals = [
        "name",
        "original_title",
        "path",
        "metadata_language",
        "metadata_country_code",
        "provider_ids",
        "year",
        "index_number",
        "parent_index_number",
        "premiere_date",
        "is_automated",
        "album_artists",
        "artist_provider_ids",
        "song_infos",
    ]

    _nullables = [
        "name",
        "original_title",
        "path",
        "metadata_language",
        "metadata_country_code",
        "provider_ids",
        "year",
        "index_number",
        "parent_index_number",
        "premiere_date",
        "artist_provider_ids",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        original_title=APIHelper.SKIP,
        path=APIHelper.SKIP,
        metadata_language=APIHelper.SKIP,
        metadata_country_code=APIHelper.SKIP,
        provider_ids=APIHelper.SKIP,
        year=APIHelper.SKIP,
        index_number=APIHelper.SKIP,
        parent_index_number=APIHelper.SKIP,
        premiere_date=APIHelper.SKIP,
        is_automated=APIHelper.SKIP,
        album_artists=APIHelper.SKIP,
        artist_provider_ids=APIHelper.SKIP,
        song_infos=APIHelper.SKIP,
    ):
        """Constructor for the AlbumInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if original_title is not APIHelper.SKIP:
            self.original_title = original_title
        if path is not APIHelper.SKIP:
            self.path = path
        if metadata_language is not APIHelper.SKIP:
            self.metadata_language = metadata_language
        if metadata_country_code is not APIHelper.SKIP:
            self.metadata_country_code = metadata_country_code
        if provider_ids is not APIHelper.SKIP:
            self.provider_ids = provider_ids
        if year is not APIHelper.SKIP:
            self.year = year
        if index_number is not APIHelper.SKIP:
            self.index_number = index_number
        if parent_index_number is not APIHelper.SKIP:
            self.parent_index_number = parent_index_number
        if premiere_date is not APIHelper.SKIP:
            self.premiere_date = (
                APIHelper.RFC3339DateTime(premiere_date) if premiere_date else None
            )
        if is_automated is not APIHelper.SKIP:
            self.is_automated = is_automated
        if album_artists is not APIHelper.SKIP:
            self.album_artists = album_artists
        if artist_provider_ids is not APIHelper.SKIP:
            self.artist_provider_ids = artist_provider_ids
        if song_infos is not APIHelper.SKIP:
            self.song_infos = song_infos

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
        original_title = (
            dictionary.get("OriginalTitle")
            if "OriginalTitle" in dictionary.keys()
            else APIHelper.SKIP
        )
        path = dictionary.get("Path") if "Path" in dictionary.keys() else APIHelper.SKIP
        metadata_language = (
            dictionary.get("MetadataLanguage")
            if "MetadataLanguage" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_country_code = (
            dictionary.get("MetadataCountryCode")
            if "MetadataCountryCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        provider_ids = (
            dictionary.get("ProviderIds")
            if "ProviderIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        year = dictionary.get("Year") if "Year" in dictionary.keys() else APIHelper.SKIP
        index_number = (
            dictionary.get("IndexNumber")
            if "IndexNumber" in dictionary.keys()
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
        is_automated = (
            dictionary.get("IsAutomated")
            if "IsAutomated" in dictionary.keys()
            else APIHelper.SKIP
        )
        album_artists = (
            dictionary.get("AlbumArtists")
            if dictionary.get("AlbumArtists")
            else APIHelper.SKIP
        )
        artist_provider_ids = (
            dictionary.get("ArtistProviderIds")
            if "ArtistProviderIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        song_infos = None
        if dictionary.get("SongInfos") is not None:
            song_infos = [
                SongInfo.from_dictionary(x) for x in dictionary.get("SongInfos")
            ]
        else:
            song_infos = APIHelper.SKIP
        # Return an object of this model
        return cls(
            name,
            original_title,
            path,
            metadata_language,
            metadata_country_code,
            provider_ids,
            year,
            index_number,
            parent_index_number,
            premiere_date,
            is_automated,
            album_artists,
            artist_provider_ids,
            song_infos,
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
        original_title = XmlUtilities.value_from_xml_element(
            root.find("OriginalTitle"), str
        )
        path = XmlUtilities.value_from_xml_element(root.find("Path"), str)
        metadata_language = XmlUtilities.value_from_xml_element(
            root.find("MetadataLanguage"), str
        )
        metadata_country_code = XmlUtilities.value_from_xml_element(
            root.find("MetadataCountryCode"), str
        )
        provider_ids = XmlUtilities.dict_from_xml_element(
            root.find("ProviderIds"), dict
        )

        year = XmlUtilities.value_from_xml_element(root.find("Year"), int)
        index_number = XmlUtilities.value_from_xml_element(
            root.find("IndexNumber"), int
        )
        parent_index_number = XmlUtilities.value_from_xml_element(
            root.find("ParentIndexNumber"), int
        )
        premiere_date = XmlUtilities.value_from_xml_element(
            root.find("PremiereDate"), APIHelper.RFC3339DateTime
        )
        is_automated = XmlUtilities.value_from_xml_element(
            root.find("IsAutomated"), bool
        )
        album_artists = XmlUtilities.list_from_xml_element(root, "AlbumArtists", str)
        artist_provider_ids = XmlUtilities.dict_from_xml_element(
            root.find("ArtistProviderIds"), dict
        )

        song_infos = XmlUtilities.list_from_xml_element(root, "SongInfo", SongInfo)

        return cls(
            name,
            original_title,
            path,
            metadata_language,
            metadata_country_code,
            provider_ids,
            year,
            index_number,
            parent_index_number,
            premiere_date,
            is_automated,
            album_artists,
            artist_provider_ids,
            song_infos,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.original_title, "OriginalTitle")
        XmlUtilities.add_as_subelement(root, self.path, "Path")
        XmlUtilities.add_as_subelement(root, self.metadata_language, "MetadataLanguage")
        XmlUtilities.add_as_subelement(
            root, self.metadata_country_code, "MetadataCountryCode"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.provider_ids, dictionary_name="ProviderIds"
        )
        XmlUtilities.add_as_subelement(root, self.year, "Year")
        XmlUtilities.add_as_subelement(root, self.index_number, "IndexNumber")
        XmlUtilities.add_as_subelement(
            root, self.parent_index_number, "ParentIndexNumber"
        )
        XmlUtilities.add_as_subelement(root, self.premiere_date, "PremiereDate")
        XmlUtilities.add_as_subelement(root, self.is_automated, "IsAutomated")
        XmlUtilities.add_list_as_subelement(root, self.album_artists, "AlbumArtists")
        XmlUtilities.add_dict_as_subelement(
            root, self.artist_provider_ids, dictionary_name="ArtistProviderIds"
        )
        XmlUtilities.add_list_as_subelement(root, self.song_infos, "SongInfo")
