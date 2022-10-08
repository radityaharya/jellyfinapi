# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SubtitleOptions(object):

    """Implementation of the 'SubtitleOptions' model.

    TODO: type model description here.

    Attributes:
        skip_if_embedded_subtitles_present (bool): TODO: type description
            here.
        skip_if_audio_track_matches (bool): TODO: type description here.
        download_languages (list of string): TODO: type description here.
        download_movie_subtitles (bool): TODO: type description here.
        download_episode_subtitles (bool): TODO: type description here.
        open_subtitles_username (string): TODO: type description here.
        open_subtitles_password_hash (string): TODO: type description here.
        is_open_subtitle_vip_account (bool): TODO: type description here.
        require_perfect_match (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "skip_if_embedded_subtitles_present": "SkipIfEmbeddedSubtitlesPresent",
        "skip_if_audio_track_matches": "SkipIfAudioTrackMatches",
        "download_languages": "DownloadLanguages",
        "download_movie_subtitles": "DownloadMovieSubtitles",
        "download_episode_subtitles": "DownloadEpisodeSubtitles",
        "open_subtitles_username": "OpenSubtitlesUsername",
        "open_subtitles_password_hash": "OpenSubtitlesPasswordHash",
        "is_open_subtitle_vip_account": "IsOpenSubtitleVipAccount",
        "require_perfect_match": "RequirePerfectMatch",
    }

    _optionals = [
        "skip_if_embedded_subtitles_present",
        "skip_if_audio_track_matches",
        "download_languages",
        "download_movie_subtitles",
        "download_episode_subtitles",
        "open_subtitles_username",
        "open_subtitles_password_hash",
        "is_open_subtitle_vip_account",
        "require_perfect_match",
    ]

    _nullables = [
        "download_languages",
        "open_subtitles_username",
        "open_subtitles_password_hash",
    ]

    def __init__(
        self,
        skip_if_embedded_subtitles_present=APIHelper.SKIP,
        skip_if_audio_track_matches=APIHelper.SKIP,
        download_languages=APIHelper.SKIP,
        download_movie_subtitles=APIHelper.SKIP,
        download_episode_subtitles=APIHelper.SKIP,
        open_subtitles_username=APIHelper.SKIP,
        open_subtitles_password_hash=APIHelper.SKIP,
        is_open_subtitle_vip_account=APIHelper.SKIP,
        require_perfect_match=APIHelper.SKIP,
    ):
        """Constructor for the SubtitleOptions class"""

        # Initialize members of the class
        if skip_if_embedded_subtitles_present is not APIHelper.SKIP:
            self.skip_if_embedded_subtitles_present = skip_if_embedded_subtitles_present
        if skip_if_audio_track_matches is not APIHelper.SKIP:
            self.skip_if_audio_track_matches = skip_if_audio_track_matches
        if download_languages is not APIHelper.SKIP:
            self.download_languages = download_languages
        if download_movie_subtitles is not APIHelper.SKIP:
            self.download_movie_subtitles = download_movie_subtitles
        if download_episode_subtitles is not APIHelper.SKIP:
            self.download_episode_subtitles = download_episode_subtitles
        if open_subtitles_username is not APIHelper.SKIP:
            self.open_subtitles_username = open_subtitles_username
        if open_subtitles_password_hash is not APIHelper.SKIP:
            self.open_subtitles_password_hash = open_subtitles_password_hash
        if is_open_subtitle_vip_account is not APIHelper.SKIP:
            self.is_open_subtitle_vip_account = is_open_subtitle_vip_account
        if require_perfect_match is not APIHelper.SKIP:
            self.require_perfect_match = require_perfect_match

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

        skip_if_embedded_subtitles_present = (
            dictionary.get("SkipIfEmbeddedSubtitlesPresent")
            if "SkipIfEmbeddedSubtitlesPresent" in dictionary.keys()
            else APIHelper.SKIP
        )
        skip_if_audio_track_matches = (
            dictionary.get("SkipIfAudioTrackMatches")
            if "SkipIfAudioTrackMatches" in dictionary.keys()
            else APIHelper.SKIP
        )
        download_languages = (
            dictionary.get("DownloadLanguages")
            if "DownloadLanguages" in dictionary.keys()
            else APIHelper.SKIP
        )
        download_movie_subtitles = (
            dictionary.get("DownloadMovieSubtitles")
            if "DownloadMovieSubtitles" in dictionary.keys()
            else APIHelper.SKIP
        )
        download_episode_subtitles = (
            dictionary.get("DownloadEpisodeSubtitles")
            if "DownloadEpisodeSubtitles" in dictionary.keys()
            else APIHelper.SKIP
        )
        open_subtitles_username = (
            dictionary.get("OpenSubtitlesUsername")
            if "OpenSubtitlesUsername" in dictionary.keys()
            else APIHelper.SKIP
        )
        open_subtitles_password_hash = (
            dictionary.get("OpenSubtitlesPasswordHash")
            if "OpenSubtitlesPasswordHash" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_open_subtitle_vip_account = (
            dictionary.get("IsOpenSubtitleVipAccount")
            if "IsOpenSubtitleVipAccount" in dictionary.keys()
            else APIHelper.SKIP
        )
        require_perfect_match = (
            dictionary.get("RequirePerfectMatch")
            if "RequirePerfectMatch" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            skip_if_embedded_subtitles_present,
            skip_if_audio_track_matches,
            download_languages,
            download_movie_subtitles,
            download_episode_subtitles,
            open_subtitles_username,
            open_subtitles_password_hash,
            is_open_subtitle_vip_account,
            require_perfect_match,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        skip_if_embedded_subtitles_present = XmlUtilities.value_from_xml_element(
            root.find("SkipIfEmbeddedSubtitlesPresent"), bool
        )
        skip_if_audio_track_matches = XmlUtilities.value_from_xml_element(
            root.find("SkipIfAudioTrackMatches"), bool
        )
        download_languages = XmlUtilities.list_from_xml_element(
            root, "DownloadLanguages", str
        )
        download_movie_subtitles = XmlUtilities.value_from_xml_element(
            root.find("DownloadMovieSubtitles"), bool
        )
        download_episode_subtitles = XmlUtilities.value_from_xml_element(
            root.find("DownloadEpisodeSubtitles"), bool
        )
        open_subtitles_username = XmlUtilities.value_from_xml_element(
            root.find("OpenSubtitlesUsername"), str
        )
        open_subtitles_password_hash = XmlUtilities.value_from_xml_element(
            root.find("OpenSubtitlesPasswordHash"), str
        )
        is_open_subtitle_vip_account = XmlUtilities.value_from_xml_element(
            root.find("IsOpenSubtitleVipAccount"), bool
        )
        require_perfect_match = XmlUtilities.value_from_xml_element(
            root.find("RequirePerfectMatch"), bool
        )

        return cls(
            skip_if_embedded_subtitles_present,
            skip_if_audio_track_matches,
            download_languages,
            download_movie_subtitles,
            download_episode_subtitles,
            open_subtitles_username,
            open_subtitles_password_hash,
            is_open_subtitle_vip_account,
            require_perfect_match,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root,
            self.skip_if_embedded_subtitles_present,
            "SkipIfEmbeddedSubtitlesPresent",
        )
        XmlUtilities.add_as_subelement(
            root, self.skip_if_audio_track_matches, "SkipIfAudioTrackMatches"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.download_languages, "DownloadLanguages"
        )
        XmlUtilities.add_as_subelement(
            root, self.download_movie_subtitles, "DownloadMovieSubtitles"
        )
        XmlUtilities.add_as_subelement(
            root, self.download_episode_subtitles, "DownloadEpisodeSubtitles"
        )
        XmlUtilities.add_as_subelement(
            root, self.open_subtitles_username, "OpenSubtitlesUsername"
        )
        XmlUtilities.add_as_subelement(
            root, self.open_subtitles_password_hash, "OpenSubtitlesPasswordHash"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_open_subtitle_vip_account, "IsOpenSubtitleVipAccount"
        )
        XmlUtilities.add_as_subelement(
            root, self.require_perfect_match, "RequirePerfectMatch"
        )
