
# Ready Request Dto

Class ReadyRequest.

## Structure

`ReadyRequestDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `when` | `datetime` | Optional | Gets or sets when the request has been made by the client. |
| `position_ticks` | `long\|int` | Optional | Gets or sets the position ticks. |
| `is_playing` | `bool` | Optional | Gets or sets a value indicating whether the client playback is unpaused. |
| `playlist_item_id` | `uuid\|string` | Optional | Gets or sets the playlist item identifier of the playing item. |

## Example (as JSON)

```json
{
  "When": null,
  "PositionTicks": null,
  "IsPlaying": null,
  "PlaylistItemId": null
}
```

