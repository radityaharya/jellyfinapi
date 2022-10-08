# Item Update

```python
item_update_controller = client.item_update
```

## Class Name

`ItemUpdateController`

## Methods

* [Get Metadata Editor Info](../../doc/controllers/item-update.md#get-metadata-editor-info)
* [Update Item](../../doc/controllers/item-update.md#update-item)
* [Update Item Content Type](../../doc/controllers/item-update.md#update-item-content-type)


# Get Metadata Editor Info

Gets metadata editor info for an item.

```python
def get_metadata_editor_info(self,
                            item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |

## Response Type

[`MetadataEditorInfo`](../../doc/models/metadata-editor-info.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = item_update_controller.get_metadata_editor_info(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Item

Updates an item.

```python
def update_item(self,
               item_id,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `body` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Body, Required | The new item properties. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
body = BaseItemDto()

result = item_update_controller.update_item(item_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Item Content Type

Updates an item's content type.

```python
def update_item_content_type(self,
                            item_id,
                            content_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `content_type` | `string` | Query, Optional | The content type of the item. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = item_update_controller.update_item_content_type(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

