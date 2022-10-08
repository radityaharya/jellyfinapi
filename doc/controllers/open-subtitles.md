# Open Subtitles

```python
open_subtitles_controller = client.open_subtitles
```

## Class Name

`OpenSubtitlesController`


# Validate Login Info

```python
def validate_login_info(self,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginInfoInput`](../../doc/models/login-info-input.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
result = open_subtitles_controller.validate_login_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 403 | Forbidden | `APIException` |

