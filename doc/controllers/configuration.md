# Configuration

```python
configuration_controller = client.configuration
```

## Class Name

`ConfigurationController`

## Methods

* [Get Configuration](../../doc/controllers/configuration.md#get-configuration)
* [Get Default Metadata Options](../../doc/controllers/configuration.md#get-default-metadata-options)
* [Get Named Configuration](../../doc/controllers/configuration.md#get-named-configuration)
* [Update Configuration](../../doc/controllers/configuration.md#update-configuration)
* [Update Media Encoder Path](../../doc/controllers/configuration.md#update-media-encoder-path)
* [Update Named Configuration](../../doc/controllers/configuration.md#update-named-configuration)


# Get Configuration

Gets application configuration.

```python
def get_configuration(self)
```

## Response Type

[`ServerConfiguration`](../../doc/models/server-configuration.md)

## Example Usage

```python
result = configuration_controller.get_configuration()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Default Metadata Options

Gets a default MetadataOptions object.

```python
def get_default_metadata_options(self)
```

## Response Type

[`MetadataOptions`](../../doc/models/metadata-options.md)

## Example Usage

```python
result = configuration_controller.get_default_metadata_options()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Named Configuration

Gets a named configuration.

```python
def get_named_configuration(self,
                           key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Template, Required | Configuration key. |

## Response Type

`binary`

## Example Usage

```python
key = 'key0'

result = configuration_controller.get_named_configuration(key)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Configuration

Updates application configuration.

```python
def update_configuration(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ServerConfiguration`](../../doc/models/server-configuration.md) | Body, Required | Configuration. |

## Response Type

`void`

## Example Usage

```python
body = ServerConfiguration()

result = configuration_controller.update_configuration(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Media Encoder Path

Updates the path to the media encoder.

```python
def update_media_encoder_path(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MediaEncoderPathDto`](../../doc/models/media-encoder-path-dto.md) | Body, Required | Media encoder path form body. |

## Response Type

`void`

## Example Usage

```python
body = MediaEncoderPathDto()

result = configuration_controller.update_media_encoder_path(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Named Configuration

Updates named configuration.

```python
def update_named_configuration(self,
                              key,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Template, Required | Configuration key. |
| `body` | `object` | Body, Required | Configuration. |

## Response Type

`void`

## Example Usage

```python
key = 'key0'
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = configuration_controller.update_named_configuration(key, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

