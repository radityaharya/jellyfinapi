# Suggestions

```python
suggestions_controller = client.suggestions
```

## Class Name

`SuggestionsController`


# Get Suggestions

Gets suggestions.

```python
def get_suggestions(self,
                   user_id,
                   media_type=None,
                   mtype=None,
                   start_index=None,
                   limit=None,
                   enable_total_record_count=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | The user id. |
| `media_type` | `List of string` | Query, Optional | The media types. |
| `mtype` | [`List of BaseItemKindEnum`](../../doc/models/base-item-kind-enum.md) | Query, Optional | The type. |
| `start_index` | `int` | Query, Optional | Optional. The start index. |
| `limit` | `int` | Query, Optional | Optional. The limit. |
| `enable_total_record_count` | `bool` | Query, Optional | Whether to enable the total record count.<br>**Default**: `False` |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
enable_total_record_count = False

result = suggestions_controller.get_suggestions(user_id, None, None, None, None, enable_total_record_count)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

