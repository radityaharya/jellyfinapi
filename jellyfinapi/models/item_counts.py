# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ItemCounts(object):

    """Implementation of the 'ItemCounts' model.

    Class LibrarySummary.

    Attributes:
        movie_count (int): Gets or sets the movie count.
        series_count (int): Gets or sets the series count.
        episode_count (int): Gets or sets the episode count.
        artist_count (int): Gets or sets the artist count.
        program_count (int): Gets or sets the program count.
        trailer_count (int): Gets or sets the trailer count.
        song_count (int): Gets or sets the song count.
        album_count (int): Gets or sets the album count.
        music_video_count (int): Gets or sets the music video count.
        box_set_count (int): Gets or sets the box set count.
        book_count (int): Gets or sets the book count.
        item_count (int): Gets or sets the item count.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "movie_count": "MovieCount",
        "series_count": "SeriesCount",
        "episode_count": "EpisodeCount",
        "artist_count": "ArtistCount",
        "program_count": "ProgramCount",
        "trailer_count": "TrailerCount",
        "song_count": "SongCount",
        "album_count": "AlbumCount",
        "music_video_count": "MusicVideoCount",
        "box_set_count": "BoxSetCount",
        "book_count": "BookCount",
        "item_count": "ItemCount",
    }

    _optionals = [
        "movie_count",
        "series_count",
        "episode_count",
        "artist_count",
        "program_count",
        "trailer_count",
        "song_count",
        "album_count",
        "music_video_count",
        "box_set_count",
        "book_count",
        "item_count",
    ]

    def __init__(
        self,
        movie_count=APIHelper.SKIP,
        series_count=APIHelper.SKIP,
        episode_count=APIHelper.SKIP,
        artist_count=APIHelper.SKIP,
        program_count=APIHelper.SKIP,
        trailer_count=APIHelper.SKIP,
        song_count=APIHelper.SKIP,
        album_count=APIHelper.SKIP,
        music_video_count=APIHelper.SKIP,
        box_set_count=APIHelper.SKIP,
        book_count=APIHelper.SKIP,
        item_count=APIHelper.SKIP,
    ):
        """Constructor for the ItemCounts class"""

        # Initialize members of the class
        if movie_count is not APIHelper.SKIP:
            self.movie_count = movie_count
        if series_count is not APIHelper.SKIP:
            self.series_count = series_count
        if episode_count is not APIHelper.SKIP:
            self.episode_count = episode_count
        if artist_count is not APIHelper.SKIP:
            self.artist_count = artist_count
        if program_count is not APIHelper.SKIP:
            self.program_count = program_count
        if trailer_count is not APIHelper.SKIP:
            self.trailer_count = trailer_count
        if song_count is not APIHelper.SKIP:
            self.song_count = song_count
        if album_count is not APIHelper.SKIP:
            self.album_count = album_count
        if music_video_count is not APIHelper.SKIP:
            self.music_video_count = music_video_count
        if box_set_count is not APIHelper.SKIP:
            self.box_set_count = box_set_count
        if book_count is not APIHelper.SKIP:
            self.book_count = book_count
        if item_count is not APIHelper.SKIP:
            self.item_count = item_count

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

        movie_count = (
            dictionary.get("MovieCount")
            if dictionary.get("MovieCount")
            else APIHelper.SKIP
        )
        series_count = (
            dictionary.get("SeriesCount")
            if dictionary.get("SeriesCount")
            else APIHelper.SKIP
        )
        episode_count = (
            dictionary.get("EpisodeCount")
            if dictionary.get("EpisodeCount")
            else APIHelper.SKIP
        )
        artist_count = (
            dictionary.get("ArtistCount")
            if dictionary.get("ArtistCount")
            else APIHelper.SKIP
        )
        program_count = (
            dictionary.get("ProgramCount")
            if dictionary.get("ProgramCount")
            else APIHelper.SKIP
        )
        trailer_count = (
            dictionary.get("TrailerCount")
            if dictionary.get("TrailerCount")
            else APIHelper.SKIP
        )
        song_count = (
            dictionary.get("SongCount")
            if dictionary.get("SongCount")
            else APIHelper.SKIP
        )
        album_count = (
            dictionary.get("AlbumCount")
            if dictionary.get("AlbumCount")
            else APIHelper.SKIP
        )
        music_video_count = (
            dictionary.get("MusicVideoCount")
            if dictionary.get("MusicVideoCount")
            else APIHelper.SKIP
        )
        box_set_count = (
            dictionary.get("BoxSetCount")
            if dictionary.get("BoxSetCount")
            else APIHelper.SKIP
        )
        book_count = (
            dictionary.get("BookCount")
            if dictionary.get("BookCount")
            else APIHelper.SKIP
        )
        item_count = (
            dictionary.get("ItemCount")
            if dictionary.get("ItemCount")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            movie_count,
            series_count,
            episode_count,
            artist_count,
            program_count,
            trailer_count,
            song_count,
            album_count,
            music_video_count,
            box_set_count,
            book_count,
            item_count,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        movie_count = XmlUtilities.value_from_xml_element(root.find("MovieCount"), int)
        series_count = XmlUtilities.value_from_xml_element(
            root.find("SeriesCount"), int
        )
        episode_count = XmlUtilities.value_from_xml_element(
            root.find("EpisodeCount"), int
        )
        artist_count = XmlUtilities.value_from_xml_element(
            root.find("ArtistCount"), int
        )
        program_count = XmlUtilities.value_from_xml_element(
            root.find("ProgramCount"), int
        )
        trailer_count = XmlUtilities.value_from_xml_element(
            root.find("TrailerCount"), int
        )
        song_count = XmlUtilities.value_from_xml_element(root.find("SongCount"), int)
        album_count = XmlUtilities.value_from_xml_element(root.find("AlbumCount"), int)
        music_video_count = XmlUtilities.value_from_xml_element(
            root.find("MusicVideoCount"), int
        )
        box_set_count = XmlUtilities.value_from_xml_element(
            root.find("BoxSetCount"), int
        )
        book_count = XmlUtilities.value_from_xml_element(root.find("BookCount"), int)
        item_count = XmlUtilities.value_from_xml_element(root.find("ItemCount"), int)

        return cls(
            movie_count,
            series_count,
            episode_count,
            artist_count,
            program_count,
            trailer_count,
            song_count,
            album_count,
            music_video_count,
            box_set_count,
            book_count,
            item_count,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.movie_count, "MovieCount")
        XmlUtilities.add_as_subelement(root, self.series_count, "SeriesCount")
        XmlUtilities.add_as_subelement(root, self.episode_count, "EpisodeCount")
        XmlUtilities.add_as_subelement(root, self.artist_count, "ArtistCount")
        XmlUtilities.add_as_subelement(root, self.program_count, "ProgramCount")
        XmlUtilities.add_as_subelement(root, self.trailer_count, "TrailerCount")
        XmlUtilities.add_as_subelement(root, self.song_count, "SongCount")
        XmlUtilities.add_as_subelement(root, self.album_count, "AlbumCount")
        XmlUtilities.add_as_subelement(root, self.music_video_count, "MusicVideoCount")
        XmlUtilities.add_as_subelement(root, self.box_set_count, "BoxSetCount")
        XmlUtilities.add_as_subelement(root, self.book_count, "BookCount")
        XmlUtilities.add_as_subelement(root, self.item_count, "ItemCount")
