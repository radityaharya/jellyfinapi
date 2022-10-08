
# Encoding Options

## Structure

`EncodingOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encoding_thread_count` | `int` | Optional | - |
| `transcoding_temp_path` | `string` | Optional | - |
| `fallback_font_path` | `string` | Optional | - |
| `enable_fallback_font` | `bool` | Optional | - |
| `down_mix_audio_boost` | `float` | Optional | - |
| `max_muxing_queue_size` | `int` | Optional | - |
| `enable_throttling` | `bool` | Optional | - |
| `throttle_delay_seconds` | `int` | Optional | - |
| `hardware_acceleration_type` | `string` | Optional | - |
| `encoder_app_path` | `string` | Optional | Gets or sets the FFmpeg path as set by the user via the UI. |
| `encoder_app_path_display` | `string` | Optional | Gets or sets the current FFmpeg path being used by the system and displayed on the transcode page. |
| `vaapi_device` | `string` | Optional | - |
| `enable_tonemapping` | `bool` | Optional | - |
| `enable_vpp_tonemapping` | `bool` | Optional | - |
| `tonemapping_algorithm` | `string` | Optional | - |
| `tonemapping_range` | `string` | Optional | - |
| `tonemapping_desat` | `float` | Optional | - |
| `tonemapping_threshold` | `float` | Optional | - |
| `tonemapping_peak` | `float` | Optional | - |
| `tonemapping_param` | `float` | Optional | - |
| `vpp_tonemapping_brightness` | `float` | Optional | - |
| `vpp_tonemapping_contrast` | `float` | Optional | - |
| `h_264_crf` | `int` | Optional | - |
| `h_265_crf` | `int` | Optional | - |
| `encoder_preset` | `string` | Optional | - |
| `deinterlace_double_rate` | `bool` | Optional | - |
| `deinterlace_method` | `string` | Optional | - |
| `enable_decoding_color_depth_10_hevc` | `bool` | Optional | - |
| `enable_decoding_color_depth_10_vp_9` | `bool` | Optional | - |
| `enable_enhanced_nvdec_decoder` | `bool` | Optional | - |
| `prefer_system_native_hw_decoder` | `bool` | Optional | - |
| `enable_intel_low_power_h_264_hw_encoder` | `bool` | Optional | - |
| `enable_intel_low_power_hevc_hw_encoder` | `bool` | Optional | - |
| `enable_hardware_encoding` | `bool` | Optional | - |
| `allow_hevc_encoding` | `bool` | Optional | - |
| `enable_subtitle_extraction` | `bool` | Optional | - |
| `hardware_decoding_codecs` | `List of string` | Optional | - |
| `allow_on_demand_metadata_based_keyframe_extraction_for_extensions` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "EncodingThreadCount": null,
  "TranscodingTempPath": null,
  "FallbackFontPath": null,
  "EnableFallbackFont": null,
  "DownMixAudioBoost": null,
  "MaxMuxingQueueSize": null,
  "EnableThrottling": null,
  "ThrottleDelaySeconds": null,
  "HardwareAccelerationType": null,
  "EncoderAppPath": null,
  "EncoderAppPathDisplay": null,
  "VaapiDevice": null,
  "EnableTonemapping": null,
  "EnableVppTonemapping": null,
  "TonemappingAlgorithm": null,
  "TonemappingRange": null,
  "TonemappingDesat": null,
  "TonemappingThreshold": null,
  "TonemappingPeak": null,
  "TonemappingParam": null,
  "VppTonemappingBrightness": null,
  "VppTonemappingContrast": null,
  "H264Crf": null,
  "H265Crf": null,
  "EncoderPreset": null,
  "DeinterlaceDoubleRate": null,
  "DeinterlaceMethod": null,
  "EnableDecodingColorDepth10Hevc": null,
  "EnableDecodingColorDepth10Vp9": null,
  "EnableEnhancedNvdecDecoder": null,
  "PreferSystemNativeHwDecoder": null,
  "EnableIntelLowPowerH264HwEncoder": null,
  "EnableIntelLowPowerHevcHwEncoder": null,
  "EnableHardwareEncoding": null,
  "AllowHevcEncoding": null,
  "EnableSubtitleExtraction": null,
  "HardwareDecodingCodecs": null,
  "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions": null
}
```

