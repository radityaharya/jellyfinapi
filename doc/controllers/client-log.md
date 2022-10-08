# Client Log

```python
client_log_controller = client.client_log
```

## Class Name

`ClientLogController`


# Log File

Upload a document.

```python
def log_file(self,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

[`ClientLogDocumentResponseDto`](../../doc/models/client-log-document-response-dto.md)

## Example Usage

```python
result = client_log_controller.log_file()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Event logging disabled. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 413 | Upload size too large. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

