
# User Policy

## Structure

`UserPolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_administrator` | `bool` | Optional | Gets or sets a value indicating whether this instance is administrator. |
| `is_hidden` | `bool` | Optional | Gets or sets a value indicating whether this instance is hidden. |
| `is_disabled` | `bool` | Optional | Gets or sets a value indicating whether this instance is disabled. |
| `max_parental_rating` | `int` | Optional | Gets or sets the max parental rating. |
| `blocked_tags` | `List of string` | Optional | - |
| `enable_user_preference_access` | `bool` | Optional | - |
| `access_schedules` | [`List of AccessSchedule`](../../doc/models/access-schedule.md) | Optional | - |
| `block_unrated_items` | [`List of UnratedItemEnum`](../../doc/models/unrated-item-enum.md) | Optional | - |
| `enable_remote_control_of_other_users` | `bool` | Optional | - |
| `enable_shared_device_control` | `bool` | Optional | - |
| `enable_remote_access` | `bool` | Optional | - |
| `enable_live_tv_management` | `bool` | Optional | - |
| `enable_live_tv_access` | `bool` | Optional | - |
| `enable_media_playback` | `bool` | Optional | - |
| `enable_audio_playback_transcoding` | `bool` | Optional | - |
| `enable_video_playback_transcoding` | `bool` | Optional | - |
| `enable_playback_remuxing` | `bool` | Optional | - |
| `force_remote_source_transcoding` | `bool` | Optional | - |
| `enable_content_deletion` | `bool` | Optional | - |
| `enable_content_deletion_from_folders` | `List of string` | Optional | - |
| `enable_content_downloading` | `bool` | Optional | - |
| `enable_sync_transcoding` | `bool` | Optional | Gets or sets a value indicating whether [enable synchronize]. |
| `enable_media_conversion` | `bool` | Optional | - |
| `enabled_devices` | `List of string` | Optional | - |
| `enable_all_devices` | `bool` | Optional | - |
| `enabled_channels` | `List of uuid\|string` | Optional | - |
| `enable_all_channels` | `bool` | Optional | - |
| `enabled_folders` | `List of uuid\|string` | Optional | - |
| `enable_all_folders` | `bool` | Optional | - |
| `invalid_login_attempt_count` | `int` | Optional | - |
| `login_attempts_before_lockout` | `int` | Optional | - |
| `max_active_sessions` | `int` | Optional | - |
| `enable_public_sharing` | `bool` | Optional | - |
| `blocked_media_folders` | `List of uuid\|string` | Optional | - |
| `blocked_channels` | `List of uuid\|string` | Optional | - |
| `remote_client_bitrate_limit` | `int` | Optional | - |
| `authentication_provider_id` | `string` | Optional | - |
| `password_reset_provider_id` | `string` | Optional | - |
| `sync_play_access` | [`SyncPlayUserAccessTypeEnum`](../../doc/models/sync-play-user-access-type-enum.md) | Optional | Enum SyncPlayUserAccessType. |

## Example (as JSON)

```json
{
  "IsAdministrator": null,
  "IsHidden": null,
  "IsDisabled": null,
  "MaxParentalRating": null,
  "BlockedTags": null,
  "EnableUserPreferenceAccess": null,
  "AccessSchedules": null,
  "BlockUnratedItems": null,
  "EnableRemoteControlOfOtherUsers": null,
  "EnableSharedDeviceControl": null,
  "EnableRemoteAccess": null,
  "EnableLiveTvManagement": null,
  "EnableLiveTvAccess": null,
  "EnableMediaPlayback": null,
  "EnableAudioPlaybackTranscoding": null,
  "EnableVideoPlaybackTranscoding": null,
  "EnablePlaybackRemuxing": null,
  "ForceRemoteSourceTranscoding": null,
  "EnableContentDeletion": null,
  "EnableContentDeletionFromFolders": null,
  "EnableContentDownloading": null,
  "EnableSyncTranscoding": null,
  "EnableMediaConversion": null,
  "EnabledDevices": null,
  "EnableAllDevices": null,
  "EnabledChannels": null,
  "EnableAllChannels": null,
  "EnabledFolders": null,
  "EnableAllFolders": null,
  "InvalidLoginAttemptCount": null,
  "LoginAttemptsBeforeLockout": null,
  "MaxActiveSessions": null,
  "EnablePublicSharing": null,
  "BlockedMediaFolders": null,
  "BlockedChannels": null,
  "RemoteClientBitrateLimit": null,
  "AuthenticationProviderId": null,
  "PasswordResetProviderId": null,
  "SyncPlayAccess": null
}
```

