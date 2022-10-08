# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TunerHostInfo(object):

    """Implementation of the 'TunerHostInfo' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        url (string): TODO: type description here.
        mtype (string): TODO: type description here.
        device_id (string): TODO: type description here.
        friendly_name (string): TODO: type description here.
        import_favorites_only (bool): TODO: type description here.
        allow_hw_transcoding (bool): TODO: type description here.
        enable_stream_looping (bool): TODO: type description here.
        source (string): TODO: type description here.
        tuner_count (int): TODO: type description here.
        user_agent (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "url": "Url",
        "mtype": "Type",
        "device_id": "DeviceId",
        "friendly_name": "FriendlyName",
        "import_favorites_only": "ImportFavoritesOnly",
        "allow_hw_transcoding": "AllowHWTranscoding",
        "enable_stream_looping": "EnableStreamLooping",
        "source": "Source",
        "tuner_count": "TunerCount",
        "user_agent": "UserAgent",
    }

    _optionals = [
        "id",
        "url",
        "mtype",
        "device_id",
        "friendly_name",
        "import_favorites_only",
        "allow_hw_transcoding",
        "enable_stream_looping",
        "source",
        "tuner_count",
        "user_agent",
    ]

    _nullables = [
        "id",
        "url",
        "mtype",
        "device_id",
        "friendly_name",
        "source",
        "user_agent",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        url=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        device_id=APIHelper.SKIP,
        friendly_name=APIHelper.SKIP,
        import_favorites_only=APIHelper.SKIP,
        allow_hw_transcoding=APIHelper.SKIP,
        enable_stream_looping=APIHelper.SKIP,
        source=APIHelper.SKIP,
        tuner_count=APIHelper.SKIP,
        user_agent=APIHelper.SKIP,
    ):
        """Constructor for the TunerHostInfo class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if url is not APIHelper.SKIP:
            self.url = url
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id
        if friendly_name is not APIHelper.SKIP:
            self.friendly_name = friendly_name
        if import_favorites_only is not APIHelper.SKIP:
            self.import_favorites_only = import_favorites_only
        if allow_hw_transcoding is not APIHelper.SKIP:
            self.allow_hw_transcoding = allow_hw_transcoding
        if enable_stream_looping is not APIHelper.SKIP:
            self.enable_stream_looping = enable_stream_looping
        if source is not APIHelper.SKIP:
            self.source = source
        if tuner_count is not APIHelper.SKIP:
            self.tuner_count = tuner_count
        if user_agent is not APIHelper.SKIP:
            self.user_agent = user_agent

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

        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        url = dictionary.get("Url") if "Url" in dictionary.keys() else APIHelper.SKIP
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        device_id = (
            dictionary.get("DeviceId")
            if "DeviceId" in dictionary.keys()
            else APIHelper.SKIP
        )
        friendly_name = (
            dictionary.get("FriendlyName")
            if "FriendlyName" in dictionary.keys()
            else APIHelper.SKIP
        )
        import_favorites_only = (
            dictionary.get("ImportFavoritesOnly")
            if "ImportFavoritesOnly" in dictionary.keys()
            else APIHelper.SKIP
        )
        allow_hw_transcoding = (
            dictionary.get("AllowHWTranscoding")
            if "AllowHWTranscoding" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_stream_looping = (
            dictionary.get("EnableStreamLooping")
            if "EnableStreamLooping" in dictionary.keys()
            else APIHelper.SKIP
        )
        source = (
            dictionary.get("Source")
            if "Source" in dictionary.keys()
            else APIHelper.SKIP
        )
        tuner_count = (
            dictionary.get("TunerCount")
            if dictionary.get("TunerCount")
            else APIHelper.SKIP
        )
        user_agent = (
            dictionary.get("UserAgent")
            if "UserAgent" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            url,
            mtype,
            device_id,
            friendly_name,
            import_favorites_only,
            allow_hw_transcoding,
            enable_stream_looping,
            source,
            tuner_count,
            user_agent,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        url = XmlUtilities.value_from_xml_element(root.find("Url"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        device_id = XmlUtilities.value_from_xml_element(root.find("DeviceId"), str)
        friendly_name = XmlUtilities.value_from_xml_element(
            root.find("FriendlyName"), str
        )
        import_favorites_only = XmlUtilities.value_from_xml_element(
            root.find("ImportFavoritesOnly"), bool
        )
        allow_hw_transcoding = XmlUtilities.value_from_xml_element(
            root.find("AllowHWTranscoding"), bool
        )
        enable_stream_looping = XmlUtilities.value_from_xml_element(
            root.find("EnableStreamLooping"), bool
        )
        source = XmlUtilities.value_from_xml_element(root.find("Source"), str)
        tuner_count = XmlUtilities.value_from_xml_element(root.find("TunerCount"), int)
        user_agent = XmlUtilities.value_from_xml_element(root.find("UserAgent"), str)

        return cls(
            id,
            url,
            mtype,
            device_id,
            friendly_name,
            import_favorites_only,
            allow_hw_transcoding,
            enable_stream_looping,
            source,
            tuner_count,
            user_agent,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.url, "Url")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.device_id, "DeviceId")
        XmlUtilities.add_as_subelement(root, self.friendly_name, "FriendlyName")
        XmlUtilities.add_as_subelement(
            root, self.import_favorites_only, "ImportFavoritesOnly"
        )
        XmlUtilities.add_as_subelement(
            root, self.allow_hw_transcoding, "AllowHWTranscoding"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_stream_looping, "EnableStreamLooping"
        )
        XmlUtilities.add_as_subelement(root, self.source, "Source")
        XmlUtilities.add_as_subelement(root, self.tuner_count, "TunerCount")
        XmlUtilities.add_as_subelement(root, self.user_agent, "UserAgent")
