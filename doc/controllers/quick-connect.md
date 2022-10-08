# Quick Connect

```python
quick_connect_controller = client.quick_connect
```

## Class Name

`QuickConnectController`

## Methods

* [Authorize](../../doc/controllers/quick-connect.md#authorize)
* [Connect](../../doc/controllers/quick-connect.md#connect)
* [Get Enabled](../../doc/controllers/quick-connect.md#get-enabled)
* [Initiate](../../doc/controllers/quick-connect.md#initiate)


# Authorize

Authorizes a pending quick connect request.

```python
def authorize(self,
             code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Query, Required | Quick connect code to authorize. |

## Response Type

`bool`

## Example Usage

```python
code = 'code8'

result = quick_connect_controller.authorize(code)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Unknown user id. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Connect

Attempts to retrieve authentication information.

```python
def connect(self,
           secret)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secret` | `string` | Query, Required | Secret previously returned from the Initiate endpoint. |

## Response Type

[`QuickConnectResult`](../../doc/models/quick-connect-result.md)

## Example Usage

```python
secret = 'secret4'

result = quick_connect_controller.connect(secret)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Unknown quick connect secret. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Enabled

Gets the current quick connect state.

```python
def get_enabled(self)
```

## Response Type

`bool`

## Example Usage

```python
result = quick_connect_controller.get_enabled()
```


# Initiate

Initiate a new quick connect request.

```python
def initiate(self)
```

## Response Type

[`QuickConnectResult`](../../doc/models/quick-connect-result.md)

## Example Usage

```python
result = quick_connect_controller.initiate()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Quick connect is not active on this server. | `APIException` |

