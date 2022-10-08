
# Notification Result Dto

A list of notifications with the total record count for pagination.

## Structure

`NotificationResultDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notifications` | [`List of NotificationDto`](../../doc/models/notification-dto.md) | Optional | Gets or sets the current page of notifications. |
| `total_record_count` | `int` | Optional | Gets or sets the total number of notifications. |

## Example (as JSON)

```json
{
  "Notifications": null,
  "TotalRecordCount": null
}
```

