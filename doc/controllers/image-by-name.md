# Image by Name

```python
image_by_name_controller = client.image_by_name
```

## Class Name

`ImageByNameController`

## Methods

* [Get General Image](../../doc/controllers/image-by-name.md#get-general-image)
* [Get General Images](../../doc/controllers/image-by-name.md#get-general-images)
* [Get Media Info Image](../../doc/controllers/image-by-name.md#get-media-info-image)
* [Get Media Info Images](../../doc/controllers/image-by-name.md#get-media-info-images)
* [Get Rating Image](../../doc/controllers/image-by-name.md#get-rating-image)
* [Get Rating Images](../../doc/controllers/image-by-name.md#get-rating-images)


# Get General Image

Get General Image.

```python
def get_general_image(self,
                     name,
                     mtype)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The name of the image. |
| `mtype` | `string` | Template, Required | Image Type (primary, backdrop, logo, etc). |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
mtype = 'type0'

result = image_by_name_controller.get_general_image(name, mtype)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Image not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get General Images

Get all general images.

```python
def get_general_images(self)
```

## Response Type

[`List of ImageByNameInfo`](../../doc/models/image-by-name-info.md)

## Example Usage

```python
result = image_by_name_controller.get_general_images()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Media Info Image

Get media info image.

```python
def get_media_info_image(self,
                        theme,
                        name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `theme` | `string` | Template, Required | The theme to get the image from. |
| `name` | `string` | Template, Required | The name of the image. |

## Response Type

`mixed`

## Example Usage

```python
theme = 'theme0'
name = 'name0'

result = image_by_name_controller.get_media_info_image(theme, name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Image not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Media Info Images

Get all media info images.

```python
def get_media_info_images(self)
```

## Response Type

[`List of ImageByNameInfo`](../../doc/models/image-by-name-info.md)

## Example Usage

```python
result = image_by_name_controller.get_media_info_images()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Rating Image

Get rating image.

```python
def get_rating_image(self,
                    theme,
                    name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `theme` | `string` | Template, Required | The theme to get the image from. |
| `name` | `string` | Template, Required | The name of the image. |

## Response Type

`mixed`

## Example Usage

```python
theme = 'theme0'
name = 'name0'

result = image_by_name_controller.get_rating_image(theme, name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Image not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Rating Images

Get all general images.

```python
def get_rating_images(self)
```

## Response Type

[`List of ImageByNameInfo`](../../doc/models/image-by-name-info.md)

## Example Usage

```python
result = image_by_name_controller.get_rating_images()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

