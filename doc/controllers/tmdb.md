# Tmdb

```python
tmdb_controller = client.tmdb
```

## Class Name

`TmdbController`


# Tmdb Client Configuration

Gets the TMDb image configuration options.

```python
def tmdb_client_configuration(self)
```

## Response Type

[`ConfigImageTypes`](../../doc/models/config-image-types.md)

## Example Usage

```python
result = tmdb_controller.tmdb_client_configuration()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

