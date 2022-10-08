# Library Structure

```python
library_structure_controller = client.library_structure
```

## Class Name

`LibraryStructureController`

## Methods

* [Add Media Path](../../doc/controllers/library-structure.md#add-media-path)
* [Add Virtual Folder](../../doc/controllers/library-structure.md#add-virtual-folder)
* [Get Virtual Folders](../../doc/controllers/library-structure.md#get-virtual-folders)
* [Remove Media Path](../../doc/controllers/library-structure.md#remove-media-path)
* [Remove Virtual Folder](../../doc/controllers/library-structure.md#remove-virtual-folder)
* [Rename Virtual Folder](../../doc/controllers/library-structure.md#rename-virtual-folder)
* [Update Library Options](../../doc/controllers/library-structure.md#update-library-options)
* [Update Media Path](../../doc/controllers/library-structure.md#update-media-path)


# Add Media Path

Add a media path to a library.

```python
def add_media_path(self,
                  body,
                  refresh_library=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MediaPathDto`](../../doc/models/media-path-dto.md) | Body, Required | The media path dto. |
| `refresh_library` | `bool` | Query, Optional | Whether to refresh the library.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
body = MediaPathDto()
body.name = 'Name6'
refresh_library = False

result = library_structure_controller.add_media_path(body, refresh_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Add Virtual Folder

Adds a virtual folder.

```python
def add_virtual_folder(self,
                      name=None,
                      collection_type=None,
                      paths=None,
                      refresh_library=False,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the virtual folder. |
| `collection_type` | [`CollectionTypeOptionsEnum`](../../doc/models/collection-type-options-enum.md) | Query, Optional | The type of the collection. |
| `paths` | `List of string` | Query, Optional | The paths of the virtual folder. |
| `refresh_library` | `bool` | Query, Optional | Whether to refresh the library.<br>**Default**: `False` |
| `body` | [`AddVirtualFolderDto`](../../doc/models/add-virtual-folder-dto.md) | Body, Optional | The library options. |

## Response Type

`void`

## Example Usage

```python
refresh_library = False

result = library_structure_controller.add_virtual_folder(None, None, None, refresh_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Virtual Folders

Gets all virtual folders.

```python
def get_virtual_folders(self)
```

## Response Type

[`List of VirtualFolderInfo`](../../doc/models/virtual-folder-info.md)

## Example Usage

```python
result = library_structure_controller.get_virtual_folders()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Remove Media Path

Remove a media path.

```python
def remove_media_path(self,
                     name=None,
                     path=None,
                     refresh_library=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the library. |
| `path` | `string` | Query, Optional | The path to remove. |
| `refresh_library` | `bool` | Query, Optional | Whether to refresh the library.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
refresh_library = False

result = library_structure_controller.remove_media_path(None, None, refresh_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Remove Virtual Folder

Removes a virtual folder.

```python
def remove_virtual_folder(self,
                         name=None,
                         refresh_library=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the folder. |
| `refresh_library` | `bool` | Query, Optional | Whether to refresh the library.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
refresh_library = False

result = library_structure_controller.remove_virtual_folder(None, refresh_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Rename Virtual Folder

Renames a virtual folder.

```python
def rename_virtual_folder(self,
                         name=None,
                         new_name=None,
                         refresh_library=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The name of the virtual folder. |
| `new_name` | `string` | Query, Optional | The new name. |
| `refresh_library` | `bool` | Query, Optional | Whether to refresh the library.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
refresh_library = False

result = library_structure_controller.rename_virtual_folder(None, None, refresh_library)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Library doesn't exist. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 409 | Library already exists. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Library Options

Update library options.

```python
def update_library_options(self,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateLibraryOptionsDto`](../../doc/models/update-library-options-dto.md) | Body, Optional | The library name and options. |

## Response Type

`void`

## Example Usage

```python
result = library_structure_controller.update_library_options()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Update Media Path

Updates a media path.

```python
def update_media_path(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateMediaPathRequestDto`](../../doc/models/update-media-path-request-dto.md) | Body, Required | The name of the library and path infos. |

## Response Type

`void`

## Example Usage

```python
body = UpdateMediaPathRequestDto()
body.name = 'Name6'
body.path_info = MediaPathInfo()

result = library_structure_controller.update_media_path(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

