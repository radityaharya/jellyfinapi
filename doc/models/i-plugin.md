
# I Plugin

Defines the MediaBrowser.Common.Plugins.IPlugin.

## Structure

`IPlugin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets the name of the plugin. |
| `description` | `string` | Optional | Gets the Description. |
| `id` | `uuid\|string` | Optional | Gets the unique id. |
| `version` | `string` | Optional | Gets the plugin version. |
| `assembly_file_path` | `string` | Optional | Gets the path to the assembly file. |
| `can_uninstall` | `bool` | Optional | Gets a value indicating whether the plugin can be uninstalled. |
| `data_folder_path` | `string` | Optional | Gets the full path to the data folder, where the plugin can store any miscellaneous files needed. |

## Example (as JSON)

```json
{}
```

