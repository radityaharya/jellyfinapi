# Playlists

```python
playlists_controller = client.playlists
```

## Class Name

`PlaylistsController`

## Methods

* [Add to Playlist](../../doc/controllers/playlists.md#add-to-playlist)
* [Create Playlist](../../doc/controllers/playlists.md#create-playlist)
* [Get Playlist Items](../../doc/controllers/playlists.md#get-playlist-items)
* [Move Item](../../doc/controllers/playlists.md#move-item)
* [Remove From Playlist](../../doc/controllers/playlists.md#remove-from-playlist)


# Add to Playlist

Adds items to a playlist.

```python
def add_to_playlist(self,
                   playlist_id,
                   ids=None,
                   user_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `uuid\|string` | Template, Required | The playlist id. |
| `ids` | `List of uuid\|string` | Query, Optional | Item id, comma delimited. |
| `user_id` | `uuid\|string` | Query, Optional | The userId. |

## Response Type

`void`

## Example Usage

```python
playlist_id = '00001160-0000-0000-0000-000000000000'

result = playlists_controller.add_to_playlist(playlist_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Create Playlist

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
Query parameters are obsolete.

```python
def create_playlist(self,
                   name=None,
                   ids=None,
                   user_id=None,
                   media_type=None,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | The playlist name. |
| `ids` | `List of uuid\|string` | Query, Optional | The item ids. |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `media_type` | `string` | Query, Optional | The media type. |
| `body` | [`CreatePlaylistDto`](../../doc/models/create-playlist-dto.md) | Body, Optional | The create playlist payload. |

## Response Type

[`PlaylistCreationResult`](../../doc/models/playlist-creation-result.md)

## Example Usage

```python
result = playlists_controller.create_playlist()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Playlist Items

Gets the original items of a playlist.

```python
def get_playlist_items(self,
                      playlist_id,
                      user_id,
                      start_index=None,
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
| `playlist_id` | `uuid\|string` | Template, Required | The playlist id. |
| `user_id` | `uuid\|string` | Query, Required | User id. |
| `start_index` | `int` | Query, Optional | Optional. The record index to start at. All items with a lower index will be dropped from the results. |
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
playlist_id = '00001160-0000-0000-0000-000000000000'
user_id = '000013ec-0000-0000-0000-000000000000'

result = playlists_controller.get_playlist_items(playlist_id, user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Playlist not found. | `APIException` |


# Move Item

Moves a playlist item.

```python
def move_item(self,
             playlist_id,
             item_id,
             new_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `string` | Template, Required | The playlist id. |
| `item_id` | `string` | Template, Required | The item id. |
| `new_index` | `int` | Template, Required | The new index. |

## Response Type

`void`

## Example Usage

```python
playlist_id = 'playlistId8'
item_id = 'itemId8'
new_index = 60

result = playlists_controller.move_item(playlist_id, item_id, new_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Remove From Playlist

Removes items from a playlist.

```python
def remove_from_playlist(self,
                        playlist_id,
                        entry_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `string` | Template, Required | The playlist id. |
| `entry_ids` | `List of string` | Query, Optional | The item ids, comma delimited. |

## Response Type

`void`

## Example Usage

```python
playlist_id = 'playlistId8'

result = playlists_controller.remove_from_playlist(playlist_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

