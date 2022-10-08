# Trakt

```python
trakt_controller = client.trakt
```

## Class Name

`TraktController`

## Methods

* [Recommended Trakt Movies](../../doc/controllers/trakt.md#recommended-trakt-movies)
* [Recommended Trakt Shows](../../doc/controllers/trakt.md#recommended-trakt-shows)
* [Trakt Device Authorization](../../doc/controllers/trakt.md#trakt-device-authorization)
* [Trakt Device De Authorization](../../doc/controllers/trakt.md#trakt-device-de-authorization)
* [Trakt Poll Authorization Status](../../doc/controllers/trakt.md#trakt-poll-authorization-status)
* [Trakt Rate Item](../../doc/controllers/trakt.md#trakt-rate-item)


# Recommended Trakt Movies

```python
def recommended_trakt_movies(self,
                            user_guid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of TraktMovie`](../../doc/models/trakt-movie.md)

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'

result = trakt_controller.recommended_trakt_movies(user_guid)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Recommended Trakt Shows

```python
def recommended_trakt_shows(self,
                           user_guid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of TraktShow`](../../doc/models/trakt-show.md)

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'

result = trakt_controller.recommended_trakt_shows(user_guid)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Trakt Device Authorization

```python
def trakt_device_authorization(self,
                              user_guid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'

result = trakt_controller.trakt_device_authorization(user_guid)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Trakt Device De Authorization

```python
def trakt_device_de_authorization(self,
                                 user_guid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |

## Response Type

`string`

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'

result = trakt_controller.trakt_device_de_authorization(user_guid)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Trakt Poll Authorization Status

```python
def trakt_poll_authorization_status(self,
                                   user_guid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'

result = trakt_controller.trakt_poll_authorization_status(user_guid)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Trakt Rate Item

```python
def trakt_rate_item(self,
                   user_guid,
                   item_id,
                   rating=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_guid` | `uuid\|string` | Template, Required | - |
| `item_id` | `uuid\|string` | Template, Required | - |
| `rating` | `int` | Query, Optional | - |

## Response Type

[`TraktSyncResponse`](../../doc/models/trakt-sync-response.md)

## Example Usage

```python
user_guid = '000010b0-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = trakt_controller.trakt_rate_item(user_guid, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

