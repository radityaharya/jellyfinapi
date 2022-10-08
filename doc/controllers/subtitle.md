# Subtitle

```python
subtitle_controller = client.subtitle
```

## Class Name

`SubtitleController`

## Methods

* [Delete Subtitle](../../doc/controllers/subtitle.md#delete-subtitle)
* [Download Remote Subtitles](../../doc/controllers/subtitle.md#download-remote-subtitles)
* [Get Fallback Font](../../doc/controllers/subtitle.md#get-fallback-font)
* [Get Fallback Font List](../../doc/controllers/subtitle.md#get-fallback-font-list)
* [Get Remote Subtitles](../../doc/controllers/subtitle.md#get-remote-subtitles)
* [Get Subtitle](../../doc/controllers/subtitle.md#get-subtitle)
* [Get Subtitle Playlist](../../doc/controllers/subtitle.md#get-subtitle-playlist)
* [Get Subtitle With Ticks](../../doc/controllers/subtitle.md#get-subtitle-with-ticks)
* [Search Remote Subtitles](../../doc/controllers/subtitle.md#search-remote-subtitles)
* [Upload Subtitle](../../doc/controllers/subtitle.md#upload-subtitle)


# Delete Subtitle

Deletes an external subtitle file.

```python
def delete_subtitle(self,
                   item_id,
                   index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `index` | `int` | Template, Required | The index of the subtitle file. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
index = 44

result = subtitle_controller.delete_subtitle(item_id, index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Item not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Download Remote Subtitles

Downloads a remote subtitle.

```python
def download_remote_subtitles(self,
                             item_id,
                             subtitle_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `subtitle_id` | `string` | Template, Required | The subtitle id. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
subtitle_id = 'subtitleId4'

result = subtitle_controller.download_remote_subtitles(item_id, subtitle_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Fallback Font

Gets a fallback font file.

```python
def get_fallback_font(self,
                     name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The name of the fallback font file to get. |

## Response Type

`mixed`

## Example Usage

```python
name = 'name0'

result = subtitle_controller.get_fallback_font(name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Fallback Font List

Gets a list of available fallback font files.

```python
def get_fallback_font_list(self)
```

## Response Type

[`List of FontFile`](../../doc/models/font-file.md)

## Example Usage

```python
result = subtitle_controller.get_fallback_font_list()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Remote Subtitles

Gets the remote subtitles.

```python
def get_remote_subtitles(self,
                        id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The item id. |

## Response Type

`binary`

## Example Usage

```python
id = 'id0'

result = subtitle_controller.get_remote_subtitles(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Subtitle

Gets subtitles in a specified format.

```python
def get_subtitle(self,
                route_item_id,
                route_media_source_id,
                route_index,
                route_format,
                item_id=None,
                media_source_id=None,
                index=None,
                format=None,
                end_position_ticks=None,
                copy_timestamps=False,
                add_vtt_time_map=False,
                start_position_ticks=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `route_item_id` | `uuid\|string` | Template, Required | The (route) item id. |
| `route_media_source_id` | `string` | Template, Required | The (route) media source id. |
| `route_index` | `int` | Template, Required | The (route) subtitle stream index. |
| `route_format` | `string` | Template, Required | The (route) format of the returned subtitle. |
| `item_id` | `uuid\|string` | Query, Optional | The item id. |
| `media_source_id` | `string` | Query, Optional | The media source id. |
| `index` | `int` | Query, Optional | The subtitle stream index. |
| `format` | `string` | Query, Optional | The format of the returned subtitle. |
| `end_position_ticks` | `long\|int` | Query, Optional | Optional. The end position of the subtitle in ticks. |
| `copy_timestamps` | `bool` | Query, Optional | Optional. Whether to copy the timestamps.<br>**Default**: `False` |
| `add_vtt_time_map` | `bool` | Query, Optional | Optional. Whether to add a VTT time map.<br>**Default**: `False` |
| `start_position_ticks` | `long\|int` | Query, Optional | The start position of the subtitle in ticks.<br>**Default**: `0` |

## Response Type

`binary`

## Example Usage

```python
route_item_id = '000014a8-0000-0000-0000-000000000000'
route_media_source_id = 'routeMediaSourceId6'
route_index = 32
route_format = 'routeFormat0'
copy_timestamps = False
add_vtt_time_map = False
start_position_ticks = 0

result = subtitle_controller.get_subtitle(route_item_id, route_media_source_id, route_index, route_format, None, None, None, None, None, copy_timestamps, add_vtt_time_map, start_position_ticks)
```


# Get Subtitle Playlist

Gets an HLS subtitle playlist.

```python
def get_subtitle_playlist(self,
                         item_id,
                         index,
                         media_source_id,
                         segment_length)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `index` | `int` | Template, Required | The subtitle stream index. |
| `media_source_id` | `string` | Template, Required | The media source id. |
| `segment_length` | `int` | Query, Required | The subtitle segment length. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
index = 44
media_source_id = 'mediaSourceId4'
segment_length = 204

result = subtitle_controller.get_subtitle_playlist(item_id, index, media_source_id, segment_length)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Subtitle With Ticks

Gets subtitles in a specified format.

```python
def get_subtitle_with_ticks(self,
                           route_item_id,
                           route_media_source_id,
                           route_index,
                           route_start_position_ticks,
                           route_format,
                           item_id=None,
                           media_source_id=None,
                           index=None,
                           start_position_ticks=None,
                           format=None,
                           end_position_ticks=None,
                           copy_timestamps=False,
                           add_vtt_time_map=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `route_item_id` | `uuid\|string` | Template, Required | The (route) item id. |
| `route_media_source_id` | `string` | Template, Required | The (route) media source id. |
| `route_index` | `int` | Template, Required | The (route) subtitle stream index. |
| `route_start_position_ticks` | `long\|int` | Template, Required | The (route) start position of the subtitle in ticks. |
| `route_format` | `string` | Template, Required | The (route) format of the returned subtitle. |
| `item_id` | `uuid\|string` | Query, Optional | The item id. |
| `media_source_id` | `string` | Query, Optional | The media source id. |
| `index` | `int` | Query, Optional | The subtitle stream index. |
| `start_position_ticks` | `long\|int` | Query, Optional | The start position of the subtitle in ticks. |
| `format` | `string` | Query, Optional | The format of the returned subtitle. |
| `end_position_ticks` | `long\|int` | Query, Optional | Optional. The end position of the subtitle in ticks. |
| `copy_timestamps` | `bool` | Query, Optional | Optional. Whether to copy the timestamps.<br>**Default**: `False` |
| `add_vtt_time_map` | `bool` | Query, Optional | Optional. Whether to add a VTT time map.<br>**Default**: `False` |

## Response Type

`binary`

## Example Usage

```python
route_item_id = '000014a8-0000-0000-0000-000000000000'
route_media_source_id = 'routeMediaSourceId6'
route_index = 32
route_start_position_ticks = 84
route_format = 'routeFormat0'
copy_timestamps = False
add_vtt_time_map = False

result = subtitle_controller.get_subtitle_with_ticks(route_item_id, route_media_source_id, route_index, route_start_position_ticks, route_format, None, None, None, None, None, None, copy_timestamps, add_vtt_time_map)
```


# Search Remote Subtitles

Search remote subtitles.

```python
def search_remote_subtitles(self,
                           item_id,
                           language,
                           is_perfect_match=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `language` | `string` | Template, Required | The language of the subtitles. |
| `is_perfect_match` | `bool` | Query, Optional | Optional. Only show subtitles which are a perfect match. |

## Response Type

[`List of RemoteSubtitleInfo`](../../doc/models/remote-subtitle-info.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
language = 'language2'

result = subtitle_controller.search_remote_subtitles(item_id, language)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Upload Subtitle

Upload an external subtitle file.

```python
def upload_subtitle(self,
                   item_id,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item the subtitle belongs to. |
| `body` | [`UploadSubtitleDto`](../../doc/models/upload-subtitle-dto.md) | Body, Required | The request body. |

## Response Type

`void`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
body = UploadSubtitleDto()
body.language = 'Language4'
body.format = 'Format6'
body.is_forced = False
body.data = 'Data0'

result = subtitle_controller.upload_subtitle(item_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

