
# Library Type Options Dto

Library type options dto.

## Structure

`LibraryTypeOptionsDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Optional | Gets or sets the type. |
| `metadata_fetchers` | [`List of LibraryOptionInfoDto`](../../doc/models/library-option-info-dto.md) | Optional | Gets or sets the metadata fetchers. |
| `image_fetchers` | [`List of LibraryOptionInfoDto`](../../doc/models/library-option-info-dto.md) | Optional | Gets or sets the image fetchers. |
| `supported_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Optional | Gets or sets the supported image types. |
| `default_image_options` | [`List of ImageOption`](../../doc/models/image-option.md) | Optional | Gets or sets the default image options. |

## Example (as JSON)

```json
{
  "Type": null,
  "MetadataFetchers": null,
  "ImageFetchers": null,
  "SupportedImageTypes": null,
  "DefaultImageOptions": null
}
```

