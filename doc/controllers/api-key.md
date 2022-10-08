# Api Key

```python
api_key_controller = client.api_key
```

## Class Name

`ApiKeyController`

## Methods

* [Create Key](../../doc/controllers/api-key.md#create-key)
* [Get Keys](../../doc/controllers/api-key.md#get-keys)
* [Revoke Key](../../doc/controllers/api-key.md#revoke-key)


# Create Key

Create a new api key.

```python
def create_key(self,
              app)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app` | `string` | Query, Required | Name of the app using the authentication key. |

## Response Type

`void`

## Example Usage

```python
app = 'app2'

result = api_key_controller.create_key(app)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Keys

Get all keys.

```python
def get_keys(self)
```

## Response Type

[`AuthenticationInfoQueryResult`](../../doc/models/authentication-info-query-result.md)

## Example Usage

```python
result = api_key_controller.get_keys()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Revoke Key

Remove an api key.

```python
def revoke_key(self,
              key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Template, Required | The access token to delete. |

## Response Type

`void`

## Example Usage

```python
key = 'key0'

result = api_key_controller.revoke_key(key)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

