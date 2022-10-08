
# Live Tv Options

## Structure

`LiveTvOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `guide_days` | `int` | Optional | - |
| `recording_path` | `string` | Optional | - |
| `movie_recording_path` | `string` | Optional | - |
| `series_recording_path` | `string` | Optional | - |
| `enable_recording_subfolders` | `bool` | Optional | - |
| `enable_original_audio_with_encoded_recordings` | `bool` | Optional | - |
| `tuner_hosts` | [`List of TunerHostInfo`](../../doc/models/tuner-host-info.md) | Optional | - |
| `listing_providers` | [`List of ListingsProviderInfo`](../../doc/models/listings-provider-info.md) | Optional | - |
| `pre_padding_seconds` | `int` | Optional | - |
| `post_padding_seconds` | `int` | Optional | - |
| `media_locations_created` | `List of string` | Optional | - |
| `recording_post_processor` | `string` | Optional | - |
| `recording_post_processor_arguments` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "GuideDays": null,
  "RecordingPath": null,
  "MovieRecordingPath": null,
  "SeriesRecordingPath": null,
  "EnableRecordingSubfolders": null,
  "EnableOriginalAudioWithEncodedRecordings": null,
  "TunerHosts": null,
  "ListingProviders": null,
  "PrePaddingSeconds": null,
  "PostPaddingSeconds": null,
  "MediaLocationsCreated": null,
  "RecordingPostProcessor": null,
  "RecordingPostProcessorArguments": null
}
```

