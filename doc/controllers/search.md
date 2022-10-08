# Search

```python
search_controller = client.search
```

## Class Name

`SearchController`


# Get

Gets the search hint result.

```python
def get(self,
       search_term,
       start_index=None,
       limit=None,
       user_id=None,
       include_item_types=None,
       exclude_item_types=None,
       media_types=None,
       parent_id=None,
       is_movie=None,
       is_series=None,
       is_news=None,
       is_kids=None,
       is_sports=None,
       include_people=True,
       include_media=True,
       include_genres=True,
       include_studios=True,
       include_artists=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_term` | `string` | Query, Required | The search term to filter on. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Supply a user id to search within a user's library or omit to search all. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | If specified, only results with the specified item types are returned. This allows multiple, comma delimeted. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | If specified, results with these item types are filtered out. This allows multiple, comma delimeted. |
| `media_types` | `List of string` | Query, Optional | If specified, only results with the specified media types are returned. This allows multiple, comma delimeted. |
| `parent_id` | `uuid\|string` | Query, Optional | If specified, only children of the parent are returned. |
| `is_movie` | `bool` | Query, Optional | Optional filter for movies. |
| `is_series` | `bool` | Query, Optional | Optional filter for series. |
| `is_news` | `bool` | Query, Optional | Optional filter for news. |
| `is_kids` | `bool` | Query, Optional | Optional filter for kids. |
| `is_sports` | `bool` | Query, Optional | Optional filter for sports. |
| `include_people` | `bool` | Query, Optional | Optional filter whether to include people.<br>**Default**: `True` |
| `include_media` | `bool` | Query, Optional | Optional filter whether to include media.<br>**Default**: `True` |
| `include_genres` | `bool` | Query, Optional | Optional filter whether to include genres.<br>**Default**: `True` |
| `include_studios` | `bool` | Query, Optional | Optional filter whether to include studios.<br>**Default**: `True` |
| `include_artists` | `bool` | Query, Optional | Optional filter whether to include artists.<br>**Default**: `True` |

## Response Type

[`SearchHintResult`](../../doc/models/search-hint-result.md)

## Example Usage

```python
search_term = 'searchTerm4'
include_people = True
include_media = True
include_genres = True
include_studios = True
include_artists = True

result = search_controller.get(search_term, None, None, None, None, None, None, None, None, None, None, None, None, include_people, include_media, include_genres, include_studios, include_artists)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

