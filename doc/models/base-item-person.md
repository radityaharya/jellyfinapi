
# Base Item Person

This is used by the api to get information about a Person within a BaseItem.

## Structure

`BaseItemPerson`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `id` | `uuid\|string` | Optional | Gets or sets the identifier. |
| `role` | `string` | Optional | Gets or sets the role. |
| `mtype` | `string` | Optional | Gets or sets the type. |
| `primary_image_tag` | `string` | Optional | Gets or sets the primary image tag. |
| `image_blur_hashes` | [`ImageBlurHashes`](../../doc/models/image-blur-hashes.md) | Optional | Gets or sets the primary image blurhash. |

## Example (as JSON)

```json
{
  "Name": null,
  "Id": null,
  "Role": null,
  "Type": null,
  "PrimaryImageTag": null,
  "ImageBlurHashes": null
}
```

