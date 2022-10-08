# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.listings_provider_info import ListingsProviderInfo
from jellyfinapi.models.tuner_host_info import TunerHostInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LiveTvOptions(object):

    """Implementation of the 'LiveTvOptions' model.

    TODO: type model description here.

    Attributes:
        guide_days (int): TODO: type description here.
        recording_path (string): TODO: type description here.
        movie_recording_path (string): TODO: type description here.
        series_recording_path (string): TODO: type description here.
        enable_recording_subfolders (bool): TODO: type description here.
        enable_original_audio_with_encoded_recordings (bool): TODO: type
            description here.
        tuner_hosts (list of TunerHostInfo): TODO: type description here.
        listing_providers (list of ListingsProviderInfo): TODO: type
            description here.
        pre_padding_seconds (int): TODO: type description here.
        post_padding_seconds (int): TODO: type description here.
        media_locations_created (list of string): TODO: type description
            here.
        recording_post_processor (string): TODO: type description here.
        recording_post_processor_arguments (string): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "guide_days": "GuideDays",
        "recording_path": "RecordingPath",
        "movie_recording_path": "MovieRecordingPath",
        "series_recording_path": "SeriesRecordingPath",
        "enable_recording_subfolders": "EnableRecordingSubfolders",
        "enable_original_audio_with_encoded_recordings": "EnableOriginalAudioWithEncodedRecordings",
        "tuner_hosts": "TunerHosts",
        "listing_providers": "ListingProviders",
        "pre_padding_seconds": "PrePaddingSeconds",
        "post_padding_seconds": "PostPaddingSeconds",
        "media_locations_created": "MediaLocationsCreated",
        "recording_post_processor": "RecordingPostProcessor",
        "recording_post_processor_arguments": "RecordingPostProcessorArguments",
    }

    _optionals = [
        "guide_days",
        "recording_path",
        "movie_recording_path",
        "series_recording_path",
        "enable_recording_subfolders",
        "enable_original_audio_with_encoded_recordings",
        "tuner_hosts",
        "listing_providers",
        "pre_padding_seconds",
        "post_padding_seconds",
        "media_locations_created",
        "recording_post_processor",
        "recording_post_processor_arguments",
    ]

    _nullables = [
        "guide_days",
        "recording_path",
        "movie_recording_path",
        "series_recording_path",
        "tuner_hosts",
        "listing_providers",
        "media_locations_created",
        "recording_post_processor",
        "recording_post_processor_arguments",
    ]

    def __init__(
        self,
        guide_days=APIHelper.SKIP,
        recording_path=APIHelper.SKIP,
        movie_recording_path=APIHelper.SKIP,
        series_recording_path=APIHelper.SKIP,
        enable_recording_subfolders=APIHelper.SKIP,
        enable_original_audio_with_encoded_recordings=APIHelper.SKIP,
        tuner_hosts=APIHelper.SKIP,
        listing_providers=APIHelper.SKIP,
        pre_padding_seconds=APIHelper.SKIP,
        post_padding_seconds=APIHelper.SKIP,
        media_locations_created=APIHelper.SKIP,
        recording_post_processor=APIHelper.SKIP,
        recording_post_processor_arguments=APIHelper.SKIP,
    ):
        """Constructor for the LiveTvOptions class"""

        # Initialize members of the class
        if guide_days is not APIHelper.SKIP:
            self.guide_days = guide_days
        if recording_path is not APIHelper.SKIP:
            self.recording_path = recording_path
        if movie_recording_path is not APIHelper.SKIP:
            self.movie_recording_path = movie_recording_path
        if series_recording_path is not APIHelper.SKIP:
            self.series_recording_path = series_recording_path
        if enable_recording_subfolders is not APIHelper.SKIP:
            self.enable_recording_subfolders = enable_recording_subfolders
        if enable_original_audio_with_encoded_recordings is not APIHelper.SKIP:
            self.enable_original_audio_with_encoded_recordings = (
                enable_original_audio_with_encoded_recordings
            )
        if tuner_hosts is not APIHelper.SKIP:
            self.tuner_hosts = tuner_hosts
        if listing_providers is not APIHelper.SKIP:
            self.listing_providers = listing_providers
        if pre_padding_seconds is not APIHelper.SKIP:
            self.pre_padding_seconds = pre_padding_seconds
        if post_padding_seconds is not APIHelper.SKIP:
            self.post_padding_seconds = post_padding_seconds
        if media_locations_created is not APIHelper.SKIP:
            self.media_locations_created = media_locations_created
        if recording_post_processor is not APIHelper.SKIP:
            self.recording_post_processor = recording_post_processor
        if recording_post_processor_arguments is not APIHelper.SKIP:
            self.recording_post_processor_arguments = recording_post_processor_arguments

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

        guide_days = (
            dictionary.get("GuideDays")
            if "GuideDays" in dictionary.keys()
            else APIHelper.SKIP
        )
        recording_path = (
            dictionary.get("RecordingPath")
            if "RecordingPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        movie_recording_path = (
            dictionary.get("MovieRecordingPath")
            if "MovieRecordingPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_recording_path = (
            dictionary.get("SeriesRecordingPath")
            if "SeriesRecordingPath" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_recording_subfolders = (
            dictionary.get("EnableRecordingSubfolders")
            if "EnableRecordingSubfolders" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_original_audio_with_encoded_recordings = (
            dictionary.get("EnableOriginalAudioWithEncodedRecordings")
            if "EnableOriginalAudioWithEncodedRecordings" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "TunerHosts" in dictionary.keys():
            tuner_hosts = (
                [TunerHostInfo.from_dictionary(x) for x in dictionary.get("TunerHosts")]
                if dictionary.get("TunerHosts")
                else None
            )
        else:
            tuner_hosts = APIHelper.SKIP
        if "ListingProviders" in dictionary.keys():
            listing_providers = (
                [
                    ListingsProviderInfo.from_dictionary(x)
                    for x in dictionary.get("ListingProviders")
                ]
                if dictionary.get("ListingProviders")
                else None
            )
        else:
            listing_providers = APIHelper.SKIP
        pre_padding_seconds = (
            dictionary.get("PrePaddingSeconds")
            if dictionary.get("PrePaddingSeconds")
            else APIHelper.SKIP
        )
        post_padding_seconds = (
            dictionary.get("PostPaddingSeconds")
            if dictionary.get("PostPaddingSeconds")
            else APIHelper.SKIP
        )
        media_locations_created = (
            dictionary.get("MediaLocationsCreated")
            if "MediaLocationsCreated" in dictionary.keys()
            else APIHelper.SKIP
        )
        recording_post_processor = (
            dictionary.get("RecordingPostProcessor")
            if "RecordingPostProcessor" in dictionary.keys()
            else APIHelper.SKIP
        )
        recording_post_processor_arguments = (
            dictionary.get("RecordingPostProcessorArguments")
            if "RecordingPostProcessorArguments" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            guide_days,
            recording_path,
            movie_recording_path,
            series_recording_path,
            enable_recording_subfolders,
            enable_original_audio_with_encoded_recordings,
            tuner_hosts,
            listing_providers,
            pre_padding_seconds,
            post_padding_seconds,
            media_locations_created,
            recording_post_processor,
            recording_post_processor_arguments,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        guide_days = XmlUtilities.value_from_xml_element(root.find("GuideDays"), int)
        recording_path = XmlUtilities.value_from_xml_element(
            root.find("RecordingPath"), str
        )
        movie_recording_path = XmlUtilities.value_from_xml_element(
            root.find("MovieRecordingPath"), str
        )
        series_recording_path = XmlUtilities.value_from_xml_element(
            root.find("SeriesRecordingPath"), str
        )
        enable_recording_subfolders = XmlUtilities.value_from_xml_element(
            root.find("EnableRecordingSubfolders"), bool
        )
        enable_original_audio_with_encoded_recordings = (
            XmlUtilities.value_from_xml_element(
                root.find("EnableOriginalAudioWithEncodedRecordings"), bool
            )
        )
        tuner_hosts = XmlUtilities.list_from_xml_element(
            root, "TunerHostInfo", TunerHostInfo
        )
        listing_providers = XmlUtilities.list_from_xml_element(
            root, "ListingsProviderInfo", ListingsProviderInfo
        )
        pre_padding_seconds = XmlUtilities.value_from_xml_element(
            root.find("PrePaddingSeconds"), int
        )
        post_padding_seconds = XmlUtilities.value_from_xml_element(
            root.find("PostPaddingSeconds"), int
        )
        media_locations_created = XmlUtilities.list_from_xml_element(
            root, "MediaLocationsCreated", str
        )
        recording_post_processor = XmlUtilities.value_from_xml_element(
            root.find("RecordingPostProcessor"), str
        )
        recording_post_processor_arguments = XmlUtilities.value_from_xml_element(
            root.find("RecordingPostProcessorArguments"), str
        )

        return cls(
            guide_days,
            recording_path,
            movie_recording_path,
            series_recording_path,
            enable_recording_subfolders,
            enable_original_audio_with_encoded_recordings,
            tuner_hosts,
            listing_providers,
            pre_padding_seconds,
            post_padding_seconds,
            media_locations_created,
            recording_post_processor,
            recording_post_processor_arguments,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.guide_days, "GuideDays")
        XmlUtilities.add_as_subelement(root, self.recording_path, "RecordingPath")
        XmlUtilities.add_as_subelement(
            root, self.movie_recording_path, "MovieRecordingPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.series_recording_path, "SeriesRecordingPath"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_recording_subfolders, "EnableRecordingSubfolders"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.enable_original_audio_with_encoded_recordings,
            "EnableOriginalAudioWithEncodedRecordings",
        )
        XmlUtilities.add_list_as_subelement(root, self.tuner_hosts, "TunerHostInfo")
        XmlUtilities.add_list_as_subelement(
            root, self.listing_providers, "ListingsProviderInfo"
        )
        XmlUtilities.add_as_subelement(
            root, self.pre_padding_seconds, "PrePaddingSeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.post_padding_seconds, "PostPaddingSeconds"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.media_locations_created, "MediaLocationsCreated"
        )
        XmlUtilities.add_as_subelement(
            root, self.recording_post_processor, "RecordingPostProcessor"
        )
        XmlUtilities.add_as_subelement(
            root,
            self.recording_post_processor_arguments,
            "RecordingPostProcessorArguments",
        )
