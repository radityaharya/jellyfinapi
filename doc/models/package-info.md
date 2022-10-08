
# Package Info

Class PackageInfo.

## Structure

`PackageInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `description` | `string` | Optional | Gets or sets a long description of the plugin containing features or helpful explanations. |
| `overview` | `string` | Optional | Gets or sets a short overview of what the plugin does. |
| `owner` | `string` | Optional | Gets or sets the owner. |
| `category` | `string` | Optional | Gets or sets the category. |
| `guid` | `uuid\|string` | Optional | Gets or sets the guid of the assembly associated with this plugin.<br>This is used to identify the proper item for automatic updates. |
| `versions` | [`List of VersionInfo`](../../doc/models/version-info.md) | Optional | Gets or sets the versions. |
| `image_url` | `string` | Optional | Gets or sets the image url for the package. |

## Example (as JSON)

```json
{
  "name": null,
  "description": null,
  "overview": null,
  "owner": null,
  "category": null,
  "guid": null,
  "versions": null,
  "imageUrl": null
}
```

