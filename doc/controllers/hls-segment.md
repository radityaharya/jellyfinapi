# Hls Segment

```python
hls_segment_controller = client.hls_segment
```

## Class Name

`HlsSegmentController`

## Methods

* [Get Hls Audio Segment Legacy Aac](../../doc/controllers/hls-segment.md#get-hls-audio-segment-legacy-aac)
* [Get Hls Audio Segment Legacy Mp 3](../../doc/controllers/hls-segment.md#get-hls-audio-segment-legacy-mp-3)
* [Get Hls Playlist Legacy](../../doc/controllers/hls-segment.md#get-hls-playlist-legacy)
* [Get Hls Video Segment Legacy](../../doc/controllers/hls-segment.md#get-hls-video-segment-legacy)
* [Stop Encoding Process](../../doc/controllers/hls-segment.md#stop-encoding-process)


# Get Hls Audio Segment Legacy Aac

Gets the specified audio segment for an audio item.

```python
def get_hls_audio_segment_legacy_aac(self,
                                    item_id,
                                    segment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Template, Required | The item id. |
| `segment_id` | `string` | Template, Required | The segment id. |

## Response Type

`mixed`

## Example Usage

```python
item_id = 'itemId8'
segment_id = 'segmentId0'

result = hls_segment_controller.get_hls_audio_segment_legacy_aac(item_id, segment_id)
```


# Get Hls Audio Segment Legacy Mp 3

Gets the specified audio segment for an audio item.

```python
def get_hls_audio_segment_legacy_mp_3(self,
                                     item_id,
                                     segment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Template, Required | The item id. |
| `segment_id` | `string` | Template, Required | The segment id. |

## Response Type

`mixed`

## Example Usage

```python
item_id = 'itemId8'
segment_id = 'segmentId0'

result = hls_segment_controller.get_hls_audio_segment_legacy_mp_3(item_id, segment_id)
```


# Get Hls Playlist Legacy

Gets a hls video playlist.

```python
def get_hls_playlist_legacy(self,
                           item_id,
                           playlist_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Template, Required | The video id. |
| `playlist_id` | `string` | Template, Required | The playlist id. |

## Response Type

`mixed`

## Example Usage

```python
item_id = 'itemId8'
playlist_id = 'playlistId8'

result = hls_segment_controller.get_hls_playlist_legacy(item_id, playlist_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Hls Video Segment Legacy

Gets a hls video segment.

```python
def get_hls_video_segment_legacy(self,
                                item_id,
                                playlist_id,
                                segment_id,
                                segment_container)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `string` | Template, Required | The item id. |
| `playlist_id` | `string` | Template, Required | The playlist id. |
| `segment_id` | `string` | Template, Required | The segment id. |
| `segment_container` | `string` | Template, Required | The segment container. |

## Response Type

`mixed`

## Example Usage

```python
item_id = 'itemId8'
playlist_id = 'playlistId8'
segment_id = 'segmentId0'
segment_container = 'segmentContainer6'

result = hls_segment_controller.get_hls_video_segment_legacy(item_id, playlist_id, segment_id, segment_container)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Hls segment not found. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Stop Encoding Process

Stops an active encoding.

```python
def stop_encoding_process(self,
                         device_id,
                         play_session_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Query, Required | The device id of the client requesting. Used to stop encoding processes when needed. |
| `play_session_id` | `string` | Query, Required | The play session id. |

## Response Type

`void`

## Example Usage

```python
device_id = 'deviceId0'
play_session_id = 'playSessionId2'

result = hls_segment_controller.stop_encoding_process(device_id, play_session_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

