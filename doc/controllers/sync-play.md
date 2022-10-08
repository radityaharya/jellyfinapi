# Sync Play

```python
sync_play_controller = client.sync_play
```

## Class Name

`SyncPlayController`

## Methods

* [Sync Play Buffering](../../doc/controllers/sync-play.md#sync-play-buffering)
* [Sync Play Create Group](../../doc/controllers/sync-play.md#sync-play-create-group)
* [Sync Play Get Groups](../../doc/controllers/sync-play.md#sync-play-get-groups)
* [Sync Play Join Group](../../doc/controllers/sync-play.md#sync-play-join-group)
* [Sync Play Leave Group](../../doc/controllers/sync-play.md#sync-play-leave-group)
* [Sync Play Move Playlist Item](../../doc/controllers/sync-play.md#sync-play-move-playlist-item)
* [Sync Play Next Item](../../doc/controllers/sync-play.md#sync-play-next-item)
* [Sync Play Pause](../../doc/controllers/sync-play.md#sync-play-pause)
* [Sync Play Ping](../../doc/controllers/sync-play.md#sync-play-ping)
* [Sync Play Previous Item](../../doc/controllers/sync-play.md#sync-play-previous-item)
* [Sync Play Queue](../../doc/controllers/sync-play.md#sync-play-queue)
* [Sync Play Ready](../../doc/controllers/sync-play.md#sync-play-ready)
* [Sync Play Remove From Playlist](../../doc/controllers/sync-play.md#sync-play-remove-from-playlist)
* [Sync Play Seek](../../doc/controllers/sync-play.md#sync-play-seek)
* [Sync Play Set Ignore Wait](../../doc/controllers/sync-play.md#sync-play-set-ignore-wait)
* [Sync Play Set New Queue](../../doc/controllers/sync-play.md#sync-play-set-new-queue)
* [Sync Play Set Playlist Item](../../doc/controllers/sync-play.md#sync-play-set-playlist-item)
* [Sync Play Set Repeat Mode](../../doc/controllers/sync-play.md#sync-play-set-repeat-mode)
* [Sync Play Set Shuffle Mode](../../doc/controllers/sync-play.md#sync-play-set-shuffle-mode)
* [Sync Play Stop](../../doc/controllers/sync-play.md#sync-play-stop)
* [Sync Play Unpause](../../doc/controllers/sync-play.md#sync-play-unpause)


# Sync Play Buffering

Notify SyncPlay group that member is buffering.

```python
def sync_play_buffering(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BufferRequestDto`](../../doc/models/buffer-request-dto.md) | Body, Required | The player status. |

## Response Type

`void`

## Example Usage

```python
body = BufferRequestDto()

result = sync_play_controller.sync_play_buffering(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Create Group

Create a new SyncPlay group.

```python
def sync_play_create_group(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NewGroupRequestDto`](../../doc/models/new-group-request-dto.md) | Body, Required | The settings of the new group. |

## Response Type

`void`

## Example Usage

```python
body = NewGroupRequestDto()

result = sync_play_controller.sync_play_create_group(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Get Groups

Gets all SyncPlay groups.

```python
def sync_play_get_groups(self)
```

## Response Type

[`List of GroupInfoDto`](../../doc/models/group-info-dto.md)

## Example Usage

```python
result = sync_play_controller.sync_play_get_groups()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Join Group

Join an existing SyncPlay group.

```python
def sync_play_join_group(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`JoinGroupRequestDto`](../../doc/models/join-group-request-dto.md) | Body, Required | The group to join. |

## Response Type

`void`

## Example Usage

```python
body = JoinGroupRequestDto()

result = sync_play_controller.sync_play_join_group(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Leave Group

Leave the joined SyncPlay group.

```python
def sync_play_leave_group(self)
```

## Response Type

`void`

## Example Usage

```python
result = sync_play_controller.sync_play_leave_group()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Move Playlist Item

Request to move an item in the playlist in SyncPlay group.

```python
def sync_play_move_playlist_item(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MovePlaylistItemRequestDto`](../../doc/models/move-playlist-item-request-dto.md) | Body, Required | The new position for the item. |

## Response Type

`void`

## Example Usage

```python
body = MovePlaylistItemRequestDto()

result = sync_play_controller.sync_play_move_playlist_item(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Next Item

Request next item in SyncPlay group.

```python
def sync_play_next_item(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NextItemRequestDto`](../../doc/models/next-item-request-dto.md) | Body, Required | The current item information. |

## Response Type

`void`

## Example Usage

```python
body = NextItemRequestDto()

result = sync_play_controller.sync_play_next_item(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Pause

Request pause in SyncPlay group.

```python
def sync_play_pause(self)
```

## Response Type

`void`

## Example Usage

```python
result = sync_play_controller.sync_play_pause()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Ping

Update session ping.

```python
def sync_play_ping(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PingRequestDto`](../../doc/models/ping-request-dto.md) | Body, Required | The new ping. |

## Response Type

`void`

## Example Usage

```python
body = PingRequestDto()

result = sync_play_controller.sync_play_ping(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Previous Item

Request previous item in SyncPlay group.

```python
def sync_play_previous_item(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PreviousItemRequestDto`](../../doc/models/previous-item-request-dto.md) | Body, Required | The current item information. |

## Response Type

`void`

## Example Usage

```python
body = PreviousItemRequestDto()

result = sync_play_controller.sync_play_previous_item(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Queue

Request to queue items to the playlist of a SyncPlay group.

```python
def sync_play_queue(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`QueueRequestDto`](../../doc/models/queue-request-dto.md) | Body, Required | The items to add. |

## Response Type

`void`

## Example Usage

```python
body = QueueRequestDto()

result = sync_play_controller.sync_play_queue(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Ready

Notify SyncPlay group that member is ready for playback.

```python
def sync_play_ready(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ReadyRequestDto`](../../doc/models/ready-request-dto.md) | Body, Required | The player status. |

## Response Type

`void`

## Example Usage

```python
body = ReadyRequestDto()

result = sync_play_controller.sync_play_ready(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Remove From Playlist

Request to remove items from the playlist in SyncPlay group.

```python
def sync_play_remove_from_playlist(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RemoveFromPlaylistRequestDto`](../../doc/models/remove-from-playlist-request-dto.md) | Body, Required | The items to remove. |

## Response Type

`void`

## Example Usage

```python
body = RemoveFromPlaylistRequestDto()

result = sync_play_controller.sync_play_remove_from_playlist(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Seek

Request seek in SyncPlay group.

```python
def sync_play_seek(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SeekRequestDto`](../../doc/models/seek-request-dto.md) | Body, Required | The new playback position. |

## Response Type

`void`

## Example Usage

```python
body = SeekRequestDto()

result = sync_play_controller.sync_play_seek(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Set Ignore Wait

Request SyncPlay group to ignore member during group-wait.

```python
def sync_play_set_ignore_wait(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`IgnoreWaitRequestDto`](../../doc/models/ignore-wait-request-dto.md) | Body, Required | The settings to set. |

## Response Type

`void`

## Example Usage

```python
body = IgnoreWaitRequestDto()

result = sync_play_controller.sync_play_set_ignore_wait(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Set New Queue

Request to set new playlist in SyncPlay group.

```python
def sync_play_set_new_queue(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PlayRequestDto`](../../doc/models/play-request-dto.md) | Body, Required | The new playlist to play in the group. |

## Response Type

`void`

## Example Usage

```python
body = PlayRequestDto()

result = sync_play_controller.sync_play_set_new_queue(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Set Playlist Item

Request to change playlist item in SyncPlay group.

```python
def sync_play_set_playlist_item(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetPlaylistItemRequestDto`](../../doc/models/set-playlist-item-request-dto.md) | Body, Required | The new item to play. |

## Response Type

`void`

## Example Usage

```python
body = SetPlaylistItemRequestDto()

result = sync_play_controller.sync_play_set_playlist_item(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Set Repeat Mode

Request to set repeat mode in SyncPlay group.

```python
def sync_play_set_repeat_mode(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetRepeatModeRequestDto`](../../doc/models/set-repeat-mode-request-dto.md) | Body, Required | The new repeat mode. |

## Response Type

`void`

## Example Usage

```python
body = SetRepeatModeRequestDto()

result = sync_play_controller.sync_play_set_repeat_mode(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Set Shuffle Mode

Request to set shuffle mode in SyncPlay group.

```python
def sync_play_set_shuffle_mode(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetShuffleModeRequestDto`](../../doc/models/set-shuffle-mode-request-dto.md) | Body, Required | The new shuffle mode. |

## Response Type

`void`

## Example Usage

```python
body = SetShuffleModeRequestDto()

result = sync_play_controller.sync_play_set_shuffle_mode(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Stop

Request stop in SyncPlay group.

```python
def sync_play_stop(self)
```

## Response Type

`void`

## Example Usage

```python
result = sync_play_controller.sync_play_stop()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Sync Play Unpause

Request unpause in SyncPlay group.

```python
def sync_play_unpause(self)
```

## Response Type

`void`

## Example Usage

```python
result = sync_play_controller.sync_play_unpause()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

