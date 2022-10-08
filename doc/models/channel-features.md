
# Channel Features

## Structure

`ChannelFeatures`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name. |
| `id` | `uuid\|string` | Optional | Gets or sets the identifier. |
| `can_search` | `bool` | Optional | Gets or sets a value indicating whether this instance can search. |
| `media_types` | [`List of ChannelMediaTypeEnum`](../../doc/models/channel-media-type-enum.md) | Optional | Gets or sets the media types. |
| `content_types` | [`List of ChannelMediaContentTypeEnum`](../../doc/models/channel-media-content-type-enum.md) | Optional | Gets or sets the content types. |
| `max_page_size` | `int` | Optional | Gets or sets the maximum number of records the channel allows retrieving at a time. |
| `auto_refresh_levels` | `int` | Optional | Gets or sets the automatic refresh levels. |
| `default_sort_fields` | [`List of ChannelItemSortFieldEnum`](../../doc/models/channel-item-sort-field-enum.md) | Optional | Gets or sets the default sort orders. |
| `supports_sort_order_toggle` | `bool` | Optional | Gets or sets a value indicating whether a sort ascending/descending toggle is supported. |
| `supports_latest_media` | `bool` | Optional | Gets or sets a value indicating whether [supports latest media]. |
| `can_filter` | `bool` | Optional | Gets or sets a value indicating whether this instance can filter. |
| `supports_content_downloading` | `bool` | Optional | Gets or sets a value indicating whether [supports content downloading]. |

## Example (as JSON)

```json
{
  "Name": null,
  "Id": null,
  "CanSearch": null,
  "MediaTypes": null,
  "ContentTypes": null,
  "MaxPageSize": null,
  "AutoRefreshLevels": null,
  "DefaultSortFields": null,
  "SupportsSortOrderToggle": null,
  "SupportsLatestMedia": null,
  "CanFilter": null,
  "SupportsContentDownloading": null
}
```

