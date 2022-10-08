
# Media Stream

Class MediaStream.

## Structure

`MediaStream`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codec` | `string` | Optional | Gets or sets the codec. |
| `codec_tag` | `string` | Optional | Gets or sets the codec tag. |
| `language` | `string` | Optional | Gets or sets the language. |
| `color_range` | `string` | Optional | Gets or sets the color range. |
| `color_space` | `string` | Optional | Gets or sets the color space. |
| `color_transfer` | `string` | Optional | Gets or sets the color transfer. |
| `color_primaries` | `string` | Optional | Gets or sets the color primaries. |
| `dv_version_major` | `int` | Optional | Gets or sets the Dolby Vision version major. |
| `dv_version_minor` | `int` | Optional | Gets or sets the Dolby Vision version minor. |
| `dv_profile` | `int` | Optional | Gets or sets the Dolby Vision profile. |
| `dv_level` | `int` | Optional | Gets or sets the Dolby Vision level. |
| `rpu_present_flag` | `int` | Optional | Gets or sets the Dolby Vision rpu present flag. |
| `el_present_flag` | `int` | Optional | Gets or sets the Dolby Vision el present flag. |
| `bl_present_flag` | `int` | Optional | Gets or sets the Dolby Vision bl present flag. |
| `dv_bl_signal_compatibility_id` | `int` | Optional | Gets or sets the Dolby Vision bl signal compatibility id. |
| `comment` | `string` | Optional | Gets or sets the comment. |
| `time_base` | `string` | Optional | Gets or sets the time base. |
| `codec_time_base` | `string` | Optional | Gets or sets the codec time base. |
| `title` | `string` | Optional | Gets or sets the title. |
| `video_range` | `string` | Optional | Gets the video range. |
| `video_range_type` | `string` | Optional | Gets the video range type. |
| `video_do_vi_title` | `string` | Optional | Gets the video dovi title. |
| `localized_undefined` | `string` | Optional | - |
| `localized_default` | `string` | Optional | - |
| `localized_forced` | `string` | Optional | - |
| `localized_external` | `string` | Optional | - |
| `display_title` | `string` | Optional | - |
| `nal_length_size` | `string` | Optional | - |
| `is_interlaced` | `bool` | Optional | Gets or sets a value indicating whether this instance is interlaced. |
| `is_avc` | `bool` | Optional | - |
| `channel_layout` | `string` | Optional | Gets or sets the channel layout. |
| `bit_rate` | `int` | Optional | Gets or sets the bit rate. |
| `bit_depth` | `int` | Optional | Gets or sets the bit depth. |
| `ref_frames` | `int` | Optional | Gets or sets the reference frames. |
| `packet_length` | `int` | Optional | Gets or sets the length of the packet. |
| `channels` | `int` | Optional | Gets or sets the channels. |
| `sample_rate` | `int` | Optional | Gets or sets the sample rate. |
| `is_default` | `bool` | Optional | Gets or sets a value indicating whether this instance is default. |
| `is_forced` | `bool` | Optional | Gets or sets a value indicating whether this instance is forced. |
| `height` | `int` | Optional | Gets or sets the height. |
| `width` | `int` | Optional | Gets or sets the width. |
| `average_frame_rate` | `float` | Optional | Gets or sets the average frame rate. |
| `real_frame_rate` | `float` | Optional | Gets or sets the real frame rate. |
| `profile` | `string` | Optional | Gets or sets the profile. |
| `mtype` | [`MediaStreamTypeEnum`](../../doc/models/media-stream-type-enum.md) | Optional | Gets or sets the type. |
| `aspect_ratio` | `string` | Optional | Gets or sets the aspect ratio. |
| `index` | `int` | Optional | Gets or sets the index. |
| `score` | `int` | Optional | Gets or sets the score. |
| `is_external` | `bool` | Optional | Gets or sets a value indicating whether this instance is external. |
| `delivery_method` | [`SubtitleDeliveryMethodEnum`](../../doc/models/subtitle-delivery-method-enum.md) | Optional | Gets or sets the method. |
| `delivery_url` | `string` | Optional | Gets or sets the delivery URL. |
| `is_external_url` | `bool` | Optional | Gets or sets a value indicating whether this instance is external URL. |
| `is_text_subtitle_stream` | `bool` | Optional | - |
| `supports_external_stream` | `bool` | Optional | Gets or sets a value indicating whether [supports external stream]. |
| `path` | `string` | Optional | Gets or sets the filename. |
| `pixel_format` | `string` | Optional | Gets or sets the pixel format. |
| `level` | `float` | Optional | Gets or sets the level. |
| `is_anamorphic` | `bool` | Optional | Gets or sets whether this instance is anamorphic. |

## Example (as JSON)

```json
{
  "Codec": null,
  "CodecTag": null,
  "Language": null,
  "ColorRange": null,
  "ColorSpace": null,
  "ColorTransfer": null,
  "ColorPrimaries": null,
  "DvVersionMajor": null,
  "DvVersionMinor": null,
  "DvProfile": null,
  "DvLevel": null,
  "RpuPresentFlag": null,
  "ElPresentFlag": null,
  "BlPresentFlag": null,
  "DvBlSignalCompatibilityId": null,
  "Comment": null,
  "TimeBase": null,
  "CodecTimeBase": null,
  "Title": null,
  "LocalizedUndefined": null,
  "LocalizedDefault": null,
  "LocalizedForced": null,
  "LocalizedExternal": null,
  "NalLengthSize": null,
  "IsInterlaced": null,
  "IsAVC": null,
  "ChannelLayout": null,
  "BitRate": null,
  "BitDepth": null,
  "RefFrames": null,
  "PacketLength": null,
  "Channels": null,
  "SampleRate": null,
  "IsDefault": null,
  "IsForced": null,
  "Height": null,
  "Width": null,
  "AverageFrameRate": null,
  "RealFrameRate": null,
  "Profile": null,
  "Type": null,
  "AspectRatio": null,
  "Index": null,
  "Score": null,
  "IsExternal": null,
  "DeliveryMethod": null,
  "DeliveryUrl": null,
  "IsExternalUrl": null,
  "SupportsExternalStream": null,
  "Path": null,
  "PixelFormat": null,
  "Level": null,
  "IsAnamorphic": null
}
```

