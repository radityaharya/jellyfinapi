
# User Dto

Class UserDto.

## Structure

`UserDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `server_id` | `string` | Optional | Gets or sets the server identifier. |
| `server_name` | `string` | Optional | Gets or sets the name of the server.<br>This is not used by the server and is for client-side usage only. |
| `id` | `uuid\|string` | Optional | Gets or sets the id. |
| `primary_image_tag` | `string` | Optional | Gets or sets the primary image tag. |
| `has_password` | `bool` | Optional | Gets or sets a value indicating whether this instance has password. |
| `has_configured_password` | `bool` | Optional | Gets or sets a value indicating whether this instance has configured password. |
| `has_configured_easy_password` | `bool` | Optional | Gets or sets a value indicating whether this instance has configured easy password. |
| `enable_auto_login` | `bool` | Optional | Gets or sets whether async login is enabled or not. |
| `last_login_date` | `datetime` | Optional | Gets or sets the last login date. |
| `last_activity_date` | `datetime` | Optional | Gets or sets the last activity date. |
| `configuration` | [`UserConfiguration`](../../doc/models/user-configuration.md) | Optional | Gets or sets the configuration. |
| `policy` | [`UserPolicy`](../../doc/models/user-policy.md) | Optional | Gets or sets the policy. |
| `primary_image_aspect_ratio` | `float` | Optional | Gets or sets the primary image aspect ratio. |

## Example (as JSON)

```json
{
  "Name": null,
  "ServerId": null,
  "ServerName": null,
  "Id": null,
  "PrimaryImageTag": null,
  "HasPassword": null,
  "HasConfiguredPassword": null,
  "HasConfiguredEasyPassword": null,
  "EnableAutoLogin": null,
  "LastLoginDate": null,
  "LastActivityDate": null,
  "Configuration": null,
  "Policy": null,
  "PrimaryImageAspectRatio": null
}
```

