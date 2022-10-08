
# Open Live Stream Dto

Open live stream dto.

## Structure

`OpenLiveStreamDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `open_token` | `string` | Optional | Gets or sets the open token. |
| `user_id` | `uuid\|string` | Optional | Gets or sets the user id. |
| `play_session_id` | `string` | Optional | Gets or sets the play session id. |
| `max_streaming_bitrate` | `int` | Optional | Gets or sets the max streaming bitrate. |
| `start_time_ticks` | `long\|int` | Optional | Gets or sets the start time in ticks. |
| `audio_stream_index` | `int` | Optional | Gets or sets the audio stream index. |
| `subtitle_stream_index` | `int` | Optional | Gets or sets the subtitle stream index. |
| `max_audio_channels` | `int` | Optional | Gets or sets the max audio channels. |
| `item_id` | `uuid\|string` | Optional | Gets or sets the item id. |
| `enable_direct_play` | `bool` | Optional | Gets or sets a value indicating whether to enable direct play. |
| `enable_direct_stream` | `bool` | Optional | Gets or sets a value indicating whether to enale direct stream. |
| `device_profile` | [`DeviceProfile`](../../doc/models/device-profile.md) | Optional | A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.<br><br /><br>Specifically, it defines the supported <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and<br><see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec profiles and levels)<br>the device is able to direct play (without transcoding or remuxing),<br>as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to transcode to</see> in case it isn't. |
| `direct_play_protocols` | [`List of MediaProtocolEnum`](../../doc/models/media-protocol-enum.md) | Optional | Gets or sets the device play protocols. |

## Example (as JSON)

```json
{
  "OpenToken": null,
  "UserId": null,
  "PlaySessionId": null,
  "MaxStreamingBitrate": null,
  "StartTimeTicks": null,
  "AudioStreamIndex": null,
  "SubtitleStreamIndex": null,
  "MaxAudioChannels": null,
  "ItemId": null,
  "EnableDirectPlay": null,
  "EnableDirectStream": null,
  "DeviceProfile": null,
  "DirectPlayProtocols": null
}
```

