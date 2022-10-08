
# Plugin Info

This is a serializable stub class that is used by the api to provide information about installed plugins.

## Structure

`PluginInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `version` | `string` | Optional | Gets or sets the version. |
| `configuration_file_name` | `string` | Optional | Gets or sets the name of the configuration file. |
| `description` | `string` | Optional | Gets or sets the description. |
| `id` | `uuid\|string` | Optional | Gets or sets the unique id. |
| `can_uninstall` | `bool` | Optional | Gets or sets a value indicating whether the plugin can be uninstalled. |
| `has_image` | `bool` | Optional | Gets or sets a value indicating whether this plugin has a valid image. |
| `status` | [`PluginStatusEnum`](../../doc/models/plugin-status-enum.md) | Optional | Gets or sets a value indicating the status of the plugin. |

## Example (as JSON)

```json
{
  "Name": null,
  "Version": null,
  "ConfigurationFileName": null,
  "Description": null,
  "Id": null,
  "CanUninstall": null,
  "HasImage": null,
  "Status": null
}
```

