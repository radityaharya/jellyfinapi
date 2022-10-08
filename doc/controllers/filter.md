# Filter

```python
filter_controller = client.filter
```

## Class Name

`FilterController`

## Methods

* [Get Query Filters](../../doc/controllers/filter.md#get-query-filters)
* [Get Query Filters Legacy](../../doc/controllers/filter.md#get-query-filters-legacy)


# Get Query Filters

Gets query filters.

```python
def get_query_filters(self,
                     user_id=None,
                     parent_id=None,
                     include_item_types=None,
                     is_airing=None,
                     is_movie=None,
                     is_sports=None,
                     is_kids=None,
                     is_news=None,
                     is_series=None,
                     recursive=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. User id. |
| `parent_id` | `uuid\|string` | Query, Optional | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `is_airing` | `bool` | Query, Optional | Optional. Is item airing. |
| `is_movie` | `bool` | Query, Optional | Optional. Is item movie. |
| `is_sports` | `bool` | Query, Optional | Optional. Is item sports. |
| `is_kids` | `bool` | Query, Optional | Optional. Is item kids. |
| `is_news` | `bool` | Query, Optional | Optional. Is item news. |
| `is_series` | `bool` | Query, Optional | Optional. Is item series. |
| `recursive` | `bool` | Query, Optional | Optional. Search recursive. |

## Response Type

[`QueryFilters`](../../doc/models/query-filters.md)

## Example Usage

```python
result = filter_controller.get_query_filters()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Query Filters Legacy

Gets legacy query filters.

```python
def get_query_filters_legacy(self,
                            user_id=None,
                            parent_id=None,
                            include_item_types=None,
                            media_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Query, Optional | Optional. User id. |
| `parent_id` | `uuid\|string` | Query, Optional | Optional. Parent id. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `media_types` | `List of string` | Query, Optional | Optional. Filter by MediaType. Allows multiple, comma delimited. |

## Response Type

[`QueryFiltersLegacy`](../../doc/models/query-filters-legacy.md)

## Example Usage

```python
result = filter_controller.get_query_filters_legacy()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

