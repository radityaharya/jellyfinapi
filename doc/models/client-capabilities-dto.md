
# Client Capabilities Dto

Client capabilities dto.

## Structure

`ClientCapabilitiesDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playable_media_types` | `List of string` | Optional | Gets or sets the list of playable media types. |
| `supported_commands` | [`List of GeneralCommandTypeEnum`](../../doc/models/general-command-type-enum.md) | Optional | Gets or sets the list of supported commands. |
| `supports_media_control` | `bool` | Optional | Gets or sets a value indicating whether session supports media control. |
| `supports_content_uploading` | `bool` | Optional | Gets or sets a value indicating whether session supports content uploading. |
| `message_callback_url` | `string` | Optional | Gets or sets the message callback url. |
| `supports_persistent_identifier` | `bool` | Optional | Gets or sets a value indicating whether session supports a persistent identifier. |
| `supports_sync` | `bool` | Optional | Gets or sets a value indicating whether session supports sync. |
| `device_profile` | [`DeviceProfile`](../../doc/models/device-profile.md) | Optional | A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.<br><br /><br>Specifically, it defines the supported <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and<br><see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec profiles and levels)<br>the device is able to direct play (without transcoding or remuxing),<br>as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to transcode to</see> in case it isn't. |
| `app_store_url` | `string` | Optional | Gets or sets the app store url. |
| `icon_url` | `string` | Optional | Gets or sets the icon url. |

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

