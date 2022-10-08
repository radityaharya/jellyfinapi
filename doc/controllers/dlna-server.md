# Dlna Server

```python
dlna_server_controller = client.dlna_server
```

## Class Name

`DlnaServerController`

## Methods

* [Get Connection Manager](../../doc/controllers/dlna-server.md#get-connection-manager)
* [Get Connection Manager 2](../../doc/controllers/dlna-server.md#get-connection-manager-2)
* [Get Connection Manager 3](../../doc/controllers/dlna-server.md#get-connection-manager-3)
* [Get Content Directory](../../doc/controllers/dlna-server.md#get-content-directory)
* [Get Content Directory 2](../../doc/controllers/dlna-server.md#get-content-directory-2)
* [Get Content Directory 3](../../doc/controllers/dlna-server.md#get-content-directory-3)
* [Get Description Xml](../../doc/controllers/dlna-server.md#get-description-xml)
* [Get Description Xml 2](../../doc/controllers/dlna-server.md#get-description-xml-2)
* [Get Icon](../../doc/controllers/dlna-server.md#get-icon)
* [Get Icon Id](../../doc/controllers/dlna-server.md#get-icon-id)
* [Get Media Receiver Registrar](../../doc/controllers/dlna-server.md#get-media-receiver-registrar)
* [Get Media Receiver Registrar 2](../../doc/controllers/dlna-server.md#get-media-receiver-registrar-2)
* [Get Media Receiver Registrar 3](../../doc/controllers/dlna-server.md#get-media-receiver-registrar-3)
* [Process Connection Manager Control Request](../../doc/controllers/dlna-server.md#process-connection-manager-control-request)
* [Process Content Directory Control Request](../../doc/controllers/dlna-server.md#process-content-directory-control-request)
* [Process Media Receiver Registrar Control Request](../../doc/controllers/dlna-server.md#process-media-receiver-registrar-control-request)


# Get Connection Manager

Gets Dlna media receiver registrar xml.

```python
def get_connection_manager(self,
                          server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_connection_manager(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Connection Manager 2

Gets Dlna media receiver registrar xml.

```python
def get_connection_manager_2(self,
                            server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_connection_manager_2(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Connection Manager 3

Gets Dlna media receiver registrar xml.

```python
def get_connection_manager_3(self,
                            server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_connection_manager_3(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Content Directory

Gets Dlna content directory xml.

```python
def get_content_directory(self,
                         server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_content_directory(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Content Directory 2

Gets Dlna content directory xml.

```python
def get_content_directory_2(self,
                           server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_content_directory_2(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Content Directory 3

Gets Dlna content directory xml.

```python
def get_content_directory_3(self,
                           server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_content_directory_3(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Description Xml

Get Description Xml.

```python
def get_description_xml(self,
                       server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_description_xml(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Description Xml 2

Get Description Xml.

```python
def get_description_xml_2(self,
                         server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_description_xml_2(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Icon

Gets a server icon.

```python
def get_icon(self,
            file_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `string` | Template, Required | The icon filename. |

## Response Type

`mixed`

## Example Usage

```python
file_name = 'fileName4'

result = dlna_server_controller.get_icon(file_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 503 | DLNA is disabled. | `APIException` |


# Get Icon Id

Gets a server icon.

```python
def get_icon_id(self,
               server_id,
               file_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |
| `file_name` | `string` | Template, Required | The icon filename. |

## Response Type

`mixed`

## Example Usage

```python
server_id = 'serverId8'
file_name = 'fileName4'

result = dlna_server_controller.get_icon_id(server_id, file_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 503 | DLNA is disabled. | `APIException` |


# Get Media Receiver Registrar

Gets Dlna media receiver registrar xml.

```python
def get_media_receiver_registrar(self,
                                server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_media_receiver_registrar(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Media Receiver Registrar 2

Gets Dlna media receiver registrar xml.

```python
def get_media_receiver_registrar_2(self,
                                  server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_media_receiver_registrar_2(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Get Media Receiver Registrar 3

Gets Dlna media receiver registrar xml.

```python
def get_media_receiver_registrar_3(self,
                                  server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.get_media_receiver_registrar_3(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Process Connection Manager Control Request

Process a connection manager control request.

```python
def process_connection_manager_control_request(self,
                                              server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.process_connection_manager_control_request(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Process Content Directory Control Request

Process a content directory control request.

```python
def process_content_directory_control_request(self,
                                             server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.process_content_directory_control_request(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |


# Process Media Receiver Registrar Control Request

Process a media receiver registrar control request.

```python
def process_media_receiver_registrar_control_request(self,
                                                    server_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `server_id` | `string` | Template, Required | Server UUID. |

## Response Type

`binary`

## Example Usage

```python
server_id = 'serverId8'

result = dlna_server_controller.process_media_receiver_registrar_control_request(server_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 503 | DLNA is disabled. | `APIException` |

