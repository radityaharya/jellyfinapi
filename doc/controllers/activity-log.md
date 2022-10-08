# Activity Log

```python
activity_log_controller = client.activity_log
```

## Class Name

`ActivityLogController`


# Get Log Entries

Gets activity log entries.

```python
def get_log_entries(self,
                   start_index=None,
                   limit=None,
                   min_date=None,
                   has_user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `min_date` | `datetime` | Query, Optional | Optional. The minimum date. Format = ISO. |
| `has_user_id` | `bool` | Query, Optional | Optional. Filter log entries if it has user id, or not. |

## Response Type

[`ActivityLogEntryQueryResult`](../../doc/models/activity-log-entry-query-result.md)

## Example Usage

```python
result = activity_log_controller.get_log_entries()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

