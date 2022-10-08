# Remote Image

```python
remote_image_controller = client.remote_image
```

## Class Name

`RemoteImageController`

## Methods

* [Download Remote Image](../../doc/controllers/remote-image.md#download-remote-image)
* [Get Remote Image Providers](../../doc/controllers/remote-image.md#get-remote-image-providers)
* [Get Remote Images](../../doc/controllers/remote-image.md#get-remote-images)


# Download Remote Image

Downloads a remote image for an item.

```python
def download_remote_image(self,
                         item_id,
                         mtype,
                         image_url=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item Id. |
| `mtype` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Required | The image type. |
| `image_url` | `string` | Query, Optional | The image url. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
mtype = ImageTypeEnum.THUMB

result = remote_image_controller.download_remote_image(item_id, mtype)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Remote image not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Remote Image Providers

Gets available remote image providers for an item.

```python
def get_remote_image_providers(self,
                              item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item Id. |

## Response Type

[`List of ImageProviderInfo`](../../doc/models/image-provider-info.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = remote_image_controller.get_remote_image_providers(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Remote Images

Gets available remote images for an item.

```python
def get_remote_images(self,
                     item_id,
                     mtype=None,
                     start_index=None,
                     limit=None,
                     provider_name=None,
                     include_all_languages=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item Id. |
| `mtype` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | The image type. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `provider_name` | `string` | Query, Optional | Optional. The image provider to use. |
| `include_all_languages` | `bool` | Query, Optional | Optional. Include all languages.<br>**Default**: `False` |

## Response Type

[`RemoteImageResult`](../../doc/models/remote-image-result.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
include_all_languages = False

result = remote_image_controller.get_remote_images(item_id, None, None, None, None, include_all_languages)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

