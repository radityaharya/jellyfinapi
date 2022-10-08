# Music Genres

```python
music_genres_controller = client.music_genres
```

## Class Name

`MusicGenresController`

## Methods

* [Get Music Genre](../../doc/controllers/music-genres.md#get-music-genre)
* [Get Music Genres](../../doc/controllers/music-genres.md#get-music-genres)


# Get Music Genre

Gets a music genre, by name.

```python
def get_music_genre(self,
                   genre_name,
                   user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `genre_name` | `string` | Template, Required | The genre name. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
genre_name = 'genreName8'

result = music_genres_controller.get_music_genre(genre_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Music Genres

**This endpoint is deprecated.**

Gets all music genres from a given item, folder, or the entire library.

```python
def get_music_genres(self,
                    start_index=None,
                    limit=None,
                    search_term=None,
                    parent_id=None,
                    fields=None,
                    exclude_item_types=None,
                    include_item_types=None,
                    is_favorite=None,
                    image_type_limit=None,
                    enable_image_types=None,
                    user_id=None,
                    name_starts_with_or_greater=None,
                    name_starts_with=None,
                    name_less_than=None,
                    sort_by=None,
                    sort_order=None,
                    enable_images=True,
                    enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `search_term` | `string` | Query, Optional | The search term. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered in based on item type. This allows multiple, comma delimited. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `user_id` | `uuid\|string` | Query, Optional | User id. |
| `name_starts_with_or_greater` | `string` | Query, Optional | Optional filter by items whose name is sorted equally or greater than a given input string. |
| `name_starts_with` | `string` | Query, Optional | Optional filter by items whose name is sorted equally than a given input string. |
| `name_less_than` | `string` | Query, Optional | Optional filter by items whose name is equally or lesser than a given input string. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |
| `enable_total_record_count` | `bool` | Query, Optional | Optional. Include total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_images = True
enable_total_record_count = True

result = music_genres_controller.get_music_genres(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_images, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

