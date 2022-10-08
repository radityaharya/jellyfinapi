# Media Info

```python
media_info_controller = client.media_info
```

## Class Name

`MediaInfoController`

## Methods

* [Close Live Stream](../../doc/controllers/media-info.md#close-live-stream)
* [Get Bitrate Test Bytes](../../doc/controllers/media-info.md#get-bitrate-test-bytes)
* [Get Playback Info](../../doc/controllers/media-info.md#get-playback-info)
* [Get Posted Playback Info](../../doc/controllers/media-info.md#get-posted-playback-info)
* [Open Live Stream](../../doc/controllers/media-info.md#open-live-stream)


# Close Live Stream

Closes a media source.

```python
def close_live_stream(self,
                     live_stream_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `live_stream_id` | `string` | Query, Required | The livestream id. |

## Response Type

`void`

## Example Usage

```python
live_stream_id = 'liveStreamId2'

result = media_info_controller.close_live_stream(live_stream_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Bitrate Test Bytes

Tests the network with a request with the size of the bitrate.

```python
def get_bitrate_test_bytes(self,
                          size=102400)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `size` | `int` | Query, Optional | The bitrate. Defaults to 102400.<br>**Default**: `102400`<br>**Constraints**: `>= 1`, `<= 100000000` |

## Response Type

`binary`

## Example Usage

```python
size = 102400

result = media_info_controller.get_bitrate_test_bytes(size)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Playback Info

Gets live playback media info for an item.

```python
def get_playback_info(self,
                     item_id,
                     user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Required | The user id. |

## Response Type

[`PlaybackInfoResponse`](../../doc/models/playback-info-response.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
user_id = '000013ec-0000-0000-0000-000000000000'

result = media_info_controller.get_playback_info(item_id, user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Posted Playback Info

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
Query parameters are obsolete.

```python
def get_posted_playback_info(self,
                            item_id,
                            user_id=None,
                            max_streaming_bitrate=None,
                            start_time_ticks=None,
                            audio_stream_index=None,
                            subtitle_stream_index=None,
                            max_audio_channels=None,
                            media_source_id=None,
                            live_stream_id=None,
                            auto_open_live_stream=None,
                            enable_direct_play=None,
                            enable_direct_stream=None,
                            enable_transcoding=None,
                            allow_video_stream_copy=None,
                            allow_audio_stream_copy=None,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `max_streaming_bitrate` | `int` | Query, Optional | The maximum streaming bitrate. |
| `start_time_ticks` | `long\|int` | Query, Optional | The start time in ticks. |
| `audio_stream_index` | `int` | Query, Optional | The audio stream index. |
| `subtitle_stream_index` | `int` | Query, Optional | The subtitle stream index. |
| `max_audio_channels` | `int` | Query, Optional | The maximum number of audio channels. |
| `media_source_id` | `string` | Query, Optional | The media source id. |
| `live_stream_id` | `string` | Query, Optional | The livestream id. |
| `auto_open_live_stream` | `bool` | Query, Optional | Whether to auto open the livestream. |
| `enable_direct_play` | `bool` | Query, Optional | Whether to enable direct play. Default: true. |
| `enable_direct_stream` | `bool` | Query, Optional | Whether to enable direct stream. Default: true. |
| `enable_transcoding` | `bool` | Query, Optional | Whether to enable transcoding. Default: true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether to allow to copy the video stream. Default: true. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether to allow to copy the audio stream. Default: true. |
| `body` | [`PlaybackInfoDto`](../../doc/models/playback-info-dto.md) | Body, Optional | The playback info. |

## Response Type

[`PlaybackInfoResponse`](../../doc/models/playback-info-response.md)

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = media_info_controller.get_posted_playback_info(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Open Live Stream

Opens a media source.

```python
def open_live_stream(self,
                    open_token=None,
                    user_id=None,
                    play_session_id=None,
                    max_streaming_bitrate=None,
                    start_time_ticks=None,
                    audio_stream_index=None,
                    subtitle_stream_index=None,
                    max_audio_channels=None,
                    item_id=None,
                    enable_direct_play=None,
                    enable_direct_stream=None,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `open_token` | `string` | Query, Optional | The open token. |
| `user_id` | `uuid\|string` | Query, Optional | The user id. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `max_streaming_bitrate` | `int` | Query, Optional | The maximum streaming bitrate. |
| `start_time_ticks` | `long\|int` | Query, Optional | The start time in ticks. |
| `audio_stream_index` | `int` | Query, Optional | The audio stream index. |
| `subtitle_stream_index` | `int` | Query, Optional | The subtitle stream index. |
| `max_audio_channels` | `int` | Query, Optional | The maximum number of audio channels. |
| `item_id` | `uuid\|string` | Query, Optional | The item id. |
| `enable_direct_play` | `bool` | Query, Optional | Whether to enable direct play. Default: true. |
| `enable_direct_stream` | `bool` | Query, Optional | Whether to enable direct stream. Default: true. |
| `body` | [`OpenLiveStreamDto`](../../doc/models/open-live-stream-dto.md) | Body, Optional | The open live stream dto. |

## Response Type

[`LiveStreamResponse`](../../doc/models/live-stream-response.md)

## Example Usage

```python
result = media_info_controller.open_live_stream()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

