
# Device Profile

A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.
<br />
Specifically, it defines the supported <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
<see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec profiles and levels)
the device is able to direct play (without transcoding or remuxing),
as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to transcode to</see> in case it isn't.

## Structure

`DeviceProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Gets or sets the name of this device profile. |
| `id` | `string` | Optional | Gets or sets the Id. |
| `identification` | [`DeviceIdentification`](../../doc/models/device-identification.md) | Optional | Gets or sets the Identification. |
| `friendly_name` | `string` | Optional | Gets or sets the friendly name of the device profile, which can be shown to users. |
| `manufacturer` | `string` | Optional | Gets or sets the manufacturer of the device which this profile represents. |
| `manufacturer_url` | `string` | Optional | Gets or sets an url for the manufacturer of the device which this profile represents. |
| `model_name` | `string` | Optional | Gets or sets the model name of the device which this profile represents. |
| `model_description` | `string` | Optional | Gets or sets the model description of the device which this profile represents. |
| `model_number` | `string` | Optional | Gets or sets the model number of the device which this profile represents. |
| `model_url` | `string` | Optional | Gets or sets the ModelUrl. |
| `serial_number` | `string` | Optional | Gets or sets the serial number of the device which this profile represents. |
| `enable_album_art_in_didl` | `bool` | Optional | Gets or sets a value indicating whether EnableAlbumArtInDidl.<br>**Default**: `False` |
| `enable_single_album_art_limit` | `bool` | Optional | Gets or sets a value indicating whether EnableSingleAlbumArtLimit.<br>**Default**: `False` |
| `enable_single_subtitle_limit` | `bool` | Optional | Gets or sets a value indicating whether EnableSingleSubtitleLimit.<br>**Default**: `False` |
| `supported_media_types` | `string` | Optional | Gets or sets the SupportedMediaTypes. |
| `user_id` | `string` | Optional | Gets or sets the UserId. |
| `album_art_pn` | `string` | Optional | Gets or sets the AlbumArtPn. |
| `max_album_art_width` | `int` | Optional | Gets or sets the MaxAlbumArtWidth. |
| `max_album_art_height` | `int` | Optional | Gets or sets the MaxAlbumArtHeight. |
| `max_icon_width` | `int` | Optional | Gets or sets the maximum allowed width of embedded icons. |
| `max_icon_height` | `int` | Optional | Gets or sets the maximum allowed height of embedded icons. |
| `max_streaming_bitrate` | `int` | Optional | Gets or sets the maximum allowed bitrate for all streamed content. |
| `max_static_bitrate` | `int` | Optional | Gets or sets the maximum allowed bitrate for statically streamed content (= direct played files). |
| `music_streaming_transcoding_bitrate` | `int` | Optional | Gets or sets the maximum allowed bitrate for transcoded music streams. |
| `max_static_music_bitrate` | `int` | Optional | Gets or sets the maximum allowed bitrate for statically streamed (= direct played) music files. |
| `sony_aggregation_flags` | `string` | Optional | Gets or sets the content of the aggregationFlags element in the urn:schemas-sonycom:av namespace. |
| `protocol_info` | `string` | Optional | Gets or sets the ProtocolInfo. |
| `timeline_offset_seconds` | `int` | Optional | Gets or sets the TimelineOffsetSeconds.<br>**Default**: `0` |
| `requires_plain_video_items` | `bool` | Optional | Gets or sets a value indicating whether RequiresPlainVideoItems.<br>**Default**: `False` |
| `requires_plain_folders` | `bool` | Optional | Gets or sets a value indicating whether RequiresPlainFolders.<br>**Default**: `False` |
| `enable_ms_media_receiver_registrar` | `bool` | Optional | Gets or sets a value indicating whether EnableMSMediaReceiverRegistrar.<br>**Default**: `False` |
| `ignore_transcode_byte_range_requests` | `bool` | Optional | Gets or sets a value indicating whether IgnoreTranscodeByteRangeRequests.<br>**Default**: `False` |
| `xml_root_attributes` | [`List of XmlAttribute`](../../doc/models/xml-attribute.md) | Optional | Gets or sets the XmlRootAttributes. |
| `direct_play_profiles` | [`List of DirectPlayProfile`](../../doc/models/direct-play-profile.md) | Optional | Gets or sets the direct play profiles. |
| `transcoding_profiles` | [`List of TranscodingProfile`](../../doc/models/transcoding-profile.md) | Optional | Gets or sets the transcoding profiles. |
| `container_profiles` | [`List of ContainerProfile`](../../doc/models/container-profile.md) | Optional | Gets or sets the container profiles. |
| `codec_profiles` | [`List of CodecProfile`](../../doc/models/codec-profile.md) | Optional | Gets or sets the codec profiles. |
| `response_profiles` | [`List of ResponseProfile`](../../doc/models/response-profile.md) | Optional | Gets or sets the ResponseProfiles. |
| `subtitle_profiles` | [`List of SubtitleProfile`](../../doc/models/subtitle-profile.md) | Optional | Gets or sets the subtitle profiles. |

## Example (as JSON)

```json
{
  "Name": null,
  "Id": null,
  "Identification": null,
  "FriendlyName": null,
  "Manufacturer": null,
  "ManufacturerUrl": null,
  "ModelName": null,
  "ModelDescription": null,
  "ModelNumber": null,
  "ModelUrl": null,
  "SerialNumber": null,
  "EnableAlbumArtInDidl": null,
  "EnableSingleAlbumArtLimit": null,
  "EnableSingleSubtitleLimit": null,
  "SupportedMediaTypes": null,
  "UserId": null,
  "AlbumArtPn": null,
  "MaxAlbumArtWidth": null,
  "MaxAlbumArtHeight": null,
  "MaxIconWidth": null,
  "MaxIconHeight": null,
  "MaxStreamingBitrate": null,
  "MaxStaticBitrate": null,
  "MusicStreamingTranscodingBitrate": null,
  "MaxStaticMusicBitrate": null,
  "SonyAggregationFlags": null,
  "ProtocolInfo": null,
  "TimelineOffsetSeconds": null,
  "RequiresPlainVideoItems": null,
  "RequiresPlainFolders": null,
  "EnableMSMediaReceiverRegistrar": null,
  "IgnoreTranscodeByteRangeRequests": null,
  "XmlRootAttributes": null,
  "DirectPlayProfiles": null,
  "TranscodingProfiles": null,
  "ContainerProfiles": null,
  "CodecProfiles": null,
  "ResponseProfiles": null,
  "SubtitleProfiles": null
}
```

