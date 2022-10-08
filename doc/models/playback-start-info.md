
# Playback Start Info

Class PlaybackStartInfo.

## Structure

`PlaybackStartInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_seek` | `bool` | Optional | Gets or sets a value indicating whether this instance can seek. |
| `item` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | Gets or sets the item. |
| `item_id` | `uuid\|string` | Optional | Gets or sets the item identifier. |
| `session_id` | `string` | Optional | Gets or sets the session id. |
| `media_source_id` | `string` | Optional | Gets or sets the media version identifier. |
| `audio_stream_index` | `int` | Optional | Gets or sets the index of the audio stream. |
| `subtitle_stream_index` | `int` | Optional | Gets or sets the index of the subtitle stream. |
| `is_paused` | `bool` | Optional | Gets or sets a value indicating whether this instance is paused. |
| `is_muted` | `bool` | Optional | Gets or sets a value indicating whether this instance is muted. |
| `position_ticks` | `long\|int` | Optional | Gets or sets the position ticks. |
| `playback_start_time_ticks` | `long\|int` | Optional | - |
| `volume_level` | `int` | Optional | Gets or sets the volume level. |
| `brightness` | `int` | Optional | - |
| `aspect_ratio` | `string` | Optional | - |
| `play_method` | [`PlayMethodEnum`](../../doc/models/play-method-enum.md) | Optional | Gets or sets the play method. |
| `live_stream_id` | `string` | Optional | Gets or sets the live stream identifier. |
| `play_session_id` | `string` | Optional | Gets or sets the play session identifier. |
| `repeat_mode` | [`RepeatModeEnum`](../../doc/models/repeat-mode-enum.md) | Optional | Gets or sets the repeat mode. |
| `now_playing_queue` | [`List of QueueItem`](../../doc/models/queue-item.md) | Optional | - |
| `playlist_item_id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "CanSeek": null,
  "Item": null,
  "ItemId": null,
  "SessionId": null,
  "MediaSourceId": null,
  "AudioStreamIndex": null,
  "SubtitleStreamIndex": null,
  "IsPaused": null,
  "IsMuted": null,
  "PositionTicks": null,
  "PlaybackStartTimeTicks": null,
  "VolumeLevel": null,
  "Brightness": null,
  "AspectRatio": null,
  "PlayMethod": null,
  "LiveStreamId": null,
  "PlaySessionId": null,
  "RepeatMode": null,
  "NowPlayingQueue": null,
  "PlaylistItemId": null
}
```

