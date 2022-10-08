# Persons

```python
persons_controller = client.persons
```

## Class Name

`PersonsController`

## Methods

* [Get Person](../../doc/controllers/persons.md#get-person)
* [Get Persons](../../doc/controllers/persons.md#get-persons)


# Get Person

Get person by name.

```python
def get_person(self,
              name,
              user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Person name. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |

## Response Type

[`BaseItemDto`](../../doc/models/base-item-dto.md)

## Example Usage

```python
name = 'name0'

result = persons_controller.get_person(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Person not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Persons

Gets all persons.

```python
def get_persons(self,
               limit=None,
               search_term=None,
               fields=None,
               filters=None,
               is_favorite=None,
               enable_user_data=None,
               image_type_limit=None,
               enable_image_types=None,
               exclude_person_types=None,
               person_types=None,
               appears_in_item_id=None,
               user_id=None,
               enable_images=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `search_term` | `string` | Query, Optional | The search term. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `filters` | [`List of ItemFilterEnum`](../../doc/models/item-filter-enum.md) | Query, Optional | Optional. Specify additional filters to apply. |
| `is_favorite` | `bool` | Query, Optional | Optional filter by items that are marked as favorite, or not. userId is required. |
| `enable_user_data` | `bool` | Query, Optional | Optional, include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional, the max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |
| `exclude_person_types` | `List of string` | Query, Optional | Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited. |
| `person_types` | `List of string` | Query, Optional | Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited. |
| `appears_in_item_id` | `uuid\|string` | Query, Optional | Optional. If specified, person results will be filtered on items related to said persons. |
| `user_id` | `uuid\|string` | Query, Optional | User id. |
| `enable_images` | `bool` | Query, Optional | Optional, include image information in output.<br>**Default**: `True` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
enable_images = True

result = persons_controller.get_persons(None, None, None, None, None, None, None, None, None, None, None, None, enable_images)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

