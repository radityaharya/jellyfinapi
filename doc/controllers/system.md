# System

```python
system_controller = client.system
```

## Class Name

`SystemController`

## Methods

* [Get Endpoint Info](../../doc/controllers/system.md#get-endpoint-info)
* [Get Log File](../../doc/controllers/system.md#get-log-file)
* [Get Ping System](../../doc/controllers/system.md#get-ping-system)
* [Get Public System Info](../../doc/controllers/system.md#get-public-system-info)
* [Get Server Logs](../../doc/controllers/system.md#get-server-logs)
* [Get System Info](../../doc/controllers/system.md#get-system-info)
* [Get Wake on Lan Info](../../doc/controllers/system.md#get-wake-on-lan-info)
* [Post Ping System](../../doc/controllers/system.md#post-ping-system)
* [Restart Application](../../doc/controllers/system.md#restart-application)
* [Shutdown Application](../../doc/controllers/system.md#shutdown-application)


# Get Endpoint Info

Gets information about the request endpoint.

```python
def get_endpoint_info(self)
```

## Response Type

[`EndPointInfo`](../../doc/models/end-point-info.md)

## Example Usage

```python
result = system_controller.get_endpoint_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Log File

Gets a log file.

```python
def get_log_file(self,
                name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Required | The name of the log file to get. |

## Response Type

`binary`

## Example Usage

```python
name = 'name0'

result = system_controller.get_log_file(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Ping System

Pings the system.

```python
def get_ping_system(self)
```

## Response Type

`string`

## Example Usage

```python
result = system_controller.get_ping_system()
```


# Get Public System Info

Gets public information about the server.

```python
def get_public_system_info(self)
```

## Response Type

[`PublicSystemInfo`](../../doc/models/public-system-info.md)

## Example Usage

```python
result = system_controller.get_public_system_info()
```


# Get Server Logs

Gets a list of available server log files.

```python
def get_server_logs(self)
```

## Response Type

[`List of LogFile`](../../doc/models/log-file.md)

## Example Usage

```python
result = system_controller.get_server_logs()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get System Info

Gets information about the server.

```python
def get_system_info(self)
```

## Response Type

[`SystemInfo`](../../doc/models/system-info.md)

## Example Usage

```python
result = system_controller.get_system_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Wake on Lan Info

**This endpoint is deprecated.**

Gets wake on lan information.

```python
def get_wake_on_lan_info(self)
```

## Response Type

[`List of WakeOnLanInfo`](../../doc/models/wake-on-lan-info.md)

## Example Usage

```python
result = system_controller.get_wake_on_lan_info()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Post Ping System

Pings the system.

```python
def post_ping_system(self)
```

## Response Type

`string`

## Example Usage

```python
result = system_controller.post_ping_system()
```


# Restart Application

Restarts the application.

```python
def restart_application(self)
```

## Response Type

`void`

## Example Usage

```python
result = system_controller.restart_application()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Shutdown Application

Shuts down the application.

```python
def shutdown_application(self)
```

## Response Type

`void`

## Example Usage

```python
result = system_controller.shutdown_application()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

