# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DirectPlayProfile(object):

    """Implementation of the 'DirectPlayProfile' model.

    TODO: type model description here.

    Attributes:
        container (string): TODO: type description here.
        audio_codec (string): TODO: type description here.
        video_codec (string): TODO: type description here.
        mtype (DlnaProfileTypeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "container": "Container",
        "audio_codec": "AudioCodec",
        "video_codec": "VideoCodec",
        "mtype": "Type",
    }

    _optionals = [
        "container",
        "audio_codec",
        "video_codec",
        "mtype",
    ]

    _nullables = [
        "container",
        "audio_codec",
        "video_codec",
    ]

    def __init__(
        self,
        container=APIHelper.SKIP,
        audio_codec=APIHelper.SKIP,
        video_codec=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
    ):
        """Constructor for the DirectPlayProfile class"""

        # Initialize members of the class
        if container is not APIHelper.SKIP:
            self.container = container
        if audio_codec is not APIHelper.SKIP:
            self.audio_codec = audio_codec
        if video_codec is not APIHelper.SKIP:
            self.video_codec = video_codec
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype

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

        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        audio_codec = (
            dictionary.get("AudioCodec")
            if "AudioCodec" in dictionary.keys()
            else APIHelper.SKIP
        )
        video_codec = (
            dictionary.get("VideoCodec")
            if "VideoCodec" in dictionary.keys()
            else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        # Return an object of this model
        return cls(container, audio_codec, video_codec, mtype)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)
        audio_codec = XmlUtilities.value_from_xml_element(root.find("AudioCodec"), str)
        video_codec = XmlUtilities.value_from_xml_element(root.find("VideoCodec"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)

        return cls(container, audio_codec, video_codec, mtype)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.audio_codec, "AudioCodec")
        XmlUtilities.add_as_subelement(root, self.video_codec, "VideoCodec")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
