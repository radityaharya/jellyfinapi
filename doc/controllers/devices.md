# Devices

```python
devices_controller = client.devices
```

## Class Name

`DevicesController`

## Methods

* [Delete Device](../../doc/controllers/devices.md#delete-device)
* [Get Device Info](../../doc/controllers/devices.md#get-device-info)
* [Get Device Options](../../doc/controllers/devices.md#get-device-options)
* [Get Devices](../../doc/controllers/devices.md#get-devices)
* [Update Device Options](../../doc/controllers/devices.md#update-device-options)


# Delete Device

Deletes a device.

```python
def delete_device(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Required | Device Id. |

## Response Type

`void`

## Example Usage

```python
id = 'id0'

result = devices_controller.delete_device(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Device Info

Get info for a device.

```python
def get_device_info(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Required | Device Id. |

## Response Type

[`DeviceInfo`](../../doc/models/device-info.md)

## Example Usage

```python
id = 'id0'

result = devices_controller.get_device_info(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Device Options

Get options for a device.

```python
def get_device_options(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Required | Device Id. |

## Response Type

[`DeviceOptions`](../../doc/models/device-options.md)

## Example Usage

```python
id = 'id0'

result = devices_controller.get_device_options(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Device not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Devices

Get Devices.

```python
def get_devices(self,
               supports_sync=None,
               user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supports_sync` | `bool` | Query, Optional | Gets or sets a value indicating whether [supports synchronize]. |
| `user_id` | `uuid\|string` | Query, Optional | Gets or sets the user identifier. |

## Response Type

[`DeviceInfoQueryResult`](../../doc/models/device-info-query-result.md)

## Example Usage

```python
result = devices_controller.get_devices()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Device Options

Update device options.

```python
def update_device_options(self,
                         id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Query, Required | Device Id. |
| `body` | [`DeviceOptionsDto`](../../doc/models/device-options-dto.md) | Body, Required | Device Options. |

## Response Type

`void`

## Example Usage

```python
id = 'id0'
body = DeviceOptionsDto()

result = devices_controller.update_device_options(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

