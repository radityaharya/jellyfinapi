# Studios

```python
studios_controller = client.studios
```

## Class Name

`StudiosController`

## Methods

* [Get Studio](../../doc/controllers/studios.md#get-studio)
* [Get Studios](../../doc/controllers/studios.md#get-studios)


# Get Studio

Gets a studio by name.

```python
def get_studio(self,
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

result = studios_controller.get_studio(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Studios

Gets all studios from a given item, folder, or the entire library.

```python
def get_studios(self,
               start_index=None,
               limit=None,
               search_term=None,
               parent_id=None,
               fields=None,
               exclude_item_types=None,
               include_item_types=None,
               is_favorite=None,
               enable_user_data=None,
               image_type_limit=None,
               enable_image_types=None,
               user_id=None,
               name_starts_with_or_greater=None,
               name_starts_with=None,
               name_less_than=None,
               enable_images=True,
               enable_total_record_count=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `search_term` | `string` | Query, Optional | Optional. Search term. |
| `parent_id` | `uuid\|string` | Query, Optional | Specify this to localize the search to a specific item or folder. Omit to use the root. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `exclude_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. |
| `include_item_types` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. |
| `enable_user_data` | `bool` | Query, Optional | Optional, include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `user_id` | `uuid\|string` | Query, Optional | User id. |
| `name_starts_with_or_greater` | `string` | Query, Optional | Optional filter by items whose name is sorted equally or greater than a given input string. |
| `name_starts_with` | `string` | Query, Optional | Optional filter by items whose name is sorted equally than a given input string. |
| `name_less_than` | `string` | Query, Optional | Optional filter by items whose name is equally or lesser than a given input string. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |
| `enable_total_record_count` | `bool` | Query, Optional | Total record count.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_images = True
enable_total_record_count = True

result = studios_controller.get_studios(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_images, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

