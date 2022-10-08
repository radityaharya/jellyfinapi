# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UserConfiguration(object):

    """Implementation of the 'UserConfiguration' model.

    Class UserConfiguration.

    Attributes:
        audio_language_preference (string): Gets or sets the audio language
            preference.
        play_default_audio_track (bool): Gets or sets a value indicating
            whether [play default audio track].
        subtitle_language_preference (string): Gets or sets the subtitle
            language preference.
        display_missing_episodes (bool): TODO: type description here.
        grouped_folders (list of string): TODO: type description here.
        subtitle_mode (SubtitlePlaybackModeEnum): An enum representing a
            subtitle playback mode.
        display_collections_view (bool): TODO: type description here.
        enable_local_password (bool): TODO: type description here.
        ordered_views (list of string): TODO: type description here.
        latest_items_excludes (list of string): TODO: type description here.
        my_media_excludes (list of string): TODO: type description here.
        hide_played_in_latest (bool): TODO: type description here.
        remember_audio_selections (bool): TODO: type description here.
        remember_subtitle_selections (bool): TODO: type description here.
        enable_next_episode_auto_play (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audio_language_preference": "AudioLanguagePreference",
        "play_default_audio_track": "PlayDefaultAudioTrack",
        "subtitle_language_preference": "SubtitleLanguagePreference",
        "display_missing_episodes": "DisplayMissingEpisodes",
        "grouped_folders": "GroupedFolders",
        "subtitle_mode": "SubtitleMode",
        "display_collections_view": "DisplayCollectionsView",
        "enable_local_password": "EnableLocalPassword",
        "ordered_views": "OrderedViews",
        "latest_items_excludes": "LatestItemsExcludes",
        "my_media_excludes": "MyMediaExcludes",
        "hide_played_in_latest": "HidePlayedInLatest",
        "remember_audio_selections": "RememberAudioSelections",
        "remember_subtitle_selections": "RememberSubtitleSelections",
        "enable_next_episode_auto_play": "EnableNextEpisodeAutoPlay",
    }

    _optionals = [
        "audio_language_preference",
        "play_default_audio_track",
        "subtitle_language_preference",
        "display_missing_episodes",
        "grouped_folders",
        "subtitle_mode",
        "display_collections_view",
        "enable_local_password",
        "ordered_views",
        "latest_items_excludes",
        "my_media_excludes",
        "hide_played_in_latest",
        "remember_audio_selections",
        "remember_subtitle_selections",
        "enable_next_episode_auto_play",
    ]

    _nullables = [
        "audio_language_preference",
        "subtitle_language_preference",
    ]

    def __init__(
        self,
        audio_language_preference=APIHelper.SKIP,
        play_default_audio_track=APIHelper.SKIP,
        subtitle_language_preference=APIHelper.SKIP,
        display_missing_episodes=APIHelper.SKIP,
        grouped_folders=APIHelper.SKIP,
        subtitle_mode=APIHelper.SKIP,
        display_collections_view=APIHelper.SKIP,
        enable_local_password=APIHelper.SKIP,
        ordered_views=APIHelper.SKIP,
        latest_items_excludes=APIHelper.SKIP,
        my_media_excludes=APIHelper.SKIP,
        hide_played_in_latest=APIHelper.SKIP,
        remember_audio_selections=APIHelper.SKIP,
        remember_subtitle_selections=APIHelper.SKIP,
        enable_next_episode_auto_play=APIHelper.SKIP,
    ):
        """Constructor for the UserConfiguration class"""

        # Initialize members of the class
        if audio_language_preference is not APIHelper.SKIP:
            self.audio_language_preference = audio_language_preference
        if play_default_audio_track is not APIHelper.SKIP:
            self.play_default_audio_track = play_default_audio_track
        if subtitle_language_preference is not APIHelper.SKIP:
            self.subtitle_language_preference = subtitle_language_preference
        if display_missing_episodes is not APIHelper.SKIP:
            self.display_missing_episodes = display_missing_episodes
        if grouped_folders is not APIHelper.SKIP:
            self.grouped_folders = grouped_folders
        if subtitle_mode is not APIHelper.SKIP:
            self.subtitle_mode = subtitle_mode
        if display_collections_view is not APIHelper.SKIP:
            self.display_collections_view = display_collections_view
        if enable_local_password is not APIHelper.SKIP:
            self.enable_local_password = enable_local_password
        if ordered_views is not APIHelper.SKIP:
            self.ordered_views = ordered_views
        if latest_items_excludes is not APIHelper.SKIP:
            self.latest_items_excludes = latest_items_excludes
        if my_media_excludes is not APIHelper.SKIP:
            self.my_media_excludes = my_media_excludes
        if hide_played_in_latest is not APIHelper.SKIP:
            self.hide_played_in_latest = hide_played_in_latest
        if remember_audio_selections is not APIHelper.SKIP:
            self.remember_audio_selections = remember_audio_selections
        if remember_subtitle_selections is not APIHelper.SKIP:
            self.remember_subtitle_selections = remember_subtitle_selections
        if enable_next_episode_auto_play is not APIHelper.SKIP:
            self.enable_next_episode_auto_play = enable_next_episode_auto_play

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

        audio_language_preference = (
            dictionary.get("AudioLanguagePreference")
            if "AudioLanguagePreference" in dictionary.keys()
            else APIHelper.SKIP
        )
        play_default_audio_track = (
            dictionary.get("PlayDefaultAudioTrack")
            if "PlayDefaultAudioTrack" in dictionary.keys()
            else APIHelper.SKIP
        )
        subtitle_language_preference = (
            dictionary.get("SubtitleLanguagePreference")
            if "SubtitleLanguagePreference" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_missing_episodes = (
            dictionary.get("DisplayMissingEpisodes")
            if "DisplayMissingEpisodes" in dictionary.keys()
            else APIHelper.SKIP
        )
        grouped_folders = (
            dictionary.get("GroupedFolders")
            if dictionary.get("GroupedFolders")
            else APIHelper.SKIP
        )
        subtitle_mode = (
            dictionary.get("SubtitleMode")
            if dictionary.get("SubtitleMode")
            else APIHelper.SKIP
        )
        display_collections_view = (
            dictionary.get("DisplayCollectionsView")
            if "DisplayCollectionsView" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_local_password = (
            dictionary.get("EnableLocalPassword")
            if "EnableLocalPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        ordered_views = (
            dictionary.get("OrderedViews")
            if dictionary.get("OrderedViews")
            else APIHelper.SKIP
        )
        latest_items_excludes = (
            dictionary.get("LatestItemsExcludes")
            if dictionary.get("LatestItemsExcludes")
            else APIHelper.SKIP
        )
        my_media_excludes = (
            dictionary.get("MyMediaExcludes")
            if dictionary.get("MyMediaExcludes")
            else APIHelper.SKIP
        )
        hide_played_in_latest = (
            dictionary.get("HidePlayedInLatest")
            if "HidePlayedInLatest" in dictionary.keys()
            else APIHelper.SKIP
        )
        remember_audio_selections = (
            dictionary.get("RememberAudioSelections")
            if "RememberAudioSelections" in dictionary.keys()
            else APIHelper.SKIP
        )
        remember_subtitle_selections = (
            dictionary.get("RememberSubtitleSelections")
            if "RememberSubtitleSelections" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_next_episode_auto_play = (
            dictionary.get("EnableNextEpisodeAutoPlay")
            if "EnableNextEpisodeAutoPlay" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            audio_language_preference,
            play_default_audio_track,
            subtitle_language_preference,
            display_missing_episodes,
            grouped_folders,
            subtitle_mode,
            display_collections_view,
            enable_local_password,
            ordered_views,
            latest_items_excludes,
            my_media_excludes,
            hide_played_in_latest,
            remember_audio_selections,
            remember_subtitle_selections,
            enable_next_episode_auto_play,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        audio_language_preference = XmlUtilities.value_from_xml_element(
            root.find("AudioLanguagePreference"), str
        )
        play_default_audio_track = XmlUtilities.value_from_xml_element(
            root.find("PlayDefaultAudioTrack"), bool
        )
        subtitle_language_preference = XmlUtilities.value_from_xml_element(
            root.find("SubtitleLanguagePreference"), str
        )
        display_missing_episodes = XmlUtilities.value_from_xml_element(
            root.find("DisplayMissingEpisodes"), bool
        )
        grouped_folders = XmlUtilities.list_from_xml_element(
            root, "GroupedFolders", str
        )
        subtitle_mode = XmlUtilities.value_from_xml_element(
            root.find("SubtitleMode"), str
        )
        display_collections_view = XmlUtilities.value_from_xml_element(
            root.find("DisplayCollectionsView"), bool
        )
        enable_local_password = XmlUtilities.value_from_xml_element(
            root.find("EnableLocalPassword"), bool
        )
        ordered_views = XmlUtilities.list_from_xml_element(root, "OrderedViews", str)
        latest_items_excludes = XmlUtilities.list_from_xml_element(
            root, "LatestItemsExcludes", str
        )
        my_media_excludes = XmlUtilities.list_from_xml_element(
            root, "MyMediaExcludes", str
        )
        hide_played_in_latest = XmlUtilities.value_from_xml_element(
            root.find("HidePlayedInLatest"), bool
        )
        remember_audio_selections = XmlUtilities.value_from_xml_element(
            root.find("RememberAudioSelections"), bool
        )
        remember_subtitle_selections = XmlUtilities.value_from_xml_element(
            root.find("RememberSubtitleSelections"), bool
        )
        enable_next_episode_auto_play = XmlUtilities.value_from_xml_element(
            root.find("EnableNextEpisodeAutoPlay"), bool
        )

        return cls(
            audio_language_preference,
            play_default_audio_track,
            subtitle_language_preference,
            display_missing_episodes,
            grouped_folders,
            subtitle_mode,
            display_collections_view,
            enable_local_password,
            ordered_views,
            latest_items_excludes,
            my_media_excludes,
            hide_played_in_latest,
            remember_audio_selections,
            remember_subtitle_selections,
            enable_next_episode_auto_play,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.audio_language_preference, "AudioLanguagePreference"
        )
        XmlUtilities.add_as_subelement(
            root, self.play_default_audio_track, "PlayDefaultAudioTrack"
        )
        XmlUtilities.add_as_subelement(
            root, self.subtitle_language_preference, "SubtitleLanguagePreference"
        )
        XmlUtilities.add_as_subelement(
            root, self.display_missing_episodes, "DisplayMissingEpisodes"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.grouped_folders, "GroupedFolders"
        )
        XmlUtilities.add_as_subelement(root, self.subtitle_mode, "SubtitleMode")
        XmlUtilities.add_as_subelement(
            root, self.display_collections_view, "DisplayCollectionsView"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_local_password, "EnableLocalPassword"
        )
        XmlUtilities.add_list_as_subelement(root, self.ordered_views, "OrderedViews")
        XmlUtilities.add_list_as_subelement(
            root, self.latest_items_excludes, "LatestItemsExcludes"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.my_media_excludes, "MyMediaExcludes"
        )
        XmlUtilities.add_as_subelement(
            root, self.hide_played_in_latest, "HidePlayedInLatest"
        )
        XmlUtilities.add_as_subelement(
            root, self.remember_audio_selections, "RememberAudioSelections"
        )
        XmlUtilities.add_as_subelement(
            root, self.remember_subtitle_selections, "RememberSubtitleSelections"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_next_episode_auto_play, "EnableNextEpisodeAutoPlay"
        )
