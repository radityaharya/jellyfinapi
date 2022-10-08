# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.profile_condition import ProfileCondition
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ResponseProfile(object):

    """Implementation of the 'ResponseProfile' model.

    TODO: type model description here.

    Attributes:
        container (string): TODO: type description here.
        audio_codec (string): TODO: type description here.
        video_codec (string): TODO: type description here.
        mtype (DlnaProfileTypeEnum): TODO: type description here.
        org_pn (string): TODO: type description here.
        mime_type (string): TODO: type description here.
        conditions (list of ProfileCondition): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "container": "Container",
        "audio_codec": "AudioCodec",
        "video_codec": "VideoCodec",
        "mtype": "Type",
        "org_pn": "OrgPn",
        "mime_type": "MimeType",
        "conditions": "Conditions",
    }

    _optionals = [
        "container",
        "audio_codec",
        "video_codec",
        "mtype",
        "org_pn",
        "mime_type",
        "conditions",
    ]

    _nullables = [
        "container",
        "audio_codec",
        "video_codec",
        "org_pn",
        "mime_type",
        "conditions",
    ]

    def __init__(
        self,
        container=APIHelper.SKIP,
        audio_codec=APIHelper.SKIP,
        video_codec=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        org_pn=APIHelper.SKIP,
        mime_type=APIHelper.SKIP,
        conditions=APIHelper.SKIP,
    ):
        """Constructor for the ResponseProfile class"""

        # Initialize members of the class
        if container is not APIHelper.SKIP:
            self.container = container
        if audio_codec is not APIHelper.SKIP:
            self.audio_codec = audio_codec
        if video_codec is not APIHelper.SKIP:
            self.video_codec = video_codec
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if org_pn is not APIHelper.SKIP:
            self.org_pn = org_pn
        if mime_type is not APIHelper.SKIP:
            self.mime_type = mime_type
        if conditions is not APIHelper.SKIP:
            self.conditions = conditions

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
        org_pn = (
            dictionary.get("OrgPn") if "OrgPn" in dictionary.keys() else APIHelper.SKIP
        )
        mime_type = (
            dictionary.get("MimeType")
            if "MimeType" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "Conditions" in dictionary.keys():
            conditions = (
                [
                    ProfileCondition.from_dictionary(x)
                    for x in dictionary.get("Conditions")
                ]
                if dictionary.get("Conditions")
                else None
            )
        else:
            conditions = APIHelper.SKIP
        # Return an object of this model
        return cls(
            container, audio_codec, video_codec, mtype, org_pn, mime_type, conditions
        )

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
        org_pn = XmlUtilities.value_from_xml_element(root.find("OrgPn"), str)
        mime_type = XmlUtilities.value_from_xml_element(root.find("MimeType"), str)
        conditions = XmlUtilities.list_from_xml_element(
            root, "ProfileCondition", ProfileCondition
        )

        return cls(
            container, audio_codec, video_codec, mtype, org_pn, mime_type, conditions
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.container, "Container")
        XmlUtilities.add_as_subelement(root, self.audio_codec, "AudioCodec")
        XmlUtilities.add_as_subelement(root, self.video_codec, "VideoCodec")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.org_pn, "OrgPn")
        XmlUtilities.add_as_subelement(root, self.mime_type, "MimeType")
        XmlUtilities.add_list_as_subelement(root, self.conditions, "ProfileCondition")
