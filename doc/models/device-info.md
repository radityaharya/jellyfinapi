
# Device Info

## Structure

`DeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `access_token` | `string` | Optional | Gets or sets the access token. |
| `id` | `string` | Optional | Gets or sets the identifier. |
| `last_user_name` | `string` | Optional | Gets or sets the last name of the user. |
| `app_name` | `string` | Optional | Gets or sets the name of the application. |
| `app_version` | `string` | Optional | Gets or sets the application version. |
| `last_user_id` | `uuid\|string` | Optional | Gets or sets the last user identifier. |
| `date_last_activity` | `datetime` | Optional | Gets or sets the date last modified. |
| `capabilities` | [`ClientCapabilities`](../../doc/models/client-capabilities.md) | Optional | Gets or sets the capabilities. |
| `icon_url` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "Name": null,
  "AccessToken": null,
  "Id": null,
  "LastUserName": null,
  "AppName": null,
  "AppVersion": null,
  "LastUserId": null,
  "DateLastActivity": null,
  "Capabilities": null,
  "IconUrl": null
}
```

