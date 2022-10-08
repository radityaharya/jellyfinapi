# Years

```python
years_controller = client.years
```

## Class Name

`YearsController`

## Methods

* [Get Year](../../doc/controllers/years.md#get-year)
* [Get Years](../../doc/controllers/years.md#get-years)


# Get Year

Gets a year.

```python
def get_year(self,
            year,
            user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `year` | `int` | Template, Required | The year. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
year = 248

result = years_controller.get_year(year)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Year not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Years

Get years.

```python
def get_years(self,
             start_index=None,
             limit=None,
             sort_order=None,
             parent_id=None,
             fields=None,
             exclude_item_types=None,
             include_item_types=None,
             media_types=None,
             sort_by=None,
             enable_user_data=None,
             image_type_limit=None,
             enable_image_types=None,
             user_id=None,
             recursive=True,
             enable_images=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_index` | `int` | Query, Optional | Skips over a given number of items within the results. Use for paging. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `sort_order` | [`List of SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort Order - Ascending,Descending. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be included based on item type. This allows multiple, comma delimited. |
| `media_types` | `List of string` | Query, Optional | Optional. Filter by MediaType. Allows multiple, comma delimited. |
| `sort_by` | `List of string` | Query, Optional | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `user_id` | `uuid\|string` | Query, Optional | User Id. |
| `recursive` | `bool` | Query, Optional | Search recursively.<br>**Default**: `True` |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
recursive = True
enable_images = True

result = years_controller.get_years(None, None, None, None, None, None, None, None, None, None, None, None, None, recursive, enable_images)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

