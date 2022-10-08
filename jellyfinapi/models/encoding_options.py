# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class EncodingOptions(object):

    """Implementation of the 'EncodingOptions' model.

    TODO: type model description here.

    Attributes:
        encoding_thread_count (int): TODO: type description here.
        transcoding_temp_path (string): TODO: type description here.
        fallback_font_path (string): TODO: type description here.
        enable_fallback_font (bool): TODO: type description here.
        down_mix_audio_boost (float): TODO: type description here.
        max_muxing_queue_size (int): TODO: type description here.
        enable_throttling (bool): TODO: type description here.
        throttle_delay_seconds (int): TODO: type description here.
        hardware_acceleration_type (string): TODO: type description here.
        encoder_app_path (string): Gets or sets the FFmpeg path as set by the
            user via the UI.
        encoder_app_path_display (string): Gets or sets the current FFmpeg
            path being used by the system and displayed on the transcode
            page.
        vaapi_device (string): TODO: type description here.
        enable_tonemapping (bool): TODO: type description here.
        enable_vpp_tonemapping (bool): TODO: type description here.
        tonemapping_algorithm (string): TODO: type description here.
        tonemapping_range (string): TODO: type description here.
        tonemapping_desat (float): TODO: type description here.
        tonemapping_threshold (float): TODO: type description here.
        tonemapping_peak (float): TODO: type description here.
        tonemapping_param (float): TODO: type description here.
        vpp_tonemapping_brightness (float): TODO: type description here.
        vpp_tonemapping_contrast (float): TODO: type description here.
        h_264_crf (int): TODO: type description here.
        h_265_crf (int): TODO: type description here.
        encoder_preset (string): TODO: type description here.
        deinterlace_double_rate (bool): TODO: type description here.
        deinterlace_method (string): TODO: type description here.
        enable_decoding_color_depth_10_hevc (bool): TODO: type description
            here.
        enable_decoding_color_depth_10_vp_9 (bool): TODO: type description
            here.
        enable_enhanced_nvdec_decoder (bool): TODO: type description here.
        prefer_system_native_hw_decoder (bool): TODO: type description here.
        enable_intel_low_power_h_264_hw_encoder (bool): TODO: type description
            here.
        enable_intel_low_power_hevc_hw_encoder (bool): TODO: type description
            here.
        enable_hardware_encoding (bool): TODO: type description here.
        allow_hevc_encoding (bool): TODO: type description here.
        enable_subtitle_extraction (bool): TODO: type description here.
        hardware_decoding_codecs (list of string): TODO: type description
            here.
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "encoding_thread_count": "EncodingThreadCount",
        "transcoding_temp_path": "TranscodingTempPath",
        "fallback_font_path": "FallbackFontPath",
        "enable_fallback_font": "EnableFallbackFont",
        "down_mix_audio_boost": "DownMixAudioBoost",
        "max_muxing_queue_size": "MaxMuxingQueueSize",
        "enable_throttling": "EnableThrottling",
        "throttle_delay_seconds": "ThrottleDelaySeconds",
        "hardware_acceleration_type": "HardwareAccelerationType",
        "encoder_app_path": "EncoderAppPath",
        "encoder_app_path_display": "EncoderAppPathDisplay",
        "vaapi_device": "VaapiDevice",
        "enable_tonemapping": "EnableTonemapping",
        "enable_vpp_tonemapping": "EnableVppTonemapping",
        "tonemapping_algorithm": "TonemappingAlgorithm",
        "tonemapping_range": "TonemappingRange",
        "tonemapping_desat": "TonemappingDesat",
        "tonemapping_threshold": "TonemappingThreshold",
        "tonemapping_peak": "TonemappingPeak",
        "tonemapping_param": "TonemappingParam",
        "vpp_tonemapping_brightness": "VppTonemappingBrightness",
        "vpp_tonemapping_contrast": "VppTonemappingContrast",
        "h_264_crf": "H264Crf",
        "h_265_crf": "H265Crf",
        "encoder_preset": "EncoderPreset",
        "deinterlace_double_rate": "DeinterlaceDoubleRate",
        "deinterlace_method": "DeinterlaceMethod",
        "enable_decoding_color_depth_10_hevc": "EnableDecodingColorDepth10Hevc",
        "enable_decoding_color_depth_10_vp_9": "EnableDecodingColorDepth10Vp9",
        "enable_enhanced_nvdec_decoder": "EnableEnhancedNvdecDecoder",
        "prefer_system_native_hw_decoder": "PreferSystemNativeHwDecoder",
        "enable_intel_low_power_h_264_hw_encoder": "EnableIntelLowPowerH264HwEncoder",
        "enable_intel_low_power_hevc_hw_encoder": "EnableIntelLowPowerHevcHwEncoder",
        "enable_hardware_encoding": "EnableHardwareEncoding",
        "allow_hevc_encoding": "AllowHevcEncoding",
        "enable_subtitle_extraction": "EnableSubtitleExtraction",
        "hardware_decoding_codecs": "HardwareDecodingCodecs",
        "allow_on_demand_metadata_based_keyframe_extraction_for_extensions": "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions",
    }

    _optionals = [
        "encoding_thread_count",
        "transcoding_temp_path",
        "fallback_font_path",
        "enable_fallback_font",
        "down_mix_audio_boost",
        "max_muxing_queue_size",
        "enable_throttling",
        "throttle_delay_seconds",
        "hardware_acceleration_type",
        "encoder_app_path",
        "encoder_app_path_display",
        "vaapi_device",
        "enable_tonemapping",
        "enable_vpp_tonemapping",
        "tonemapping_algorithm",
        "tonemapping_range",
        "tonemapping_desat",
        "tonemapping_threshold",
        "tonemapping_peak",
        "tonemapping_param",
        "vpp_tonemapping_brightness",
        "vpp_tonemapping_contrast",
        "h_264_crf",
        "h_265_crf",
        "encoder_preset",
        "deinterlace_double_rate",
        "deinterlace_method",
        "enable_decoding_color_depth_10_hevc",
        "enable_decoding_color_depth_10_vp_9",
        "enable_enhanced_nvdec_decoder",
        "prefer_system_native_hw_decoder",
        "enable_intel_low_power_h_264_hw_encoder",
        "enable_intel_low_power_hevc_hw_encoder",
        "enable_hardware_encoding",
        "allow_hevc_encoding",
        "enable_subtitle_extraction",
        "hardware_decoding_codecs",
        "allow_on_demand_metadata_based_keyframe_extraction_for_extensions",
    ]

    _nullables = [
        "transcoding_temp_path",
        "fallback_font_path",
        "hardware_acceleration_type",
        "encoder_app_path",
        "encoder_app_path_display",
        "vaapi_device",
        "tonemapping_algorithm",
        "tonemapping_range",
        "encoder_preset",
        "deinterlace_method",
        "hardware_decoding_codecs",
        "allow_on_demand_metadata_based_keyframe_extraction_for_extensions",
    ]

    def __init__(
        self,
        encoding_thread_count=APIHelper.SKIP,
        transcoding_temp_path=APIHelper.SKIP,
        fallback_font_path=APIHelper.SKIP,
        enable_fallback_font=APIHelper.SKIP,
        down_mix_audio_boost=APIHelper.SKIP,
        max_muxing_queue_size=APIHelper.SKIP,
        enable_throttling=APIHelper.SKIP,
        throttle_delay_seconds=APIHelper.SKIP,
        hardware_acceleration_type=APIHelper.SKIP,
        encoder_app_path=APIHelper.SKIP,
        encoder_app_path_display=APIHelper.SKIP,
        vaapi_device=APIHelper.SKIP,
        enable_tonemapping=APIHelper.SKIP,
        enable_vpp_tonemapping=APIHelper.SKIP,
        tonemapping_algorithm=APIHelper.SKIP,
        tonemapping_range=APIHelper.SKIP,
        tonemapping_desat=APIHelper.SKIP,
        tonemapping_threshold=APIHelper.SKIP,
        tonemapping_peak=APIHelper.SKIP,
        tonemapping_param=APIHelper.SKIP,
        vpp_tonemapping_brightness=APIHelper.SKIP,
        vpp_tonemapping_contrast=APIHelper.SKIP,
        h_264_crf=APIHelper.SKIP,
        h_265_crf=APIHelper.SKIP,
        encoder_preset=APIHelper.SKIP,
        deinterlace_double_rate=APIHelper.SKIP,
        deinterlace_method=APIHelper.SKIP,
        enable_decoding_color_depth_10_hevc=APIHelper.SKIP,
        enable_decoding_color_depth_10_vp_9=APIHelper.SKIP,
        enable_enhanced_nvdec_decoder=APIHelper.SKIP,
        prefer_system_native_hw_decoder=APIHelper.SKIP,
        enable_intel_low_power_h_264_hw_encoder=APIHelper.SKIP,
        enable_intel_low_power_hevc_hw_encoder=APIHelper.SKIP,
        enable_hardware_encoding=APIHelper.SKIP,
        allow_hevc_encoding=APIHelper.SKIP,
        enable_subtitle_extraction=APIHelper.SKIP,
        hardware_decoding_codecs=APIHelper.SKIP,
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions=APIHelper.SKIP,
    ):
        """Constructor for the EncodingOptions class"""

        # Initialize members of the class
        if encoding_thread_count is not APIHelper.SKIP:
            self.encoding_thread_count = encoding_thread_count
        if transcoding_temp_path is not APIHelper.SKIP:
            self.transcoding_temp_path = transcoding_temp_path
        if fallback_font_path is not APIHelper.SKIP:
            self.fallback_font_path = fallback_font_path
        if enable_fallback_font is not APIHelper.SKIP:
            self.enable_fallback_font = enable_fallback_font
        if down_mix_audio_boost is not APIHelper.SKIP:
            self.down_mix_audio_boost = down_mix_audio_boost
        if max_muxing_queue_size is not APIHelper.SKIP:
            self.max_muxing_queue_size = max_muxing_queue_size
        if enable_throttling is not APIHelper.SKIP:
            self.enable_throttling = enable_throttling
        if throttle_delay_seconds is not APIHelper.SKIP:
            self.throttle_delay_seconds = throttle_delay_seconds
        if hardware_acceleration_type is not APIHelper.SKIP:
            self.hardware_acceleration_type = hardware_acceleration_type
        if encoder_app_path is not APIHelper.SKIP:
            self.encoder_app_path = encoder_app_path
        if encoder_app_path_display is not APIHelper.SKIP:
            self.encoder_app_path_display = encoder_app_path_display
        if vaapi_device is not APIHelper.SKIP:
            self.vaapi_device = vaapi_device
        if enable_tonemapping is not APIHelper.SKIP:
            self.enable_tonemapping = enable_tonemapping
        if enable_vpp_tonemapping is not APIHelper.SKIP:
            self.enable_vpp_tonemapping = enable_vpp_tonemapping
        if tonemapping_algorithm is not APIHelper.SKIP:
            self.tonemapping_algorithm = tonemapping_algorithm
        if tonemapping_range is not APIHelper.SKIP:
            self.tonemapping_range = tonemapping_range
        if tonemapping_desat is not APIHelper.SKIP:
            self.tonemapping_desat = tonemapping_desat
        if tonemapping_threshold is not APIHelper.SKIP:
            self.tonemapping_threshold = tonemapping_threshold
        if tonemapping_peak is not APIHelper.SKIP:
            self.tonemapping_peak = tonemapping_peak
        if tonemapping_param is not APIHelper.SKIP:
            self.tonemapping_param = tonemapping_param
        if vpp_tonemapping_brightness is not APIHelper.SKIP:
            self.vpp_tonemapping_brightness = vpp_tonemapping_brightness
        if vpp_tonemapping_contrast is not APIHelper.SKIP:
            self.vpp_tonemapping_contrast = vpp_tonemapping_contrast
        if h_264_crf is not APIHelper.SKIP:
            self.h_264_crf = h_264_crf
        if h_265_crf is not APIHelper.SKIP:
            self.h_265_crf = h_265_crf
        if encoder_preset is not APIHelper.SKIP:
            self.encoder_preset = encoder_preset
        if deinterlace_double_rate is not APIHelper.SKIP:
            self.deinterlace_double_rate = deinterlace_double_rate
        if deinterlace_method is not APIHelper.SKIP:
            self.deinterlace_method = deinterlace_method
        if enable_decoding_color_depth_10_hevc is not APIHelper.SKIP:
            self.enable_decoding_color_depth_10_hevc = (
                enable_decoding_color_depth_10_hevc
            )
        if enable_decoding_color_depth_10_vp_9 is not APIHelper.SKIP:
            self.enable_decoding_color_depth_10_vp_9 = (
                enable_decoding_color_depth_10_vp_9
            )
        if enable_enhanced_nvdec_decoder is not APIHelper.SKIP:
            self.enable_enhanced_nvdec_decoder = enable_enhanced_nvdec_decoder
        if prefer_system_native_hw_decoder is not APIHelper.SKIP:
            self.prefer_system_native_hw_decoder = prefer_system_native_hw_decoder
        if enable_intel_low_power_h_264_hw_encoder is not APIHelper.SKIP:
            self.enable_intel_low_power_h_264_hw_encoder = (
                enable_intel_low_power_h_264_hw_encoder
            )
        if enable_intel_low_power_hevc_hw_encoder is not APIHelper.SKIP:
            self.enable_intel_low_power_hevc_hw_encoder = (
                enable_intel_low_power_hevc_hw_encoder
            )
        if enable_hardware_encoding is not APIHelper.SKIP:
            self.enable_hardware_encoding = enable_hardware_encoding
        if allow_hevc_encoding is not APIHelper.SKIP:
            self.allow_hevc_encoding = allow_hevc_encoding
        if enable_subtitle_extraction is not APIHelper.SKIP:
            self.enable_subtitle_extraction = enable_subtitle_extraction
        if hardware_decoding_codecs is not APIHelper.SKIP:
            self.hardware_decoding_codecs = hardware_decoding_codecs
        if (
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            is not APIHelper.SKIP
        ):
            self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
                allow_on_demand_metadata_based_keyframe_extraction_for_extensions
            )

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        encoding_thread_count = (
            dictionary.get("EncodingThreadCount")
            if dictionary.get("EncodingThreadCount")
            else APIHelper.SKIP
        )
        transcoding_temp_path = (
            dictionary.get("TranscodingTempPath")
            if "TranscodingTempPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        fallback_font_path = (
            dictionary.get("FallbackFontPath")
            if "FallbackFontPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_fallback_font = (
            dictionary.get("EnableFallbackFont")
            if "EnableFallbackFont" in dictionary.keys()
            else APIHelper.SKIP
        )
        down_mix_audio_boost = (
            dictionary.get("DownMixAudioBoost")
            if dictionary.get("DownMixAudioBoost")
            else APIHelper.SKIP
        )
        max_muxing_queue_size = (
            dictionary.get("MaxMuxingQueueSize")
            if dictionary.get("MaxMuxingQueueSize")
            else APIHelper.SKIP
        )
        enable_throttling = (
            dictionary.get("EnableThrottling")
            if "EnableThrottling" in dictionary.keys()
            else APIHelper.SKIP
        )
        throttle_delay_seconds = (
            dictionary.get("ThrottleDelaySeconds")
            if dictionary.get("ThrottleDelaySeconds")
            else APIHelper.SKIP
        )
        hardware_acceleration_type = (
            dictionary.get("HardwareAccelerationType")
            if "HardwareAccelerationType" in dictionary.keys()
            else APIHelper.SKIP
        )
        encoder_app_path = (
            dictionary.get("EncoderAppPath")
            if "EncoderAppPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        encoder_app_path_display = (
            dictionary.get("EncoderAppPathDisplay")
            if "EncoderAppPathDisplay" in dictionary.keys()
            else APIHelper.SKIP
        )
        vaapi_device = (
            dictionary.get("VaapiDevice")
            if "VaapiDevice" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_tonemapping = (
            dictionary.get("EnableTonemapping")
            if "EnableTonemapping" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_vpp_tonemapping = (
            dictionary.get("EnableVppTonemapping")
            if "EnableVppTonemapping" in dictionary.keys()
            else APIHelper.SKIP
        )
        tonemapping_algorithm = (
            dictionary.get("TonemappingAlgorithm")
            if "TonemappingAlgorithm" in dictionary.keys()
            else APIHelper.SKIP
        )
        tonemapping_range = (
            dictionary.get("TonemappingRange")
            if "TonemappingRange" in dictionary.keys()
            else APIHelper.SKIP
        )
        tonemapping_desat = (
            dictionary.get("TonemappingDesat")
            if dictionary.get("TonemappingDesat")
            else APIHelper.SKIP
        )
        tonemapping_threshold = (
            dictionary.get("TonemappingThreshold")
            if dictionary.get("TonemappingThreshold")
            else APIHelper.SKIP
        )
        tonemapping_peak = (
            dictionary.get("TonemappingPeak")
            if dictionary.get("TonemappingPeak")
            else APIHelper.SKIP
        )
        tonemapping_param = (
            dictionary.get("TonemappingParam")
            if dictionary.get("TonemappingParam")
            else APIHelper.SKIP
        )
        vpp_tonemapping_brightness = (
            dictionary.get("VppTonemappingBrightness")
            if dictionary.get("VppTonemappingBrightness")
            else APIHelper.SKIP
        )
        vpp_tonemapping_contrast = (
            dictionary.get("VppTonemappingContrast")
            if dictionary.get("VppTonemappingContrast")
            else APIHelper.SKIP
        )
        h_264_crf = (
            dictionary.get("H264Crf") if dictionary.get("H264Crf") else APIHelper.SKIP
        )
        h_265_crf = (
            dictionary.get("H265Crf") if dictionary.get("H265Crf") else APIHelper.SKIP
        )
        encoder_preset = (
            dictionary.get("EncoderPreset")
            if "EncoderPreset" in dictionary.keys()
            else APIHelper.SKIP
        )
        deinterlace_double_rate = (
            dictionary.get("DeinterlaceDoubleRate")
            if "DeinterlaceDoubleRate" in dictionary.keys()
            else APIHelper.SKIP
        )
        deinterlace_method = (
            dictionary.get("DeinterlaceMethod")
            if "DeinterlaceMethod" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_decoding_color_depth_10_hevc = (
            dictionary.get("EnableDecodingColorDepth10Hevc")
            if "EnableDecodingColorDepth10Hevc" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_decoding_color_depth_10_vp_9 = (
            dictionary.get("EnableDecodingColorDepth10Vp9")
            if "EnableDecodingColorDepth10Vp9" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_enhanced_nvdec_decoder = (
            dictionary.get("EnableEnhancedNvdecDecoder")
            if "EnableEnhancedNvdecDecoder" in dictionary.keys()
            else APIHelper.SKIP
        )
        prefer_system_native_hw_decoder = (
            dictionary.get("PreferSystemNativeHwDecoder")
            if "PreferSystemNativeHwDecoder" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_intel_low_power_h_264_hw_encoder = (
            dictionary.get("EnableIntelLowPowerH264HwEncoder")
            if "EnableIntelLowPowerH264HwEncoder" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_intel_low_power_hevc_hw_encoder = (
            dictionary.get("EnableIntelLowPowerHevcHwEncoder")
            if "EnableIntelLowPowerHevcHwEncoder" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_hardware_encoding = (
            dictionary.get("EnableHardwareEncoding")
            if "EnableHardwareEncoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_hevc_encoding = (
            dictionary.get("AllowHevcEncoding")
            if "AllowHevcEncoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_subtitle_extraction = (
            dictionary.get("EnableSubtitleExtraction")
            if "EnableSubtitleExtraction" in dictionary.keys()
            else APIHelper.SKIP
        )
        hardware_decoding_codecs = (
            dictionary.get("HardwareDecodingCodecs")
            if "HardwareDecodingCodecs" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
            dictionary.get("AllowOnDemandMetadataBasedKeyframeExtractionForExtensions")
            if "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions"
            in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            encoding_thread_count,
            transcoding_temp_path,
            fallback_font_path,
            enable_fallback_font,
            down_mix_audio_boost,
            max_muxing_queue_size,
            enable_throttling,
            throttle_delay_seconds,
            hardware_acceleration_type,
            encoder_app_path,
            encoder_app_path_display,
            vaapi_device,
            enable_tonemapping,
            enable_vpp_tonemapping,
            tonemapping_algorithm,
            tonemapping_range,
            tonemapping_desat,
            tonemapping_threshold,
            tonemapping_peak,
            tonemapping_param,
            vpp_tonemapping_brightness,
            vpp_tonemapping_contrast,
            h_264_crf,
            h_265_crf,
            encoder_preset,
            deinterlace_double_rate,
            deinterlace_method,
            enable_decoding_color_depth_10_hevc,
            enable_decoding_color_depth_10_vp_9,
            enable_enhanced_nvdec_decoder,
            prefer_system_native_hw_decoder,
            enable_intel_low_power_h_264_hw_encoder,
            enable_intel_low_power_hevc_hw_encoder,
            enable_hardware_encoding,
            allow_hevc_encoding,
            enable_subtitle_extraction,
            hardware_decoding_codecs,
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        encoding_thread_count = XmlUtilities.value_from_xml_element(
            root.find("EncodingThreadCount"), int
        )
        transcoding_temp_path = XmlUtilities.value_from_xml_element(
            root.find("TranscodingTempPath"), str
        )
        fallback_font_path = XmlUtilities.value_from_xml_element(
            root.find("FallbackFontPath"), str
        )
        enable_fallback_font = XmlUtilities.value_from_xml_element(
            root.find("EnableFallbackFont"), bool
        )
        down_mix_audio_boost = XmlUtilities.value_from_xml_element(
            root.find("DownMixAudioBoost"), float
        )
        max_muxing_queue_size = XmlUtilities.value_from_xml_element(
            root.find("MaxMuxingQueueSize"), int
        )
        enable_throttling = XmlUtilities.value_from_xml_element(
            root.find("EnableThrottling"), bool
        )
        throttle_delay_seconds = XmlUtilities.value_from_xml_element(
            root.find("ThrottleDelaySeconds"), int
        )
        hardware_acceleration_type = XmlUtilities.value_from_xml_element(
            root.find("HardwareAccelerationType"), str
        )
        encoder_app_path = XmlUtilities.value_from_xml_element(
            root.find("EncoderAppPath"), str
        )
        encoder_app_path_display = XmlUtilities.value_from_xml_element(
            root.find("EncoderAppPathDisplay"), str
        )
        vaapi_device = XmlUtilities.value_from_xml_element(
            root.find("VaapiDevice"), str
        )
        enable_tonemapping = XmlUtilities.value_from_xml_element(
            root.find("EnableTonemapping"), bool
        )
        enable_vpp_tonemapping = XmlUtilities.value_from_xml_element(
            root.find("EnableVppTonemapping"), bool
        )
        tonemapping_algorithm = XmlUtilities.value_from_xml_element(
            root.find("TonemappingAlgorithm"), str
        )
        tonemapping_range = XmlUtilities.value_from_xml_element(
            root.find("TonemappingRange"), str
        )
        tonemapping_desat = XmlUtilities.value_from_xml_element(
            root.find("TonemappingDesat"), float
        )
        tonemapping_threshold = XmlUtilities.value_from_xml_element(
            root.find("TonemappingThreshold"), float
        )
        tonemapping_peak = XmlUtilities.value_from_xml_element(
            root.find("TonemappingPeak"), float
        )
        tonemapping_param = XmlUtilities.value_from_xml_element(
            root.find("TonemappingParam"), float
        )
        vpp_tonemapping_brightness = XmlUtilities.value_from_xml_element(
            root.find("VppTonemappingBrightness"), float
        )
        vpp_tonemapping_contrast = XmlUtilities.value_from_xml_element(
            root.find("VppTonemappingContrast"), float
        )
        h_264_crf = XmlUtilities.value_from_xml_element(root.find("H264Crf"), int)
        h_265_crf = XmlUtilities.value_from_xml_element(root.find("H265Crf"), int)
        encoder_preset = XmlUtilities.value_from_xml_element(
            root.find("EncoderPreset"), str
        )
        deinterlace_double_rate = XmlUtilities.value_from_xml_element(
            root.find("DeinterlaceDoubleRate"), bool
        )
        deinterlace_method = XmlUtilities.value_from_xml_element(
            root.find("DeinterlaceMethod"), str
        )
        enable_decoding_color_depth_10_hevc = XmlUtilities.value_from_xml_element(
            root.find("EnableDecodingColorDepth10Hevc"), bool
        )
        enable_decoding_color_depth_10_vp_9 = XmlUtilities.value_from_xml_element(
            root.find("EnableDecodingColorDepth10Vp9"), bool
        )
        enable_enhanced_nvdec_decoder = XmlUtilities.value_from_xml_element(
            root.find("EnableEnhancedNvdecDecoder"), bool
        )
        prefer_system_native_hw_decoder = XmlUtilities.value_from_xml_element(
            root.find("PreferSystemNativeHwDecoder"), bool
        )
        enable_intel_low_power_h_264_hw_encoder = XmlUtilities.value_from_xml_element(
            root.find("EnableIntelLowPowerH264HwEncoder"), bool
        )
        enable_intel_low_power_hevc_hw_encoder = XmlUtilities.value_from_xml_element(
            root.find("EnableIntelLowPowerHevcHwEncoder"), bool
        )
        enable_hardware_encoding = XmlUtilities.value_from_xml_element(
            root.find("EnableHardwareEncoding"), bool
        )
        allow_hevc_encoding = XmlUtilities.value_from_xml_element(
            root.find("AllowHevcEncoding"), bool
        )
        enable_subtitle_extraction = XmlUtilities.value_from_xml_element(
            root.find("EnableSubtitleExtraction"), bool
        )
        hardware_decoding_codecs = XmlUtilities.list_from_xml_element(
            root, "HardwareDecodingCodecs", str
        )
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions = (
            XmlUtilities.list_from_xml_element(
                root, "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions", str
            )
        )

        return cls(
            encoding_thread_count,
            transcoding_temp_path,
            fallback_font_path,
            enable_fallback_font,
            down_mix_audio_boost,
            max_muxing_queue_size,
            enable_throttling,
            throttle_delay_seconds,
            hardware_acceleration_type,
            encoder_app_path,
            encoder_app_path_display,
            vaapi_device,
            enable_tonemapping,
            enable_vpp_tonemapping,
            tonemapping_algorithm,
            tonemapping_range,
            tonemapping_desat,
            tonemapping_threshold,
            tonemapping_peak,
            tonemapping_param,
            vpp_tonemapping_brightness,
            vpp_tonemapping_contrast,
            h_264_crf,
            h_265_crf,
            encoder_preset,
            deinterlace_double_rate,
            deinterlace_method,
            enable_decoding_color_depth_10_hevc,
            enable_decoding_color_depth_10_vp_9,
            enable_enhanced_nvdec_decoder,
            prefer_system_native_hw_decoder,
            enable_intel_low_power_h_264_hw_encoder,
            enable_intel_low_power_hevc_hw_encoder,
            enable_hardware_encoding,
            allow_hevc_encoding,
            enable_subtitle_extraction,
            hardware_decoding_codecs,
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.encoding_thread_count, "EncodingThreadCount"
        )
        XmlUtilities.add_as_subelement(
            root, self.transcoding_temp_path, "TranscodingTempPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.fallback_font_path, "FallbackFontPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_fallback_font, "EnableFallbackFont"
        )
        XmlUtilities.add_as_subelement(
            root, self.down_mix_audio_boost, "DownMixAudioBoost"
        )
        XmlUtilities.add_as_subelement(
            root, self.max_muxing_queue_size, "MaxMuxingQueueSize"
        )
        XmlUtilities.add_as_subelement(root, self.enable_throttling, "EnableThrottling")
        XmlUtilities.add_as_subelement(
            root, self.throttle_delay_seconds, "ThrottleDelaySeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.hardware_acceleration_type, "HardwareAccelerationType"
        )
        XmlUtilities.add_as_subelement(root, self.encoder_app_path, "EncoderAppPath")
        XmlUtilities.add_as_subelement(
            root, self.encoder_app_path_display, "EncoderAppPathDisplay"
        )
        XmlUtilities.add_as_subelement(root, self.vaapi_device, "VaapiDevice")
        XmlUtilities.add_as_subelement(
            root, self.enable_tonemapping, "EnableTonemapping"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_vpp_tonemapping, "EnableVppTonemapping"
        )
        XmlUtilities.add_as_subelement(
            root, self.tonemapping_algorithm, "TonemappingAlgorithm"
        )
        XmlUtilities.add_as_subelement(root, self.tonemapping_range, "TonemappingRange")
        XmlUtilities.add_as_subelement(root, self.tonemapping_desat, "TonemappingDesat")
        XmlUtilities.add_as_subelement(
            root, self.tonemapping_threshold, "TonemappingThreshold"
        )
        XmlUtilities.add_as_subelement(root, self.tonemapping_peak, "TonemappingPeak")
        XmlUtilities.add_as_subelement(root, self.tonemapping_param, "TonemappingParam")
        XmlUtilities.add_as_subelement(
            root, self.vpp_tonemapping_brightness, "VppTonemappingBrightness"
        )
        XmlUtilities.add_as_subelement(
            root, self.vpp_tonemapping_contrast, "VppTonemappingContrast"
        )
        XmlUtilities.add_as_subelement(root, self.h_264_crf, "H264Crf")
        XmlUtilities.add_as_subelement(root, self.h_265_crf, "H265Crf")
        XmlUtilities.add_as_subelement(root, self.encoder_preset, "EncoderPreset")
        XmlUtilities.add_as_subelement(
            root, self.deinterlace_double_rate, "DeinterlaceDoubleRate"
        )
        XmlUtilities.add_as_subelement(
            root, self.deinterlace_method, "DeinterlaceMethod"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_decoding_color_depth_10_hevc,
            "EnableDecodingColorDepth10Hevc",
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_decoding_color_depth_10_vp_9,
            "EnableDecodingColorDepth10Vp9",
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_enhanced_nvdec_decoder, "EnableEnhancedNvdecDecoder"
        )
        XmlUtilities.add_as_subelement(
            root, self.prefer_system_native_hw_decoder, "PreferSystemNativeHwDecoder"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_intel_low_power_h_264_hw_encoder,
            "EnableIntelLowPowerH264HwEncoder",
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_intel_low_power_hevc_hw_encoder,
            "EnableIntelLowPowerHevcHwEncoder",
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_hardware_encoding, "EnableHardwareEncoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_hevc_encoding, "AllowHevcEncoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_subtitle_extraction, "EnableSubtitleExtraction"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.hardware_decoding_codecs, "HardwareDecodingCodecs"
        )
        XmlUtilities.add_list_as_subelement(
            root,
            self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
            "AllowOnDemandMetadataBasedKeyframeExtractionForExtensions",
        )
