# Image

```python
image_controller = client.image
```

## Class Name

`ImageController`

## Methods

* [Delete Custom Splashscreen](../../doc/controllers/image.md#delete-custom-splashscreen)
* [Delete Item Image](../../doc/controllers/image.md#delete-item-image)
* [Delete Item Image by Index](../../doc/controllers/image.md#delete-item-image-by-index)
* [Delete User Image](../../doc/controllers/image.md#delete-user-image)
* [Delete User Image by Index](../../doc/controllers/image.md#delete-user-image-by-index)
* [Get Artist Image](../../doc/controllers/image.md#get-artist-image)
* [Get Genre Image](../../doc/controllers/image.md#get-genre-image)
* [Get Genre Image by Index](../../doc/controllers/image.md#get-genre-image-by-index)
* [Get Item Image](../../doc/controllers/image.md#get-item-image)
* [Get Item Image 2](../../doc/controllers/image.md#get-item-image-2)
* [Get Item Image by Index](../../doc/controllers/image.md#get-item-image-by-index)
* [Get Item Image Infos](../../doc/controllers/image.md#get-item-image-infos)
* [Get Music Genre Image](../../doc/controllers/image.md#get-music-genre-image)
* [Get Music Genre Image by Index](../../doc/controllers/image.md#get-music-genre-image-by-index)
* [Get Person Image](../../doc/controllers/image.md#get-person-image)
* [Get Person Image by Index](../../doc/controllers/image.md#get-person-image-by-index)
* [Get Splashscreen](../../doc/controllers/image.md#get-splashscreen)
* [Get Studio Image](../../doc/controllers/image.md#get-studio-image)
* [Get Studio Image by Index](../../doc/controllers/image.md#get-studio-image-by-index)
* [Get User Image](../../doc/controllers/image.md#get-user-image)
* [Get User Image by Index](../../doc/controllers/image.md#get-user-image-by-index)
* [Post User Image](../../doc/controllers/image.md#post-user-image)
* [Post User Image by Index](../../doc/controllers/image.md#post-user-image-by-index)
* [Set Item Image](../../doc/controllers/image.md#set-item-image)
* [Set Item Image by Index](../../doc/controllers/image.md#set-item-image-by-index)
* [Update Item Image Index](../../doc/controllers/image.md#update-item-image-index)
* [Upload Custom Splashscreen](../../doc/controllers/image.md#upload-custom-splashscreen)


# Delete Custom Splashscreen

Delete a custom splashscreen.

```python
def delete_custom_splashscreen(self)
```

## Response Type

`void`

## Example Usage

```python
result = image_controller.delete_custom_splashscreen()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to delete splashscreen.. | `APIException` |


# Delete Item Image

Delete an item's image.

```python
def delete_item_image(self,
                     item_id,
                     image_type,
                     image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Query, Optional | The image index. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.delete_item_image(item_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Delete Item Image by Index

Delete an item's image.

```python
def delete_item_image_by_index(self,
                              item_id,
                              image_type,
                              image_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | The image index. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.delete_item_image_by_index(item_id, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Delete User Image

Delete the user's image.

```python
def delete_user_image(self,
                     user_id,
                     image_type,
                     index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User Id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | (Unused) Image type. |
| `index` | `int` | Query, Optional | (Unused) Image index. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.delete_user_image(user_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to delete the image. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Delete User Image by Index

Delete the user's image.

```python
def delete_user_image_by_index(self,
                              user_id,
                              image_type,
                              index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User Id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | (Unused) Image type. |
| `index` | `int` | Template, Required | (Unused) Image index. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
index = 44

result = image_controller.delete_user_image_by_index(user_id, image_type, index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to delete the image. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Artist Image

Get artist image by name.

```python
def get_artist_image(self,
                    name,
                    image_type,
                    image_index,
                    tag=None,
                    format=None,
                    max_width=None,
                    max_height=None,
                    percent_played=None,
                    unplayed_count=None,
                    width=None,
                    height=None,
                    quality=None,
                    fill_width=None,
                    fill_height=None,
                    crop_whitespace=None,
                    add_played_indicator=None,
                    blur=None,
                    background_color=None,
                    foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Artist name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_artist_image(name, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Genre Image

Get genre image by name.

```python
def get_genre_image(self,
                   name,
                   image_type,
                   tag=None,
                   format=None,
                   max_width=None,
                   max_height=None,
                   percent_played=None,
                   unplayed_count=None,
                   width=None,
                   height=None,
                   quality=None,
                   fill_width=None,
                   fill_height=None,
                   crop_whitespace=None,
                   add_played_indicator=None,
                   blur=None,
                   background_color=None,
                   foreground_layer=None,
                   image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Genre name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX

result = image_controller.get_genre_image(name, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Genre Image by Index

Get genre image by name.

```python
def get_genre_image_by_index(self,
                            name,
                            image_type,
                            image_index,
                            tag=None,
                            format=None,
                            max_width=None,
                            max_height=None,
                            percent_played=None,
                            unplayed_count=None,
                            width=None,
                            height=None,
                            quality=None,
                            fill_width=None,
                            fill_height=None,
                            crop_whitespace=None,
                            add_played_indicator=None,
                            blur=None,
                            background_color=None,
                            foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Genre name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_genre_image_by_index(name, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Item Image

Gets the item's image.

```python
def get_item_image(self,
                  item_id,
                  image_type,
                  max_width=None,
                  max_height=None,
                  width=None,
                  height=None,
                  quality=None,
                  fill_width=None,
                  fill_height=None,
                  tag=None,
                  crop_whitespace=None,
                  format=None,
                  add_played_indicator=None,
                  percent_played=None,
                  unplayed_count=None,
                  blur=None,
                  background_color=None,
                  foreground_layer=None,
                  image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.get_item_image(item_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Item Image 2

Gets the item's image.

```python
def get_item_image_2(self,
                    item_id,
                    image_type,
                    max_width,
                    max_height,
                    tag,
                    format,
                    percent_played,
                    unplayed_count,
                    image_index,
                    width=None,
                    height=None,
                    quality=None,
                    fill_width=None,
                    fill_height=None,
                    crop_whitespace=None,
                    add_played_indicator=None,
                    blur=None,
                    background_color=None,
                    foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `max_width` | `int` | Template, Required | The maximum image width to return. |
| `max_height` | `int` | Template, Required | The maximum image height to return. |
| `tag` | `string` | Template, Required | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Template, Required | Determines the output format of the image - original,gif,jpg,png. |
| `percent_played` | `float` | Template, Required | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Template, Required | Optional. Unplayed count overlay to render. |
| `image_index` | `int` | Template, Required | Image index. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
max_width = 200
max_height = 48
tag = 'tag6'
format = ImageFormatEnum.WEBP
percent_played = 252.64
unplayed_count = 8
image_index = 102

result = image_controller.get_item_image_2(item_id, image_type, max_width, max_height, tag, format, percent_played, unplayed_count, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Item Image by Index

Gets the item's image.

```python
def get_item_image_by_index(self,
                           item_id,
                           image_type,
                           image_index,
                           max_width=None,
                           max_height=None,
                           width=None,
                           height=None,
                           quality=None,
                           fill_width=None,
                           fill_height=None,
                           tag=None,
                           crop_whitespace=None,
                           format=None,
                           add_played_indicator=None,
                           percent_played=None,
                           unplayed_count=None,
                           blur=None,
                           background_color=None,
                           foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_item_image_by_index(item_id, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Item Image Infos

Get item image infos.

```python
def get_item_image_infos(self,
                        item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`List of ImageInfo`](../../doc/models/image-info.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = image_controller.get_item_image_infos(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Music Genre Image

Get music genre image by name.

```python
def get_music_genre_image(self,
                         name,
                         image_type,
                         tag=None,
                         format=None,
                         max_width=None,
                         max_height=None,
                         percent_played=None,
                         unplayed_count=None,
                         width=None,
                         height=None,
                         quality=None,
                         fill_width=None,
                         fill_height=None,
                         crop_whitespace=None,
                         add_played_indicator=None,
                         blur=None,
                         background_color=None,
                         foreground_layer=None,
                         image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Music genre name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX

result = image_controller.get_music_genre_image(name, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Music Genre Image by Index

Get music genre image by name.

```python
def get_music_genre_image_by_index(self,
                                  name,
                                  image_type,
                                  image_index,
                                  tag=None,
                                  format=None,
                                  max_width=None,
                                  max_height=None,
                                  percent_played=None,
                                  unplayed_count=None,
                                  width=None,
                                  height=None,
                                  quality=None,
                                  fill_width=None,
                                  fill_height=None,
                                  crop_whitespace=None,
                                  add_played_indicator=None,
                                  blur=None,
                                  background_color=None,
                                  foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Music genre name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_music_genre_image_by_index(name, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Person Image

Get person image by name.

```python
def get_person_image(self,
                    name,
                    image_type,
                    tag=None,
                    format=None,
                    max_width=None,
                    max_height=None,
                    percent_played=None,
                    unplayed_count=None,
                    width=None,
                    height=None,
                    quality=None,
                    fill_width=None,
                    fill_height=None,
                    crop_whitespace=None,
                    add_played_indicator=None,
                    blur=None,
                    background_color=None,
                    foreground_layer=None,
                    image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Person name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX

result = image_controller.get_person_image(name, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Person Image by Index

Get person image by name.

```python
def get_person_image_by_index(self,
                             name,
                             image_type,
                             image_index,
                             tag=None,
                             format=None,
                             max_width=None,
                             max_height=None,
                             percent_played=None,
                             unplayed_count=None,
                             width=None,
                             height=None,
                             quality=None,
                             fill_width=None,
                             fill_height=None,
                             crop_whitespace=None,
                             add_played_indicator=None,
                             blur=None,
                             background_color=None,
                             foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Person name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_person_image_by_index(name, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Splashscreen

Generates or gets the splashscreen.

```python
def get_splashscreen(self,
                    tag=None,
                    format=None,
                    max_width=None,
                    max_height=None,
                    width=None,
                    height=None,
                    fill_width=None,
                    fill_height=None,
                    blur=None,
                    background_color=None,
                    foreground_layer=None,
                    quality=90)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag` | `string` | Query, Optional | Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `blur` | `int` | Query, Optional | Blur image. |
| `background_color` | `string` | Query, Optional | Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Apply a foreground layer on top of the image. |
| `quality` | `int` | Query, Optional | Quality setting, from 0-100.<br>**Default**: `90`<br>**Constraints**: `>= 0`, `<= 100` |

## Response Type

`mixed`

## Example Usage

```python
quality = 90

result = image_controller.get_splashscreen(None, None, None, None, None, None, None, None, None, None, None, quality)
```


# Get Studio Image

Get studio image by name.

```python
def get_studio_image(self,
                    name,
                    image_type,
                    tag=None,
                    format=None,
                    max_width=None,
                    max_height=None,
                    percent_played=None,
                    unplayed_count=None,
                    width=None,
                    height=None,
                    quality=None,
                    fill_width=None,
                    fill_height=None,
                    crop_whitespace=None,
                    add_played_indicator=None,
                    blur=None,
                    background_color=None,
                    foreground_layer=None,
                    image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Studio name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX

result = image_controller.get_studio_image(name, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Studio Image by Index

Get studio image by name.

```python
def get_studio_image_by_index(self,
                             name,
                             image_type,
                             image_index,
                             tag=None,
                             format=None,
                             max_width=None,
                             max_height=None,
                             percent_played=None,
                             unplayed_count=None,
                             width=None,
                             height=None,
                             quality=None,
                             fill_width=None,
                             fill_height=None,
                             crop_whitespace=None,
                             add_played_indicator=None,
                             blur=None,
                             background_color=None,
                             foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | Studio name. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_studio_image_by_index(name, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get User Image

Get user profile image.

```python
def get_user_image(self,
                  user_id,
                  image_type,
                  tag=None,
                  format=None,
                  max_width=None,
                  max_height=None,
                  percent_played=None,
                  unplayed_count=None,
                  width=None,
                  height=None,
                  quality=None,
                  fill_width=None,
                  fill_height=None,
                  crop_whitespace=None,
                  add_played_indicator=None,
                  blur=None,
                  background_color=None,
                  foreground_layer=None,
                  image_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |
| `image_index` | `int` | Query, Optional | Image index. |

## Response Type

`mixed`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.get_user_image(user_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get User Image by Index

Get user profile image.

```python
def get_user_image_by_index(self,
                           user_id,
                           image_type,
                           image_index,
                           tag=None,
                           format=None,
                           max_width=None,
                           max_height=None,
                           percent_played=None,
                           unplayed_count=None,
                           width=None,
                           height=None,
                           quality=None,
                           fill_width=None,
                           fill_height=None,
                           crop_whitespace=None,
                           add_played_indicator=None,
                           blur=None,
                           background_color=None,
                           foreground_layer=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Image index. |
| `tag` | `string` | Query, Optional | Optional. Supply the cache tag from the item object to receive strong caching headers. |
| `format` | [`ImageFormatEnum`](../../doc/models/image-format-enum.md) | Query, Optional | Determines the output format of the image - original,gif,jpg,png. |
| `max_width` | `int` | Query, Optional | The maximum image width to return. |
| `max_height` | `int` | Query, Optional | The maximum image height to return. |
| `percent_played` | `float` | Query, Optional | Optional. Percent to render for the percent played overlay. |
| `unplayed_count` | `int` | Query, Optional | Optional. Unplayed count overlay to render. |
| `width` | `int` | Query, Optional | The fixed image width to return. |
| `height` | `int` | Query, Optional | The fixed image height to return. |
| `quality` | `int` | Query, Optional | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. |
| `fill_width` | `int` | Query, Optional | Width of box to fill. |
| `fill_height` | `int` | Query, Optional | Height of box to fill. |
| `crop_whitespace` | `bool` | Query, Optional | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. |
| `add_played_indicator` | `bool` | Query, Optional | Optional. Add a played indicator. |
| `blur` | `int` | Query, Optional | Optional. Blur image. |
| `background_color` | `string` | Query, Optional | Optional. Apply a background color for transparent images. |
| `foreground_layer` | `string` | Query, Optional | Optional. Apply a foreground layer on top of the image. |

## Response Type

`mixed`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.get_user_image_by_index(user_id, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Post User Image

Sets the user image.

```python
def post_user_image(self,
                   user_id,
                   image_type,
                   index=None,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User Id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | (Unused) Image type. |
| `index` | `int` | Query, Optional | (Unused) Image index. |
| `body` | `object` | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.post_user_image(user_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to delete the image. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Post User Image by Index

Sets the user image.

```python
def post_user_image_by_index(self,
                            user_id,
                            image_type,
                            index,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User Id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | (Unused) Image type. |
| `index` | `int` | Template, Required | (Unused) Image index. |
| `body` | `object` | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
index = 44

result = image_controller.post_user_image_by_index(user_id, image_type, index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to delete the image. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Set Item Image

Set item image.

```python
def set_item_image(self,
                  item_id,
                  image_type,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `body` | `object` | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX

result = image_controller.set_item_image(item_id, image_type)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Set Item Image by Index

Set item image.

```python
def set_item_image_by_index(self,
                           item_id,
                           image_type,
                           image_index,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | (Unused) Image index. |
| `body` | `object` | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
image_index = 102

result = image_controller.set_item_image_by_index(item_id, image_type, image_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Update Item Image Index

Updates the index for an item image.

```python
def update_item_image_index(self,
                           item_id,
                           image_type,
                           image_index,
                           new_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `image_type` | [`ImageTypeEnum`](../../doc/models/image-type-enum.md) | Template, Required | Image type. |
| `image_index` | `int` | Template, Required | Old image index. |
| `new_index` | `int` | Query, Required | New image index. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
image_type = ImageTypeEnum.BOX
image_index = 102
new_index = 60

result = image_controller.update_item_image_index(item_id, image_type, image_index, new_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Upload Custom Splashscreen

Uploads a custom splashscreen.
The body is expected to the image contents base64 encoded.

```python
def upload_custom_splashscreen(self,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
result = image_controller.upload_custom_splashscreen()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error reading MimeType from uploaded image. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | Unauthorized | `APIException` |
| 403 | User does not have permission to upload splashscreen.. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

