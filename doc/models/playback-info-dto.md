
# Playback Info Dto

Plabyback info dto.

## Structure

`PlaybackInfoDto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|string` | Optional | Gets or sets the playback userId. |
| `max_streaming_bitrate` | `int` | Optional | Gets or sets the max streaming bitrate. |
| `start_time_ticks` | `long\|int` | Optional | Gets or sets the start time in ticks. |
| `audio_stream_index` | `int` | Optional | Gets or sets the audio stream index. |
| `subtitle_stream_index` | `int` | Optional | Gets or sets the subtitle stream index. |
| `max_audio_channels` | `int` | Optional | Gets or sets the max audio channels. |
| `media_source_id` | `string` | Optional | Gets or sets the media source id. |
| `live_stream_id` | `string` | Optional | Gets or sets the live stream id. |
| `device_profile` | [`DeviceProfile`](../../doc/models/device-profile.md) | Optional | A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.<br><br /><br>Specifically, it defines the supported <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and<br><see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec profiles and levels)<br>the device is able to direct play (without transcoding or remuxing),<br>as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to transcode to</see> in case it isn't. |
| `enable_direct_play` | `bool` | Optional | Gets or sets a value indicating whether to enable direct play. |
| `enable_direct_stream` | `bool` | Optional | Gets or sets a value indicating whether to enable direct stream. |
| `enable_transcoding` | `bool` | Optional | Gets or sets a value indicating whether to enable transcoding. |
| `allow_video_stream_copy` | `bool` | Optional | Gets or sets a value indicating whether to enable video stream copy. |
| `allow_audio_stream_copy` | `bool` | Optional | Gets or sets a value indicating whether to allow audio stream copy. |
| `auto_open_live_stream` | `bool` | Optional | Gets or sets a value indicating whether to auto open the live stream. |

## Example (as JSON)

```json
{
  "UserId": null,
  "MaxStreamingBitrate": null,
  "StartTimeTicks": null,
  "AudioStreamIndex": null,
  "SubtitleStreamIndex": null,
  "MaxAudioChannels": null,
  "MediaSourceId": null,
  "LiveStreamId": null,
  "DeviceProfile": null,
  "EnableDirectPlay": null,
  "EnableDirectStream": null,
  "EnableTranscoding": null,
  "AllowVideoStreamCopy": null,
  "AllowAudioStreamCopy": null,
  "AutoOpenLiveStream": null
}
```

