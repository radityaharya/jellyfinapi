# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ExternalIdInfo(object):

    """Implementation of the 'ExternalIdInfo' model.

    Represents the external id information for serialization to the client.

    Attributes:
        name (string): Gets or sets the display name of the external id
            provider (IE: IMDB, MusicBrainz, etc).
        key (string): Gets or sets the unique key for this id. This key should
            be unique across all providers.
        mtype (ExternalIdMediaTypeEnum): Gets or sets the specific media type
            for this id. This is used to distinguish between the different
            external id types for providers with multiple ids.  A null value
            indicates there is no specific media type associated with the
            external id, or this is the  default id for the external provider
            so there is no need to specify a type.
        url_format_string (string): Gets or sets the URL format string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "key": "Key",
        "mtype": "Type",
        "url_format_string": "UrlFormatString",
    }

    _optionals = [
        "name",
        "key",
        "mtype",
        "url_format_string",
    ]

    _nullables = [
        "mtype",
        "url_format_string",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        key=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        url_format_string=APIHelper.SKIP,
    ):
        """Constructor for the ExternalIdInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if key is not APIHelper.SKIP:
            self.key = key
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if url_format_string is not APIHelper.SKIP:
            self.url_format_string = url_format_string

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        key = dictionary.get("Key") if dictionary.get("Key") else APIHelper.SKIP
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        url_format_string = (
            dictionary.get("UrlFormatString")
            if "UrlFormatString" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, key, mtype, url_format_string)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        key = XmlUtilities.value_from_xml_element(root.find("Key"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        url_format_string = XmlUtilities.value_from_xml_element(
            root.find("UrlFormatString"), str
        )

        return cls(name, key, mtype, url_format_string)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.key, "Key")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.url_format_string, "UrlFormatString")
