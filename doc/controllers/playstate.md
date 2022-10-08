# Playstate

```python
playstate_controller = client.playstate
```

## Class Name

`PlaystateController`

## Methods

* [Mark Played Item](../../doc/controllers/playstate.md#mark-played-item)
* [Mark Unplayed Item](../../doc/controllers/playstate.md#mark-unplayed-item)
* [On Playback Progress](../../doc/controllers/playstate.md#on-playback-progress)
* [On Playback Start](../../doc/controllers/playstate.md#on-playback-start)
* [On Playback Stopped](../../doc/controllers/playstate.md#on-playback-stopped)
* [Ping Playback Session](../../doc/controllers/playstate.md#ping-playback-session)
* [Report Playback Progress](../../doc/controllers/playstate.md#report-playback-progress)
* [Report Playback Start](../../doc/controllers/playstate.md#report-playback-start)
* [Report Playback Stopped](../../doc/controllers/playstate.md#report-playback-stopped)


# Mark Played Item

Marks an item as played for user.

```python
def mark_played_item(self,
                    user_id,
                    item_id,
                    date_played=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `date_played` | `datetime` | Query, Optional | Optional. The date the item was played. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = playstate_controller.mark_played_item(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Mark Unplayed Item

Marks an item as unplayed for user.

```python
def mark_unplayed_item(self,
                      user_id,
                      item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |

## Response Type

[`UserItemDataDto`](../../doc/models/user-item-data-dto.md)

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = playstate_controller.mark_unplayed_item(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# On Playback Progress

Reports a user's playback progress.

```python
def on_playback_progress(self,
                        user_id,
                        item_id,
                        media_source_id=None,
                        position_ticks=None,
                        audio_stream_index=None,
                        subtitle_stream_index=None,
                        volume_level=None,
                        play_method=None,
                        live_stream_id=None,
                        play_session_id=None,
                        repeat_mode=None,
                        is_paused=False,
                        is_muted=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `media_source_id` | `string` | Query, Optional | The id of the MediaSource. |
| `position_ticks` | `long\|int` | Query, Optional | Optional. The current position, in ticks. 1 tick = 10000 ms. |
| `audio_stream_index` | `int` | Query, Optional | The audio stream index. |
| `subtitle_stream_index` | `int` | Query, Optional | The subtitle stream index. |
| `volume_level` | `int` | Query, Optional | Scale of 0-100. |
| `play_method` | [`PlayMethodEnum`](../../doc/models/play-method-enum.md) | Query, Optional | The play method. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `repeat_mode` | [`RepeatModeEnum`](../../doc/models/repeat-mode-enum.md) | Query, Optional | The repeat mode. |
| `is_paused` | `bool` | Query, Optional | Indicates if the player is paused.<br>**Default**: `False` |
| `is_muted` | `bool` | Query, Optional | Indicates if the player is muted.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'
is_paused = False
is_muted = False

result = playstate_controller.on_playback_progress(user_id, item_id, None, None, None, None, None, None, None, None, None, is_paused, is_muted)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# On Playback Start

Reports that a user has begun playing an item.

```python
def on_playback_start(self,
                     user_id,
                     item_id,
                     media_source_id=None,
                     audio_stream_index=None,
                     subtitle_stream_index=None,
                     play_method=None,
                     live_stream_id=None,
                     play_session_id=None,
                     can_seek=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `media_source_id` | `string` | Query, Optional | The id of the MediaSource. |
| `audio_stream_index` | `int` | Query, Optional | The audio stream index. |
| `subtitle_stream_index` | `int` | Query, Optional | The subtitle stream index. |
| `play_method` | [`PlayMethodEnum`](../../doc/models/play-method-enum.md) | Query, Optional | The play method. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `can_seek` | `bool` | Query, Optional | Indicates if the client can seek.<br>**Default**: `False` |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'
can_seek = False

result = playstate_controller.on_playback_start(user_id, item_id, None, None, None, None, None, None, can_seek)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# On Playback Stopped

Reports that a user has stopped playing an item.

```python
def on_playback_stopped(self,
                       user_id,
                       item_id,
                       media_source_id=None,
                       next_media_type=None,
                       position_ticks=None,
                       live_stream_id=None,
                       play_session_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Template, Required | User id. |
| `item_id` | `uuid\|string` | Template, Required | Item id. |
| `media_source_id` | `string` | Query, Optional | The id of the MediaSource. |
| `next_media_type` | `string` | Query, Optional | The next media type that will play. |
| `position_ticks` | `long\|int` | Query, Optional | Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `play_session_id` | `string` | Query, Optional | The play session id. |

## Response Type

`void`

## Example Usage

```python
user_id = '000013ec-0000-0000-0000-000000000000'
item_id = '0000130e-0000-0000-0000-000000000000'

result = playstate_controller.on_playback_stopped(user_id, item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Ping Playback Session

Pings a playback session.

```python
def ping_playback_session(self,
                         play_session_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `play_session_id` | `string` | Query, Required | Playback session id. |

## Response Type

`void`

## Example Usage

```python
play_session_id = 'playSessionId2'

result = playstate_controller.ping_playback_session(play_session_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Report Playback Progress

Reports playback progress within a session.

```python
def report_playback_progress(self,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PlaybackProgressInfo`](../../doc/models/playback-progress-info.md) | Body, Optional | The playback progress info. |

## Response Type

`void`

## Example Usage

```python
result = playstate_controller.report_playback_progress()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Report Playback Start

Reports playback has started within a session.

```python
def report_playback_start(self,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PlaybackStartInfo`](../../doc/models/playback-start-info.md) | Body, Optional | The playback start info. |

## Response Type

`void`

## Example Usage

```python
result = playstate_controller.report_playback_start()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Report Playback Stopped

Reports playback has stopped within a session.

```python
def report_playback_stopped(self,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PlaybackStopInfo`](../../doc/models/playback-stop-info.md) | Body, Optional | The playback stop info. |

## Response Type

`void`

## Example Usage

```python
result = playstate_controller.report_playback_stopped()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

