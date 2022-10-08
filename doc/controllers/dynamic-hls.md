# Dynamic Hls

```python
dynamic_hls_controller = client.dynamic_hls
```

## Class Name

`DynamicHlsController`

## Methods

* [Get Hls Audio Segment](../../doc/controllers/dynamic-hls.md#get-hls-audio-segment)
* [Get Hls Video Segment](../../doc/controllers/dynamic-hls.md#get-hls-video-segment)
* [Get Live Hls Stream](../../doc/controllers/dynamic-hls.md#get-live-hls-stream)
* [Get Master Hls Audio Playlist](../../doc/controllers/dynamic-hls.md#get-master-hls-audio-playlist)
* [Get Master Hls Video Playlist](../../doc/controllers/dynamic-hls.md#get-master-hls-video-playlist)
* [Get Variant Hls Audio Playlist](../../doc/controllers/dynamic-hls.md#get-variant-hls-audio-playlist)
* [Get Variant Hls Video Playlist](../../doc/controllers/dynamic-hls.md#get-variant-hls-video-playlist)


# Get Hls Audio Segment

Gets a video stream using HTTP live streaming.

```python
def get_hls_audio_segment(self,
                         item_id,
                         playlist_id,
                         segment_id,
                         container,
                         runtime_ticks,
                         actual_segment_length_ticks,
                         static=None,
                         params=None,
                         tag=None,
                         device_profile_id=None,
                         play_session_id=None,
                         segment_container=None,
                         segment_length=None,
                         min_segments=None,
                         media_source_id=None,
                         device_id=None,
                         audio_codec=None,
                         enable_auto_stream_copy=None,
                         allow_video_stream_copy=None,
                         allow_audio_stream_copy=None,
                         break_on_non_key_frames=None,
                         audio_sample_rate=None,
                         max_audio_bit_depth=None,
                         max_streaming_bitrate=None,
                         audio_bit_rate=None,
                         audio_channels=None,
                         max_audio_channels=None,
                         profile=None,
                         level=None,
                         framerate=None,
                         max_framerate=None,
                         copy_timestamps=None,
                         start_time_ticks=None,
                         width=None,
                         height=None,
                         video_bit_rate=None,
                         subtitle_stream_index=None,
                         subtitle_method=None,
                         max_ref_frames=None,
                         max_video_bit_depth=None,
                         require_avc=None,
                         de_interlace=None,
                         require_non_anamorphic=None,
                         transcoding_max_audio_channels=None,
                         cpu_core_limit=None,
                         live_stream_id=None,
                         enable_mpegts_m_2_ts_mode=None,
                         video_codec=None,
                         subtitle_codec=None,
                         transcode_reasons=None,
                         audio_stream_index=None,
                         video_stream_index=None,
                         context=None,
                         stream_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `playlist_id` | `string` | Template, Required | The playlist id. |
| `segment_id` | `int` | Template, Required | The segment id. |
| `container` | `string` | Template, Required | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. |
| `runtime_ticks` | `long\|int` | Query, Required | The position of the requested segment in ticks. |
| `actual_segment_length_ticks` | `long\|int` | Query, Required | The length of the requested segment in ticks. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `max_streaming_bitrate` | `int` | Query, Optional | Optional. The maximum streaming bitrate. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
playlist_id = 'playlistId8'
segment_id = 170
container = 'container2'
runtime_ticks = 68
actual_segment_length_ticks = 38

result = dynamic_hls_controller.get_hls_audio_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Hls Video Segment

Gets a video stream using HTTP live streaming.

```python
def get_hls_video_segment(self,
                         item_id,
                         playlist_id,
                         segment_id,
                         container,
                         runtime_ticks,
                         actual_segment_length_ticks,
                         static=None,
                         params=None,
                         tag=None,
                         device_profile_id=None,
                         play_session_id=None,
                         segment_container=None,
                         segment_length=None,
                         min_segments=None,
                         media_source_id=None,
                         device_id=None,
                         audio_codec=None,
                         enable_auto_stream_copy=None,
                         allow_video_stream_copy=None,
                         allow_audio_stream_copy=None,
                         break_on_non_key_frames=None,
                         audio_sample_rate=None,
                         max_audio_bit_depth=None,
                         audio_bit_rate=None,
                         audio_channels=None,
                         max_audio_channels=None,
                         profile=None,
                         level=None,
                         framerate=None,
                         max_framerate=None,
                         copy_timestamps=None,
                         start_time_ticks=None,
                         width=None,
                         height=None,
                         max_width=None,
                         max_height=None,
                         video_bit_rate=None,
                         subtitle_stream_index=None,
                         subtitle_method=None,
                         max_ref_frames=None,
                         max_video_bit_depth=None,
                         require_avc=None,
                         de_interlace=None,
                         require_non_anamorphic=None,
                         transcoding_max_audio_channels=None,
                         cpu_core_limit=None,
                         live_stream_id=None,
                         enable_mpegts_m_2_ts_mode=None,
                         video_codec=None,
                         subtitle_codec=None,
                         transcode_reasons=None,
                         audio_stream_index=None,
                         video_stream_index=None,
                         context=None,
                         stream_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `playlist_id` | `string` | Template, Required | The playlist id. |
| `segment_id` | `int` | Template, Required | The segment id. |
| `container` | `string` | Template, Required | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. |
| `runtime_ticks` | `long\|int` | Query, Required | The position of the requested segment in ticks. |
| `actual_segment_length_ticks` | `long\|int` | Query, Required | The length of the requested segment in ticks. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The desired segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `max_width` | `int` | Query, Optional | Optional. The maximum horizontal resolution of the encoded video. |
| `max_height` | `int` | Query, Optional | Optional. The maximum vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vp8, vp9, vpx (deprecated), wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
playlist_id = 'playlistId8'
segment_id = 170
container = 'container2'
runtime_ticks = 68
actual_segment_length_ticks = 38

result = dynamic_hls_controller.get_hls_video_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Live Hls Stream

Gets a hls live stream.

```python
def get_live_hls_stream(self,
                       item_id,
                       container=None,
                       static=None,
                       params=None,
                       tag=None,
                       device_profile_id=None,
                       play_session_id=None,
                       segment_container=None,
                       segment_length=None,
                       min_segments=None,
                       media_source_id=None,
                       device_id=None,
                       audio_codec=None,
                       enable_auto_stream_copy=None,
                       allow_video_stream_copy=None,
                       allow_audio_stream_copy=None,
                       break_on_non_key_frames=None,
                       audio_sample_rate=None,
                       max_audio_bit_depth=None,
                       audio_bit_rate=None,
                       audio_channels=None,
                       max_audio_channels=None,
                       profile=None,
                       level=None,
                       framerate=None,
                       max_framerate=None,
                       copy_timestamps=None,
                       start_time_ticks=None,
                       width=None,
                       height=None,
                       video_bit_rate=None,
                       subtitle_stream_index=None,
                       subtitle_method=None,
                       max_ref_frames=None,
                       max_video_bit_depth=None,
                       require_avc=None,
                       de_interlace=None,
                       require_non_anamorphic=None,
                       transcoding_max_audio_channels=None,
                       cpu_core_limit=None,
                       live_stream_id=None,
                       enable_mpegts_m_2_ts_mode=None,
                       video_codec=None,
                       subtitle_codec=None,
                       transcode_reasons=None,
                       audio_stream_index=None,
                       video_stream_index=None,
                       context=None,
                       stream_options=None,
                       max_width=None,
                       max_height=None,
                       enable_subtitles_in_manifest=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `container` | `string` | Query, Optional | The audio container. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment lenght. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vp8, vp9, vpx (deprecated), wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |
| `max_width` | `int` | Query, Optional | Optional. The max width. |
| `max_height` | `int` | Query, Optional | Optional. The max height. |
| `enable_subtitles_in_manifest` | `bool` | Query, Optional | Optional. Whether to enable subtitles in the manifest. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = dynamic_hls_controller.get_live_hls_stream(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Master Hls Audio Playlist

Gets an audio hls playlist stream.

```python
def get_master_hls_audio_playlist(self,
                                 item_id,
                                 media_source_id,
                                 static=None,
                                 params=None,
                                 tag=None,
                                 device_profile_id=None,
                                 play_session_id=None,
                                 segment_container=None,
                                 segment_length=None,
                                 min_segments=None,
                                 device_id=None,
                                 audio_codec=None,
                                 enable_auto_stream_copy=None,
                                 allow_video_stream_copy=None,
                                 allow_audio_stream_copy=None,
                                 break_on_non_key_frames=None,
                                 audio_sample_rate=None,
                                 max_audio_bit_depth=None,
                                 max_streaming_bitrate=None,
                                 audio_bit_rate=None,
                                 audio_channels=None,
                                 max_audio_channels=None,
                                 profile=None,
                                 level=None,
                                 framerate=None,
                                 max_framerate=None,
                                 copy_timestamps=None,
                                 start_time_ticks=None,
                                 width=None,
                                 height=None,
                                 video_bit_rate=None,
                                 subtitle_stream_index=None,
                                 subtitle_method=None,
                                 max_ref_frames=None,
                                 max_video_bit_depth=None,
                                 require_avc=None,
                                 de_interlace=None,
                                 require_non_anamorphic=None,
                                 transcoding_max_audio_channels=None,
                                 cpu_core_limit=None,
                                 live_stream_id=None,
                                 enable_mpegts_m_2_ts_mode=None,
                                 video_codec=None,
                                 subtitle_codec=None,
                                 transcode_reasons=None,
                                 audio_stream_index=None,
                                 video_stream_index=None,
                                 context=None,
                                 stream_options=None,
                                 enable_adaptive_bitrate_streaming=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `media_source_id` | `string` | Query, Required | The media version id, if playing an alternate version. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `max_streaming_bitrate` | `int` | Query, Optional | Optional. The maximum streaming bitrate. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vp8, vp9, vpx (deprecated), wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |
| `enable_adaptive_bitrate_streaming` | `bool` | Query, Optional | Enable adaptive bitrate streaming.<br>**Default**: `True` |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
media_source_id = 'mediaSourceId4'
enable_adaptive_bitrate_streaming = True

result = dynamic_hls_controller.get_master_hls_audio_playlist(item_id, media_source_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_adaptive_bitrate_streaming)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Master Hls Video Playlist

Gets a video hls playlist stream.

```python
def get_master_hls_video_playlist(self,
                                 item_id,
                                 media_source_id,
                                 static=None,
                                 params=None,
                                 tag=None,
                                 device_profile_id=None,
                                 play_session_id=None,
                                 segment_container=None,
                                 segment_length=None,
                                 min_segments=None,
                                 device_id=None,
                                 audio_codec=None,
                                 enable_auto_stream_copy=None,
                                 allow_video_stream_copy=None,
                                 allow_audio_stream_copy=None,
                                 break_on_non_key_frames=None,
                                 audio_sample_rate=None,
                                 max_audio_bit_depth=None,
                                 audio_bit_rate=None,
                                 audio_channels=None,
                                 max_audio_channels=None,
                                 profile=None,
                                 level=None,
                                 framerate=None,
                                 max_framerate=None,
                                 copy_timestamps=None,
                                 start_time_ticks=None,
                                 width=None,
                                 height=None,
                                 max_width=None,
                                 max_height=None,
                                 video_bit_rate=None,
                                 subtitle_stream_index=None,
                                 subtitle_method=None,
                                 max_ref_frames=None,
                                 max_video_bit_depth=None,
                                 require_avc=None,
                                 de_interlace=None,
                                 require_non_anamorphic=None,
                                 transcoding_max_audio_channels=None,
                                 cpu_core_limit=None,
                                 live_stream_id=None,
                                 enable_mpegts_m_2_ts_mode=None,
                                 video_codec=None,
                                 subtitle_codec=None,
                                 transcode_reasons=None,
                                 audio_stream_index=None,
                                 video_stream_index=None,
                                 context=None,
                                 stream_options=None,
                                 enable_adaptive_bitrate_streaming=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `media_source_id` | `string` | Query, Required | The media version id, if playing an alternate version. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `max_width` | `int` | Query, Optional | Optional. The maximum horizontal resolution of the encoded video. |
| `max_height` | `int` | Query, Optional | Optional. The maximum vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vp8, vp9, vpx (deprecated), wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |
| `enable_adaptive_bitrate_streaming` | `bool` | Query, Optional | Enable adaptive bitrate streaming.<br>**Default**: `True` |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'
media_source_id = 'mediaSourceId4'
enable_adaptive_bitrate_streaming = True

result = dynamic_hls_controller.get_master_hls_video_playlist(item_id, media_source_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, enable_adaptive_bitrate_streaming)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Variant Hls Audio Playlist

Gets an audio stream using HTTP live streaming.

```python
def get_variant_hls_audio_playlist(self,
                                  item_id,
                                  static=None,
                                  params=None,
                                  tag=None,
                                  device_profile_id=None,
                                  play_session_id=None,
                                  segment_container=None,
                                  segment_length=None,
                                  min_segments=None,
                                  media_source_id=None,
                                  device_id=None,
                                  audio_codec=None,
                                  enable_auto_stream_copy=None,
                                  allow_video_stream_copy=None,
                                  allow_audio_stream_copy=None,
                                  break_on_non_key_frames=None,
                                  audio_sample_rate=None,
                                  max_audio_bit_depth=None,
                                  max_streaming_bitrate=None,
                                  audio_bit_rate=None,
                                  audio_channels=None,
                                  max_audio_channels=None,
                                  profile=None,
                                  level=None,
                                  framerate=None,
                                  max_framerate=None,
                                  copy_timestamps=None,
                                  start_time_ticks=None,
                                  width=None,
                                  height=None,
                                  video_bit_rate=None,
                                  subtitle_stream_index=None,
                                  subtitle_method=None,
                                  max_ref_frames=None,
                                  max_video_bit_depth=None,
                                  require_avc=None,
                                  de_interlace=None,
                                  require_non_anamorphic=None,
                                  transcoding_max_audio_channels=None,
                                  cpu_core_limit=None,
                                  live_stream_id=None,
                                  enable_mpegts_m_2_ts_mode=None,
                                  video_codec=None,
                                  subtitle_codec=None,
                                  transcode_reasons=None,
                                  audio_stream_index=None,
                                  video_stream_index=None,
                                  context=None,
                                  stream_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `max_streaming_bitrate` | `int` | Query, Optional | Optional. The maximum streaming bitrate. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = dynamic_hls_controller.get_variant_hls_audio_playlist(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |


# Get Variant Hls Video Playlist

Gets a video stream using HTTP live streaming.

```python
def get_variant_hls_video_playlist(self,
                                  item_id,
                                  static=None,
                                  params=None,
                                  tag=None,
                                  device_profile_id=None,
                                  play_session_id=None,
                                  segment_container=None,
                                  segment_length=None,
                                  min_segments=None,
                                  media_source_id=None,
                                  device_id=None,
                                  audio_codec=None,
                                  enable_auto_stream_copy=None,
                                  allow_video_stream_copy=None,
                                  allow_audio_stream_copy=None,
                                  break_on_non_key_frames=None,
                                  audio_sample_rate=None,
                                  max_audio_bit_depth=None,
                                  audio_bit_rate=None,
                                  audio_channels=None,
                                  max_audio_channels=None,
                                  profile=None,
                                  level=None,
                                  framerate=None,
                                  max_framerate=None,
                                  copy_timestamps=None,
                                  start_time_ticks=None,
                                  width=None,
                                  height=None,
                                  max_width=None,
                                  max_height=None,
                                  video_bit_rate=None,
                                  subtitle_stream_index=None,
                                  subtitle_method=None,
                                  max_ref_frames=None,
                                  max_video_bit_depth=None,
                                  require_avc=None,
                                  de_interlace=None,
                                  require_non_anamorphic=None,
                                  transcoding_max_audio_channels=None,
                                  cpu_core_limit=None,
                                  live_stream_id=None,
                                  enable_mpegts_m_2_ts_mode=None,
                                  video_codec=None,
                                  subtitle_codec=None,
                                  transcode_reasons=None,
                                  audio_stream_index=None,
                                  video_stream_index=None,
                                  context=None,
                                  stream_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `uuid\|string` | Template, Required | The item id. |
| `static` | `bool` | Query, Optional | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. |
| `params` | `string` | Query, Optional | The streaming parameters. |
| `tag` | `string` | Query, Optional | The tag. |
| `device_profile_id` | `string` | Query, Optional | Optional. The dlna device profile id to utilize. |
| `play_session_id` | `string` | Query, Optional | The play session id. |
| `segment_container` | `string` | Query, Optional | The segment container. |
| `segment_length` | `int` | Query, Optional | The segment length. |
| `min_segments` | `int` | Query, Optional | The minimum number of segments. |
| `media_source_id` | `string` | Query, Optional | The media version id, if playing an alternate version. |
| `device_id` | `string` | Query, Optional | The device id of the client requesting. Used to stop encoding processes when needed. |
| `audio_codec` | `string` | Query, Optional | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. |
| `enable_auto_stream_copy` | `bool` | Query, Optional | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. |
| `allow_video_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the video stream url. |
| `allow_audio_stream_copy` | `bool` | Query, Optional | Whether or not to allow copying of the audio stream url. |
| `break_on_non_key_frames` | `bool` | Query, Optional | Optional. Whether to break on non key frames. |
| `audio_sample_rate` | `int` | Query, Optional | Optional. Specify a specific audio sample rate, e.g. 44100. |
| `max_audio_bit_depth` | `int` | Query, Optional | Optional. The maximum audio bit depth. |
| `audio_bit_rate` | `int` | Query, Optional | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. |
| `audio_channels` | `int` | Query, Optional | Optional. Specify a specific number of audio channels to encode to, e.g. 2. |
| `max_audio_channels` | `int` | Query, Optional | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. |
| `profile` | `string` | Query, Optional | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. |
| `level` | `string` | Query, Optional | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. |
| `framerate` | `float` | Query, Optional | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `max_framerate` | `float` | Query, Optional | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. |
| `copy_timestamps` | `bool` | Query, Optional | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. |
| `start_time_ticks` | `long\|int` | Query, Optional | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. |
| `width` | `int` | Query, Optional | Optional. The fixed horizontal resolution of the encoded video. |
| `height` | `int` | Query, Optional | Optional. The fixed vertical resolution of the encoded video. |
| `max_width` | `int` | Query, Optional | Optional. The maximum horizontal resolution of the encoded video. |
| `max_height` | `int` | Query, Optional | Optional. The maximum vertical resolution of the encoded video. |
| `video_bit_rate` | `int` | Query, Optional | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. |
| `subtitle_stream_index` | `int` | Query, Optional | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. |
| `subtitle_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Query, Optional | Optional. Specify the subtitle delivery method. |
| `max_ref_frames` | `int` | Query, Optional | Optional. |
| `max_video_bit_depth` | `int` | Query, Optional | Optional. The maximum video bit depth. |
| `require_avc` | `bool` | Query, Optional | Optional. Whether to require avc. |
| `de_interlace` | `bool` | Query, Optional | Optional. Whether to deinterlace the video. |
| `require_non_anamorphic` | `bool` | Query, Optional | Optional. Whether to require a non anamorphic stream. |
| `transcoding_max_audio_channels` | `int` | Query, Optional | Optional. The maximum number of audio channels to transcode. |
| `cpu_core_limit` | `int` | Query, Optional | Optional. The limit of how many cpu cores to use. |
| `live_stream_id` | `string` | Query, Optional | The live stream id. |
| `enable_mpegts_m_2_ts_mode` | `bool` | Query, Optional | Optional. Whether to enable the MpegtsM2Ts mode. |
| `video_codec` | `string` | Query, Optional | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vp8, vp9, vpx (deprecated), wmv. |
| `subtitle_codec` | `string` | Query, Optional | Optional. Specify a subtitle codec to encode to. |
| `transcode_reasons` | `string` | Query, Optional | Optional. The transcoding reason. |
| `audio_stream_index` | `int` | Query, Optional | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. |
| `video_stream_index` | `int` | Query, Optional | Optional. The index of the video stream to use. If omitted the first video stream will be used. |
| `context` | [`EncodingContextEnum`](../../doc/models/encoding-context-enum.md) | Query, Optional | Optional. The MediaBrowser.Model.Dlna.EncodingContext. |
| `stream_options` | `dict` | Query, Optional | Optional. The streaming options. |

## Response Type

`mixed`

## Example Usage

```python
item_id = '0000130e-0000-0000-0000-000000000000'

result = dynamic_hls_controller.get_variant_hls_video_playlist(item_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |

