
# Virtual Folder Info

Used to hold information about a user's list of configured virtual folders.

## Structure

`VirtualFolderInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `locations` | `List of string` | Optional | Gets or sets the locations. |
| `collection_type` | [`CollectionTypeOptionsEnum`](../../doc/models/collection-type-options-enum.md) | Optional | Gets or sets the type of the collection. |
| `library_options` | [`LibraryOptions`](../../doc/models/library-options.md) | Optional | - |
| `item_id` | `string` | Optional | Gets or sets the item identifier. |
| `primary_image_item_id` | `string` | Optional | Gets or sets the primary image item identifier. |
| `refresh_progress` | `float` | Optional | - |
| `refresh_status` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "Name": null,
  "Locations": null,
  "CollectionType": null,
  "LibraryOptions": null,
  "ItemId": null,
  "PrimaryImageItemId": null,
  "RefreshProgress": null,
  "RefreshStatus": null
}
```

