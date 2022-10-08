# Universal Audio

```python
universal_audio_controller = client.universal_audio
```

## Class Name

`UniversalAudioController`


# Get Universal Audio Stream

Gets an audio stream.

```python
def get_universal_audio_stream(self,
                              item_id,
                              container=None,
                              media_source_id=None,
                              device_id=None,
                              user_id=None,
                              audio_codec=None,
                              max_audio_channels=None,
                              transcoding_audio_channels=None,
                              max_streaming_bitrate=None,
                              audio_bit_rate=None,
                              start_time_ticks=None,
                              transcoding_container=None,
                              transcoding_protocol=None,
                              max_audio_sample_rate=None,
                              max_audio_bit_depth=None,
                              enable_remote_media=None,
                              break_on_non_key_frames=False,
                              enable_redirection=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `container` | `List of string` | Query, Optional | Optional. The audio container. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `user_id` | `uuid\|string` | Query, Optional | Optional. The user id. |
| `audio_codec` | `string` | Query, Optional | Optional. The audio codec to transcode to. |
| `max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels. |
| `transcoding_audio_channels` | `int` | Query, Optional | Optional. The number of how many audio channels to transcode to. |
| `max_streaming_bitrate` | `int` | Query, Optional | Optional. The maximum streaming bitrate. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `transcoding_container` | `string` | Query, Optional | Optional. The container to transcode to. |
| `transcoding_protocol` | `string` | Query, Optional | Optional. The transcoding protocol. |
| `max_audio_sample_rate` | `int` | Query, Optional | Optional. The maximum audio sample rate. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `enable_remote_media` | `bool` | Query, Optional | Optional. Whether to enable remote media. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames.<br>**Default**: `False` |
| `enable_redirection` | `bool` | Query, Optional | Whether to enable redirection. Defaults to true.<br>**Default**: `True` |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
break_on_non_key_frames = False
enable_redirection = True

result = universal_audio_controller.get_universal_audio_stream(item_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, break_on_non_key_frames, enable_redirection)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

