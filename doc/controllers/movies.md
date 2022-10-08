# Movies

```python
movies_controller = client.movies
```

## Class Name

`MoviesController`


# Get Movie Recommendations

Gets movie recommendations.

```python
def get_movie_recommendations(self,
                             user_id=None,
                             parent_id=None,
                             fields=None,
                             category_limit=5,
                             item_limit=8)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. The fields to return. |
| `category_limit` | `int` | Query, Optional | The max number of categories to return.<br>**Default**: `5` |
| `item_limit` | `int` | Query, Optional | The max number of items to return per category.<br>**Default**: `8` |

## Response Type

[`List of RecommendationDto`](../../doc/models/recommendation-dto.md)

## Example Usage

```python
category_limit = 5
item_limit = 8

result = movies_controller.get_movie_recommendations(None, None, None, category_limit, item_limit)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

