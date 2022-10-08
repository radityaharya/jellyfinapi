
# Server Configuration

Represents the server configuration.

## Structure

`ServerConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `log_file_retention_days` | `int` | Optional | Gets or sets the number of days we should retain log files. |
| `is_startup_wizard_completed` | `bool` | Optional | Gets or sets a value indicating whether this instance is first run. |
| `cache_path` | `string` | Optional | Gets or sets the cache path. |
| `previous_version` | `string` | Optional | Gets or sets the last known version that was ran using the configuration. |
| `previous_version_str` | `string` | Optional | Gets or sets the stringified PreviousVersion to be stored/loaded,<br>because System.Version itself isn't xml-serializable. |
| `enable_metrics` | `bool` | Optional | Gets or sets a value indicating whether to enable prometheus metrics exporting. |
| `enable_normalized_item_by_name_ids` | `bool` | Optional | - |
| `is_port_authorized` | `bool` | Optional | Gets or sets a value indicating whether this instance is port authorized. |
| `quick_connect_available` | `bool` | Optional | Gets or sets a value indicating whether quick connect is available for use on this server. |
| `enable_case_sensitive_item_ids` | `bool` | Optional | Gets or sets a value indicating whether [enable case sensitive item ids]. |
| `disable_live_tv_channel_user_data_name` | `bool` | Optional | - |
| `metadata_path` | `string` | Optional | Gets or sets the metadata path. |
| `metadata_network_path` | `string` | Optional | - |
| `preferred_metadata_language` | `string` | Optional | Gets or sets the preferred metadata language. |
| `metadata_country_code` | `string` | Optional | Gets or sets the metadata country code. |
| `sort_replace_characters` | `List of string` | Optional | Gets or sets characters to be replaced with a ' ' in strings to create a sort name. |
| `sort_remove_characters` | `List of string` | Optional | Gets or sets characters to be removed from strings to create a sort name. |
| `sort_remove_words` | `List of string` | Optional | Gets or sets words to be removed from strings to create a sort name. |
| `min_resume_pct` | `int` | Optional | Gets or sets the minimum percentage of an item that must be played in order for playstate to be updated. |
| `max_resume_pct` | `int` | Optional | Gets or sets the maximum percentage of an item that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. |
| `min_resume_duration_seconds` | `int` | Optional | Gets or sets the minimum duration that an item must have in order to be eligible for playstate updates.. |
| `min_audiobook_resume` | `int` | Optional | Gets or sets the minimum minutes of a book that must be played in order for playstate to be updated. |
| `max_audiobook_resume` | `int` | Optional | Gets or sets the remaining minutes of a book that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. |
| `library_monitor_delay` | `int` | Optional | Gets or sets the delay in seconds that we will wait after a file system change to try and discover what has been added/removed<br>Some delay is necessary with some items because their creation is not atomic.  It involves the creation of several<br>different directories and files. |
| `image_saving_convention` | [`ImageSavingConventionEnum`](../../doc/models/image-saving-convention-enum.md) | Optional | Gets or sets the image saving convention. |
| `metadata_options` | [`List of MetadataOptions`](../../doc/models/metadata-options.md) | Optional | - |
| `skip_deserialization_for_basic_types` | `bool` | Optional | - |
| `server_name` | `string` | Optional | - |
| `ui_culture` | `string` | Optional | - |
| `save_metadata_hidden` | `bool` | Optional | - |
| `content_types` | [`List of NameValuePair`](../../doc/models/name-value-pair.md) | Optional | - |
| `remote_client_bitrate_limit` | `int` | Optional | - |
| `enable_folder_view` | `bool` | Optional | - |
| `enable_grouping_into_collections` | `bool` | Optional | - |
| `display_specials_within_seasons` | `bool` | Optional | - |
| `codecs_used` | `List of string` | Optional | - |
| `plugin_repositories` | [`List of RepositoryInfo`](../../doc/models/repository-info.md) | Optional | - |
| `enable_external_content_in_suggestions` | `bool` | Optional | - |
| `image_extraction_timeout_ms` | `int` | Optional | - |
| `path_substitutions` | [`List of PathSubstitution`](../../doc/models/path-substitution.md) | Optional | - |
| `enable_slow_response_warning` | `bool` | Optional | Gets or sets a value indicating whether slow server responses should be logged as a warning. |
| `slow_response_threshold_ms` | `long\|int` | Optional | Gets or sets the threshold for the slow response time warning in ms. |
| `cors_hosts` | `List of string` | Optional | Gets or sets the cors hosts. |
| `activity_log_retention_days` | `int` | Optional | Gets or sets the number of days we should retain activity logs. |
| `library_scan_fanout_concurrency` | `int` | Optional | Gets or sets the how the library scan fans out. |
| `library_metadata_refresh_concurrency` | `int` | Optional | Gets or sets the how many metadata refreshes can run concurrently. |
| `remove_old_plugins` | `bool` | Optional | Gets or sets a value indicating whether older plugins should automatically be deleted from the plugin folder. |
| `allow_client_log_upload` | `bool` | Optional | Gets or sets a value indicating whether clients should be allowed to upload logs. |

## Example (as JSON)

```json
{
  "LogFileRetentionDays": null,
  "IsStartupWizardCompleted": null,
  "CachePath": null,
  "PreviousVersion": null,
  "PreviousVersionStr": null,
  "EnableMetrics": null,
  "EnableNormalizedItemByNameIds": null,
  "IsPortAuthorized": null,
  "QuickConnectAvailable": null,
  "EnableCaseSensitiveItemIds": null,
  "DisableLiveTvChannelUserDataName": null,
  "MetadataPath": null,
  "MetadataNetworkPath": null,
  "PreferredMetadataLanguage": null,
  "MetadataCountryCode": null,
  "SortReplaceCharacters": null,
  "SortRemoveCharacters": null,
  "SortRemoveWords": null,
  "MinResumePct": null,
  "MaxResumePct": null,
  "MinResumeDurationSeconds": null,
  "MinAudiobookResume": null,
  "MaxAudiobookResume": null,
  "LibraryMonitorDelay": null,
  "ImageSavingConvention": null,
  "MetadataOptions": null,
  "SkipDeserializationForBasicTypes": null,
  "ServerName": null,
  "UICulture": null,
  "SaveMetadataHidden": null,
  "ContentTypes": null,
  "RemoteClientBitrateLimit": null,
  "EnableFolderView": null,
  "EnableGroupingIntoCollections": null,
  "DisplaySpecialsWithinSeasons": null,
  "CodecsUsed": null,
  "PluginRepositories": null,
  "EnableExternalContentInSuggestions": null,
  "ImageExtractionTimeoutMs": null,
  "PathSubstitutions": null,
  "EnableSlowResponseWarning": null,
  "SlowResponseThresholdMs": null,
  "CorsHosts": null,
  "ActivityLogRetentionDays": null,
  "LibraryScanFanoutConcurrency": null,
  "LibraryMetadataRefreshConcurrency": null,
  "RemoveOldPlugins": null,
  "AllowClientLogUpload": null
}
```

