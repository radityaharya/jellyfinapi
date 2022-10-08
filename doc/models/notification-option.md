
# Notification Option

## Structure

`NotificationOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Optional | - |
| `disabled_monitor_users` | `List of string` | Optional | Gets or sets user Ids to not monitor (it's opt out). |
| `send_to_users` | `List of string` | Optional | Gets or sets user Ids to send to (if SendToUserMode == Custom). |
| `enabled` | `bool` | Optional | Gets or sets a value indicating whether this MediaBrowser.Model.Notifications.NotificationOption is enabled. |
| `disabled_services` | `List of string` | Optional | Gets or sets the disabled services. |
| `send_to_user_mode` | [`SendToUserTypeEnum`](../../doc/models/send-to-user-type-enum.md) | Optional | Gets or sets the send to user mode. |

## Example (as JSON)

```json
{
  "Type": null,
  "DisabledMonitorUsers": null,
  "SendToUsers": null,
  "Enabled": null,
  "DisabledServices": null,
  "SendToUserMode": null
}
```

