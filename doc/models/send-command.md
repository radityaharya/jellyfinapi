
# Send Command

Class SendCommand.

## Structure

`SendCommand`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_id` | `uuid\|string` | Optional | Gets the group identifier. |
| `playlist_item_id` | `uuid\|string` | Optional | Gets the playlist identifier of the playing item. |
| `when` | `datetime` | Optional | Gets or sets the UTC time when to execute the command. |
| `position_ticks` | `long\|int` | Optional | Gets the position ticks. |
| `command` | [`SendCommandTypeEnum`](../../doc/models/send-command-type-enum.md) | Optional | Gets the command. |
| `emitted_at` | `datetime` | Optional | Gets the UTC time when this command has been emitted. |

## Example (as JSON)

```json
{
  "GroupId": null,
  "PlaylistItemId": null,
  "When": null,
  "PositionTicks": null,
  "Command": null,
  "EmittedAt": null
}
```

