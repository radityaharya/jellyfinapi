
# Client Capabilities

## Structure

`ClientCapabilities`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playable_media_types` | `List of string` | Optional | - |
| `supported_commands` | [`List of GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Optional | - |
| `supports_media_control` | `bool` | Optional | - |
| `supports_content_uploading` | `bool` | Optional | - |
| `message_callback_url` | `string` | Optional | - |
| `supports_persistent_identifier` | `bool` | Optional | - |
| `supports_sync` | `bool` | Optional | - |
| `device_profile` | [`DeviceProfile`](../../doc/models/device-profile.md) | Optional | A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.<br><br /><br>Specifically, it defines the supported <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and<br><see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec profiles and levels)<br>the device is able to direct play (without transcoding or remuxing),<br>as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to transcode to</see> in case it isn't. |
| `app_store_url` | `string` | Optional | - |
| `icon_url` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "PlayableMediaTypes": null,
  "SupportedCommands": null,
  "SupportsMediaControl": null,
  "SupportsContentUploading": null,
  "MessageCallbackUrl": null,
  "SupportsPersistentIdentifier": null,
  "SupportsSync": null,
  "DeviceProfile": null,
  "AppStoreUrl": null,
  "IconUrl": null
}
```

