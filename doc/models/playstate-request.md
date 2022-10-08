
# Playstate Request

## Structure

`PlaystateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `command` | [`PlaystateCommandEnum`](../../doc/models/playstate-command-enum.md) | Optional | Enum PlaystateCommand. |
| `seek_position_ticks` | `long\|int` | Optional | - |
| `controlling_user_id` | `string` | Optional | Gets or sets the controlling user identifier. |

## Example (as JSON)

```json
{
  "Command": null,
  "SeekPositionTicks": null,
  "ControllingUserId": null
}
```

