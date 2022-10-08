
# Play Request

Class PlayRequest.

## Structure

`PlayRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List of uuid\|string` | Optional | Gets or sets the item ids. |
| `start_position_ticks` | `long\|int` | Optional | Gets or sets the start position ticks that the first item should be played at. |
| `play_command` | [`PlayCommandEnum`](../../doc/models/play-command-enum.md) | Optional | Gets or sets the play command. |
| `controlling_user_id` | `uuid\|string` | Optional | Gets or sets the controlling user identifier. |
| `subtitle_stream_index` | `int` | Optional | - |
| `audio_stream_index` | `int` | Optional | - |
| `media_source_id` | `string` | Optional | - |
| `start_index` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "ItemIds": null,
  "StartPositionTicks": null,
  "PlayCommand": null,
  "ControllingUserId": null,
  "SubtitleStreamIndex": null,
  "AudioStreamIndex": null,
  "MediaSourceId": null,
  "StartIndex": null
}
```

