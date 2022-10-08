# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SearchHint(object):

    """Implementation of the 'SearchHint' model.

    Class SearchHintResult.

    Attributes:
        item_id (uuid|string): Gets or sets the item id.
        id (uuid|string): TODO: type description here.
        name (string): Gets or sets the name.
        matched_term (string): Gets or sets the matched term.
        index_number (int): Gets or sets the index number.
        production_year (int): Gets or sets the production year.
        parent_index_number (int): Gets or sets the parent index number.
        primary_image_tag (string): Gets or sets the image tag.
        thumb_image_tag (string): Gets or sets the thumb image tag.
        thumb_image_item_id (string): Gets or sets the thumb image item
            identifier.
        backdrop_image_tag (string): Gets or sets the backdrop image tag.
        backdrop_image_item_id (string): Gets or sets the backdrop image item
            identifier.
        mtype (string): Gets or sets the type.
        is_folder (bool): TODO: type description here.
        run_time_ticks (long|int): Gets or sets the run time ticks.
        media_type (string): Gets or sets the type of the media.
        start_date (datetime): TODO: type description here.
        end_date (datetime): TODO: type description here.
        series (string): Gets or sets the series.
        status (string): TODO: type description here.
        album (string): Gets or sets the album.
        album_id (uuid|string): TODO: type description here.
        album_artist (string): Gets or sets the album artist.
        artists (list of string): Gets or sets the artists.
        song_count (int): Gets or sets the song count.
        episode_count (int): Gets or sets the episode count.
        channel_id (uuid|string): Gets or sets the channel identifier.
        channel_name (string): Gets or sets the name of the channel.
        primary_image_aspect_ratio (float): Gets or sets the primary image
            aspect ratio.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "item_id": "ItemId",
        "id": "Id",
        "name": "Name",
        "matched_term": "MatchedTerm",
        "index_number": "IndexNumber",
        "production_year": "ProductionYear",
        "parent_index_number": "ParentIndexNumber",
        "primary_image_tag": "PrimaryImageTag",
        "thumb_image_tag": "ThumbImageTag",
        "thumb_image_item_id": "ThumbImageItemId",
        "backdrop_image_tag": "BackdropImageTag",
        "backdrop_image_item_id": "BackdropImageItemId",
        "mtype": "Type",
        "is_folder": "IsFolder",
        "run_time_ticks": "RunTimeTicks",
        "media_type": "MediaType",
        "start_date": "StartDate",
        "end_date": "EndDate",
        "series": "Series",
        "status": "Status",
        "album": "Album",
        "album_id": "AlbumId",
        "album_artist": "AlbumArtist",
        "artists": "Artists",
        "song_count": "SongCount",
        "episode_count": "EpisodeCount",
        "channel_id": "ChannelId",
        "channel_name": "ChannelName",
        "primary_image_aspect_ratio": "PrimaryImageAspectRatio",
    }

    _optionals = [
        "item_id",
        "id",
        "name",
        "matched_term",
        "index_number",
        "production_year",
        "parent_index_number",
        "primary_image_tag",
        "thumb_image_tag",
        "thumb_image_item_id",
        "backdrop_image_tag",
        "backdrop_image_item_id",
        "mtype",
        "is_folder",
        "run_time_ticks",
        "media_type",
        "start_date",
        "end_date",
        "series",
        "status",
        "album",
        "album_id",
        "album_artist",
        "artists",
        "song_count",
        "episode_count",
        "channel_id",
        "channel_name",
        "primary_image_aspect_ratio",
    ]

    _nullables = [
        "name",
        "matched_term",
        "index_number",
        "production_year",
        "parent_index_number",
        "primary_image_tag",
        "thumb_image_tag",
        "thumb_image_item_id",
        "backdrop_image_tag",
        "backdrop_image_item_id",
        "mtype",
        "is_folder",
        "run_time_ticks",
        "media_type",
        "start_date",
        "end_date",
        "series",
        "status",
        "album",
        "album_artist",
        "artists",
        "song_count",
        "episode_count",
        "channel_name",
        "primary_image_aspect_ratio",
    ]

    def __init__(
        self,
        item_id=APIHelper.SKIP,
        id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        matched_term=APIHelper.SKIP,
        index_number=APIHelper.SKIP,
        production_year=APIHelper.SKIP,
        parent_index_number=APIHelper.SKIP,
        primary_image_tag=APIHelper.SKIP,
        thumb_image_tag=APIHelper.SKIP,
        thumb_image_item_id=APIHelper.SKIP,
        backdrop_image_tag=APIHelper.SKIP,
        backdrop_image_item_id=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        is_folder=APIHelper.SKIP,
        run_time_ticks=APIHelper.SKIP,
        media_type=APIHelper.SKIP,
        start_date=APIHelper.SKIP,
        end_date=APIHelper.SKIP,
        series=APIHelper.SKIP,
        status=APIHelper.SKIP,
        album=APIHelper.SKIP,
        album_id=APIHelper.SKIP,
        album_artist=APIHelper.SKIP,
        artists=APIHelper.SKIP,
        song_count=APIHelper.SKIP,
        episode_count=APIHelper.SKIP,
        channel_id=APIHelper.SKIP,
        channel_name=APIHelper.SKIP,
        primary_image_aspect_ratio=APIHelper.SKIP,
    ):
        """Constructor for the SearchHint class"""

        # Initialize members of the class
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if matched_term is not APIHelper.SKIP:
            self.matched_term = matched_term
        if index_number is not APIHelper.SKIP:
            self.index_number = index_number
        if production_year is not APIHelper.SKIP:
            self.production_year = production_year
        if parent_index_number is not APIHelper.SKIP:
            self.parent_index_number = parent_index_number
        if primary_image_tag is not APIHelper.SKIP:
            self.primary_image_tag = primary_image_tag
        if thumb_image_tag is not APIHelper.SKIP:
            self.thumb_image_tag = thumb_image_tag
        if thumb_image_item_id is not APIHelper.SKIP:
            self.thumb_image_item_id = thumb_image_item_id
        if backdrop_image_tag is not APIHelper.SKIP:
            self.backdrop_image_tag = backdrop_image_tag
        if backdrop_image_item_id is not APIHelper.SKIP:
            self.backdrop_image_item_id = backdrop_image_item_id
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if is_folder is not APIHelper.SKIP:
            self.is_folder = is_folder
        if run_time_ticks is not APIHelper.SKIP:
            self.run_time_ticks = run_time_ticks
        if media_type is not APIHelper.SKIP:
            self.media_type = media_type
        if start_date is not APIHelper.SKIP:
            self.start_date = (
                APIHelper.RFC3339DateTime(start_date) if start_date else None
            )
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.RFC3339DateTime(end_date) if end_date else None
        if series is not APIHelper.SKIP:
            self.series = series
        if status is not APIHelper.SKIP:
            self.status = status
        if album is not APIHelper.SKIP:
            self.album = album
        if album_id is not APIHelper.SKIP:
            self.album_id = album_id
        if album_artist is not APIHelper.SKIP:
            self.album_artist = album_artist
        if artists is not APIHelper.SKIP:
            self.artists = artists
        if song_count is not APIHelper.SKIP:
            self.song_count = song_count
        if episode_count is not APIHelper.SKIP:
            self.episode_count = episode_count
        if channel_id is not APIHelper.SKIP:
            self.channel_id = channel_id
        if channel_name is not APIHelper.SKIP:
            self.channel_name = channel_name
        if primary_image_aspect_ratio is not APIHelper.SKIP:
            self.primary_image_aspect_ratio = primary_image_aspect_ratio

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

        item_id = (
            dictionary.get("ItemId") if dictionary.get("ItemId") else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        matched_term = (
            dictionary.get("MatchedTerm")
            if "MatchedTerm" in dictionary.keys()
            else APIHelper.SKIP
        )
        index_number = (
            dictionary.get("IndexNumber")
            if "IndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        production_year = (
            dictionary.get("ProductionYear")
            if "ProductionYear" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_index_number = (
            dictionary.get("ParentIndexNumber")
            if "ParentIndexNumber" in dictionary.keys()
            else APIHelper.SKIP
        )
        primary_image_tag = (
            dictionary.get("PrimaryImageTag")
            if "PrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        thumb_image_tag = (
            dictionary.get("ThumbImageTag")
            if "ThumbImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        thumb_image_item_id = (
            dictionary.get("ThumbImageItemId")
            if "ThumbImageItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        backdrop_image_tag = (
            dictionary.get("BackdropImageTag")
            if "BackdropImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        backdrop_image_item_id = (
            dictionary.get("BackdropImageItemId")
            if "BackdropImageItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        is_folder = (
            dictionary.get("IsFolder")
            if "IsFolder" in dictionary.keys()
            else APIHelper.SKIP
        )
        run_time_ticks = (
            dictionary.get("RunTimeTicks")
            if "RunTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        media_type = (
            dictionary.get("MediaType")
            if "MediaType" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "StartDate" in dictionary.keys():
            start_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("StartDate")
                ).datetime
                if dictionary.get("StartDate")
                else None
            )
        else:
            start_date = APIHelper.SKIP
        if "EndDate" in dictionary.keys():
            end_date = (
                APIHelper.RFC3339DateTime.from_value(dictionary.get("EndDate")).datetime
                if dictionary.get("EndDate")
                else None
            )
        else:
            end_date = APIHelper.SKIP
        series = (
            dictionary.get("Series")
            if "Series" in dictionary.keys()
            else APIHelper.SKIP
        )
        status = (
            dictionary.get("Status")
            if "Status" in dictionary.keys()
            else APIHelper.SKIP
        )
        album = (
            dictionary.get("Album") if "Album" in dictionary.keys() else APIHelper.SKIP
        )
        album_id = (
            dictionary.get("AlbumId") if dictionary.get("AlbumId") else APIHelper.SKIP
        )
        album_artist = (
            dictionary.get("AlbumArtist")
            if "AlbumArtist" in dictionary.keys()
            else APIHelper.SKIP
        )
        artists = (
            dictionary.get("Artists")
            if "Artists" in dictionary.keys()
            else APIHelper.SKIP
        )
        song_count = (
            dictionary.get("SongCount")
            if "SongCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        episode_count = (
            dictionary.get("EpisodeCount")
            if "EpisodeCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_id = (
            dictionary.get("ChannelId")
            if dictionary.get("ChannelId")
            else APIHelper.SKIP
        )
        channel_name = (
            dictionary.get("ChannelName")
            if "ChannelName" in dictionary.keys()
            else APIHelper.SKIP
        )
        primary_image_aspect_ratio = (
            dictionary.get("PrimaryImageAspectRatio")
            if "PrimaryImageAspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            item_id,
            id,
            name,
            matched_term,
            index_number,
            production_year,
            parent_index_number,
            primary_image_tag,
            thumb_image_tag,
            thumb_image_item_id,
            backdrop_image_tag,
            backdrop_image_item_id,
            mtype,
            is_folder,
            run_time_ticks,
            media_type,
            start_date,
            end_date,
            series,
            status,
            album,
            album_id,
            album_artist,
            artists,
            song_count,
            episode_count,
            channel_id,
            channel_name,
            primary_image_aspect_ratio,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        matched_term = XmlUtilities.value_from_xml_element(
            root.find("MatchedTerm"), str
        )
        index_number = XmlUtilities.value_from_xml_element(
            root.find("IndexNumber"), int
        )
        production_year = XmlUtilities.value_from_xml_element(
            root.find("ProductionYear"), int
        )
        parent_index_number = XmlUtilities.value_from_xml_element(
            root.find("ParentIndexNumber"), int
        )
        primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageTag"), str
        )
        thumb_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ThumbImageTag"), str
        )
        thumb_image_item_id = XmlUtilities.value_from_xml_element(
            root.find("ThumbImageItemId"), str
        )
        backdrop_image_tag = XmlUtilities.value_from_xml_element(
            root.find("BackdropImageTag"), str
        )
        backdrop_image_item_id = XmlUtilities.value_from_xml_element(
            root.find("BackdropImageItemId"), str
        )
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        is_folder = XmlUtilities.value_from_xml_element(root.find("IsFolder"), bool)
        run_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("RunTimeTicks"), int
        )
        media_type = XmlUtilities.value_from_xml_element(root.find("MediaType"), str)
        start_date = XmlUtilities.value_from_xml_element(
            root.find("StartDate"), APIHelper.RFC3339DateTime
        )
        end_date = XmlUtilities.value_from_xml_element(
            root.find("EndDate"), APIHelper.RFC3339DateTime
        )
        series = XmlUtilities.value_from_xml_element(root.find("Series"), str)
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)
        album = XmlUtilities.value_from_xml_element(root.find("Album"), str)
        album_id = XmlUtilities.value_from_xml_element(root.find("AlbumId"), str)
        album_artist = XmlUtilities.value_from_xml_element(
            root.find("AlbumArtist"), str
        )
        artists = XmlUtilities.list_from_xml_element(root, "Artists", str)
        song_count = XmlUtilities.value_from_xml_element(root.find("SongCount"), int)
        episode_count = XmlUtilities.value_from_xml_element(
            root.find("EpisodeCount"), int
        )
        channel_id = XmlUtilities.value_from_xml_element(root.find("ChannelId"), str)
        channel_name = XmlUtilities.value_from_xml_element(
            root.find("ChannelName"), str
        )
        primary_image_aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageAspectRatio"), float
        )

        return cls(
            item_id,
            id,
            name,
            matched_term,
            index_number,
            production_year,
            parent_index_number,
            primary_image_tag,
            thumb_image_tag,
            thumb_image_item_id,
            backdrop_image_tag,
            backdrop_image_item_id,
            mtype,
            is_folder,
            run_time_ticks,
            media_type,
            start_date,
            end_date,
            series,
            status,
            album,
            album_id,
            album_artist,
            artists,
            song_count,
            episode_count,
            channel_id,
            channel_name,
            primary_image_aspect_ratio,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.matched_term, "MatchedTerm")
        XmlUtilities.add_as_subelement(root, self.index_number, "IndexNumber")
        XmlUtilities.add_as_subelement(root, self.production_year, "ProductionYear")
        XmlUtilities.add_as_subelement(
            root, self.parent_index_number, "ParentIndexNumber"
        )
        XmlUtilities.add_as_subelement(root, self.primary_image_tag, "PrimaryImageTag")
        XmlUtilities.add_as_subelement(root, self.thumb_image_tag, "ThumbImageTag")
        XmlUtilities.add_as_subelement(
            root, self.thumb_image_item_id, "ThumbImageItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.backdrop_image_tag, "BackdropImageTag"
        )
        XmlUtilities.add_as_subelement(
            root, self.backdrop_image_item_id, "BackdropImageItemId"
        )
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.is_folder, "IsFolder")
        XmlUtilities.add_as_subelement(root, self.run_time_ticks, "RunTimeTicks")
        XmlUtilities.add_as_subelement(root, self.media_type, "MediaType")
        XmlUtilities.add_as_subelement(root, self.start_date, "StartDate")
        XmlUtilities.add_as_subelement(root, self.end_date, "EndDate")
        XmlUtilities.add_as_subelement(root, self.series, "Series")
        XmlUtilities.add_as_subelement(root, self.status, "Status")
        XmlUtilities.add_as_subelement(root, self.album, "Album")
        XmlUtilities.add_as_subelement(root, self.album_id, "AlbumId")
        XmlUtilities.add_as_subelement(root, self.album_artist, "AlbumArtist")
        XmlUtilities.add_list_as_subelement(root, self.artists, "Artists")
        XmlUtilities.add_as_subelement(root, self.song_count, "SongCount")
        XmlUtilities.add_as_subelement(root, self.episode_count, "EpisodeCount")
        XmlUtilities.add_as_subelement(root, self.channel_id, "ChannelId")
        XmlUtilities.add_as_subelement(root, self.channel_name, "ChannelName")
        XmlUtilities.add_as_subelement(
            root, self.primary_image_aspect_ratio, "PrimaryImageAspectRatio"
        )
