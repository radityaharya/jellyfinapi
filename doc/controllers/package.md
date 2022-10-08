# Package

```python
package_controller = client.package
```

## Class Name

`PackageController`

## Methods

* [Cancel Package Installation](../../doc/controllers/package.md#cancel-package-installation)
* [Get Package Info](../../doc/controllers/package.md#get-package-info)
* [Get Packages](../../doc/controllers/package.md#get-packages)
* [Get Repositories](../../doc/controllers/package.md#get-repositories)
* [Install Package](../../doc/controllers/package.md#install-package)
* [Set Repositories](../../doc/controllers/package.md#set-repositories)


# Cancel Package Installation

Cancels a package installation.

```python
def cancel_package_installation(self,
                               package_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `package_id` | `uuid\|string` | Template, Required | Installation Id. |

## Response Type

`void`

## Example Usage

```python
package_id = '00000d24-0000-0000-0000-000000000000'

result = package_controller.cancel_package_installation(package_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Package Info

Gets a package by name or assembly GUID.

```python
def get_package_info(self,
                    name,
                    assembly_guid=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The name of the package. |
| `assembly_guid` | `uuid\|string` | Query, Optional | The GUID of the associated assembly. |

## Response Type

[`PackageInfo`](../../doc/models/package-info.md)

## Example Usage

```python
name = 'name0'

result = package_controller.get_package_info(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Packages

Gets available packages.

```python
def get_packages(self)
```

## Response Type

[`List of PackageInfo`](../../doc/models/package-info.md)

## Example Usage

```python
result = package_controller.get_packages()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Repositories

Gets all package repositories.

```python
def get_repositories(self)
```

## Response Type

[`List of RepositoryInfo`](../../doc/models/repository-info.md)

## Example Usage

```python
result = package_controller.get_repositories()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Install Package

Installs a package.

```python
def install_package(self,
                   name,
                   assembly_guid=None,
                   version=None,
                   repository_url=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Package name. |
| `assembly_guid` | `uuid\|string` | Query, Optional | GUID of the associated assembly. |
| `version` | `string` | Query, Optional | Optional version. Defaults to latest version. |
| `repository_url` | `string` | Query, Optional | Optional. Specify the repository to install from. |

## Response Type

`void`

## Example Usage

```python
name = 'name0'

result = package_controller.install_package(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Package not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Set Repositories

Sets the enabled and existing package repositories.

```python
def set_repositories(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of RepositoryInfo`](../../doc/models/repository-info.md) | Body, Required | The list of package repositories. |

## Response Type

`void`

## Example Usage

```python
body = []

body.append(RepositoryInfo())

body.append(RepositoryInfo())


result = package_controller.set_repositories(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

