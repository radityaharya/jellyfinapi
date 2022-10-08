
# Player State Info

## Structure

`PlayerStateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `position_ticks` | `long\|int` | Optional | Gets or sets the now playing position ticks. |
| `can_seek` | `bool` | Optional | Gets or sets a value indicating whether this instance can seek. |
| `is_paused` | `bool` | Optional | Gets or sets a value indicating whether this instance is paused. |
| `is_muted` | `bool` | Optional | Gets or sets a value indicating whether this instance is muted. |
| `volume_level` | `int` | Optional | Gets or sets the volume level. |
| `audio_stream_index` | `int` | Optional | Gets or sets the index of the now playing audio stream. |
| `subtitle_stream_index` | `int` | Optional | Gets or sets the index of the now playing subtitle stream. |
| `media_source_id` | `string` | Optional | Gets or sets the now playing media version identifier. |
| `play_method` | [`PlayMethodEnum`](../../doc/models/play-method-enum.md) | Optional | Gets or sets the play method. |
| `repeat_mode` | [`RepeatModeEnum`](../../doc/models/repeat-mode-enum.md) | Optional | Gets or sets the repeat mode. |
| `live_stream_id` | `string` | Optional | Gets or sets the now playing live stream identifier. |

## Example (as JSON)

```json
{
  "PositionTicks": null,
  "CanSeek": null,
  "IsPaused": null,
  "IsMuted": null,
  "VolumeLevel": null,
  "AudioStreamIndex": null,
  "SubtitleStreamIndex": null,
  "MediaSourceId": null,
  "PlayMethod": null,
  "RepeatMode": null,
  "LiveStreamId": null
}
```

