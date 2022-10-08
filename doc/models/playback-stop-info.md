
# Playback Stop Info

Class PlaybackStopInfo.

## Structure

`PlaybackStopInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | Gets or sets the item. |
| `item_id` | `uuid\|string` | Optional | Gets or sets the item identifier. |
| `session_id` | `string` | Optional | Gets or sets the session id. |
| `media_source_id` | `string` | Optional | Gets or sets the media version identifier. |
| `position_ticks` | `long\|int` | Optional | Gets or sets the position ticks. |
| `live_stream_id` | `string` | Optional | Gets or sets the live stream identifier. |
| `play_session_id` | `string` | Optional | Gets or sets the play session identifier. |
| `failed` | `bool` | Optional | Gets or sets a value indicating whether this MediaBrowser.Model.Session.PlaybackStopInfo is failed. |
| `next_media_type` | `string` | Optional | - |
| `playlist_item_id` | `string` | Optional | - |
| `now_playing_queue` | [`List of QueueItem`](../../doc/models/queue-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "Item": null,
  "ItemId": null,
  "SessionId": null,
  "MediaSourceId": null,
  "PositionTicks": null,
  "LiveStreamId": null,
  "PlaySessionId": null,
  "Failed": null,
  "NextMediaType": null,
  "PlaylistItemId": null,
  "NowPlayingQueue": null
}
```

