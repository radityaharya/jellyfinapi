# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_path_info import MediaPathInfo
from jellyfinapi.models.type_options import TypeOptions
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LibraryOptions(object):

    """Implementation of the 'LibraryOptions' model.

    TODO: type model description here.

    Attributes:
        enable_photos (bool): TODO: type description here.
        enable_realtime_monitor (bool): TODO: type description here.
        enable_chapter_image_extraction (bool): TODO: type description here.
        extract_chapter_images_during_library_scan (bool): TODO: type
            description here.
        path_infos (list of MediaPathInfo): TODO: type description here.
        save_local_metadata (bool): TODO: type description here.
        enable_internet_providers (bool): TODO: type description here.
        enable_automatic_series_grouping (bool): TODO: type description here.
        enable_embedded_titles (bool): TODO: type description here.
        enable_embedded_episode_infos (bool): TODO: type description here.
        automatic_refresh_interval_days (int): TODO: type description here.
        preferred_metadata_language (string): Gets or sets the preferred
            metadata language.
        metadata_country_code (string): Gets or sets the metadata country
            code.
        season_zero_display_name (string): TODO: type description here.
        metadata_savers (list of string): TODO: type description here.
        disabled_local_metadata_readers (list of string): TODO: type
            description here.
        local_metadata_reader_order (list of string): TODO: type description
            here.
        disabled_subtitle_fetchers (list of string): TODO: type description
            here.
        subtitle_fetcher_order (list of string): TODO: type description here.
        skip_subtitles_if_embedded_subtitles_present (bool): TODO: type
            description here.
        skip_subtitles_if_audio_track_matches (bool): TODO: type description
            here.
        subtitle_download_languages (list of string): TODO: type description
            here.
        require_perfect_subtitle_match (bool): TODO: type description here.
        save_subtitles_with_media (bool): TODO: type description here.
        automatically_add_to_collection (bool): TODO: type description here.
        allow_embedded_subtitles (EmbeddedSubtitleOptionsEnum): An enum
            representing the options to disable embedded subs.
        type_options (list of TypeOptions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_photos": "EnablePhotos",
        "enable_realtime_monitor": "EnableRealtimeMonitor",
        "enable_chapter_image_extraction": "EnableChapterImageExtraction",
        "extract_chapter_images_during_library_scan": "ExtractChapterImagesDuringLibraryScan",
        "path_infos": "PathInfos",
        "save_local_metadata": "SaveLocalMetadata",
        "enable_internet_providers": "EnableInternetProviders",
        "enable_automatic_series_grouping": "EnableAutomaticSeriesGrouping",
        "enable_embedded_titles": "EnableEmbeddedTitles",
        "enable_embedded_episode_infos": "EnableEmbeddedEpisodeInfos",
        "automatic_refresh_interval_days": "AutomaticRefreshIntervalDays",
        "preferred_metadata_language": "PreferredMetadataLanguage",
        "metadata_country_code": "MetadataCountryCode",
        "season_zero_display_name": "SeasonZeroDisplayName",
        "metadata_savers": "MetadataSavers",
        "disabled_local_metadata_readers": "DisabledLocalMetadataReaders",
        "local_metadata_reader_order": "LocalMetadataReaderOrder",
        "disabled_subtitle_fetchers": "DisabledSubtitleFetchers",
        "subtitle_fetcher_order": "SubtitleFetcherOrder",
        "skip_subtitles_if_embedded_subtitles_present": "SkipSubtitlesIfEmbeddedSubtitlesPresent",
        "skip_subtitles_if_audio_track_matches": "SkipSubtitlesIfAudioTrackMatches",
        "subtitle_download_languages": "SubtitleDownloadLanguages",
        "require_perfect_subtitle_match": "RequirePerfectSubtitleMatch",
        "save_subtitles_with_media": "SaveSubtitlesWithMedia",
        "automatically_add_to_collection": "AutomaticallyAddToCollection",
        "allow_embedded_subtitles": "AllowEmbeddedSubtitles",
        "type_options": "TypeOptions",
    }

    _optionals = [
        "enable_photos",
        "enable_realtime_monitor",
        "enable_chapter_image_extraction",
        "extract_chapter_images_during_library_scan",
        "path_infos",
        "save_local_metadata",
        "enable_internet_providers",
        "enable_automatic_series_grouping",
        "enable_embedded_titles",
        "enable_embedded_episode_infos",
        "automatic_refresh_interval_days",
        "preferred_metadata_language",
        "metadata_country_code",
        "season_zero_display_name",
        "metadata_savers",
        "disabled_local_metadata_readers",
        "local_metadata_reader_order",
        "disabled_subtitle_fetchers",
        "subtitle_fetcher_order",
        "skip_subtitles_if_embedded_subtitles_present",
        "skip_subtitles_if_audio_track_matches",
        "subtitle_download_languages",
        "require_perfect_subtitle_match",
        "save_subtitles_with_media",
        "automatically_add_to_collection",
        "allow_embedded_subtitles",
        "type_options",
    ]

    _nullables = [
        "preferred_metadata_language",
        "metadata_country_code",
        "metadata_savers",
        "local_metadata_reader_order",
        "subtitle_download_languages",
    ]

    def __init__(
        self,
        enable_photos=APIHelper.SKIP,
        enable_realtime_monitor=APIHelper.SKIP,
        enable_chapter_image_extraction=APIHelper.SKIP,
        extract_chapter_images_during_library_scan=APIHelper.SKIP,
        path_infos=APIHelper.SKIP,
        save_local_metadata=APIHelper.SKIP,
        enable_internet_providers=APIHelper.SKIP,
        enable_automatic_series_grouping=APIHelper.SKIP,
        enable_embedded_titles=APIHelper.SKIP,
        enable_embedded_episode_infos=APIHelper.SKIP,
        automatic_refresh_interval_days=APIHelper.SKIP,
        preferred_metadata_language=APIHelper.SKIP,
        metadata_country_code=APIHelper.SKIP,
        season_zero_display_name=APIHelper.SKIP,
        metadata_savers=APIHelper.SKIP,
        disabled_local_metadata_readers=APIHelper.SKIP,
        local_metadata_reader_order=APIHelper.SKIP,
        disabled_subtitle_fetchers=APIHelper.SKIP,
        subtitle_fetcher_order=APIHelper.SKIP,
        skip_subtitles_if_embedded_subtitles_present=APIHelper.SKIP,
        skip_subtitles_if_audio_track_matches=APIHelper.SKIP,
        subtitle_download_languages=APIHelper.SKIP,
        require_perfect_subtitle_match=APIHelper.SKIP,
        save_subtitles_with_media=APIHelper.SKIP,
        automatically_add_to_collection=APIHelper.SKIP,
        allow_embedded_subtitles=APIHelper.SKIP,
        type_options=APIHelper.SKIP,
    ):
        """Constructor for the LibraryOptions class"""

        # Initialize members of the class
        if enable_photos is not APIHelper.SKIP:
            self.enable_photos = enable_photos
        if enable_realtime_monitor is not APIHelper.SKIP:
            self.enable_realtime_monitor = enable_realtime_monitor
        if enable_chapter_image_extraction is not APIHelper.SKIP:
            self.enable_chapter_image_extraction = enable_chapter_image_extraction
        if extract_chapter_images_during_library_scan is not APIHelper.SKIP:
            self.extract_chapter_images_during_library_scan = (
                extract_chapter_images_during_library_scan
            )
        if path_infos is not APIHelper.SKIP:
            self.path_infos = path_infos
        if save_local_metadata is not APIHelper.SKIP:
            self.save_local_metadata = save_local_metadata
        if enable_internet_providers is not APIHelper.SKIP:
            self.enable_internet_providers = enable_internet_providers
        if enable_automatic_series_grouping is not APIHelper.SKIP:
            self.enable_automatic_series_grouping = enable_automatic_series_grouping
        if enable_embedded_titles is not APIHelper.SKIP:
            self.enable_embedded_titles = enable_embedded_titles
        if enable_embedded_episode_infos is not APIHelper.SKIP:
            self.enable_embedded_episode_infos = enable_embedded_episode_infos
        if automatic_refresh_interval_days is not APIHelper.SKIP:
            self.automatic_refresh_interval_days = automatic_refresh_interval_days
        if preferred_metadata_language is not APIHelper.SKIP:
            self.preferred_metadata_language = preferred_metadata_language
        if metadata_country_code is not APIHelper.SKIP:
            self.metadata_country_code = metadata_country_code
        if season_zero_display_name is not APIHelper.SKIP:
            self.season_zero_display_name = season_zero_display_name
        if metadata_savers is not APIHelper.SKIP:
            self.metadata_savers = metadata_savers
        if disabled_local_metadata_readers is not APIHelper.SKIP:
            self.disabled_local_metadata_readers = disabled_local_metadata_readers
        if local_metadata_reader_order is not APIHelper.SKIP:
            self.local_metadata_reader_order = local_metadata_reader_order
        if disabled_subtitle_fetchers is not APIHelper.SKIP:
            self.disabled_subtitle_fetchers = disabled_subtitle_fetchers
        if subtitle_fetcher_order is not APIHelper.SKIP:
            self.subtitle_fetcher_order = subtitle_fetcher_order
        if skip_subtitles_if_embedded_subtitles_present is not APIHelper.SKIP:
            self.skip_subtitles_if_embedded_subtitles_present = (
                skip_subtitles_if_embedded_subtitles_present
            )
        if skip_subtitles_if_audio_track_matches is not APIHelper.SKIP:
            self.skip_subtitles_if_audio_track_matches = (
                skip_subtitles_if_audio_track_matches
            )
        if subtitle_download_languages is not APIHelper.SKIP:
            self.subtitle_download_languages = subtitle_download_languages
        if require_perfect_subtitle_match is not APIHelper.SKIP:
            self.require_perfect_subtitle_match = require_perfect_subtitle_match
        if save_subtitles_with_media is not APIHelper.SKIP:
            self.save_subtitles_with_media = save_subtitles_with_media
        if automatically_add_to_collection is not APIHelper.SKIP:
            self.automatically_add_to_collection = automatically_add_to_collection
        if allow_embedded_subtitles is not APIHelper.SKIP:
            self.allow_embedded_subtitles = allow_embedded_subtitles
        if type_options is not APIHelper.SKIP:
            self.type_options = type_options

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

        enable_photos = (
            dictionary.get("EnablePhotos")
            if "EnablePhotos" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_realtime_monitor = (
            dictionary.get("EnableRealtimeMonitor")
            if "EnableRealtimeMonitor" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_chapter_image_extraction = (
            dictionary.get("EnableChapterImageExtraction")
            if "EnableChapterImageExtraction" in dictionary.keys()
            else APIHelper.SKIP
        )
        extract_chapter_images_during_library_scan = (
            dictionary.get("ExtractChapterImagesDuringLibraryScan")
            if "ExtractChapterImagesDuringLibraryScan" in dictionary.keys()
            else APIHelper.SKIP
        )
        path_infos = None
        if dictionary.get("PathInfos") is not None:
            path_infos = [
                MediaPathInfo.from_dictionary(x) for x in dictionary.get("PathInfos")
            ]
        else:
            path_infos = APIHelper.SKIP
        save_local_metadata = (
            dictionary.get("SaveLocalMetadata")
            if "SaveLocalMetadata" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_internet_providers = (
            dictionary.get("EnableInternetProviders")
            if "EnableInternetProviders" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_automatic_series_grouping = (
            dictionary.get("EnableAutomaticSeriesGrouping")
            if "EnableAutomaticSeriesGrouping" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_embedded_titles = (
            dictionary.get("EnableEmbeddedTitles")
            if "EnableEmbeddedTitles" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_embedded_episode_infos = (
            dictionary.get("EnableEmbeddedEpisodeInfos")
            if "EnableEmbeddedEpisodeInfos" in dictionary.keys()
            else APIHelper.SKIP
        )
        automatic_refresh_interval_days = (
            dictionary.get("AutomaticRefreshIntervalDays")
            if dictionary.get("AutomaticRefreshIntervalDays")
            else APIHelper.SKIP
        )
        preferred_metadata_language = (
            dictionary.get("PreferredMetadataLanguage")
            if "PreferredMetadataLanguage" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_country_code = (
            dictionary.get("MetadataCountryCode")
            if "MetadataCountryCode" in dictionary.keys()
            else APIHelper.SKIP
        )
        season_zero_display_name = (
            dictionary.get("SeasonZeroDisplayName")
            if dictionary.get("SeasonZeroDisplayName")
            else APIHelper.SKIP
        )
        metadata_savers = (
            dictionary.get("MetadataSavers")
            if "MetadataSavers" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_local_metadata_readers = (
            dictionary.get("DisabledLocalMetadataReaders")
            if dictionary.get("DisabledLocalMetadataReaders")
            else APIHelper.SKIP
        )
        local_metadata_reader_order = (
            dictionary.get("LocalMetadataReaderOrder")
            if "LocalMetadataReaderOrder" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_subtitle_fetchers = (
            dictionary.get("DisabledSubtitleFetchers")
            if dictionary.get("DisabledSubtitleFetchers")
            else APIHelper.SKIP
        )
        subtitle_fetcher_order = (
            dictionary.get("SubtitleFetcherOrder")
            if dictionary.get("SubtitleFetcherOrder")
            else APIHelper.SKIP
        )
        skip_subtitles_if_embedded_subtitles_present = (
            dictionary.get("SkipSubtitlesIfEmbeddedSubtitlesPresent")
            if "SkipSubtitlesIfEmbeddedSubtitlesPresent" in dictionary.keys()
            else APIHelper.SKIP
        )
        skip_subtitles_if_audio_track_matches = (
            dictionary.get("SkipSubtitlesIfAudioTrackMatches")
            if "SkipSubtitlesIfAudioTrackMatches" in dictionary.keys()
            else APIHelper.SKIP
        )
        subtitle_download_languages = (
            dictionary.get("SubtitleDownloadLanguages")
            if "SubtitleDownloadLanguages" in dictionary.keys()
            else APIHelper.SKIP
        )
        require_perfect_subtitle_match = (
            dictionary.get("RequirePerfectSubtitleMatch")
            if "RequirePerfectSubtitleMatch" in dictionary.keys()
            else APIHelper.SKIP
        )
        save_subtitles_with_media = (
            dictionary.get("SaveSubtitlesWithMedia")
            if "SaveSubtitlesWithMedia" in dictionary.keys()
            else APIHelper.SKIP
        )
        automatically_add_to_collection = (
            dictionary.get("AutomaticallyAddToCollection")
            if "AutomaticallyAddToCollection" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_embedded_subtitles = (
            dictionary.get("AllowEmbeddedSubtitles")
            if dictionary.get("AllowEmbeddedSubtitles")
            else APIHelper.SKIP
        )
        type_options = None
        if dictionary.get("TypeOptions") is not None:
            type_options = [
                TypeOptions.from_dictionary(x) for x in dictionary.get("TypeOptions")
            ]
        else:
            type_options = APIHelper.SKIP
        # Return an object of this model
        return cls(
            enable_photos,
            enable_realtime_monitor,
            enable_chapter_image_extraction,
            extract_chapter_images_during_library_scan,
            path_infos,
            save_local_metadata,
            enable_internet_providers,
            enable_automatic_series_grouping,
            enable_embedded_titles,
            enable_embedded_episode_infos,
            automatic_refresh_interval_days,
            preferred_metadata_language,
            metadata_country_code,
            season_zero_display_name,
            metadata_savers,
            disabled_local_metadata_readers,
            local_metadata_reader_order,
            disabled_subtitle_fetchers,
            subtitle_fetcher_order,
            skip_subtitles_if_embedded_subtitles_present,
            skip_subtitles_if_audio_track_matches,
            subtitle_download_languages,
            require_perfect_subtitle_match,
            save_subtitles_with_media,
            automatically_add_to_collection,
            allow_embedded_subtitles,
            type_options,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        enable_photos = XmlUtilities.value_from_xml_element(
            root.find("EnablePhotos"), bool
        )
        enable_realtime_monitor = XmlUtilities.value_from_xml_element(
            root.find("EnableRealtimeMonitor"), bool
        )
        enable_chapter_image_extraction = XmlUtilities.value_from_xml_element(
            root.find("EnableChapterImageExtraction"), bool
        )
        extract_chapter_images_during_library_scan = (
            XmlUtilities.value_from_xml_element(
                root.find("ExtractChapterImagesDuringLibraryScan"), bool
            )
        )
        path_infos = XmlUtilities.list_from_xml_element(
            root, "MediaPathInfo", MediaPathInfo
        )
        save_local_metadata = XmlUtilities.value_from_xml_element(
            root.find("SaveLocalMetadata"), bool
        )
        enable_internet_providers = XmlUtilities.value_from_xml_element(
            root.find("EnableInternetProviders"), bool
        )
        enable_automatic_series_grouping = XmlUtilities.value_from_xml_element(
            root.find("EnableAutomaticSeriesGrouping"), bool
        )
        enable_embedded_titles = XmlUtilities.value_from_xml_element(
            root.find("EnableEmbeddedTitles"), bool
        )
        enable_embedded_episode_infos = XmlUtilities.value_from_xml_element(
            root.find("EnableEmbeddedEpisodeInfos"), bool
        )
        automatic_refresh_interval_days = XmlUtilities.value_from_xml_element(
            root.find("AutomaticRefreshIntervalDays"), int
        )
        preferred_metadata_language = XmlUtilities.value_from_xml_element(
            root.find("PreferredMetadataLanguage"), str
        )
        metadata_country_code = XmlUtilities.value_from_xml_element(
            root.find("MetadataCountryCode"), str
        )
        season_zero_display_name = XmlUtilities.value_from_xml_element(
            root.find("SeasonZeroDisplayName"), str
        )
        metadata_savers = XmlUtilities.list_from_xml_element(
            root, "MetadataSavers", str
        )
        disabled_local_metadata_readers = XmlUtilities.list_from_xml_element(
            root, "DisabledLocalMetadataReaders", str
        )
        local_metadata_reader_order = XmlUtilities.list_from_xml_element(
            root, "LocalMetadataReaderOrder", str
        )
        disabled_subtitle_fetchers = XmlUtilities.list_from_xml_element(
            root, "DisabledSubtitleFetchers", str
        )
        subtitle_fetcher_order = XmlUtilities.list_from_xml_element(
            root, "SubtitleFetcherOrder", str
        )
        skip_subtitles_if_embedded_subtitles_present = (
            XmlUtilities.value_from_xml_element(
                root.find("SkipSubtitlesIfEmbeddedSubtitlesPresent"), bool
            )
        )
        skip_subtitles_if_audio_track_matches = XmlUtilities.value_from_xml_element(
            root.find("SkipSubtitlesIfAudioTrackMatches"), bool
        )
        subtitle_download_languages = XmlUtilities.list_from_xml_element(
            root, "SubtitleDownloadLanguages", str
        )
        require_perfect_subtitle_match = XmlUtilities.value_from_xml_element(
            root.find("RequirePerfectSubtitleMatch"), bool
        )
        save_subtitles_with_media = XmlUtilities.value_from_xml_element(
            root.find("SaveSubtitlesWithMedia"), bool
        )
        automatically_add_to_collection = XmlUtilities.value_from_xml_element(
            root.find("AutomaticallyAddToCollection"), bool
        )
        allow_embedded_subtitles = XmlUtilities.value_from_xml_element(
            root.find("AllowEmbeddedSubtitles"), str
        )
        type_options = XmlUtilities.list_from_xml_element(
            root, "TypeOptions", TypeOptions
        )

        return cls(
            enable_photos,
            enable_realtime_monitor,
            enable_chapter_image_extraction,
            extract_chapter_images_during_library_scan,
            path_infos,
            save_local_metadata,
            enable_internet_providers,
            enable_automatic_series_grouping,
            enable_embedded_titles,
            enable_embedded_episode_infos,
            automatic_refresh_interval_days,
            preferred_metadata_language,
            metadata_country_code,
            season_zero_display_name,
            metadata_savers,
            disabled_local_metadata_readers,
            local_metadata_reader_order,
            disabled_subtitle_fetchers,
            subtitle_fetcher_order,
            skip_subtitles_if_embedded_subtitles_present,
            skip_subtitles_if_audio_track_matches,
            subtitle_download_languages,
            require_perfect_subtitle_match,
            save_subtitles_with_media,
            automatically_add_to_collection,
            allow_embedded_subtitles,
            type_options,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.enable_photos, "EnablePhotos")
        XmlUtilities.add_as_subelement(
            root, self.enable_realtime_monitor, "EnableRealtimeMonitor"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_chapter_image_extraction, "EnableChapterImageExtraction"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.extract_chapter_images_during_library_scan,
            "ExtractChapterImagesDuringLibraryScan",
        )
        XmlUtilities.add_list_as_subelement(root, self.path_infos, "MediaPathInfo")
        XmlUtilities.add_as_subelement(
            root, self.save_local_metadata, "SaveLocalMetadata"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_internet_providers, "EnableInternetProviders"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_automatic_series_grouping, "EnableAutomaticSeriesGrouping"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_embedded_titles, "EnableEmbeddedTitles"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_embedded_episode_infos, "EnableEmbeddedEpisodeInfos"
        )
        XmlUtilities.add_as_subelement(
            root, self.automatic_refresh_interval_days, "AutomaticRefreshIntervalDays"
        )
        XmlUtilities.add_as_subelement(
            root, self.preferred_metadata_language, "PreferredMetadataLanguage"
        )
        XmlUtilities.add_as_subelement(
            root, self.metadata_country_code, "MetadataCountryCode"
        )
        XmlUtilities.add_as_subelement(
            root, self.season_zero_display_name, "SeasonZeroDisplayName"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_savers, "MetadataSavers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_local_metadata_readers, "DisabledLocalMetadataReaders"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.local_metadata_reader_order, "LocalMetadataReaderOrder"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_subtitle_fetchers, "DisabledSubtitleFetchers"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.subtitle_fetcher_order, "SubtitleFetcherOrder"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.skip_subtitles_if_embedded_subtitles_present,
            "SkipSubtitlesIfEmbeddedSubtitlesPresent",
        )
        XmlUtilities.add_as_subelement(
            root,
            self.skip_subtitles_if_audio_track_matches,
            "SkipSubtitlesIfAudioTrackMatches",
        )
        XmlUtilities.add_list_as_subelement(
            root, self.subtitle_download_languages, "SubtitleDownloadLanguages"
        )
        XmlUtilities.add_as_subelement(
            root, self.require_perfect_subtitle_match, "RequirePerfectSubtitleMatch"
        )
        XmlUtilities.add_as_subelement(
            root, self.save_subtitles_with_media, "SaveSubtitlesWithMedia"
        )
        XmlUtilities.add_as_subelement(
            root, self.automatically_add_to_collection, "AutomaticallyAddToCollection"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_embedded_subtitles, "AllowEmbeddedSubtitles"
        )
        XmlUtilities.add_list_as_subelement(root, self.type_options, "TypeOptions")
