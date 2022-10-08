
# Library Options

## Structure

`LibraryOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_photos` | `bool` | Optional | - |
| `enable_realtime_monitor` | `bool` | Optional | - |
| `enable_chapter_image_extraction` | `bool` | Optional | - |
| `extract_chapter_images_during_library_scan` | `bool` | Optional | - |
| `path_infos` | [`List of MediaPathInfo`](../../doc/models/media-path-info.md) | Optional | - |
| `save_local_metadata` | `bool` | Optional | - |
| `enable_internet_providers` | `bool` | Optional | - |
| `enable_automatic_series_grouping` | `bool` | Optional | - |
| `enable_embedded_titles` | `bool` | Optional | - |
| `enable_embedded_episode_infos` | `bool` | Optional | - |
| `automatic_refresh_interval_days` | `int` | Optional | - |
| `preferred_metadata_language` | `string` | Optional | Gets or sets the preferred metadata language. |
| `metadata_country_code` | `string` | Optional | Gets or sets the metadata country code. |
| `season_zero_display_name` | `string` | Optional | - |
| `metadata_savers` | `List of string` | Optional | - |
| `disabled_local_metadata_readers` | `List of string` | Optional | - |
| `local_metadata_reader_order` | `List of string` | Optional | - |
| `disabled_subtitle_fetchers` | `List of string` | Optional | - |
| `subtitle_fetcher_order` | `List of string` | Optional | - |
| `skip_subtitles_if_embedded_subtitles_present` | `bool` | Optional | - |
| `skip_subtitles_if_audio_track_matches` | `bool` | Optional | - |
| `subtitle_download_languages` | `List of string` | Optional | - |
| `require_perfect_subtitle_match` | `bool` | Optional | - |
| `save_subtitles_with_media` | `bool` | Optional | - |
| `automatically_add_to_collection` | `bool` | Optional | - |
| `allow_embedded_subtitles` | [`EmbeddedSubtitleOptionsEnum`](../../doc/models/embedded-subtitle-options-enum.md) | Optional | An enum representing the options to disable embedded subs. |
| `type_options` | [`List of TypeOptions`](../../doc/models/type-options.md) | Optional | - |

## Example (as JSON)

```json
{
  "EnablePhotos": null,
  "EnableRealtimeMonitor": null,
  "EnableChapterImageExtraction": null,
  "ExtractChapterImagesDuringLibraryScan": null,
  "PathInfos": null,
  "SaveLocalMetadata": null,
  "EnableInternetProviders": null,
  "EnableAutomaticSeriesGrouping": null,
  "EnableEmbeddedTitles": null,
  "EnableEmbeddedEpisodeInfos": null,
  "AutomaticRefreshIntervalDays": null,
  "PreferredMetadataLanguage": null,
  "MetadataCountryCode": null,
  "SeasonZeroDisplayName": null,
  "MetadataSavers": null,
  "DisabledLocalMetadataReaders": null,
  "LocalMetadataReaderOrder": null,
  "DisabledSubtitleFetchers": null,
  "SubtitleFetcherOrder": null,
  "SkipSubtitlesIfEmbeddedSubtitlesPresent": null,
  "SkipSubtitlesIfAudioTrackMatches": null,
  "SubtitleDownloadLanguages": null,
  "RequirePerfectSubtitleMatch": null,
  "SaveSubtitlesWithMedia": null,
  "AutomaticallyAddToCollection": null,
  "AllowEmbeddedSubtitles": null,
  "TypeOptions": null
}
```

