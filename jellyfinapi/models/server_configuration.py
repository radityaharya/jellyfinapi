# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.metadata_options import MetadataOptions
from jellyfinapi.models.name_value_pair import NameValuePair
from jellyfinapi.models.path_substitution import PathSubstitution
from jellyfinapi.models.repository_info import RepositoryInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ServerConfiguration(object):

    """Implementation of the 'ServerConfiguration' model.

    Represents the server configuration.

    Attributes:
        log_file_retention_days (int): Gets or sets the number of days we
            should retain log files.
        is_startup_wizard_completed (bool): Gets or sets a value indicating
            whether this instance is first run.
        cache_path (string): Gets or sets the cache path.
        previous_version (string): Gets or sets the last known version that
            was ran using the configuration.
        previous_version_str (string): Gets or sets the stringified
            PreviousVersion to be stored/loaded,  because System.Version
            itself isn't xml-serializable.
        enable_metrics (bool): Gets or sets a value indicating whether to
            enable prometheus metrics exporting.
        enable_normalized_item_by_name_ids (bool): TODO: type description
            here.
        is_port_authorized (bool): Gets or sets a value indicating whether
            this instance is port authorized.
        quick_connect_available (bool): Gets or sets a value indicating
            whether quick connect is available for use on this server.
        enable_case_sensitive_item_ids (bool): Gets or sets a value indicating
            whether [enable case sensitive item ids].
        disable_live_tv_channel_user_data_name (bool): TODO: type description
            here.
        metadata_path (string): Gets or sets the metadata path.
        metadata_network_path (string): TODO: type description here.
        preferred_metadata_language (string): Gets or sets the preferred
            metadata language.
        metadata_country_code (string): Gets or sets the metadata country
            code.
        sort_replace_characters (list of string): Gets or sets characters to
            be replaced with a ' ' in strings to create a sort name.
        sort_remove_characters (list of string): Gets or sets characters to be
            removed from strings to create a sort name.
        sort_remove_words (list of string): Gets or sets words to be removed
            from strings to create a sort name.
        min_resume_pct (int): Gets or sets the minimum percentage of an item
            that must be played in order for playstate to be updated.
        max_resume_pct (int): Gets or sets the maximum percentage of an item
            that can be played while still saving playstate. If this
            percentage is crossed playstate will be reset to the beginning and
            the item will be marked watched.
        min_resume_duration_seconds (int): Gets or sets the minimum duration
            that an item must have in order to be eligible for playstate
            updates..
        min_audiobook_resume (int): Gets or sets the minimum minutes of a book
            that must be played in order for playstate to be updated.
        max_audiobook_resume (int): Gets or sets the remaining minutes of a
            book that can be played while still saving playstate. If this
            percentage is crossed playstate will be reset to the beginning and
            the item will be marked watched.
        library_monitor_delay (int): Gets or sets the delay in seconds that we
            will wait after a file system change to try and discover what has
            been added/removed  Some delay is necessary with some items
            because their creation is not atomic.  It involves the creation of
            several  different directories and files.
        image_saving_convention (ImageSavingConventionEnum): Gets or sets the
            image saving convention.
        metadata_options (list of MetadataOptions): TODO: type description
            here.
        skip_deserialization_for_basic_types (bool): TODO: type description
            here.
        server_name (string): TODO: type description here.
        ui_culture (string): TODO: type description here.
        save_metadata_hidden (bool): TODO: type description here.
        content_types (list of NameValuePair): TODO: type description here.
        remote_client_bitrate_limit (int): TODO: type description here.
        enable_folder_view (bool): TODO: type description here.
        enable_grouping_into_collections (bool): TODO: type description here.
        display_specials_within_seasons (bool): TODO: type description here.
        codecs_used (list of string): TODO: type description here.
        plugin_repositories (list of RepositoryInfo): TODO: type description
            here.
        enable_external_content_in_suggestions (bool): TODO: type description
            here.
        image_extraction_timeout_ms (int): TODO: type description here.
        path_substitutions (list of PathSubstitution): TODO: type description
            here.
        enable_slow_response_warning (bool): Gets or sets a value indicating
            whether slow server responses should be logged as a warning.
        slow_response_threshold_ms (long|int): Gets or sets the threshold for
            the slow response time warning in ms.
        cors_hosts (list of string): Gets or sets the cors hosts.
        activity_log_retention_days (int): Gets or sets the number of days we
            should retain activity logs.
        library_scan_fanout_concurrency (int): Gets or sets the how the
            library scan fans out.
        library_metadata_refresh_concurrency (int): Gets or sets the how many
            metadata refreshes can run concurrently.
        remove_old_plugins (bool): Gets or sets a value indicating whether
            older plugins should automatically be deleted from the plugin
            folder.
        allow_client_log_upload (bool): Gets or sets a value indicating
            whether clients should be allowed to upload logs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "log_file_retention_days": "LogFileRetentionDays",
        "is_startup_wizard_completed": "IsStartupWizardCompleted",
        "cache_path": "CachePath",
        "previous_version": "PreviousVersion",
        "previous_version_str": "PreviousVersionStr",
        "enable_metrics": "EnableMetrics",
        "enable_normalized_item_by_name_ids": "EnableNormalizedItemByNameIds",
        "is_port_authorized": "IsPortAuthorized",
        "quick_connect_available": "QuickConnectAvailable",
        "enable_case_sensitive_item_ids": "EnableCaseSensitiveItemIds",
        "disable_live_tv_channel_user_data_name": "DisableLiveTvChannelUserDataName",
        "metadata_path": "MetadataPath",
        "metadata_network_path": "MetadataNetworkPath",
        "preferred_metadata_language": "PreferredMetadataLanguage",
        "metadata_country_code": "MetadataCountryCode",
        "sort_replace_characters": "SortReplaceCharacters",
        "sort_remove_characters": "SortRemoveCharacters",
        "sort_remove_words": "SortRemoveWords",
        "min_resume_pct": "MinResumePct",
        "max_resume_pct": "MaxResumePct",
        "min_resume_duration_seconds": "MinResumeDurationSeconds",
        "min_audiobook_resume": "MinAudiobookResume",
        "max_audiobook_resume": "MaxAudiobookResume",
        "library_monitor_delay": "LibraryMonitorDelay",
        "image_saving_convention": "ImageSavingConvention",
        "metadata_options": "MetadataOptions",
        "skip_deserialization_for_basic_types": "SkipDeserializationForBasicTypes",
        "server_name": "ServerName",
        "ui_culture": "UICulture",
        "save_metadata_hidden": "SaveMetadataHidden",
        "content_types": "ContentTypes",
        "remote_client_bitrate_limit": "RemoteClientBitrateLimit",
        "enable_folder_view": "EnableFolderView",
        "enable_grouping_into_collections": "EnableGroupingIntoCollections",
        "display_specials_within_seasons": "DisplaySpecialsWithinSeasons",
        "codecs_used": "CodecsUsed",
        "plugin_repositories": "PluginRepositories",
        "enable_external_content_in_suggestions": "EnableExternalContentInSuggestions",
        "image_extraction_timeout_ms": "ImageExtractionTimeoutMs",
        "path_substitutions": "PathSubstitutions",
        "enable_slow_response_warning": "EnableSlowResponseWarning",
        "slow_response_threshold_ms": "SlowResponseThresholdMs",
        "cors_hosts": "CorsHosts",
        "activity_log_retention_days": "ActivityLogRetentionDays",
        "library_scan_fanout_concurrency": "LibraryScanFanoutConcurrency",
        "library_metadata_refresh_concurrency": "LibraryMetadataRefreshConcurrency",
        "remove_old_plugins": "RemoveOldPlugins",
        "allow_client_log_upload": "AllowClientLogUpload",
    }

    _optionals = [
        "log_file_retention_days",
        "is_startup_wizard_completed",
        "cache_path",
        "previous_version",
        "previous_version_str",
        "enable_metrics",
        "enable_normalized_item_by_name_ids",
        "is_port_authorized",
        "quick_connect_available",
        "enable_case_sensitive_item_ids",
        "disable_live_tv_channel_user_data_name",
        "metadata_path",
        "metadata_network_path",
        "preferred_metadata_language",
        "metadata_country_code",
        "sort_replace_characters",
        "sort_remove_characters",
        "sort_remove_words",
        "min_resume_pct",
        "max_resume_pct",
        "min_resume_duration_seconds",
        "min_audiobook_resume",
        "max_audiobook_resume",
        "library_monitor_delay",
        "image_saving_convention",
        "metadata_options",
        "skip_deserialization_for_basic_types",
        "server_name",
        "ui_culture",
        "save_metadata_hidden",
        "content_types",
        "remote_client_bitrate_limit",
        "enable_folder_view",
        "enable_grouping_into_collections",
        "display_specials_within_seasons",
        "codecs_used",
        "plugin_repositories",
        "enable_external_content_in_suggestions",
        "image_extraction_timeout_ms",
        "path_substitutions",
        "enable_slow_response_warning",
        "slow_response_threshold_ms",
        "cors_hosts",
        "activity_log_retention_days",
        "library_scan_fanout_concurrency",
        "library_metadata_refresh_concurrency",
        "remove_old_plugins",
        "allow_client_log_upload",
    ]

    _nullables = [
        "cache_path",
        "previous_version",
        "previous_version_str",
        "activity_log_retention_days",
    ]

    def __init__(
        self,
        log_file_retention_days=APIHelper.SKIP,
        is_startup_wizard_completed=APIHelper.SKIP,
        cache_path=APIHelper.SKIP,
        previous_version=APIHelper.SKIP,
        previous_version_str=APIHelper.SKIP,
        enable_metrics=APIHelper.SKIP,
        enable_normalized_item_by_name_ids=APIHelper.SKIP,
        is_port_authorized=APIHelper.SKIP,
        quick_connect_available=APIHelper.SKIP,
        enable_case_sensitive_item_ids=APIHelper.SKIP,
        disable_live_tv_channel_user_data_name=APIHelper.SKIP,
        metadata_path=APIHelper.SKIP,
        metadata_network_path=APIHelper.SKIP,
        preferred_metadata_language=APIHelper.SKIP,
        metadata_country_code=APIHelper.SKIP,
        sort_replace_characters=APIHelper.SKIP,
        sort_remove_characters=APIHelper.SKIP,
        sort_remove_words=APIHelper.SKIP,
        min_resume_pct=APIHelper.SKIP,
        max_resume_pct=APIHelper.SKIP,
        min_resume_duration_seconds=APIHelper.SKIP,
        min_audiobook_resume=APIHelper.SKIP,
        max_audiobook_resume=APIHelper.SKIP,
        library_monitor_delay=APIHelper.SKIP,
        image_saving_convention=APIHelper.SKIP,
        metadata_options=APIHelper.SKIP,
        skip_deserialization_for_basic_types=APIHelper.SKIP,
        server_name=APIHelper.SKIP,
        ui_culture=APIHelper.SKIP,
        save_metadata_hidden=APIHelper.SKIP,
        content_types=APIHelper.SKIP,
        remote_client_bitrate_limit=APIHelper.SKIP,
        enable_folder_view=APIHelper.SKIP,
        enable_grouping_into_collections=APIHelper.SKIP,
        display_specials_within_seasons=APIHelper.SKIP,
        codecs_used=APIHelper.SKIP,
        plugin_repositories=APIHelper.SKIP,
        enable_external_content_in_suggestions=APIHelper.SKIP,
        image_extraction_timeout_ms=APIHelper.SKIP,
        path_substitutions=APIHelper.SKIP,
        enable_slow_response_warning=APIHelper.SKIP,
        slow_response_threshold_ms=APIHelper.SKIP,
        cors_hosts=APIHelper.SKIP,
        activity_log_retention_days=APIHelper.SKIP,
        library_scan_fanout_concurrency=APIHelper.SKIP,
        library_metadata_refresh_concurrency=APIHelper.SKIP,
        remove_old_plugins=APIHelper.SKIP,
        allow_client_log_upload=APIHelper.SKIP,
    ):
        """Constructor for the ServerConfiguration class"""

        # Initialize members of the class
        if log_file_retention_days is not APIHelper.SKIP:
            self.log_file_retention_days = log_file_retention_days
        if is_startup_wizard_completed is not APIHelper.SKIP:
            self.is_startup_wizard_completed = is_startup_wizard_completed
        if cache_path is not APIHelper.SKIP:
            self.cache_path = cache_path
        if previous_version is not APIHelper.SKIP:
            self.previous_version = previous_version
        if previous_version_str is not APIHelper.SKIP:
            self.previous_version_str = previous_version_str
        if enable_metrics is not APIHelper.SKIP:
            self.enable_metrics = enable_metrics
        if enable_normalized_item_by_name_ids is not APIHelper.SKIP:
            self.enable_normalized_item_by_name_ids = enable_normalized_item_by_name_ids
        if is_port_authorized is not APIHelper.SKIP:
            self.is_port_authorized = is_port_authorized
        if quick_connect_available is not APIHelper.SKIP:
            self.quick_connect_available = quick_connect_available
        if enable_case_sensitive_item_ids is not APIHelper.SKIP:
            self.enable_case_sensitive_item_ids = enable_case_sensitive_item_ids
        if disable_live_tv_channel_user_data_name is not APIHelper.SKIP:
            self.disable_live_tv_channel_user_data_name = (
                disable_live_tv_channel_user_data_name
            )
        if metadata_path is not APIHelper.SKIP:
            self.metadata_path = metadata_path
        if metadata_network_path is not APIHelper.SKIP:
            self.metadata_network_path = metadata_network_path
        if preferred_metadata_language is not APIHelper.SKIP:
            self.preferred_metadata_language = preferred_metadata_language
        if metadata_country_code is not APIHelper.SKIP:
            self.metadata_country_code = metadata_country_code
        if sort_replace_characters is not APIHelper.SKIP:
            self.sort_replace_characters = sort_replace_characters
        if sort_remove_characters is not APIHelper.SKIP:
            self.sort_remove_characters = sort_remove_characters
        if sort_remove_words is not APIHelper.SKIP:
            self.sort_remove_words = sort_remove_words
        if min_resume_pct is not APIHelper.SKIP:
            self.min_resume_pct = min_resume_pct
        if max_resume_pct is not APIHelper.SKIP:
            self.max_resume_pct = max_resume_pct
        if min_resume_duration_seconds is not APIHelper.SKIP:
            self.min_resume_duration_seconds = min_resume_duration_seconds
        if min_audiobook_resume is not APIHelper.SKIP:
            self.min_audiobook_resume = min_audiobook_resume
        if max_audiobook_resume is not APIHelper.SKIP:
            self.max_audiobook_resume = max_audiobook_resume
        if library_monitor_delay is not APIHelper.SKIP:
            self.library_monitor_delay = library_monitor_delay
        if image_saving_convention is not APIHelper.SKIP:
            self.image_saving_convention = image_saving_convention
        if metadata_options is not APIHelper.SKIP:
            self.metadata_options = metadata_options
        if skip_deserialization_for_basic_types is not APIHelper.SKIP:
            self.skip_deserialization_for_basic_types = (
                skip_deserialization_for_basic_types
            )
        if server_name is not APIHelper.SKIP:
            self.server_name = server_name
        if ui_culture is not APIHelper.SKIP:
            self.ui_culture = ui_culture
        if save_metadata_hidden is not APIHelper.SKIP:
            self.save_metadata_hidden = save_metadata_hidden
        if content_types is not APIHelper.SKIP:
            self.content_types = content_types
        if remote_client_bitrate_limit is not APIHelper.SKIP:
            self.remote_client_bitrate_limit = remote_client_bitrate_limit
        if enable_folder_view is not APIHelper.SKIP:
            self.enable_folder_view = enable_folder_view
        if enable_grouping_into_collections is not APIHelper.SKIP:
            self.enable_grouping_into_collections = enable_grouping_into_collections
        if display_specials_within_seasons is not APIHelper.SKIP:
            self.display_specials_within_seasons = display_specials_within_seasons
        if codecs_used is not APIHelper.SKIP:
            self.codecs_used = codecs_used
        if plugin_repositories is not APIHelper.SKIP:
            self.plugin_repositories = plugin_repositories
        if enable_external_content_in_suggestions is not APIHelper.SKIP:
            self.enable_external_content_in_suggestions = (
                enable_external_content_in_suggestions
            )
        if image_extraction_timeout_ms is not APIHelper.SKIP:
            self.image_extraction_timeout_ms = image_extraction_timeout_ms
        if path_substitutions is not APIHelper.SKIP:
            self.path_substitutions = path_substitutions
        if enable_slow_response_warning is not APIHelper.SKIP:
            self.enable_slow_response_warning = enable_slow_response_warning
        if slow_response_threshold_ms is not APIHelper.SKIP:
            self.slow_response_threshold_ms = slow_response_threshold_ms
        if cors_hosts is not APIHelper.SKIP:
            self.cors_hosts = cors_hosts
        if activity_log_retention_days is not APIHelper.SKIP:
            self.activity_log_retention_days = activity_log_retention_days
        if library_scan_fanout_concurrency is not APIHelper.SKIP:
            self.library_scan_fanout_concurrency = library_scan_fanout_concurrency
        if library_metadata_refresh_concurrency is not APIHelper.SKIP:
            self.library_metadata_refresh_concurrency = (
                library_metadata_refresh_concurrency
            )
        if remove_old_plugins is not APIHelper.SKIP:
            self.remove_old_plugins = remove_old_plugins
        if allow_client_log_upload is not APIHelper.SKIP:
            self.allow_client_log_upload = allow_client_log_upload

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

        log_file_retention_days = (
            dictionary.get("LogFileRetentionDays")
            if dictionary.get("LogFileRetentionDays")
            else APIHelper.SKIP
        )
        is_startup_wizard_completed = (
            dictionary.get("IsStartupWizardCompleted")
            if "IsStartupWizardCompleted" in dictionary.keys()
            else APIHelper.SKIP
        )
        cache_path = (
            dictionary.get("CachePath")
            if "CachePath" in dictionary.keys()
            else APIHelper.SKIP
        )
        previous_version = (
            dictionary.get("PreviousVersion")
            if "PreviousVersion" in dictionary.keys()
            else APIHelper.SKIP
        )
        previous_version_str = (
            dictionary.get("PreviousVersionStr")
            if "PreviousVersionStr" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_metrics = (
            dictionary.get("EnableMetrics")
            if "EnableMetrics" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_normalized_item_by_name_ids = (
            dictionary.get("EnableNormalizedItemByNameIds")
            if "EnableNormalizedItemByNameIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_port_authorized = (
            dictionary.get("IsPortAuthorized")
            if "IsPortAuthorized" in dictionary.keys()
            else APIHelper.SKIP
        )
        quick_connect_available = (
            dictionary.get("QuickConnectAvailable")
            if "QuickConnectAvailable" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_case_sensitive_item_ids = (
            dictionary.get("EnableCaseSensitiveItemIds")
            if "EnableCaseSensitiveItemIds" in dictionary.keys()
            else APIHelper.SKIP
        )
        disable_live_tv_channel_user_data_name = (
            dictionary.get("DisableLiveTvChannelUserDataName")
            if "DisableLiveTvChannelUserDataName" in dictionary.keys()
            else APIHelper.SKIP
        )
        metadata_path = (
            dictionary.get("MetadataPath")
            if dictionary.get("MetadataPath")
            else APIHelper.SKIP
        )
        metadata_network_path = (
            dictionary.get("MetadataNetworkPath")
            if dictionary.get("MetadataNetworkPath")
            else APIHelper.SKIP
        )
        preferred_metadata_language = (
            dictionary.get("PreferredMetadataLanguage")
            if dictionary.get("PreferredMetadataLanguage")
            else APIHelper.SKIP
        )
        metadata_country_code = (
            dictionary.get("MetadataCountryCode")
            if dictionary.get("MetadataCountryCode")
            else APIHelper.SKIP
        )
        sort_replace_characters = (
            dictionary.get("SortReplaceCharacters")
            if dictionary.get("SortReplaceCharacters")
            else APIHelper.SKIP
        )
        sort_remove_characters = (
            dictionary.get("SortRemoveCharacters")
            if dictionary.get("SortRemoveCharacters")
            else APIHelper.SKIP
        )
        sort_remove_words = (
            dictionary.get("SortRemoveWords")
            if dictionary.get("SortRemoveWords")
            else APIHelper.SKIP
        )
        min_resume_pct = (
            dictionary.get("MinResumePct")
            if dictionary.get("MinResumePct")
            else APIHelper.SKIP
        )
        max_resume_pct = (
            dictionary.get("MaxResumePct")
            if dictionary.get("MaxResumePct")
            else APIHelper.SKIP
        )
        min_resume_duration_seconds = (
            dictionary.get("MinResumeDurationSeconds")
            if dictionary.get("MinResumeDurationSeconds")
            else APIHelper.SKIP
        )
        min_audiobook_resume = (
            dictionary.get("MinAudiobookResume")
            if dictionary.get("MinAudiobookResume")
            else APIHelper.SKIP
        )
        max_audiobook_resume = (
            dictionary.get("MaxAudiobookResume")
            if dictionary.get("MaxAudiobookResume")
            else APIHelper.SKIP
        )
        library_monitor_delay = (
            dictionary.get("LibraryMonitorDelay")
            if dictionary.get("LibraryMonitorDelay")
            else APIHelper.SKIP
        )
        image_saving_convention = (
            dictionary.get("ImageSavingConvention")
            if dictionary.get("ImageSavingConvention")
            else APIHelper.SKIP
        )
        metadata_options = None
        if dictionary.get("MetadataOptions") is not None:
            metadata_options = [
                MetadataOptions.from_dictionary(x)
                for x in dictionary.get("MetadataOptions")
            ]
        else:
            metadata_options = APIHelper.SKIP
        skip_deserialization_for_basic_types = (
            dictionary.get("SkipDeserializationForBasicTypes")
            if "SkipDeserializationForBasicTypes" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_name = (
            dictionary.get("ServerName")
            if dictionary.get("ServerName")
            else APIHelper.SKIP
        )
        ui_culture = (
            dictionary.get("UICulture")
            if dictionary.get("UICulture")
            else APIHelper.SKIP
        )
        save_metadata_hidden = (
            dictionary.get("SaveMetadataHidden")
            if "SaveMetadataHidden" in dictionary.keys()
            else APIHelper.SKIP
        )
        content_types = None
        if dictionary.get("ContentTypes") is not None:
            content_types = [
                NameValuePair.from_dictionary(x) for x in dictionary.get("ContentTypes")
            ]
        else:
            content_types = APIHelper.SKIP
        remote_client_bitrate_limit = (
            dictionary.get("RemoteClientBitrateLimit")
            if dictionary.get("RemoteClientBitrateLimit")
            else APIHelper.SKIP
        )
        enable_folder_view = (
            dictionary.get("EnableFolderView")
            if "EnableFolderView" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_grouping_into_collections = (
            dictionary.get("EnableGroupingIntoCollections")
            if "EnableGroupingIntoCollections" in dictionary.keys()
            else APIHelper.SKIP
        )
        display_specials_within_seasons = (
            dictionary.get("DisplaySpecialsWithinSeasons")
            if "DisplaySpecialsWithinSeasons" in dictionary.keys()
            else APIHelper.SKIP
        )
        codecs_used = (
            dictionary.get("CodecsUsed")
            if dictionary.get("CodecsUsed")
            else APIHelper.SKIP
        )
        plugin_repositories = None
        if dictionary.get("PluginRepositories") is not None:
            plugin_repositories = [
                RepositoryInfo.from_dictionary(x)
                for x in dictionary.get("PluginRepositories")
            ]
        else:
            plugin_repositories = APIHelper.SKIP
        enable_external_content_in_suggestions = (
            dictionary.get("EnableExternalContentInSuggestions")
            if "EnableExternalContentInSuggestions" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_extraction_timeout_ms = (
            dictionary.get("ImageExtractionTimeoutMs")
            if dictionary.get("ImageExtractionTimeoutMs")
            else APIHelper.SKIP
        )
        path_substitutions = None
        if dictionary.get("PathSubstitutions") is not None:
            path_substitutions = [
                PathSubstitution.from_dictionary(x)
                for x in dictionary.get("PathSubstitutions")
            ]
        else:
            path_substitutions = APIHelper.SKIP
        enable_slow_response_warning = (
            dictionary.get("EnableSlowResponseWarning")
            if "EnableSlowResponseWarning" in dictionary.keys()
            else APIHelper.SKIP
        )
        slow_response_threshold_ms = (
            dictionary.get("SlowResponseThresholdMs")
            if dictionary.get("SlowResponseThresholdMs")
            else APIHelper.SKIP
        )
        cors_hosts = (
            dictionary.get("CorsHosts")
            if dictionary.get("CorsHosts")
            else APIHelper.SKIP
        )
        activity_log_retention_days = (
            dictionary.get("ActivityLogRetentionDays")
            if "ActivityLogRetentionDays" in dictionary.keys()
            else APIHelper.SKIP
        )
        library_scan_fanout_concurrency = (
            dictionary.get("LibraryScanFanoutConcurrency")
            if dictionary.get("LibraryScanFanoutConcurrency")
            else APIHelper.SKIP
        )
        library_metadata_refresh_concurrency = (
            dictionary.get("LibraryMetadataRefreshConcurrency")
            if dictionary.get("LibraryMetadataRefreshConcurrency")
            else APIHelper.SKIP
        )
        remove_old_plugins = (
            dictionary.get("RemoveOldPlugins")
            if "RemoveOldPlugins" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_client_log_upload = (
            dictionary.get("AllowClientLogUpload")
            if "AllowClientLogUpload" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            log_file_retention_days,
            is_startup_wizard_completed,
            cache_path,
            previous_version,
            previous_version_str,
            enable_metrics,
            enable_normalized_item_by_name_ids,
            is_port_authorized,
            quick_connect_available,
            enable_case_sensitive_item_ids,
            disable_live_tv_channel_user_data_name,
            metadata_path,
            metadata_network_path,
            preferred_metadata_language,
            metadata_country_code,
            sort_replace_characters,
            sort_remove_characters,
            sort_remove_words,
            min_resume_pct,
            max_resume_pct,
            min_resume_duration_seconds,
            min_audiobook_resume,
            max_audiobook_resume,
            library_monitor_delay,
            image_saving_convention,
            metadata_options,
            skip_deserialization_for_basic_types,
            server_name,
            ui_culture,
            save_metadata_hidden,
            content_types,
            remote_client_bitrate_limit,
            enable_folder_view,
            enable_grouping_into_collections,
            display_specials_within_seasons,
            codecs_used,
            plugin_repositories,
            enable_external_content_in_suggestions,
            image_extraction_timeout_ms,
            path_substitutions,
            enable_slow_response_warning,
            slow_response_threshold_ms,
            cors_hosts,
            activity_log_retention_days,
            library_scan_fanout_concurrency,
            library_metadata_refresh_concurrency,
            remove_old_plugins,
            allow_client_log_upload,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        log_file_retention_days = XmlUtilities.value_from_xml_element(
            root.find("LogFileRetentionDays"), int
        )
        is_startup_wizard_completed = XmlUtilities.value_from_xml_element(
            root.find("IsStartupWizardCompleted"), bool
        )
        cache_path = XmlUtilities.value_from_xml_element(root.find("CachePath"), str)
        previous_version = XmlUtilities.value_from_xml_element(
            root.find("PreviousVersion"), str
        )
        previous_version_str = XmlUtilities.value_from_xml_element(
            root.find("PreviousVersionStr"), str
        )
        enable_metrics = XmlUtilities.value_from_xml_element(
            root.find("EnableMetrics"), bool
        )
        enable_normalized_item_by_name_ids = XmlUtilities.value_from_xml_element(
            root.find("EnableNormalizedItemByNameIds"), bool
        )
        is_port_authorized = XmlUtilities.value_from_xml_element(
            root.find("IsPortAuthorized"), bool
        )
        quick_connect_available = XmlUtilities.value_from_xml_element(
            root.find("QuickConnectAvailable"), bool
        )
        enable_case_sensitive_item_ids = XmlUtilities.value_from_xml_element(
            root.find("EnableCaseSensitiveItemIds"), bool
        )
        disable_live_tv_channel_user_data_name = XmlUtilities.value_from_xml_element(
            root.find("DisableLiveTvChannelUserDataName"), bool
        )
        metadata_path = XmlUtilities.value_from_xml_element(
            root.find("MetadataPath"), str
        )
        metadata_network_path = XmlUtilities.value_from_xml_element(
            root.find("MetadataNetworkPath"), str
        )
        preferred_metadata_language = XmlUtilities.value_from_xml_element(
            root.find("PreferredMetadataLanguage"), str
        )
        metadata_country_code = XmlUtilities.value_from_xml_element(
            root.find("MetadataCountryCode"), str
        )
        sort_replace_characters = XmlUtilities.list_from_xml_element(
            root, "SortReplaceCharacters", str
        )
        sort_remove_characters = XmlUtilities.list_from_xml_element(
            root, "SortRemoveCharacters", str
        )
        sort_remove_words = XmlUtilities.list_from_xml_element(
            root, "SortRemoveWords", str
        )
        min_resume_pct = XmlUtilities.value_from_xml_element(
            root.find("MinResumePct"), int
        )
        max_resume_pct = XmlUtilities.value_from_xml_element(
            root.find("MaxResumePct"), int
        )
        min_resume_duration_seconds = XmlUtilities.value_from_xml_element(
            root.find("MinResumeDurationSeconds"), int
        )
        min_audiobook_resume = XmlUtilities.value_from_xml_element(
            root.find("MinAudiobookResume"), int
        )
        max_audiobook_resume = XmlUtilities.value_from_xml_element(
            root.find("MaxAudiobookResume"), int
        )
        library_monitor_delay = XmlUtilities.value_from_xml_element(
            root.find("LibraryMonitorDelay"), int
        )
        image_saving_convention = XmlUtilities.value_from_xml_element(
            root.find("ImageSavingConvention"), str
        )
        metadata_options = XmlUtilities.list_from_xml_element(
            root, "MetadataOptions", MetadataOptions
        )
        skip_deserialization_for_basic_types = XmlUtilities.value_from_xml_element(
            root.find("SkipDeserializationForBasicTypes"), bool
        )
        server_name = XmlUtilities.value_from_xml_element(root.find("ServerName"), str)
        ui_culture = XmlUtilities.value_from_xml_element(root.find("UICulture"), str)
        save_metadata_hidden = XmlUtilities.value_from_xml_element(
            root.find("SaveMetadataHidden"), bool
        )
        content_types = XmlUtilities.list_from_xml_element(
            root, "NameValuePair", NameValuePair
        )
        remote_client_bitrate_limit = XmlUtilities.value_from_xml_element(
            root.find("RemoteClientBitrateLimit"), int
        )
        enable_folder_view = XmlUtilities.value_from_xml_element(
            root.find("EnableFolderView"), bool
        )
        enable_grouping_into_collections = XmlUtilities.value_from_xml_element(
            root.find("EnableGroupingIntoCollections"), bool
        )
        display_specials_within_seasons = XmlUtilities.value_from_xml_element(
            root.find("DisplaySpecialsWithinSeasons"), bool
        )
        codecs_used = XmlUtilities.list_from_xml_element(root, "CodecsUsed", str)
        plugin_repositories = XmlUtilities.list_from_xml_element(
            root, "RepositoryInfo", RepositoryInfo
        )
        enable_external_content_in_suggestions = XmlUtilities.value_from_xml_element(
            root.find("EnableExternalContentInSuggestions"), bool
        )
        image_extraction_timeout_ms = XmlUtilities.value_from_xml_element(
            root.find("ImageExtractionTimeoutMs"), int
        )
        path_substitutions = XmlUtilities.list_from_xml_element(
            root, "PathSubstitution", PathSubstitution
        )
        enable_slow_response_warning = XmlUtilities.value_from_xml_element(
            root.find("EnableSlowResponseWarning"), bool
        )
        slow_response_threshold_ms = XmlUtilities.value_from_xml_element(
            root.find("SlowResponseThresholdMs"), int
        )
        cors_hosts = XmlUtilities.list_from_xml_element(root, "CorsHosts", str)
        activity_log_retention_days = XmlUtilities.value_from_xml_element(
            root.find("ActivityLogRetentionDays"), int
        )
        library_scan_fanout_concurrency = XmlUtilities.value_from_xml_element(
            root.find("LibraryScanFanoutConcurrency"), int
        )
        library_metadata_refresh_concurrency = XmlUtilities.value_from_xml_element(
            root.find("LibraryMetadataRefreshConcurrency"), int
        )
        remove_old_plugins = XmlUtilities.value_from_xml_element(
            root.find("RemoveOldPlugins"), bool
        )
        allow_client_log_upload = XmlUtilities.value_from_xml_element(
            root.find("AllowClientLogUpload"), bool
        )

        return cls(
            log_file_retention_days,
            is_startup_wizard_completed,
            cache_path,
            previous_version,
            previous_version_str,
            enable_metrics,
            enable_normalized_item_by_name_ids,
            is_port_authorized,
            quick_connect_available,
            enable_case_sensitive_item_ids,
            disable_live_tv_channel_user_data_name,
            metadata_path,
            metadata_network_path,
            preferred_metadata_language,
            metadata_country_code,
            sort_replace_characters,
            sort_remove_characters,
            sort_remove_words,
            min_resume_pct,
            max_resume_pct,
            min_resume_duration_seconds,
            min_audiobook_resume,
            max_audiobook_resume,
            library_monitor_delay,
            image_saving_convention,
            metadata_options,
            skip_deserialization_for_basic_types,
            server_name,
            ui_culture,
            save_metadata_hidden,
            content_types,
            remote_client_bitrate_limit,
            enable_folder_view,
            enable_grouping_into_collections,
            display_specials_within_seasons,
            codecs_used,
            plugin_repositories,
            enable_external_content_in_suggestions,
            image_extraction_timeout_ms,
            path_substitutions,
            enable_slow_response_warning,
            slow_response_threshold_ms,
            cors_hosts,
            activity_log_retention_days,
            library_scan_fanout_concurrency,
            library_metadata_refresh_concurrency,
            remove_old_plugins,
            allow_client_log_upload,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.log_file_retention_days, "LogFileRetentionDays"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_startup_wizard_completed, "IsStartupWizardCompleted"
        )
        XmlUtilities.add_as_subelement(root, self.cache_path, "CachePath")
        XmlUtilities.add_as_subelement(root, self.previous_version, "PreviousVersion")
        XmlUtilities.add_as_subelement(
            root, self.previous_version_str, "PreviousVersionStr"
        )
        XmlUtilities.add_as_subelement(root, self.enable_metrics, "EnableMetrics")
        XmlUtilities.add_as_subelement(
            root,
            self.enable_normalized_item_by_name_ids,
            "EnableNormalizedItemByNameIds",
        )
        XmlUtilities.add_as_subelement(
            root, self.is_port_authorized, "IsPortAuthorized"
        )
        XmlUtilities.add_as_subelement(
            root, self.quick_connect_available, "QuickConnectAvailable"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_case_sensitive_item_ids, "EnableCaseSensitiveItemIds"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.disable_live_tv_channel_user_data_name,
            "DisableLiveTvChannelUserDataName",
        )
        XmlUtilities.add_as_subelement(root, self.metadata_path, "MetadataPath")
        XmlUtilities.add_as_subelement(
            root, self.metadata_network_path, "MetadataNetworkPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.preferred_metadata_language, "PreferredMetadataLanguage"
        )
        XmlUtilities.add_as_subelement(
            root, self.metadata_country_code, "MetadataCountryCode"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.sort_replace_characters, "SortReplaceCharacters"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.sort_remove_characters, "SortRemoveCharacters"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.sort_remove_words, "SortRemoveWords"
        )
        XmlUtilities.add_as_subelement(root, self.min_resume_pct, "MinResumePct")
        XmlUtilities.add_as_subelement(root, self.max_resume_pct, "MaxResumePct")
        XmlUtilities.add_as_subelement(
            root, self.min_resume_duration_seconds, "MinResumeDurationSeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.min_audiobook_resume, "MinAudiobookResume"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_audiobook_resume, "MaxAudiobookResume"
        )
        XmlUtilities.add_as_subelement(
            root, self.library_monitor_delay, "LibraryMonitorDelay"
        )
        XmlUtilities.add_as_subelement(
            root, self.image_saving_convention, "ImageSavingConvention"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_options, "MetadataOptions"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.skip_deserialization_for_basic_types,
            "SkipDeserializationForBasicTypes",
        )
        XmlUtilities.add_as_subelement(root, self.server_name, "ServerName")
        XmlUtilities.add_as_subelement(root, self.ui_culture, "UICulture")
        XmlUtilities.add_as_subelement(
            root, self.save_metadata_hidden, "SaveMetadataHidden"
        )
        XmlUtilities.add_list_as_subelement(root, self.content_types, "NameValuePair")
        XmlUtilities.add_as_subelement(
            root, self.remote_client_bitrate_limit, "RemoteClientBitrateLimit"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_folder_view, "EnableFolderView"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_grouping_into_collections, "EnableGroupingIntoCollections"
        )
        XmlUtilities.add_as_subelement(
            root, self.display_specials_within_seasons, "DisplaySpecialsWithinSeasons"
        )
        XmlUtilities.add_list_as_subelement(root, self.codecs_used, "CodecsUsed")
        XmlUtilities.add_list_as_subelement(
            root, self.plugin_repositories, "RepositoryInfo"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_external_content_in_suggestions,
            "EnableExternalContentInSuggestions",
        )
        XmlUtilities.add_as_subelement(
            root, self.image_extraction_timeout_ms, "ImageExtractionTimeoutMs"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.path_substitutions, "PathSubstitution"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_slow_response_warning, "EnableSlowResponseWarning"
        )
        XmlUtilities.add_as_subelement(
            root, self.slow_response_threshold_ms, "SlowResponseThresholdMs"
        )
        XmlUtilities.add_list_as_subelement(root, self.cors_hosts, "CorsHosts")
        XmlUtilities.add_as_subelement(
            root, self.activity_log_retention_days, "ActivityLogRetentionDays"
        )
        XmlUtilities.add_as_subelement(
            root, self.library_scan_fanout_concurrency, "LibraryScanFanoutConcurrency"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.library_metadata_refresh_concurrency,
            "LibraryMetadataRefreshConcurrency",
        )
        XmlUtilities.add_as_subelement(
            root, self.remove_old_plugins, "RemoveOldPlugins"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_client_log_upload, "AllowClientLogUpload"
        )
