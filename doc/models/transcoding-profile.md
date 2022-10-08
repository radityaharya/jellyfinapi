
# Transcoding Profile

## Structure

`TranscodingProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `container` | `string` | Optional | - |
| `mtype` | [`DlnaProfileTypeEnum`](../../doc/models/dlna-profile-type-enum.md) | Optional | - |
| `video_codec` | `string` | Optional | - |
| `audio_codec` | `string` | Optional | - |
| `protocol` | `string` | Optional | - |
| `estimate_content_length` | `bool` | Optional | **Default**: `False` |
| `enable_mpegts_m_2_ts_mode` | `bool` | Optional | **Default**: `False` |
| `transcode_seek_info` | [`TranscodeSeekInfoEnum`](../../doc/models/transcode-seek-info-enum.md) | Optional | **Default**: `'Auto'` |
| `copy_timestamps` | `bool` | Optional | **Default**: `False` |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Optional | **Default**: `'Streaming'` |
| `enable_subtitles_in_manifest` | `bool` | Optional | **Default**: `False` |
| `max_audio_channels` | `string` | Optional | - |
| `min_segments` | `int` | Optional | **Default**: `0` |
| `segment_length` | `int` | Optional | **Default**: `0` |
| `break_on_non_key_frames` | `bool` | Optional | **Default**: `False` |
| `conditions` | [`List of ProfileCondition`](../../doc/models/profile-condition.md) | Optional | - |

## Example (as JSON)

```json
{
  "Container": null,
  "Type": null,
  "VideoCodec": null,
  "AudioCodec": null,
  "Protocol": null,
  "EstimateContentLength": null,
  "EnableMpegtsM2TsMode": null,
  "TranscodeSeekInfo": null,
  "CopyTimestamps": null,
  "Context": null,
  "EnableSubtitlesInManifest": null,
  "MaxAudioChannels": null,
  "MinSegments": null,
  "SegmentLength": null,
  "BreakOnNonKeyFrames": null,
  "Conditions": null
}
```

