
# Get Programs Dto

Get programs dto.

## Structure

`GetProgramsDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_ids` | `List of uuid\|string` | Optional | Gets or sets the channels to return guide information for. |
| `user_id` | `uuid\|string` | Optional | Gets or sets optional. Filter by user id. |
| `min_start_date` | `datetime` | Optional | Gets or sets the minimum premiere start date.<br>Optional. |
| `has_aired` | `bool` | Optional | Gets or sets filter by programs that have completed airing, or not.<br>Optional. |
| `is_airing` | `bool` | Optional | Gets or sets filter by programs that are currently airing, or not.<br>Optional. |
| `max_start_date` | `datetime` | Optional | Gets or sets the maximum premiere start date.<br>Optional. |
| `min_end_date` | `datetime` | Optional | Gets or sets the minimum premiere end date.<br>Optional. |
| `max_end_date` | `datetime` | Optional | Gets or sets the maximum premiere end date.<br>Optional. |
| `is_movie` | `bool` | Optional | Gets or sets filter for movies.<br>Optional. |
| `is_series` | `bool` | Optional | Gets or sets filter for series.<br>Optional. |
| `is_news` | `bool` | Optional | Gets or sets filter for news.<br>Optional. |
| `is_kids` | `bool` | Optional | Gets or sets filter for kids.<br>Optional. |
| `is_sports` | `bool` | Optional | Gets or sets filter for sports.<br>Optional. |
| `start_index` | `int` | Optional | Gets or sets the record index to start at. All items with a lower index will be dropped from the results.<br>Optional. |
| `limit` | `int` | Optional | Gets or sets the maximum number of records to return.<br>Optional. |
| `sort_by` | `List of string` | Optional | Gets or sets specify one or more sort orders, comma delimited. Options: Name, StartDate.<br>Optional. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Optional | Gets or sets sort Order - Ascending,Descending. |
| `genres` | `List of string` | Optional | Gets or sets the genres to return guide information for. |
| `genre_ids` | `List of uuid\|string` | Optional | Gets or sets the genre ids to return guide information for. |
| `enable_images` | `bool` | Optional | Gets or sets include image information in output.<br>Optional. |
| `enable_total_record_count` | `bool` | Optional | Gets or sets a value indicating whether retrieve total record count. |
| `image_type_limit` | `int` | Optional | Gets or sets the max number of images to return, per image type.<br>Optional. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Optional | Gets or sets the image types to include in the output.<br>Optional. |
| `enable_user_data` | `bool` | Optional | Gets or sets include user data.<br>Optional. |
| `series_timer_id` | `string` | Optional | Gets or sets filter by series timer id.<br>Optional. |
| `library_series_id` | `uuid\|string` | Optional | Gets or sets filter by library series id.<br>Optional. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Optional | Gets or sets specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.<br>Optional. |

## Example (as JSON)

```json
{
  "ChannelIds": null,
  "UserId": null,
  "MinStartDate": null,
  "HasAired": null,
  "IsAiring": null,
  "MaxStartDate": null,
  "MinEndDate": null,
  "MaxEndDate": null,
  "IsMovie": null,
  "IsSeries": null,
  "IsNews": null,
  "IsKids": null,
  "IsSports": null,
  "StartIndex": null,
  "Limit": null,
  "SortBy": null,
  "SortOrder": null,
  "Genres": null,
  "GenreIds": null,
  "EnableImages": null,
  "EnableTotalRecordCount": null,
  "ImageTypeLimit": null,
  "EnableImageTypes": null,
  "EnableUserData": null,
  "SeriesTimerId": null,
  "LibrarySeriesId": null,
  "Fields": null
}
```

