# Plugins

```python
plugins_controller = client.plugins
```

## Class Name

`PluginsController`

## Methods

* [Disable Plugin](../../doc/controllers/plugins.md#disable-plugin)
* [Enable Plugin](../../doc/controllers/plugins.md#enable-plugin)
* [Get Plugin Configuration](../../doc/controllers/plugins.md#get-plugin-configuration)
* [Get Plugin Image](../../doc/controllers/plugins.md#get-plugin-image)
* [Get Plugin Manifest](../../doc/controllers/plugins.md#get-plugin-manifest)
* [Get Plugins](../../doc/controllers/plugins.md#get-plugins)
* [Uninstall Plugin](../../doc/controllers/plugins.md#uninstall-plugin)
* [Uninstall Plugin by Version](../../doc/controllers/plugins.md#uninstall-plugin-by-version)
* [Update Plugin Configuration](../../doc/controllers/plugins.md#update-plugin-configuration)


# Disable Plugin

Disable a plugin.

```python
def disable_plugin(self,
                  plugin_id,
                  version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |
| `version` | `string` | Template, Required | Plugin version. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'
version = 'version4'

result = plugins_controller.disable_plugin(plugin_id, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Enable Plugin

Enables a disabled plugin.

```python
def enable_plugin(self,
                 plugin_id,
                 version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |
| `version` | `string` | Template, Required | Plugin version. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'
version = 'version4'

result = plugins_controller.enable_plugin(plugin_id, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Plugin Configuration

Gets plugin configuration.

```python
def get_plugin_configuration(self,
                            plugin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |

## Response Type

`object`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'

result = plugins_controller.get_plugin_configuration(plugin_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found or plugin configuration not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Plugin Image

Gets a plugin's image.

```python
def get_plugin_image(self,
                    plugin_id,
                    version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |
| `version` | `string` | Template, Required | Plugin version. |

## Response Type

`mixed`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'
version = 'version4'

result = plugins_controller.get_plugin_image(plugin_id, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Plugin Manifest

Gets a plugin's manifest.

```python
def get_plugin_manifest(self,
                       plugin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'

result = plugins_controller.get_plugin_manifest(plugin_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Plugins

Gets a list of currently installed plugins.

```python
def get_plugins(self)
```

## Response Type

[`List of PluginInfo`](../../doc/models/plugin-info.md)

## Example Usage

```python
result = plugins_controller.get_plugins()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Uninstall Plugin

**This endpoint is deprecated.**

Uninstalls a plugin.

```python
def uninstall_plugin(self,
                    plugin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'

result = plugins_controller.uninstall_plugin(plugin_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Uninstall Plugin by Version

Uninstalls a plugin by version.

```python
def uninstall_plugin_by_version(self,
                               plugin_id,
                               version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |
| `version` | `string` | Template, Required | Plugin version. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'
version = 'version4'

result = plugins_controller.uninstall_plugin_by_version(plugin_id, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Plugin Configuration

Accepts plugin configuration as JSON body.

```python
def update_plugin_configuration(self,
                               plugin_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plugin_id` | `uuid\|string` | Template, Required | Plugin id. |

## Response Type

`void`

## Example Usage

```python
plugin_id = '00000c42-0000-0000-0000-000000000000'

result = plugins_controller.update_plugin_configuration(plugin_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Plugin not found or plugin does not have configuration. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

