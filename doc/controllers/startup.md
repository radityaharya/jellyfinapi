# Startup

```python
startup_controller = client.startup
```

## Class Name

`StartupController`

## Methods

* [Complete Wizard](../../doc/controllers/startup.md#complete-wizard)
* [Get First User](../../doc/controllers/startup.md#get-first-user)
* [Get First User 2](../../doc/controllers/startup.md#get-first-user-2)
* [Get Startup Configuration](../../doc/controllers/startup.md#get-startup-configuration)
* [Set Remote Access](../../doc/controllers/startup.md#set-remote-access)
* [Update Initial Configuration](../../doc/controllers/startup.md#update-initial-configuration)
* [Update Startup User](../../doc/controllers/startup.md#update-startup-user)


# Complete Wizard

Completes the startup wizard.

```python
def complete_wizard(self)
```

## Response Type

`void`

## Example Usage

```python
result = startup_controller.complete_wizard()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get First User

Gets the first user.

```python
def get_first_user(self)
```

## Response Type

[`StartupUserDto`](../../doc/models/startup-user-dto.md)

## Example Usage

```python
result = startup_controller.get_first_user()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get First User 2

Gets the first user.

```python
def get_first_user_2(self)
```

## Response Type

[`StartupUserDto`](../../doc/models/startup-user-dto.md)

## Example Usage

```python
result = startup_controller.get_first_user_2()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Startup Configuration

Gets the initial startup wizard configuration.

```python
def get_startup_configuration(self)
```

## Response Type

[`StartupConfigurationDto`](../../doc/models/startup-configuration-dto.md)

## Example Usage

```python
result = startup_controller.get_startup_configuration()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Set Remote Access

Sets remote access and UPnP.

```python
def set_remote_access(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StartupRemoteAccessDto`](../../doc/models/startup-remote-access-dto.md) | Body, Required | The startup remote access dto. |

## Response Type

`void`

## Example Usage

```python
body = StartupRemoteAccessDto()
body.enable_remote_access = False
body.enable_automatic_port_mapping = False

result = startup_controller.set_remote_access(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Initial Configuration

Sets the initial startup wizard configuration.

```python
def update_initial_configuration(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StartupConfigurationDto`](../../doc/models/startup-configuration-dto.md) | Body, Required | The updated startup configuration. |

## Response Type

`void`

## Example Usage

```python
body = StartupConfigurationDto()

result = startup_controller.update_initial_configuration(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Startup User

Sets the user name and password.

```python
def update_startup_user(self,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StartupUserDto`](../../doc/models/startup-user-dto.md) | Body, Optional | The DTO containing username and password. |

## Response Type

`void`

## Example Usage

```python
result = startup_controller.update_startup_user()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

