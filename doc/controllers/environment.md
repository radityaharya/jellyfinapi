# Environment

```python
environment_controller = client.environment
```

## Class Name

`EnvironmentController`

## Methods

* [Get Default Directory Browser](../../doc/controllers/environment.md#get-default-directory-browser)
* [Get Directory Contents](../../doc/controllers/environment.md#get-directory-contents)
* [Get Drives](../../doc/controllers/environment.md#get-drives)
* [Get Network Shares](../../doc/controllers/environment.md#get-network-shares)
* [Get Parent Path](../../doc/controllers/environment.md#get-parent-path)
* [Validate Path](../../doc/controllers/environment.md#validate-path)


# Get Default Directory Browser

Get Default directory browser.

```python
def get_default_directory_browser(self)
```

## Response Type

[`DefaultDirectoryBrowserInfoDto`](../../doc/models/default-directory-browser-info-dto.md)

## Example Usage

```python
result = environment_controller.get_default_directory_browser()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Directory Contents

Gets the contents of a given directory in the file system.

```python
def get_directory_contents(self,
                          path,
                          include_files=False,
                          include_directories=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `path` | `string` | Query, Required | The path. |
| `include_files` | `bool` | Query, Optional | An optional filter to include or exclude files from the results. true/false.<br>**Default**: `False` |
| `include_directories` | `bool` | Query, Optional | An optional filter to include or exclude folders from the results. true/false.<br>**Default**: `False` |

## Response Type

[`List of FileSystemEntryInfo`](../../doc/models/file-system-entry-info.md)

## Example Usage

```python
path = 'path6'
include_files = False
include_directories = False

result = environment_controller.get_directory_contents(path, include_files, include_directories)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Drives

Gets available drives from the server's file system.

```python
def get_drives(self)
```

## Response Type

[`List of FileSystemEntryInfo`](../../doc/models/file-system-entry-info.md)

## Example Usage

```python
result = environment_controller.get_drives()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Network Shares

**This endpoint is deprecated.**

Gets network paths.

```python
def get_network_shares(self)
```

## Response Type

[`List of FileSystemEntryInfo`](../../doc/models/file-system-entry-info.md)

## Example Usage

```python
result = environment_controller.get_network_shares()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Parent Path

Gets the parent path of a given path.

```python
def get_parent_path(self,
                   path)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `path` | `string` | Query, Required | The path. |

## Response Type

`string`

## Example Usage

```python
path = 'path6'

result = environment_controller.get_parent_path(path)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Validate Path

Validates path.

```python
def validate_path(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ValidatePathDto`](../../doc/models/validate-path-dto.md) | Body, Required | Validate request object. |

## Response Type

`void`

## Example Usage

```python
body = ValidatePathDto()

result = environment_controller.validate_path(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Path not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

