
# Quick Connect Result

Stores the state of an quick connect request.

## Structure

`QuickConnectResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authenticated` | `bool` | Optional | Gets or sets a value indicating whether this request is authorized. |
| `secret` | `string` | Optional | Gets the secret value used to uniquely identify this request. Can be used to retrieve authentication information. |
| `code` | `string` | Optional | Gets the user facing code used so the user can quickly differentiate this request from others. |
| `device_id` | `string` | Optional | Gets the requesting device id. |
| `device_name` | `string` | Optional | Gets the requesting device name. |
| `app_name` | `string` | Optional | Gets the requesting app name. |
| `app_version` | `string` | Optional | Gets the requesting app version. |
| `date_added` | `datetime` | Optional | Gets or sets the DateTime that this request was created. |

## Example (as JSON)

```json
{
  "Authenticated": null,
  "Secret": null,
  "Code": null,
  "DeviceId": null,
  "DeviceName": null,
  "AppName": null,
  "AppVersion": null,
  "DateAdded": null
}
```

