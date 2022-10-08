
# Display Preferences Dto

Defines the display preferences for any item that supports them (usually Folders).

## Structure

`DisplayPreferencesDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Gets or sets the user id. |
| `view_type` | `string` | Optional | Gets or sets the type of the view. |
| `sort_by` | `string` | Optional | Gets or sets the sort by. |
| `index_by` | `string` | Optional | Gets or sets the index by. |
| `remember_indexing` | `bool` | Optional | Gets or sets a value indicating whether [remember indexing]. |
| `primary_image_height` | `int` | Optional | Gets or sets the height of the primary image. |
| `primary_image_width` | `int` | Optional | Gets or sets the width of the primary image. |
| `custom_prefs` | `dict` | Optional | Gets or sets the custom prefs. |
| `scroll_direction` | [`ScrollDirectionEnum`](../../doc/models/scroll-direction-enum.md) | Optional | An enum representing the axis that should be scrolled. |
| `show_backdrop` | `bool` | Optional | Gets or sets a value indicating whether to show backdrops on this item. |
| `remember_sorting` | `bool` | Optional | Gets or sets a value indicating whether [remember sorting]. |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Optional | An enum representing the sorting order. |
| `show_sidebar` | `bool` | Optional | Gets or sets a value indicating whether [show sidebar]. |
| `client` | `string` | Optional | Gets or sets the client. |

## Example (as JSON)

```json
{
  "Id": null,
  "ViewType": null,
  "SortBy": null,
  "IndexBy": null,
  "RememberIndexing": null,
  "PrimaryImageHeight": null,
  "PrimaryImageWidth": null,
  "CustomPrefs": null,
  "ScrollDirection": null,
  "ShowBackdrop": null,
  "RememberSorting": null,
  "SortOrder": null,
  "ShowSidebar": null,
  "Client": null
}
```

