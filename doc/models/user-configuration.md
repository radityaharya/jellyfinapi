
# User Configuration

Class UserConfiguration.

## Structure

`UserConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `audio_language_preference` | `string` | Optional | Gets or sets the audio language preference. |
| `play_default_audio_track` | `bool` | Optional | Gets or sets a value indicating whether [play default audio track]. |
| `subtitle_language_preference` | `string` | Optional | Gets or sets the subtitle language preference. |
| `display_missing_episodes` | `bool` | Optional | - |
| `grouped_folders` | `List of string` | Optional | - |
| `subtitle_mode` | [`SubtitlePlaybackModeEnum`](../../doc/models/subtitle-playback-mode-enum.md) | Optional | An enum representing a subtitle playback mode. |
| `display_collections_view` | `bool` | Optional | - |
| `enable_local_password` | `bool` | Optional | - |
| `ordered_views` | `List of string` | Optional | - |
| `latest_items_excludes` | `List of string` | Optional | - |
| `my_media_excludes` | `List of string` | Optional | - |
| `hide_played_in_latest` | `bool` | Optional | - |
| `remember_audio_selections` | `bool` | Optional | - |
| `remember_subtitle_selections` | `bool` | Optional | - |
| `enable_next_episode_auto_play` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "AudioLanguagePreference": null,
  "PlayDefaultAudioTrack": null,
  "SubtitleLanguagePreference": null,
  "DisplayMissingEpisodes": null,
  "GroupedFolders": null,
  "SubtitleMode": null,
  "DisplayCollectionsView": null,
  "EnableLocalPassword": null,
  "OrderedViews": null,
  "LatestItemsExcludes": null,
  "MyMediaExcludes": null,
  "HidePlayedInLatest": null,
  "RememberAudioSelections": null,
  "RememberSubtitleSelections": null,
  "EnableNextEpisodeAutoPlay": null
}
```

