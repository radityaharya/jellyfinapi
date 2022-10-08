
# Base Item

Class BaseItem.

## Structure

`BaseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `size` | `long\|int` | Optional | - |
| `container` | `string` | Optional | - |
| `is_hd` | `bool` | Optional | - |
| `is_shortcut` | `bool` | Optional | - |
| `shortcut_path` | `string` | Optional | - |
| `width` | `int` | Optional | - |
| `height` | `int` | Optional | - |
| `extra_ids` | `List of uuid\|string` | Optional | - |
| `date_last_saved` | `datetime` | Optional | - |
| `remote_trailers` | [`List of MediaUrl`](../../doc/models/media-url.md) | Optional | Gets or sets the remote trailers. |
| `supports_external_transfer` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "Size": null,
  "Container": null,
  "IsShortcut": null,
  "ShortcutPath": null,
  "Width": null,
  "Height": null,
  "ExtraIds": null,
  "DateLastSaved": null,
  "RemoteTrailers": null
}
```

