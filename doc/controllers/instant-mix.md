# Instant Mix

```python
instant_mix_controller = client.instant_mix
```

## Class Name

`InstantMixController`

## Methods

* [Get Instant Mix From Album](../../doc/controllers/instant-mix.md#get-instant-mix-from-album)
* [Get Instant Mix From Artists](../../doc/controllers/instant-mix.md#get-instant-mix-from-artists)
* [Get Instant Mix From Artists 2](../../doc/controllers/instant-mix.md#get-instant-mix-from-artists-2)
* [Get Instant Mix From Item](../../doc/controllers/instant-mix.md#get-instant-mix-from-item)
* [Get Instant Mix From Music Genre by Id](../../doc/controllers/instant-mix.md#get-instant-mix-from-music-genre-by-id)
* [Get Instant Mix From Music Genre by Name](../../doc/controllers/instant-mix.md#get-instant-mix-from-music-genre-by-name)
* [Get Instant Mix From Playlist](../../doc/controllers/instant-mix.md#get-instant-mix-from-playlist)
* [Get Instant Mix From Song](../../doc/controllers/instant-mix.md#get-instant-mix-from-song)


# Get Instant Mix From Album

Creates an instant playlist based on a given album.

```python
def get_instant_mix_from_album(self,
                              id,
                              user_id=None,
                              limit=None,
                              fields=None,
                              enable_images=None,
                              enable_user_data=None,
                              image_type_limit=None,
                              enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_album(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Artists

Creates an instant playlist based on a given artist.

```python
def get_instant_mix_from_artists(self,
                                id,
                                user_id=None,
                                limit=None,
                                fields=None,
                                enable_images=None,
                                enable_user_data=None,
                                image_type_limit=None,
                                enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_artists(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Artists 2

**This endpoint is deprecated.**

Creates an instant playlist based on a given artist.

```python
def get_instant_mix_from_artists_2(self,
                                  id,
                                  user_id=None,
                                  limit=None,
                                  fields=None,
                                  enable_images=None,
                                  enable_user_data=None,
                                  image_type_limit=None,
                                  enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Query, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_artists_2(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Item

Creates an instant playlist based on a given item.

```python
def get_instant_mix_from_item(self,
                             id,
                             user_id=None,
                             limit=None,
                             fields=None,
                             enable_images=None,
                             enable_user_data=None,
                             image_type_limit=None,
                             enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_item(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Music Genre by Id

Creates an instant playlist based on a given genre.

```python
def get_instant_mix_from_music_genre_by_id(self,
                                          id,
                                          user_id=None,
                                          limit=None,
                                          fields=None,
                                          enable_images=None,
                                          enable_user_data=None,
                                          image_type_limit=None,
                                          enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Query, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_music_genre_by_id(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Music Genre by Name

Creates an instant playlist based on a given genre.

```python
def get_instant_mix_from_music_genre_by_name(self,
                                            name,
                                            user_id=None,
                                            limit=None,
                                            fields=None,
                                            enable_images=None,
                                            enable_user_data=None,
                                            image_type_limit=None,
                                            enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The genre name. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
name = 'name0'

result = instant_mix_controller.get_instant_mix_from_music_genre_by_name(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Playlist

Creates an instant playlist based on a given playlist.

```python
def get_instant_mix_from_playlist(self,
                                 id,
                                 user_id=None,
                                 limit=None,
                                 fields=None,
                                 enable_images=None,
                                 enable_user_data=None,
                                 image_type_limit=None,
                                 enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_playlist(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Instant Mix From Song

Creates an instant playlist based on a given song.

```python
def get_instant_mix_from_song(self,
                             id,
                             user_id=None,
                             limit=None,
                             fields=None,
                             enable_images=None,
                             enable_user_data=None,
                             image_type_limit=None,
                             enable_image_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. Filter by user id, and attach user data. |
| `limit` | `int` | Query, Optional | Optional. The maximum number of records to return. |
| `fields` | [`List of ItemFieldsEnum`](../../doc/models/item-fields-enum.md) | Query, Optional | Optional. Specify additional fields of information to return in the output. |
| `enable_images` | `bool` | Query, Optional | Optional. Include image information in output. |
| `enable_user_data` | `bool` | Query, Optional | Optional. Include user data. |
| `image_type_limit` | `int` | Query, Optional | Optional. The max number of images to return, per image type. |
| `enable_image_types` | [`List of ImageTypeEnum`](../../doc/models/image-type-enum.md) | Query, Optional | Optional. The image types to include in the output. |

## Response Type

[`BaseItemDtoQueryResult`](../../doc/models/base-item-dto-query-result.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = instant_mix_controller.get_instant_mix_from_song(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

