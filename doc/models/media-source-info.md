
# Media Source Info

## Structure

`MediaSourceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol` | [`MediaProtocolEnum`](../../doc/models/media-protocol-enum.md) | Optional | - |
| `id` | `string` | Optional | - |
| `path` | `string` | Optional | - |
| `encoder_path` | `string` | Optional | - |
| `encoder_protocol` | [`MediaProtocolEnum`](../../doc/models/media-protocol-enum.md) | Optional | - |
| `mtype` | [`MediaSourceTypeEnum`](../../doc/models/media-source-type-enum.md) | Optional | - |
| `container` | `string` | Optional | - |
| `size` | `long\|int` | Optional | - |
| `name` | `string` | Optional | - |
| `is_remote` | `bool` | Optional | Gets or sets a value indicating whether the media is remote.<br>Differentiate internet url vs local network. |
| `e_tag` | `string` | Optional | - |
| `run_time_ticks` | `long\|int` | Optional | - |
| `read_at_native_framerate` | `bool` | Optional | - |
| `ignore_dts` | `bool` | Optional | - |
| `ignore_index` | `bool` | Optional | - |
| `gen_pts_input` | `bool` | Optional | - |
| `supports_transcoding` | `bool` | Optional | - |
| `supports_direct_stream` | `bool` | Optional | - |
| `supports_direct_play` | `bool` | Optional | - |
| `is_infinite_stream` | `bool` | Optional | - |
| `requires_opening` | `bool` | Optional | - |
| `open_token` | `string` | Optional | - |
| `requires_closing` | `bool` | Optional | - |
| `live_stream_id` | `string` | Optional | - |
| `buffer_ms` | `int` | Optional | - |
| `requires_looping` | `bool` | Optional | - |
| `supports_probing` | `bool` | Optional | - |
| `video_type` | [`VideoTypeEnum`](../../doc/models/video-type-enum.md) | Optional | - |
| `iso_type` | [`IsoTypeEnum`](../../doc/models/iso-type-enum.md) | Optional | - |
| `video_3_d_format` | [`Video3DFormatEnum`](../../doc/models/video-3-d-format-enum.md) | Optional | - |
| `media_streams` | [`List of MediaStream`](../../doc/models/media-stream.md) | Optional | - |
| `media_attachments` | [`List of MediaAttachment`](../../doc/models/media-attachment.md) | Optional | - |
| `formats` | `List of string` | Optional | - |
| `bitrate` | `int` | Optional | - |
| `timestamp` | [`TransportStreamTimestampEnum`](../../doc/models/transport-stream-timestamp-enum.md) | Optional | - |
| `required_http_headers` | `dict` | Optional | - |
| `transcoding_url` | `string` | Optional | - |
| `transcoding_sub_protocol` | `string` | Optional | - |
| `transcoding_container` | `string` | Optional | - |
| `analyze_duration_ms` | `int` | Optional | - |
| `default_audio_stream_index` | `int` | Optional | - |
| `default_subtitle_stream_index` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "Protocol": null,
  "Id": null,
  "Path": null,
  "EncoderPath": null,
  "EncoderProtocol": null,
  "Type": null,
  "Container": null,
  "Size": null,
  "Name": null,
  "IsRemote": null,
  "ETag": null,
  "RunTimeTicks": null,
  "ReadAtNativeFramerate": null,
  "IgnoreDts": null,
  "IgnoreIndex": null,
  "GenPtsInput": null,
  "SupportsTranscoding": null,
  "SupportsDirectStream": null,
  "SupportsDirectPlay": null,
  "IsInfiniteStream": null,
  "RequiresOpening": null,
  "OpenToken": null,
  "RequiresClosing": null,
  "LiveStreamId": null,
  "BufferMs": null,
  "RequiresLooping": null,
  "SupportsProbing": null,
  "VideoType": null,
  "IsoType": null,
  "Video3DFormat": null,
  "MediaStreams": null,
  "MediaAttachments": null,
  "Formats": null,
  "Bitrate": null,
  "Timestamp": null,
  "RequiredHttpHeaders": null,
  "TranscodingUrl": null,
  "TranscodingSubProtocol": null,
  "TranscodingContainer": null,
  "AnalyzeDurationMs": null,
  "DefaultAudioStreamIndex": null,
  "DefaultSubtitleStreamIndex": null
}
```

