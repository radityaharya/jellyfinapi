
# Session Info

Class SessionInfo.

## Structure

`SessionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `play_state` | [`PlayerStateInfo`](../../doc/models/player-state-info.md) | Optional | - |
| `additional_users` | [`List of SessionUserInfo`](../../doc/models/session-user-info.md) | Optional | - |
| `capabilities` | [`ClientCapabilities`](../../doc/models/client-capabilities.md) | Optional | - |
| `remote_end_point` | `string` | Optional | Gets or sets the remote end point. |
| `playable_media_types` | `List of string` | Optional | Gets the playable media types. |
| `id` | `string` | Optional | Gets or sets the id. |
| `user_id` | `uuid\|string` | Optional | Gets or sets the user id. |
| `user_name` | `string` | Optional | Gets or sets the username. |
| `client` | `string` | Optional | Gets or sets the type of the client. |
| `last_activity_date` | `datetime` | Optional | Gets or sets the last activity date. |
| `last_playback_check_in` | `datetime` | Optional | Gets or sets the last playback check in. |
| `device_name` | `string` | Optional | Gets or sets the name of the device. |
| `device_type` | `string` | Optional | Gets or sets the type of the device. |
| `now_playing_item` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | This is strictly used as a data transfer object from the api layer.<br>This holds information about a BaseItem in a format that is convenient for the client. |
| `full_now_playing_item` | [`BaseItem`](../../doc/models/base-item.md) | Optional | Class BaseItem. |
| `now_viewing_item` | [`BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | This is strictly used as a data transfer object from the api layer.<br>This holds information about a BaseItem in a format that is convenient for the client. |
| `device_id` | `string` | Optional | Gets or sets the device id. |
| `application_version` | `string` | Optional | Gets or sets the application version. |
| `transcoding_info` | [`TranscodingInfo`](../../doc/models/transcoding-info.md) | Optional | - |
| `is_active` | `bool` | Optional | Gets a value indicating whether this instance is active. |
| `supports_media_control` | `bool` | Optional | - |
| `supports_remote_control` | `bool` | Optional | - |
| `now_playing_queue` | [`List of QueueItem`](../../doc/models/queue-item.md) | Optional | - |
| `now_playing_queue_full_items` | [`List of BaseItemDto`](../../doc/models/base-item-dto.md) | Optional | - |
| `has_custom_device_name` | `bool` | Optional | - |
| `playlist_item_id` | `string` | Optional | - |
| `server_id` | `string` | Optional | - |
| `user_primary_image_tag` | `string` | Optional | - |
| `supported_commands` | [`List of GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Optional | Gets the supported commands. |

## Example (as JSON)

```json
{
  "PlayState": null,
  "AdditionalUsers": null,
  "Capabilities": null,
  "RemoteEndPoint": null,
  "Id": null,
  "UserId": null,
  "UserName": null,
  "Client": null,
  "LastActivityDate": null,
  "LastPlaybackCheckIn": null,
  "DeviceName": null,
  "DeviceType": null,
  "NowPlayingItem": null,
  "FullNowPlayingItem": null,
  "NowViewingItem": null,
  "DeviceId": null,
  "ApplicationVersion": null,
  "TranscodingInfo": null,
  "NowPlayingQueue": null,
  "NowPlayingQueueFullItems": null,
  "HasCustomDeviceName": null,
  "PlaylistItemId": null,
  "ServerId": null,
  "UserPrimaryImageTag": null
}
```

