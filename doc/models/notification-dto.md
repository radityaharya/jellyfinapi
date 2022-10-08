
# Notification Dto

The notification DTO.

## Structure

`NotificationDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Gets or sets the notification ID. Defaults to an empty string. |
| `user_id` | `string` | Optional | Gets or sets the notification's user ID. Defaults to an empty string. |
| `date` | `datetime` | Optional | Gets or sets the notification date. |
| `is_read` | `bool` | Optional | Gets or sets a value indicating whether the notification has been read. Defaults to false. |
| `name` | `string` | Optional | Gets or sets the notification's name. Defaults to an empty string. |
| `description` | `string` | Optional | Gets or sets the notification's description. Defaults to an empty string. |
| `url` | `string` | Optional | Gets or sets the notification's URL. Defaults to an empty string. |
| `level` | [`NotificationLevelEnum`](../../doc/models/notification-level-enum.md) | Optional | Gets or sets the notification level. |

## Example (as JSON)

```json
{
  "Id": null,
  "UserId": null,
  "Date": null,
  "IsRead": null,
  "Name": null,
  "Description": null,
  "Url": null,
  "Level": null
}
```

