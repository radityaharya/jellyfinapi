
# Transcoding Info

## Structure

`TranscodingInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `audio_codec` | `string` | Optional | - |
| `video_codec` | `string` | Optional | - |
| `container` | `string` | Optional | - |
| `is_video_direct` | `bool` | Optional | - |
| `is_audio_direct` | `bool` | Optional | - |
| `bitrate` | `int` | Optional | - |
| `framerate` | `float` | Optional | - |
| `completion_percentage` | `float` | Optional | - |
| `width` | `int` | Optional | - |
| `height` | `int` | Optional | - |
| `audio_channels` | `int` | Optional | - |
| `hardware_acceleration_type` | [`HardwareEncodingTypeEnum`](../../doc/models/hardware-encoding-type-enum.md) | Optional | - |
| `transcode_reasons` | [`TranscodeReasonsEnum`](../../doc/models/transcode-reasons-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "AudioCodec": null,
  "VideoCodec": null,
  "Container": null,
  "IsVideoDirect": null,
  "IsAudioDirect": null,
  "Bitrate": null,
  "Framerate": null,
  "CompletionPercentage": null,
  "Width": null,
  "Height": null,
  "AudioChannels": null,
  "HardwareAccelerationType": null,
  "TranscodeReasons": null
}
```

