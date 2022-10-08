# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UserItemDataDto(object):

    """Implementation of the 'UserItemDataDto' model.

    Class UserItemDataDto.

    Attributes:
        rating (float): Gets or sets the rating.
        played_percentage (float): Gets or sets the played percentage.
        unplayed_item_count (int): Gets or sets the unplayed item count.
        playback_position_ticks (long|int): Gets or sets the playback position
            ticks.
        play_count (int): Gets or sets the play count.
        is_favorite (bool): Gets or sets a value indicating whether this
            instance is favorite.
        likes (bool): Gets or sets a value indicating whether this
            MediaBrowser.Model.Dto.UserItemDataDto is likes.
        last_played_date (datetime): Gets or sets the last played date.
        played (bool): Gets or sets a value indicating whether this
            MediaBrowser.Model.Dto.UserItemDataDto is played.
        key (string): Gets or sets the key.
        item_id (string): Gets or sets the item identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rating": "Rating",
        "played_percentage": "PlayedPercentage",
        "unplayed_item_count": "UnplayedItemCount",
        "playback_position_ticks": "PlaybackPositionTicks",
        "play_count": "PlayCount",
        "is_favorite": "IsFavorite",
        "likes": "Likes",
        "last_played_date": "LastPlayedDate",
        "played": "Played",
        "key": "Key",
        "item_id": "ItemId",
    }

    _optionals = [
        "rating",
        "played_percentage",
        "unplayed_item_count",
        "playback_position_ticks",
        "play_count",
        "is_favorite",
        "likes",
        "last_played_date",
        "played",
        "key",
        "item_id",
    ]

    _nullables = [
        "rating",
        "played_percentage",
        "unplayed_item_count",
        "likes",
        "last_played_date",
        "key",
        "item_id",
    ]

    def __init__(
        self,
        rating=APIHelper.SKIP,
        played_percentage=APIHelper.SKIP,
        unplayed_item_count=APIHelper.SKIP,
        playback_position_ticks=APIHelper.SKIP,
        play_count=APIHelper.SKIP,
        is_favorite=APIHelper.SKIP,
        likes=APIHelper.SKIP,
        last_played_date=APIHelper.SKIP,
        played=APIHelper.SKIP,
        key=APIHelper.SKIP,
        item_id=APIHelper.SKIP,
    ):
        """Constructor for the UserItemDataDto class"""

        # Initialize members of the class
        if rating is not APIHelper.SKIP:
            self.rating = rating
        if played_percentage is not APIHelper.SKIP:
            self.played_percentage = played_percentage
        if unplayed_item_count is not APIHelper.SKIP:
            self.unplayed_item_count = unplayed_item_count
        if playback_position_ticks is not APIHelper.SKIP:
            self.playback_position_ticks = playback_position_ticks
        if play_count is not APIHelper.SKIP:
            self.play_count = play_count
        if is_favorite is not APIHelper.SKIP:
            self.is_favorite = is_favorite
        if likes is not APIHelper.SKIP:
            self.likes = likes
        if last_played_date is not APIHelper.SKIP:
            self.last_played_date = (
                APIHelper.RFC3339DateTime(last_played_date)
                if last_played_date
                else None
            )
        if played is not APIHelper.SKIP:
            self.played = played
        if key is not APIHelper.SKIP:
            self.key = key
        if item_id is not APIHelper.SKIP:
            self.item_id = item_id

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

        rating = (
            dictionary.get("Rating")
            if "Rating" in dictionary.keys()
            else APIHelper.SKIP
        )
        played_percentage = (
            dictionary.get("PlayedPercentage")
            if "PlayedPercentage" in dictionary.keys()
            else APIHelper.SKIP
        )
        unplayed_item_count = (
            dictionary.get("UnplayedItemCount")
            if "UnplayedItemCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        playback_position_ticks = (
            dictionary.get("PlaybackPositionTicks")
            if dictionary.get("PlaybackPositionTicks")
            else APIHelper.SKIP
        )
        play_count = (
            dictionary.get("PlayCount")
            if dictionary.get("PlayCount")
            else APIHelper.SKIP
        )
        is_favorite = (
            dictionary.get("IsFavorite")
            if "IsFavorite" in dictionary.keys()
            else APIHelper.SKIP
        )
        likes = (
            dictionary.get("Likes") if "Likes" in dictionary.keys() else APIHelper.SKIP
        )
        if "LastPlayedDate" in dictionary.keys():
            last_played_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("LastPlayedDate")
                ).datetime
                if dictionary.get("LastPlayedDate")
                else None
            )
        else:
            last_played_date = APIHelper.SKIP
        played = (
            dictionary.get("Played")
            if "Played" in dictionary.keys()
            else APIHelper.SKIP
        )
        key = dictionary.get("Key") if "Key" in dictionary.keys() else APIHelper.SKIP
        item_id = (
            dictionary.get("ItemId")
            if "ItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            rating,
            played_percentage,
            unplayed_item_count,
            playback_position_ticks,
            play_count,
            is_favorite,
            likes,
            last_played_date,
            played,
            key,
            item_id,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        rating = XmlUtilities.value_from_xml_element(root.find("Rating"), float)
        played_percentage = XmlUtilities.value_from_xml_element(
            root.find("PlayedPercentage"), float
        )
        unplayed_item_count = XmlUtilities.value_from_xml_element(
            root.find("UnplayedItemCount"), int
        )
        playback_position_ticks = XmlUtilities.value_from_xml_element(
            root.find("PlaybackPositionTicks"), int
        )
        play_count = XmlUtilities.value_from_xml_element(root.find("PlayCount"), int)
        is_favorite = XmlUtilities.value_from_xml_element(root.find("IsFavorite"), bool)
        likes = XmlUtilities.value_from_xml_element(root.find("Likes"), bool)
        last_played_date = XmlUtilities.value_from_xml_element(
            root.find("LastPlayedDate"), APIHelper.RFC3339DateTime
        )
        played = XmlUtilities.value_from_xml_element(root.find("Played"), bool)
        key = XmlUtilities.value_from_xml_element(root.find("Key"), str)
        item_id = XmlUtilities.value_from_xml_element(root.find("ItemId"), str)

        return cls(
            rating,
            played_percentage,
            unplayed_item_count,
            playback_position_ticks,
            play_count,
            is_favorite,
            likes,
            last_played_date,
            played,
            key,
            item_id,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.rating, "Rating")
        XmlUtilities.add_as_subelement(root, self.played_percentage, "PlayedPercentage")
        XmlUtilities.add_as_subelement(
            root, self.unplayed_item_count, "UnplayedItemCount"
        )
        XmlUtilities.add_as_subelement(
            root, self.playback_position_ticks, "PlaybackPositionTicks"
        )
        XmlUtilities.add_as_subelement(root, self.play_count, "PlayCount")
        XmlUtilities.add_as_subelement(root, self.is_favorite, "IsFavorite")
        XmlUtilities.add_as_subelement(root, self.likes, "Likes")
        XmlUtilities.add_as_subelement(root, self.last_played_date, "LastPlayedDate")
        XmlUtilities.add_as_subelement(root, self.played, "Played")
        XmlUtilities.add_as_subelement(root, self.key, "Key")
        XmlUtilities.add_as_subelement(root, self.item_id, "ItemId")
