
# Activity Log Entry

An activity log entry.

## Structure

`ActivityLogEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | Gets or sets the identifier. |
| `name` | `string` | Optional | Gets or sets the name. |
| `overview` | `string` | Optional | Gets or sets the overview. |
| `short_overview` | `string` | Optional | Gets or sets the short overview. |
| `mtype` | `string` | Optional | Gets or sets the type. |
| `item_id` | `string` | Optional | Gets or sets the item identifier. |
| `date` | `datetime` | Optional | Gets or sets the date. |
| `user_id` | `uuid\|string` | Optional | Gets or sets the user identifier. |
| `user_primary_image_tag` | `string` | Optional | Gets or sets the user primary image tag. |
| `severity` | [`LogLevelEnum`](../../doc/models/log-level-enum.md) | Optional | Gets or sets the log severity. |

## Example (as JSON)

```json
{
  "Id": null,
  "Name": null,
  "Overview": null,
  "ShortOverview": null,
  "Type": null,
  "ItemId": null,
  "Date": null,
  "UserId": null,
  "UserPrimaryImageTag": null,
  "Severity": null
}
```

