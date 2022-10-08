
# External Id Info

Represents the external id information for serialization to the client.

## Structure

`ExternalIdInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz, etc). |
| `key` | `string` | Optional | Gets or sets the unique key for this id. This key should be unique across all providers. |
| `mtype` | [`ExternalIdMediaTypeEnum`](../../doc/models/external-id-media-type-enum.md) | Optional | Gets or sets the specific media type for this id. This is used to distinguish between the different<br>external id types for providers with multiple ids.<br>A null value indicates there is no specific media type associated with the external id, or this is the<br>default id for the external provider so there is no need to specify a type. |
| `url_format_string` | `string` | Optional | Gets or sets the URL format string. |

## Example (as JSON)

```json
{
  "Name": null,
  "Key": null,
  "Type": null,
  "UrlFormatString": null
}
```

