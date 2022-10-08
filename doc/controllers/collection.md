# Collection

```python
collection_controller = client.collection
```

## Class Name

`CollectionController`

## Methods

* [Add to Collection](../../doc/controllers/collection.md#add-to-collection)
* [Create Collection](../../doc/controllers/collection.md#create-collection)
* [Remove From Collection](../../doc/controllers/collection.md#remove-from-collection)


# Add to Collection

Adds items to a collection.

```python
def add_to_collection(self,
                     collection_id,
                     ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `collection_id` | `uuid\|string` | Template, Required | The collection id. |
| `ids` | `List of uuid\|string` | Query, Required | Item ids, comma delimited. |

## Response Type

`void`

## Example Usage

```python
collection_id = '0000055a-0000-0000-0000-000000000000'
ids = ['00000add-0000-0000-0000-000000000000', '00000ade-0000-0000-0000-000000000000']

result = collection_controller.add_to_collection(collection_id, ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Create Collection

Creates a new collection.

```python
def create_collection(self,
                     name=None,
                     ids=None,
                     parent_id=None,
                     is_locked=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the collection. |
| `ids` | `List of string` | Query, Optional | Item Ids to add to the collection. |
| `parent_id` | `uuid\|string` | Query, Optional | Optional. Create the collection within a specific folder. |
| `is_locked` | `bool` | Query, Optional | Whether or not to lock the new collection.<br>**Default**: `False` |

## Response Type

[`CollectionCreationResult`](../../doc/models/collection-creation-result.md)

## Example Usage

```python
is_locked = False

result = collection_controller.create_collection(None, None, None, is_locked)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Remove From Collection

Removes items from a collection.

```python
def remove_from_collection(self,
                          collection_id,
                          ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `collection_id` | `uuid\|string` | Template, Required | The collection id. |
| `ids` | `List of uuid\|string` | Query, Required | Item ids, comma delimited. |

## Response Type

`void`

## Example Usage

```python
collection_id = '0000055a-0000-0000-0000-000000000000'
ids = ['00000add-0000-0000-0000-000000000000', '00000ade-0000-0000-0000-000000000000']

result = collection_controller.remove_from_collection(collection_id, ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

