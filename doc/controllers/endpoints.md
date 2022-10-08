# Endpoints

```python
endpoints_controller = client.endpoints
```

## Class Name

`EndpointsController`

## Methods

* [Get Pin](../../doc/controllers/endpoints.md#get-pin)
* [Get Pin Status](../../doc/controllers/endpoints.md#get-pin-status)
* [Get User Settings](../../doc/controllers/endpoints.md#get-user-settings)


# Get Pin

```python
def get_pin(self)
```

## Response Type

[`CodeResponse`](../../doc/models/code-response.md)

## Example Usage

```python
result = endpoints_controller.get_pin()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Pin Status

```python
def get_pin_status(self,
                  user_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_code` | `string` | Template, Required | - |

## Response Type

[`CodeStatusResponse`](../../doc/models/code-status-response.md)

## Example Usage

```python
user_code = 'userCode0'

result = endpoints_controller.get_pin_status(user_code)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get User Settings

```python
def get_user_settings(self,
                     user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`UserSettings`](../../doc/models/user-settings.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'

result = endpoints_controller.get_user_settings(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

