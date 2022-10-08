# Artists

```python
artists_controller = client.artists
```

## Class Name

`ArtistsController`

## Methods

* [Get Album Artists](../../doc/controllers/artists.md#get-album-artists)
* [Get Artist by Name](../../doc/controllers/artists.md#get-artist-by-name)
* [Get Artists](../../doc/controllers/artists.md#get-artists)


# Get Album Artists

Gets all album artists from a given item, folder, or the entire library.

```python
def get_album_artists(self,
                     min_community_rating=None,
                     start_index=None,
                     limit=None,
                     search_term=None,
                     parent_id=None,
                     fields=None,
                     exclude_item_types=None,
                     include_item_types=None,
                     filters=None,
                     is_favorite=None,
                     media_types=None,
                     genres=None,
                     genre_ids=None,
                     official_ratings=None,
                     tags=None,
                     years=None,
                     enable_user_data=None,
                     image_type_limit=None,
                     enable_image_types=None,
                     person=None,
                     person_ids=None,
                     person_types=None,
                     studios=None,
                     studio_ids=None,
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
| `min_community_rating` | `float` | Query, Optional | Optional filter by minimum community rating. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `search_term` | `string` | Query, Optional | Optional. Search term. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. |
| `media_types` | `List of string` | Query, Optional | Optional filter by MediaType. Allows multiple, comma delimited. |
| `genres` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. |
| `genre_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. |
| `official_ratings` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. |
| `tags` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. |
| `years` | `List of int` | Query, Optional | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. |
| `enable_user_data` | `bool` | Query, Optional | Optional, include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `person` | `string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person. |
| `person_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person ids. |
| `person_types` | `List of string` | Query, Optional | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. |
| `studios` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. |
| `studio_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. |
| `user_id` | `uuid\|string` | Query, Optional | User id. |
| `name_starts_with_or_greater` | `string` | Query, Optional | Optional filter by items whose name is sorted equally or greater than a given input string. |
| `name_starts_with` | `string` | Query, Optional | Optional filter by items whose name is sorted equally than a given input string. |
| `name_less_than` | `string` | Query, Optional | Optional filter by items whose name is equally or lesser than a given input string. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |
| `enable_total_record_count` | `bool` | Query, Optional | Total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_images = True
enable_total_record_count = True

result = artists_controller.get_album_artists(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_images, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Artist by Name

Gets an artist by name.

```python
def get_artist_by_name(self,
                      name,
                      user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Studio name. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
name = 'name0'

result = artists_controller.get_artist_by_name(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Artists

Gets all artists from a given item, folder, or the entire library.

```python
def get_artists(self,
               min_community_rating=None,
               start_index=None,
               limit=None,
               search_term=None,
               parent_id=None,
               fields=None,
               exclude_item_types=None,
               include_item_types=None,
               filters=None,
               is_favorite=None,
               media_types=None,
               genres=None,
               genre_ids=None,
               official_ratings=None,
               tags=None,
               years=None,
               enable_user_data=None,
               image_type_limit=None,
               enable_image_types=None,
               person=None,
               person_ids=None,
               person_types=None,
               studios=None,
               studio_ids=None,
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
| `min_community_rating` | `float` | Query, Optional | Optional filter by minimum community rating. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `search_term` | `string` | Query, Optional | Optional. Search term. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. |
| `media_types` | `List of string` | Query, Optional | Optional filter by MediaType. Allows multiple, comma delimited. |
| `genres` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. |
| `genre_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. |
| `official_ratings` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. |
| `tags` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. |
| `years` | `List of int` | Query, Optional | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. |
| `enable_user_data` | `bool` | Query, Optional | Optional, include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `person` | `string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person. |
| `person_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered to include only those containing the specified person ids. |
| `person_types` | `List of string` | Query, Optional | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. |
| `studios` | `List of string` | Query, Optional | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. |
| `studio_ids` | `List of uuid\|string` | Query, Optional | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. |
| `user_id` | `uuid\|string` | Query, Optional | User id. |
| `name_starts_with_or_greater` | `string` | Query, Optional | Optional filter by items whose name is sorted equally or greater than a given input string. |
| `name_starts_with` | `string` | Query, Optional | Optional filter by items whose name is sorted equally than a given input string. |
| `name_less_than` | `string` | Query, Optional | Optional filter by items whose name is equally or lesser than a given input string. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |
| `enable_total_record_count` | `bool` | Query, Optional | Total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_images = True
enable_total_record_count = True

result = artists_controller.get_artists(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_images, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

